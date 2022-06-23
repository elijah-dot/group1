from .models import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import AppointmentForm


































































































































def available(request):
    vets = Vet.objects.all()


    context = {'vets': vets,'user':request.user}
    return render(request,'pet/available.html', context=context)

def booking(request,vetName):
    form = AppointmentForm()
    
    pets = Pet.objects.all().filter(user_id=request.user)
    form.fields['pet'].queryset = pets
    try:
        vet = Vet.objects.get(pk=vetName)
        context = {'form': form, 'vet':vet,'user':request.user}
    except Profle.DoesNotExist:
        return Http404
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # print(form.errors)
        if form.is_valid():
          new_appointment = Appointment(pet=form.cleaned_data['pet'], vet=vet, time_booked=form.cleaned_data['time_booked'],service=form.cleaned_data['service'], date=form.cleaned_data['date'],when_the_booking_was_done=datetime.now(),pet_owner=request.user)
          new_appointment.save()
          print(new_appointment)




          return HttpResponseRedirect (reverse('available'))
        return render(request,'pet/booking.html')
    return render(request,'pet/booking.html',context=context)

def user_appointments(request):
    try:
        logged_user = Profle.objects.get(user=1)
        appointments = Appointment.objects.all().filter(pet_owner=logged_user)
    except Exception as e:
        message = 'You do not have any Appointments'
        context = {'message': message,'user':request.user}
        return render(request,'pet/appointments.html',context=context)

    context = {'appointments': appointments,'user':request.user}

    return render(request,'pet/appointments.html',context=context)




def vet_appointments(request):
    try:
        appointments = Appointment.objects.all().filter(vet=request.user)
    except Exception as e:
        message = 'You do not have any Appointments'
        context = {'message': message}
        return render(request,'pet/appointments.html',context=context)

    context = {'appointments': appointments,'user':request.user}

    return render(request,'pet/appointments.html',context=context)

def delete_appointment(request,appointment):
    app = Appointment.objects.get(pk=appointment)
    app.delete()
    return HttpResponseRedirect(reverse('user_appointments'))


