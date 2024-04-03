from django import forms
from .models import Car

class  CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [ 'car_id', 'car_name','car_year']
        widgets = {
            'car_name': forms.TextInput(attrs={'size':20} ),
            'car_year': forms.Select(choices=((y, y) for y in range(2024, 1950, -1))),
        }