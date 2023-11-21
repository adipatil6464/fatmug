from django.shortcuts import render,HttpResponse
from datetime import datetime
# Create your views here.
def purchase_orders(request):
    if request.POST == 'POST':
        po_number = request.POST['po_number']
        vendor = request.POST['vendor']
        order_date = datetime.now()
        delivery_date = request.POST['delivery_date']
        items = request.POST['items']
        quantity = request.POST['quantity']
        status = request.POST['status']
        quality_rating = request.POST['quality_rating']
        issue_date = request.POST['issue_date']
        acknowledgment_date = request.POST['acknowledgment_date']



