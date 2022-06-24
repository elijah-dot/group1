from django import forms
from .models import Pet
#create class to define form fields
class PetForm(forms.ModelForm):
  class Meta:
    model = Pet 
    fields = ('name','age','kind','user')
    # exclude=('user',)
