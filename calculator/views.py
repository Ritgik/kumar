from django.shortcuts import render, redirect
from .models import Calculation

def calculator_view(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
            Calculation.objects.create(expression=expression, result=result)
        except Exception as e:
            result = str(e)
        return render(request, 'calculator/calculator.html', {
            'result': result,
            'calculations': Calculation.objects.all()
        })

    return render(request, 'calculator/calculator.html', {
        'calculations': Calculation.objects.all()
    })