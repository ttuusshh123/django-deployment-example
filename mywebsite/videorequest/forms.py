from django import forms


class VideoForm(forms.Form):
    videoname=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
    'class' : 'videoname'
    }))
    videodesc=forms.CharField(widget=forms.TextInput(attrs={
    'class' : 'videodesc'
    }))
