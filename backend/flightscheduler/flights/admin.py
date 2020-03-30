from django.contrib import admin
from .models import Schedule


def oneway_trip(modeladmin,request,querset):
    querset.update(trip_type="One Way")

oneway_trip.short_description="set trip type One Way"

class TripTypeAdmin(admin.ModelAdmin):
    list_display = ['airline','trip_type']
    ordering = ['airline']
    actions = [oneway_trip]

# Register your models here.
admin.site.register(Schedule,TripTypeAdmin)