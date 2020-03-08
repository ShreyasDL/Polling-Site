from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase) :
    def test_was_published_future(self) :
        question = Question(pub_date = timezone.now()+datetime.timedelta(days=30))
        self.assertIs(question.was_published_recently(),False)