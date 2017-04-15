# -*- coding: utf-8 -*-
import json

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from game.serialisers import *


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects


class SelectSubjectView(APIView):

    def get(self, request):
        subjects = Subject.objects.values('name')
        subject_list = []
        for subject in subjects:
            subject_list.append(subject['name'])
        return Response(subject_list, content_type='application/json')


class LevelView(APIView):

    def get(self, request,):
        subject = request.query_params.get('subject')
        level = int(request.query_params.get('level'))
        city = request.query_params.get('city')
        data = {}
        subject = Subject.objects.get(name=subject)
        level = Level.objects.get(subject=subject, number=level)
        data['level_desc'] = level.desc
        hospital = Hospital.objects.filter(city=city).values()[0]
        hospital['latitude'] = str(hospital['latitude'])
        hospital['longitude'] = str(hospital['longitude'])
        data['hospital'] = hospital
        questions = Question.objects.filter(level=level).values()
        data['questions'] = sorted(questions, key=lambda x: x['seq'])
        return Response(data, content_type='application/json', headers={'Access-Control-Allow-Origin': '*'})

    def post(self, request):
        user_id = request.data.get('user')
        user = User.objects.get(id=user_id)
        response = request.data.get('response')
        for question in response:
            question_obj = Question.objects.get(id=question['id'])
            print question
            data = {
                'user': user,
                'question': question_obj,
                'answer': question['response']
            }

            Answer.objects.create(**data)
        return Response(status=200)

