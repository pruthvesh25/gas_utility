from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer  # Ensure customer is set
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()

    return render(request, 'customer_service/submit_request.html', {'form': form})

from django.shortcuts import render
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def request_status(request):
    # Fetch the service requests for the logged-in user
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/request_status.html', {'requests': requests})
