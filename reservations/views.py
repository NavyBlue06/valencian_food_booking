from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import ReservationForm, BookingForm  # Cleaner import
from django.contrib.auth.forms import UserCreationForm


# Home page
def home(request):
    return render(request, 'reservations/home.html')


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
    return render(request, 'reservations/book_table.html', {'form': form})


# List bookings (requires login)
@login_required
def my_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservations/my_booking.html', {'bookings': bookings})  #  Make sure template is named exactly like this!

#Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'reservations/register.html', {'form': form})

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

    return render(request, 'reservations/edit_booking.html', {'form': form})  #  Always render — even after invalid POST
