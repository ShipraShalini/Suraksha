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
        level = request.query_params.get('level')
        city = request.query_params.get('city')
        data = {}
        subject = Subject.objects.get(name=subject)
        if level == 1:
            data['level_desc'] = subject.desc
        hospital = Hospital.objects.filter(city=city).values()[0]
        # data['hospital'] = hospital
        hospital['latitude'] = str(hospital['latitude'])
        hospital['longitude'] = str(hospital['longitude'])
        data['hospital'] = hospital
        

        questions = Question.objects.filter(level=level, subject=subject).values()
        data['questions'] = sorted(questions, key=lambda x: x['seq'])
        return Response(data, content_type='application/json')

    def post(self, request):
        user_id = request.data.get('userId')
        questions = json.loads(request.data.get('questions'))

        user = User.objects.get(id=user_id)

        for question in questions:
            question = Question.objects.get(id=question['id'])
            data = {
                'user': user,
                'question': question,
                'answer': question.answer
            }
            Answer.objects.create(**data)


