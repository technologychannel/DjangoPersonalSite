from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'name', 'birth_date', 'class_name', 'phone_number']