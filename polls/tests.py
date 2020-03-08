from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase) :
    def test_was_published_future(self) :
        question = Question(pub_date = timezone.now()+datetime.timedelta(days=30))
        self.assertIs(question.was_published_recently(),False)

    def test_past_question(self) :
        now = timezone.now()
        time = now - datetime.timedelta(days=1,seconds=1)
        question = Question(pub_date = time)
        self.assertIs(question.was_published_recently(),False)

    def test_for_recent(self) :
        now = timezone.now()
        time = now - datetime.timedelta(hours=23,minutes=59,seconds=59)
        question = Question(pub_date = time)
        self.assertIs(question.was_published_recently(),True)