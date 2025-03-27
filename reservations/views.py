from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import ReservationForm, BookingForm  # Cleaner import


# Home page
def home(request):
    return render(request, 'home.html')


# Booking form view
def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made!')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'book_table.html', {'form': form})


# List bookings (requires login)
@login_required
def my_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_booking.html', {'bookings': bookings})  #  Make sure template is named exactly like this!


# Edit a booking (requires login)
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_booking')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form})  #  Always render — even after invalid POST
