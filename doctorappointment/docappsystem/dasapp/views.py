from django.shortcuts import render
from .models import Page, DoctorReg

def appointment_view(request):
    page = Page.objects.all()  # Ensure this fetches the Page data
    doctorview = DoctorReg.objects.all()  # Fetch doctors for the dropdown
    context = {
        'page': page,
        'doctorview': doctorview,
    }
    return render(request, 'appointment.html', context)

def some_view(request):
    page = Page.objects.all()  # Fetch all Page objects
    context = {
        'page': page,
        # ...other context variables...
    }
    return render(request, 'some_template.html', context)
