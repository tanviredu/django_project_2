from .models import Comment 
from django import forms 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        ## only this three can be
        fields = ('name','email','body')

        ## user dot get a chance it to set the activate
        ## he will only post then the admin will activate