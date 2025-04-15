from .models import contact
from  django import forms
    





class contactform (forms.modelform):
    class meta:
        model = contact
        field =['name','email','phone number','message']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
