from django.db import models

class Tour(models.Model):
    CATEGORY_CHOICES = (
        ('Nature', 'Nature & Flowers'),
        ('Fort', 'Historical Forts'),
        ('Waterfall', 'Waterfalls'),
        ('Spiritual', 'Spiritual & Temples'),
        ('Student', '🎓 Student Special'),
    )
    VEHICLE_CHOICES = (
        ('Sedan', '🚗 Sedan (Swift Dzire)'),
        ('SUV', '🚙 SUV (Innova)'),
        ('Auto', '🛺 Auto Rickshaw'),
        ('Tempo', '🚐 Tempo Traveller'),
    )
    PACKAGE_CHOICES = (
        ('Half-Day', 'Half-Day (4-5 Hrs)'),
        ('Full-Day', 'Full-Day (8-10 Hrs)'),
        ('Custom', 'Custom Package'),
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    # THIS MUST BE image, NOT image_url
    image = models.ImageField(upload_to='tour_images/', blank=True, null=True)
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Nature')
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_CHOICES, default='Sedan')
    package_type = models.CharField(max_length=50, choices=PACKAGE_CHOICES, default='Full-Day')
    duration_hours = models.IntegerField()
    price = models.IntegerField(help_text="Price in INR")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    travel_date = models.DateField()
    pickup_location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.tour.name}"