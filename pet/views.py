from .forms import PetForm
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def pet(request):
    #check the form is submitted or not
    if request.method == 'POST':
        pet = PetForm(request.POST)
        #check the form data are valid or not
        if pet.is_valid():
            #Read the submitted values
            name = request.POST.get('name')
            age = request.POST.get('age')
            kind = request.POST.get('kind')
            user = request.POST.get('user')
            #merge the values
            data = ['Your pet registration is completed successfully.<br />', 'Name:', name, '<br />','Age:', age, '<br />', 'Kind:', kind, '<br />','User:', user]
            #return form values as response
            return HttpResponse(data)
        else:
            #display the petform
            form = PetForm()
            return render(request,"pet.html",{'form':form})
            
    form = PetForm()        
    return render(request,"pet.html",{'form':form})