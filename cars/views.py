from django.shortcuts import render


def cars_views(request):
    return render(request=request, template_name='cars.html')
