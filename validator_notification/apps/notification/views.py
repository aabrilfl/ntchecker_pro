import logging

from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from validator_notification.apps.notification.providers.providers import NotificationsProvider
from validator_notification.apps.device.models import Device
from validator_notification.apps.utils.decorators.service_permissions import service_permissions
from validator_notification.apps.utils.enumerations.permissions_list import permissions_list
from .serializers import GeneralNotificationSerializer, IndividualNotificationSerializer
from .models import GeneralNotification, IndividualNotification


logger = logging.getLogger(__name__)


class GeneralNotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = GeneralNotificationSerializer

    @service_permissions((permissions_list.STAFF_PERMISSION, ))
    def get_queryset(self):
        return GeneralNotification.objects.all()

    @service_permissions((permissions_list.STAFF_PERMISSION, ))
    def perform_create(self, serializer):
        general_notification = serializer.save()

        devices = Device.objects.all()
        logger.info('GeneralNotification: Create: Individual Notifications to create: %s' % len(devices))
        for device in devices:
            user = device.user
            if user.is_active:
                IndividualNotification.objects.create(
                    general=general_notification,
                    user=user,
                    device=device,
                    option_selected=''
                )
            logger.info('GeneralNotification: IndividualNotification: Create: %s User: %s' % (user.is_active, user.username))
        logger.info('GeneralNotification: Create: Finished')


class IndividualNotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = IndividualNotificationSerializer

    @staticmethod
    def _get_provider(request):
        return NotificationsProvider()

    @staticmethod
    def _get_individual_notifications(response):
        serialized_response = IndividualNotificationSerializer(instance=response, many=True)
        data_response = {
            'data': serialized_response.instance
        }
        return Response(data_response, status=status.HTTP_200_OK)

    def list(self, request):
        provider = self._get_provider(self.request)
        response = provider.get_by_user(user=request.user)
        return self._get_individual_notifications(response)

    @action(methods=['get'], detail=False, url_path='all')
    @service_permissions((permissions_list.STAFF_PERMISSION, ))
    def get_all_queryset(self, request):
        query_params = request.query_params
        date_from = query_params.get('from')
        date_to = query_params.get('to')
        provider = self._get_provider(request)
        if query_params.get('file') == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            response = provider.get_csv(response, date_from=date_from, date_to=date_to,
                                        general_id=query_params.get('general_id'))
        elif query_params.get('general_id'):
            response = provider.get(date_from, date_to, query_params.get('general_id'))
            response = self._get_individual_notifications(response)
        else:
            response = provider.get(date_from, date_to)
            response = self._get_individual_notifications(response)
        return response

    def get_queryset(self):
        return self.request.user.individual_notifications.all()
