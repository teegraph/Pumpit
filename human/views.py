from .models import Human
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .serializers import HumanSerializers


class HumanViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, )
    queryset = Human.objects.all()
    serializer_class = HumanSerializers
