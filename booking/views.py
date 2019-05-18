from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from booking.models import BookingModel
# Create your views here.


def showBooking(request):
	booking = BookingModel.objects.all()
	return	render(request, 'booking/index.html', {'booking':booking})


def saveBooking(request, count=None):
	if count:
		for i in range(count):
			print("TRyiing Ravi")
			channel_layer = get_channel_layer()
			async_to_sync(channel_layer.group_send)(
            	"gossip", {"type": "booking.gossip",
                       "event": "New Booking",
                       "username": 'neilravi'
                       })
		return HttpResponse("You got {} notifications".format(count))
	else:
		return HttpResponse("No Args")




