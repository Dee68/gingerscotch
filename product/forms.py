from django import forms
from django.forms import widgets
from .models import Review

class ReviewForm(forms.ModelForm):
    review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Review
        fields = ['name','message','rating']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReviewForm, self).__init__(*args, **kwargs)

       
       