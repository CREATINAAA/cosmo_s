import json
import logging
from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import PermissionSlugIsMissing
from ..service.webhook_handler import webhook_handler

logger = logging.getLogger(__name__)


class OrderCreationAPIView(APIView):
    permission_classes = [PermissionSlugIsMissing]
    
    def post(self, request, *args, **kwargs):
        logger.info(f"request time: {datetime.now()}\n"
                    f"request data: {json.dumps(request.data)}\n")
        webhook_handler(request.data, kwargs.get("warehouse"))
        return Response(status=status.HTTP_200_OK)
