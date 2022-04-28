
from django.forms import EmailInput, ModelForm, FileInput, NumberInput, TextInput, Textarea, Select
from .models import Post, Like, Comment, Verification


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')

        widgets = {
            'content': Textarea(attrs={
                'class': 'textarea is-info',
                'placeholder': 'Content',
                'rows': '3'
            }),
            'image': FileInput(attrs={
                'class': 'file-input', 
                'name': 'resume',
                'accept': 'image/*, video/*',
                '@change': 'OnFileSelected'
            }),
        }
    
class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )

        widgets = {
            'body': Textarea(attrs={
                'class': 'textarea mobile-txtarea modal-view',
                'style': 'font-size: 14px;',
                'placeholder': 'Add a Coment..',
                'cols': '50',
                'rows': '3'
            })
        }

class VerificationForm(ModelForm):
    class Meta:
        model = Verification
        fields = ('first_name', 'email', 'phone_number', 'job')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g Jamshid Iskandarov',
            }),
            'email': EmailInput(attrs={
                'class': 'input mb-2',
                'placeholder': 'e.g. alexsmith@gmail.com',
            }),
            'phone_number': NumberInput(attrs={
                'class': 'input mb-2',
                'placeholder': 'e.g +998909174227',
            }),
        }