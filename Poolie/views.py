from django.shortcuts import render, redirect
from django.contrib import messages
from Poolie.models import Registration
from Poolie.models import Publishride
from Poolie.models import Contact
from Poolie.models import Passenger

from django.http import HttpResponse
from django.conf import settings


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj3 = Contact(name=name, email=email, message=message)
        obj3.save()

        messages.success(request, "Registration form submitted!")

    return render(request, 'index.html')


def driver(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Check if the email and password exist in Registration
        try:
            registration = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            messages.warning(
                request, 'Register as a driver first! No entry found in Database')
            # Redirect to the registration page
            return redirect('registration')

        source = request.POST.get('source')
        destination = request.POST.get('destination')
        seats = request.POST.get('seats')
        contact_number = request.POST.get('contactNumber')
        date_of_journey = request.POST.get('dateOfJourney')
        time_of_journey = request.POST.get('timeOfJourney')
        cost_per_seat = request.POST.get('costPerSeat')
        gender = request.POST.get('gender')

        obj2 = Publishride(
            source=source,
            destination=destination,
            seats=seats,
            contact_number=contact_number,
            email=email,
            date_of_journey=date_of_journey,
            time_of_journey=time_of_journey,
            cost_per_seat=cost_per_seat,
            gender=gender
        )
        obj2.save()
        messages.success(request, "Ride Published !!!")
        return redirect('index')  # Redirect to the index page

    return render(request, 'driver.html')


def passenger(request):
    return render(request, 'passenger.html')


def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        license_no = request.POST.get('license-no')
        insurance_no = request.POST.get('insurance-no')

        obj = Registration(name=name, email=email, password=password,
                           license_no=license_no, insurance_no=insurance_no)
        obj.save()

        messages.success(request, "Registration form submitted!")

    return render(request, 'registration.html')


def search_ride(request):
    if request.method == "POST":
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        dateOfJourney = request.POST.get('dateOfJourney')
        contact_number = request.POST['contactNumber']
        email = request.POST['email']
        seats = request.POST['seats']
        passenger = Passenger(
            source=source,
            destination=destination,
            contact_number=contact_number,
            email=email,
            seats=seats,
            date_of_journey=dateOfJourney,
        )

        # Save the passenger object
        passenger.save()

        # Filter the Publishride objects based on source, destination, and dateOfJourney
        rides = Publishride.objects.filter(
            source=source, destination=destination, date_of_journey=dateOfJourney)
        if not rides:
            messages.warning(request, 'No rides available.')
        else:
            messages.success(request, 'Rides Found.')

        return render(request, 'passenger.html', {'rides': rides})

    return render(request, 'passenger.html')


def send_email(request):
    send_mail(
        "Ride Confirmation for Passenger",
        '''Passenger Name - Rahil Ankhad
        Source - Mumbai
        Destination - Pune
        Contact No. - 7400354926
        Date - 30/05/22
        Time - 5:00 PM
        ''',
        "krihjain383@gmail.com",
        ["krish.jain@spit.ac.in"],
        fail_silently=False,

    )

    send_mail(
        "Ride Booked",
        '''Driver Name - Krish Jain
        Source - Mumbai
        Destination - Pune
        Contact No. - 9372544048
        Date - 30/05/2023
        Time - 5:00 PM
        Cost per seat - 500
        No. of seats - 2
        ''',
        "krishjain383@gmail.com",
        ["rahil.ankhad@spit.ac.in"],
        fail_silently=False,
    )


