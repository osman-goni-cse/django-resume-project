from django.shortcuts import render

# Create your views here.

def services(request):
  context = {'services': 'active'}
  # context['services'] = True, css er active link er jonno
  return render(request, 'serv/services.html', context)