from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'john doe'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'johndoe@gmail.com'
        }
    ))
    body= forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'enter your comment',
            'rows':'3'
        }
    ))
    class Meta:
        model = Comment
        fields = ('name','email','body')