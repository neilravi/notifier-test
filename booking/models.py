from django.db import models

# Create your models here.

"""class BookingModel(models.Model):
	user = models.CharField(max_length=50)
	date = models.DateField(null=False, blank=False)
	number_of_people = models.IntegerField(blank=True, null=True)
	note = models.TextField(blank=True)

	def __str__(self):
		return self.user
	class Meta:
		db_table = 'booking'"""