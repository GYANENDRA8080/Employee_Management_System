from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("Welcome to Employee Management System")

def about(request):
    return HttpResponse("This is the about page of Employee Management System")