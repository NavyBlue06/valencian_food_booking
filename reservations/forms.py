from django import forms
from reservations.models import Reservation
from .models import Booking


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
        fields = ['date', 'time' , 'guests']
        
            
      