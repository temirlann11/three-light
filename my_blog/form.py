from django import forms
from .models import Comments
from .models import CustomUser

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text_comments', 'name', 'email']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }