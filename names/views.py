from django.shortcuts import render, redirect
from .forms import IftarForm

def register(request):

    if request.method == "POST":
        form = IftarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = IftarForm()

    return render(request,'register.html',{'form':form})


def thanks(request):
    return render(request,'thanks.html')