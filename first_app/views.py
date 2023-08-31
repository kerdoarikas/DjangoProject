from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.
class MyHomeView(TemplateView):
    template_name = 'first_app/home.html'

class StudentListView(ListView):
    model = Student
    queryset = Student.objects.order_by('name')
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    template_name = 'first_app/student_form_create.html'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('first_app:student_list')

class StudentUpdateView(UpdateView):
    #template_name = 'first_app/student_form.html'
    model = Student
    fields = ['name', 'weight']
    success_url = reverse_lazy('first_app:student_list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('first_app:student_list')