import os
import django
import urllib.request

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tours.models import Tour

def download_image(url, filename):
    # Create media folder if it doesn't exist
    os.makedirs('media/tour_images', exist_ok=True)
    filepath = f'media/tour_images/{filename}'
    
    # Download real image
    urllib.request.urlretrieve(url, filepath)
    return filepath

# Real Satara Images from Wikimedia Commons
tours_data = [
    {
        "name": "Kaas Plateau (Valley of Flowers)",
        "description": "A UNESCO World Heritage Site. Visit during September to see millions of wild flowers blooming across the plateau. A breathtaking photographic experience.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Kaas_plateau_sky.jpg/800px-Kaas_plateau_sky.jpg",
        "filename": "kaas.jpg",
        "duration": 6, "price": 2500
    },
    {
        "name": "Thoseghar Waterfalls",
        "description": "A serene waterfall located near Satara. The waterfall drops from a height of about 200 meters. Best visited during the monsoon season (July to September).",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Thoseghar_waterfalls.jpg/800px-Thoseghar_waterfalls.jpg",
        "filename": "thoseghar.jpg",
        "duration": 8, "price": 2000
    },
    {
        "name": "Sajjangad Fort",
        "description": "The spiritual abode of Sant Ramdas Swami. Offers stunning sunset views of the Satara valley and the surrounding Western Ghats. Peaceful and historic.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Sajjangad_-_Front_View.jpg/800px-Sajjangad_-_Front_View.jpg",
        "filename": "sajjangad.jpg",
        "duration": 4, "price": 1500
    },
    {
        "name": "Vajrai Waterfall Trek",
        "description": "Maharashtra's tallest waterfall at 1840 feet. Located near Bhambavli village. Requires a short trek through lush green forests. Ultimate monsoon adventure.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Vajrai_Waterfall_2.jpg/800px-Vajrai_Waterfall_2.jpg",
        "filename": "vajrai.jpg",
        "duration": 10, "price": 3500
    },
    {
        "name": "Koyna Dam & Natraj Mandir",
        "description": "One of the largest dams in Maharashtra located in Koyna Nagar. Surrounded by thick forests. A perfect blend of engineering marvel and natural beauty.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Koyna_Nagar_Dam.jpg/800px-Koyna_Nagar_Dam.jpg",
        "filename": "koyna.jpg",
        "duration": 12, "price": 4500
    }
]

print("Starting SataraGo Database Population...")

for data in tours_data:
    print(f"Downloading image for {data['name']}...")
    image_path = download_image(data['url'], data['filename'])
    
    # Create Tour in Database
    Tour.objects.create(
        name=data['name'],
        description=data['description'],
        image=f"tour_images/{data['filename']}",
        duration_hours=data['duration'],
        price=data['price']
    )
    print(f"Successfully added {data['name']}!")

print("\n✅ All Satara tours and real images have been added successfully!")