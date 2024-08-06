from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method=='POST':
        number_one=request.POST.get('number_one')
        number_two=request.POST.get('number_two')
        operators=request.POST.get('operators')

        if operators=='add':
            result=float(number_one) + float(number_two)
            return render(request, 'home.html', {'result':result})

        elif operators=='subtract':
            result=float(number_one) - float(number_two)
            return render(request, 'home.html', {'result':result})

        elif operators=='divide':
            result=float(number_one) / float(number_two)
            return render(request, 'home.html', {'result':result})

        elif operators=='multiply':
            result=float(number_one) * float(number_two)
            return render(request, 'home.html', {'result':result})

    else:
        return render(request, 'home.html')        


