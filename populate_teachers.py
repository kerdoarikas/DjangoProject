import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

faker = Faker()


def populate_teachers(n=5):

    subjects = ['Math', 'Estonian', 'Geometry', 'Biology', 'Programming']
    for entry in range(n):
        fake_name = faker.name()
        mixed_subjects = random.choices(subjects)
        fake_subject = random.choices(mixed_subjects)[0]
        print(f'{fake_name}, {fake_subject}')
        teacher = Teacher.objects.get_or_create(name=fake_name, subject=fake_subject)


populate_teachers()
