from django.contrib import admin
from .models import Vaccine, Campaign, Review, AvailableTime, DoseBooking

# Register your models here.

admin.site.register(Vaccine)
admin.site.register(Campaign)
admin.site.register(Review)
admin.site.register(AvailableTime)
admin.site.register(DoseBooking)
