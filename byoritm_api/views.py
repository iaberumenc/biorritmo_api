from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Health(APIView):
    filterset_fields = []
    http_method_names = ['get']

    def get(self, request):
        return Response(status=status.HTTP_200_OK)