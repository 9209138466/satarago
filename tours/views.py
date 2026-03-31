from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Tour, Booking

def home(request):
    featured_tours = Tour.objects.filter(is_active=True)[:4]
    return render(request, 'home.html', {'featured_tours': featured_tours})

def all_tours(request):
    all_tours = Tour.objects.filter(is_active=True)
    categories = all_tours.values_list('category', flat=True).distinct()
    selected_spot = request.GET.get('spot')
    
    if selected_spot:
        tours = all_tours.filter(category=selected_spot)
    else:
        tours = all_tours 
        
    return render(request, 'tour_list.html', {
        'tours': tours,
        'categories': categories,
        'selected_spot': selected_spot
    })

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customer_phone = request.POST.get('phone')
        travel_date = request.POST.get('date')
        pickup_location = request.POST.get('pickup')
        
        booking = Booking.objects.create(
            tour=tour,
            customer_name=customer_name,
            customer_phone=customer_phone,
            travel_date=travel_date,
            pickup_location=pickup_location
        )

        # Customer goes to success page to send you a WhatsApp manually
        from django.urls import reverse
        return redirect(f"{reverse('success')}?name={customer_name}&tour={tour.name}&date={travel_date}&phone={customer_phone}")

    return render(request, 'tour_detail.html', {'tour': tour})

def success(request):
    name = request.GET.get('name', '')
    tour = request.GET.get('tour', '')
    date = request.GET.get('date', '')
    phone = request.GET.get('phone', '')
    
    return render(request, 'success.html', {
        'name': name, 'tour': tour, 'date': date, 'phone': phone
    })

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})