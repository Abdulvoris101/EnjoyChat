from .models import ChatImageUpload
from django.forms import ModelForm

class ChatImageForm(ModelForm):
    class Meta:
        model = ChatImageUpload
        fields = '__all__'
        