#Post forms

#Django
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm):
    #Post model form

    #La clase meta es la configuracion
    #de la clase en general
    class Meta:
        #Form settings

        model = Post
        fields = ('user','profile','title','photo')