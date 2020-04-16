from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from match.models import Match
from match.serializers import MatchSerializers
import requests


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializers

    def list(self, request):
        match = Match.objects.all()
        datas = MatchSerializers(match, many=True).data
        response = list()
        for data in datas:
            url = reverse("human-detail", args=[data["human_id"]], request=request)
            r = requests.get(url)
            data["human"] = r.json()
            response.append(data)
        return Response(datas, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        response = requests.get(reverse("human-detail", args=[pk], request=request))
        if response.status_code != 200:
            return Response(status=status.HTTP_404_NOT_FOUND)
        json = response.json()
        try:
            match = Match.objects.get(first_name=json["first_name"], second_name=json["second_name"],
                                      age=json["age"], gender=json["gender"])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = MatchSerializers(match).data
        response["human"] = json
        return Response(response, status=status.HTTP_200_OK)
