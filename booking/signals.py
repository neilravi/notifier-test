from .models import BookingModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from booking.models import BookingModel


#---------------------------------Signals ---------------------------------------------///


@receiver(post_save, sender=BookingModel)
def add_booking(sender, instance, created, **kwargs):
    if created:
        print("TRyiing Ravi")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "booking.gossip",
                       "event": "New Booking",
                       "username": instance.user
                       })