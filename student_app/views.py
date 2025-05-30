from django.shortcuts import render, redirect
from .models import PaymentDetail
from datetime import datetime

def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        card_number = request.POST.get('cardNumber')
        expiry = request.POST.get('exp')
        cvv = request.POST.get('cvv')
        mob_number = request.POST.get('mob_number')
        billing_address = request.POST.get('billing')

        try:
            expiry_date = datetime.strptime(expiry, "%m/%y").date()
        except ValueError:
            return render(request, 'payment.html', {'error': 'Invalid expiry date format. Use MM/YY.'})

        PaymentDetail.objects.create(
            full_name=full_name,
            email=email,
            card_number=card_number,
            expiry_date=expiry_date,
            cvv=cvv,
            mob_number=mob_number,
            billing_address=billing_address
            
        )
        return redirect('home')

    return render(request, 'payment.html')

