from django.shortcuts import render
from formapp.forms import Student
# Create your views here.


def homepage(request):
    form = Student()
    if request.method == "POST":
        form = Student(request.POST)
        # name = request.POST["name"]
        # rollno = request.POST["rollno"]
        # course = request.POST["course"]
        # fee = request.POST["fee"]
        # phone = request.POST["phone"]
        return render(request, "homepage.html", {"form": form, "name": name})
    return render(request, "homepage.html", {"form": form})
