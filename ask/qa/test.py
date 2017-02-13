import os
import unittest
import sys

sys.path.append('/home/box/web/ask')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ask.settings'
import django

if hasattr(django, 'setup'):
    django.setup()

from django.contrib.auth.models import User
from django.db.models import Max
from django.utils import timezone

import time


class TestInitData(unittest.TestCase):
    def test_import(self):
        from qa.models import Question
        from qa.models import Answer
        res = Question.objects.all().aggregate(Max('rating'))
        max_rating = res['rating__max'] or 0
        user, _ = User.objects.get_or_create(
            username='x',
            defaults={'password': 'y', 'last_login': timezone.now()})
        for i in range(30):
            question = Question.objects.create(
                title='question ' + str(i),
                text='text ' + str(i),
                author=user,
                rating=max_rating + i
            )
        time.sleep(2)
        question = Question.objects.create(title='question last', text='text', a
        uthor = user)
        question, _ = Question.objects.get_or_create(pk=3141592, title='question
        about
        pi
        ', text='
        what is the
        last
        digit?', author=user)
        question.answer_set.all().delete()
        for i in range(10):
            answer = Answer.objects.create(text='answer ' + str(i), question=que
        stion, author = user)

suite = unittest.TestLoader().loadTestsFromTestCase(globals().get(sys.argv[1]))
unittest.TextTestRunner(verbosity=0).run(suite)
