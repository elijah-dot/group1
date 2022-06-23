from datetime import datetime
from django import forms

class DatePickerInput(forms.DateInput):
        input_type = 'date'
        min = datetime.today()
        
        

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'