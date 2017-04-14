from django.forms import ModelForm

from game.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'age', 'city']

