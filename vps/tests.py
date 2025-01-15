import typing
import uuid

import factory
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from vps.models import VPS

CREATE_VPS_ENDPOINT = "vps-list"
READ_VPS_ENDPOINT = "vps-detail"

CreatedVPSObject = typing.Any
TargetVPSObject = typing.Any
StubVPSObject = typing.Any


class VPSFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VPS

    uid = uuid.uuid4()
    cpu = 2
    ram = 4096
    hdd = 20
    status = "started"


def assert_vps_data(created: CreatedVPSObject, target: TargetVPSObject) -> None:
    assert created["cpu"] == target["cpu"]
    assert created["ram"] == target["ram"]
    assert created["hdd"] == target["hdd"]
    assert created["status"] == target["status"]


def create_vps(client: APIClient, stub: typing.Optional[StubVPSObject] = None) -> CreatedVPSObject:
    stub = stub if stub else VPSFactory.stub()
    target = {"cpu": stub.cpu, "ram": stub.ram, "hdd": stub.hdd, "status": stub.status}
    response = client.post(reverse(CREATE_VPS_ENDPOINT), target)
    assert response.status_code == status.HTTP_201_CREATED
    assert_vps_data(response.data, target)

    return response.data


def create_vps_filter_request(client: APIClient, target: TargetVPSObject, filter_query: str) -> None:
    response = client.get(f"{reverse(CREATE_VPS_ENDPOINT)}{filter_query}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    assert_vps_data(response.data["results"][0], target)


@pytest.mark.django_db
def test_create_vps():
    client = APIClient()
    create_vps(client)


@pytest.mark.django_db
def test_get_vps():
    client = APIClient()
    vps = create_vps(client)
    response = client.get(reverse(READ_VPS_ENDPOINT, kwargs={"pk": vps["uid"]}))
    assert response.status_code == status.HTTP_200_OK
    assert_vps_data(response.data, vps)


@pytest.mark.django_db
def test_update_vps_status():
    client = APIClient()
    vps = create_vps(client)
    response = client.patch(reverse(READ_VPS_ENDPOINT, kwargs={"pk": vps["uid"]}), {"status": "blocked"})
    assert response.status_code == status.HTTP_200_OK

    vps = dict(vps)
    vps["status"] = "blocked"
    assert_vps_data(response.data, vps)


@pytest.mark.django_db
def test_vps_list_and_filters():
    client = APIClient()

    create_vps_filter_request(
        client, create_vps(client, stub=VPSFactory.stub(cpu=2, ram=4096, hdd=100)), "?cpu__lte=2&ram__gte=4096&hdd=100"
    )

    create_vps_filter_request(
        client,
        create_vps(client, stub=VPSFactory.stub(cpu=2, ram=8192, hdd=500)),
        "?cpu__gte=2&ram__lte=8192&hdd__gte=500",
    )

    create_vps_filter_request(client, create_vps(client, stub=VPSFactory.stub(cpu=4, ram=2048, hdd=300)), "?&hdd=300")


@pytest.mark.django_db
def test_vps_removing():
    client = APIClient()
    vps = create_vps(client)
    assert VPS.objects.filter().count() == 1
    response = client.delete(reverse(READ_VPS_ENDPOINT, kwargs={"pk": vps["uid"]}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert VPS.objects.filter().count() == 0
