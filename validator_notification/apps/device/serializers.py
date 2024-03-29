from rest_framework import serializers

from validator_notification.apps.device.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=False)
    tlf = serializers.CharField(required=True, allow_blank=True)
    platform = serializers.CharField(required=True, allow_blank=False)
    owner = serializers.CharField(required=True, allow_blank=False)
    device = serializers.CharField(required=False, allow_blank=True)
    os_family = serializers.CharField(required=False, allow_blank=True)
    os_version = serializers.CharField(required=False, allow_blank=True)
    onesignal_id = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Device
        fields = '__all__'

    def to_representation(self, instance) -> str:
        ret = super().to_representation(instance)
        ret['tlf'] = instance.get_tlf_with_mask()
        ret['onesignal_id'] = instance.get_onesignal_id_with_mask()
        return ret
