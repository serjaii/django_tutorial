import os
import django
from django.contrib.auth import get_user_model
from polls.models import Question, Choice
from django.utils import timezone

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("User admin created")

q_text_1 = "¿Cual es tu lenguaje favorito?"
if not Question.objects.filter(question_text=q_text_1).exists():
    q = Question(question_text=q_text_1, pub_date=timezone.now())
    q.save()
    q.choice_set.create(choice_text='Python', votes=0)
    q.choice_set.create(choice_text='Java', votes=0)
    q.choice_set.create(choice_text='C++', votes=0)
    print("Question 1 created")

q_text_2 = "¿Te gusta Django?"
if not Question.objects.filter(question_text=q_text_2).exists():
    q = Question(question_text=q_text_2, pub_date=timezone.now())
    q.save()
    q.choice_set.create(choice_text='Si', votes=0)
    q.choice_set.create(choice_text='No', votes=0)
    print("Question 2 created")
