from rest_framework import status, viewsets
from rest_framework.response import Response

from vps.models import VPS
from vps.serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        updated_status = request.data.get("status", instance.status)

        if updated_status not in map(lambda x: x[0], VPS.STATUSES):
            return Response({"detail": "Status is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = updated_status
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
