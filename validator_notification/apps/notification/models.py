from django.db import models
from django.contrib.auth.models import User as DjangoUser
from .utils.enumerations import options_notification, status_notification
from validator_notification.apps.device.models import Device
from validator_notification.apps.utils.helpers.data_mask import get_str_with_mask


class GeneralNotification(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='')
    thumbnail = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)


class IndividualNotification(models.Model):
    general = models.ForeignKey(GeneralNotification, related_name="general_notification",
                                on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(DjangoUser, related_name="individual_notifications",
                                on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(Device, related_name="devices",
                                 on_delete=models.CASCADE, null=True)
    option_selected = models.CharField(max_length=10, choices=options_notification.tuples(),
                                       default='', null=True)
    status = models.CharField(max_length=50, choices=status_notification.tuples(),
                                       default=status_notification.NEW.value, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.CharField(max_length=350, null=True)

    def get_tlf_with_mask(self) -> str:
        return get_str_with_mask(tail_to_convert=self.device.tlf, mask_symbol='*', n_unmaskchar=4)

    def get_onesignal_id_with_mask(self) -> str:
        return get_str_with_mask(tail_to_convert=self.device.onesignal_id or '', mask_symbol='*', n_unmaskchar=6)
