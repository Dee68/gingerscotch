from django import forms
from django.forms import widgets
from .models import Review

class ReviewForm(forms.ModelForm):
    review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Review
        fields = ['name','message','rating']

        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control','id':'name','name':'name','placeholder':'Enter your name'}),
        #     'message':forms.Textarea(attrs={'class':'form-control','id':'message','name':'message','placeholder':'Enter your review'}),
        #     'rating':forms.IntegerField()
        # }
       