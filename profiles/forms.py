from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Profile

class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'First Name'  
            }),
            'last_name': TextInput(attrs={
                'class': 'input', 
                'placeholder': 'Last Name' 
            }),
            'bio': Textarea(attrs={
                'class': 'textarea is-info',
                'placeholder': 'Bio',
                'rows': '3'
            }),
            'avatar': FileInput(attrs={
                'class': 'file-input', 
                'name': 'resume',
                '@change': 'OnFileSelected'
            }),
        }