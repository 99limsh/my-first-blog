from django.shortcuts import render


def covid(request):
    return render(request, 'covid_chart.html')

def home(request):
    return render(request, 'home.html')
