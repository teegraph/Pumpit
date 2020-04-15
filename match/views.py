from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from human.models import Human
from human.serializers import HumanSerializers
from match.models import Match
from match.serializers import MatchSerializers


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializers

    def retrieve(self, request, pk=None):
        try:
            match = Match.objects.get(human=pk)
        except ObjectDoesNotExist:
            raise Http404
        match_serializer = MatchSerializers(match, many=True, read_only=True)
        response = match_serializer.data
        return Response(response, status=status.HTTP_200_OK)
