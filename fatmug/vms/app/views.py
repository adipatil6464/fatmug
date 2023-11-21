from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from app.models import *
# Create your views here.
from django.shortcuts import render
from .models import Vendor

def purchase_orders(request):
    VENDOR = Vendor.objects.all()
    
    if request.method == 'POST':
        po_number = request.POST.get('po_number')
        vendor = request.POST.get('vendor')
        order_date = request.POST.get('order_date')
        delivery_date = request.POST.get('delivery_date')
        items = request.POST.get('items')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        quality_rating = request.POST.get('quality_rating')
        issue_date = request.POST.get('issue_date')
        acknowledgment_date = request.POST.get('acknowledgment_date')

        ven = Vendor.objects.get(id=vendor)
        POModel.objects.create(po_number=po_number, vendor=ven, order_date=order_date, delivery_date=delivery_date, items=items, quantity=quantity, status=status, quality_rating=quality_rating, issue_date=issue_date, acknowledgment_date=acknowledgment_date)
        # return redirect('home',{'VENDOR': VENDOR})
    # This line will cause an error as variables are accessed outside the if block
    # print(po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating, issue_date, acknowledgment_date)

    return render(request, 'purchaseorder.html', {'VENDOR': VENDOR})


