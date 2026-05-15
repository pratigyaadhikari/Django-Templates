from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is home page")
    people = [
        {
            "name": "Ram",
            "age": 22,
            "city": "Kathmandu",
            "profession": "Engineer"
        },
        {
            "name": "Sita",
            "age": 20,
            "city": "Pokhara",
            "profession": "Doctor"
        },
        {
            "name": "Hari",
            "age": 25,
            "city": "Lalitpur",
            "profession": "Teacher"
        },
        {
            "name": "Gita",
            "age": 23,
            "city": "Bhaktapur",
            "profession": "Designer"
        },
        {
            "name": "Shyam",
            "age": 24,
            "city": "Biratnagar",
            "profession": "Developer"
        }
            ]
    
    context = {
        "title":"Homepage",
        "body":"Welcome to homepage",
        "people": people  
    }
    return render(request,'home.html',context)
    
def about_us(request):
    # return HttpResponse("hello")
    services = [
        "Web Development",
        "Backend Development",
        "UI Design",
        "API Development"
        ]
    context = {
        "title":"About Us",
        "body": "Welcome to our website",
        "message": "We provide quality education",
        "services":services
    }
    return render(request,'about_us.html',context)

def contact_page(request):
    # return HttpResponse(" contact us for more!")
    context = {
      "title": "Contact Page",
      "body" : "If any problem, contact here",
      "email": "contact@gmail.com",
      "phone": 9880654321
        }
    return render(request,'contact_page.html',context)