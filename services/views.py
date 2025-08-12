from django.shortcuts import render
from .models import Services





def services(request):
    return render(request, 'services/services.html', {})





def service_detail(request, search):
    service = Services.objects.get(search = search)

    return render(request, 'services/service-detail.html', {'service':service})