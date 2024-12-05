from django.shortcuts import render, redirect

from restaurant.models import Reservation, Message, Subscribe, Order

from . serializers import ReservationSerializer
from rest_framework import viewsets

from django.contrib import messages

from django.core.mail import send_mail



# Create your views here.


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer




def index(request):
    return render(request, 'index.html')


def order(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        order = Order(name=name, phone=phone, address=address)

        order.save()
        messages.success(request, 'Order successfully placed!')
    return render(request, 'orders.html')


def form(request):
    return render(request, 'form.html')


def pay(request):
    return render(request, 'pay.html')

def reservation(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        reservation = Reservation(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)

        reservation.save()
        messages.success(request, 'Your reservation request has been made successfully. Thank you!')
        return redirect('/')
        
    return render(request, 'index.html')



def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = Message(name=name, email=email, subject=subject, message=message)

        message.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('/')

    return render(request, 'index.html')


def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']

        subscribe = Subscribe(email=email)

        subscribe.save()
        messages.success(request, 'Your subscription request has been sent. Thank you!')
        return redirect('/')

    return render(request, 'index.html')


def view_data(request):
    reservations = Reservation.objects.all()
    messages = Message.objects.all()
    subscribes = Subscribe.objects.all()
    return render(request, 'view_data.html', {'reservations':reservations, 'messages':messages, 'subscibers':subscribes})
