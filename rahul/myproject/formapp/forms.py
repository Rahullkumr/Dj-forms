from django import forms


class Student(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    course = forms.CharField()
    fee = forms.FloatField()
    phone = forms.IntegerField()
