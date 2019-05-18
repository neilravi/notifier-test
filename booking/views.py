from django.shortcuts import render
from .models import BookingModel
# Create your views here.


def showBooking(request):
	booking = BookingModel.objects.all()
	return	render(request, 'booking/index.html', {'booking':booking})


def saveBooking(request):
	'''booking = BookingModel()
	booking.name = request.POST['name']
	booking.note = 
	booking.date = 
	booking.number_of_people ='''
	pass 