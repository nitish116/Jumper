from django import forms

class MyRegistrationForm(forms.Form):
    
    runopt = forms.CharField(label='runopt', max_length=100)
    ride_num = forms.CharField(label='ride_num', max_length=100)