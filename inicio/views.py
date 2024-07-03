from django.shortcuts import render

def inicio(request):
   # return HttpResponse('Bienvenidos!!')
   return render (request, 'inicio/index.html')

