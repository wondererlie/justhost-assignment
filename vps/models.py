import uuid

from django.db import models
from django.utils.text import gettext_lazy as _


class VPS(models.Model):
    STATUSES = (
        ("started", "Started"),
        ("blocked", "Blocked"),
        ("stopped", "Stopped"),
    )

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUSES)

    class Meta:
        ordering = ("status",)
        verbose_name = _("VPS Server")
        verbose_name_plural = _("VPS Servers")

        db_table = "vps_servers"

    def __str__(self):
        return f"VPS {self.uid} - Status: {self.status}"
