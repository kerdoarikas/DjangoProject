from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Subject

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

class SubjectListView(ListView):
    model = Subject
    queryset = Subject.objects.order_by('subject_name')
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject

class SubjectCreateView(CreateView):
    template_name = 'first_app/subject_form_create.html'
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('first_app:subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['subject_name']
    success_url = reverse_lazy('first_app:subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('first_app:subject_list')