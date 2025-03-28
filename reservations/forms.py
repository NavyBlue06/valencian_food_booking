from django import forms
from .models import Reservation, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'name', 
            'phone',
            'email', 
            'date', 
            'time', 
            'guests', 
            'message',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            
        }
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        # Call Django's original form setup so everything works as expected
        super(CustomerUserCreationForm, self).__init__(*args, **kwargs)

        # Add Bootstrap styling + placeholder text to the username field
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',               # makes it look nice
            'placeholder': 'Choose a username'     # gray text inside the box
        })

        # Do the same for password1 (first password field)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })

        # And again for password2 (confirm password)
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repeat the password'
        })

        # Remove the long default help text under password fields
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''