from django.contrib import admin
from .models import Tour, Booking

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'package_type', 'price', 'is_active')
    list_filter = ('is_active', 'vehicle_type', 'package_type') # Adds filter sidebar
    list_editable = ('is_active', 'price') # Lets you edit price directly from the list

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'tour', 'travel_date', 'is_confirmed')
    list_filter = ('is_confirmed',)