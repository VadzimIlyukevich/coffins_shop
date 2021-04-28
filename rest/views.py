from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class CoffinApiViewsSet(viewsets.ModelViewSet):
    queryset = Coffin.objects.all()
    serializer_class = CoffinSerializer

    action_to_serializer = {
        'list': CoffinRetrieveSerializer,
        'retrieve': CoffinRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class FormOfCoffinDetailApiViewsSet(viewsets.ModelViewSet):
    queryset = FormOfCoffin.objects.all()
    serializer_class = FormOfCoffinSerializer

    action_to_serializer = {
        'list': FormOfCoffinDetailSerializer,
        'retrieve': FormOfCoffinDetailSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class RequestApiViewsSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestApiView(APIView):
    def post(self, request):
        request_request = RequestSerializer(data=request.data)
        if request_request.is_valid():
            request_request.save()
        return Response(request_request.data, status=201)

    def get(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)
