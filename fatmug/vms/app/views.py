from django.shortcuts import render,redirect
from . models import *
# Create your views here.

def create_vender(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact_details = request.POST.get('contact_details')
        address = request.POST.get('address')
        vendor_code = request.POST.get('vendor_code')
        # on_time_delivery_rate=request.POST.get('on_time_delivery_rate')
        # quality_rating_avg=request.POST.get('quality_rating_avg')
        # average_response_time=request.POST.get('average_response_time')
        # fulfillment_rate=request.POST.get('fulfillment_rate')


        # Create a new Vendor instance
        vendor = Vendor.objects.create(
            name=name,
            contact_details=contact_details,
            address=address,
            vendor_code=vendor_code,
            on_time_delivery_rate=0.0 , # You can set default values here
            quality_rating_avg=0.0,
            average_response_time=0.0,
            fulfillment_rate=0.0
        )

        # Redirect to a page showing the list of vendors
    return render(request,"create_vender.html")
    # return render(request, 'list.html') 

 