from django.http import HttpResponse
from django.shortcuts import render
 

def home(request):
    isActive= True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True

     
    # isActive= True
    name="LearnCodewithDiwanshu"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'wap to print pascals triangle'
    ]
    student= {
       'student_name' : "Diwanshu", 
        'student_college' : "MU",
        'student_city' : "Indore"
    }
    data = {
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student

    }
    # print("test function is call from views")
    # return HttpResponse("<h1>Hello this is index page</h1>")
    return render(request, "home.html",data)
def about(request):
    print("about function is call from views")
    # return HttpResponse("<h1>Hello this is about page</h1>")
    return render(request, "about.html", {})
def services(request):
    print("services function is call from views")
    # return HttpResponse("<h1>Hello this is services page</h1>")
    return render(request, "services.html", {})