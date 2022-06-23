from django import forms
from .models import *
from .widgets import DatePickerInput






















































































































class AppointmentForm(forms.ModelForm):

    years = range(datetime.now().year,datetime.now().year+1,1)
    


    date = forms.DateField(widget=forms.SelectDateWidget(years=years))
    
    class Meta:
        model = Appointment
        exclude = ['vet']

        labels = {
            'time_booked':'pick a time',
            'service': 'service',
            'pet':'pet',
        }