from django import forms

from .models import Courier

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'
        exclude = ['created_at', 'updated_at']