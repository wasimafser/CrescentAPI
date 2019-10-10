from django.shortcuts import render

# Create your views here.
def singinview(request):
    return render(request, 'templates/timetable/signinhtml.html')
