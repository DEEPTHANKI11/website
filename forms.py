# Contains MyFormClass
from django import forms
from django import forms
from .models import Person
class MyFormClass(forms.Form):
    # Form fields and methods here
    pass

# Avoid importing here if it's causing circular dependency
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'phone', 'message']