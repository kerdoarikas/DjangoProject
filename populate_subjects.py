import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Subject

faker = Faker()


def populate_subjects(n=5):

    subjects = ['Math', 'Estonian', 'Geometry', 'Biology', 'Programming']
    for entry in range(n):
        mixed_subjects = random.choices(subjects)
        fake_subject = random.choices(mixed_subjects)[0]
        print(f'{fake_subject}')
        subject_name = Subject.objects.get_or_create(subject_name=fake_subject)


populate_subjects()
