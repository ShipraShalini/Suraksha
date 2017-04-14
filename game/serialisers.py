from rest_framework.serializers import ModelSerializer

from game.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'