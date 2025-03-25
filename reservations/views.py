from django.shortcuts import render, redirect
from django.contrib import messages  # import messages
from reservations.forms import ReservationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made!')
            return redirect('home')  # redirect to home page
    else:
        form = ReservationForm()
    return render(request, 'book_table.html', {'form': form})

def my_bookings(request):
    bookings= Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})
