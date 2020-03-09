from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse
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
    
def create_question(question_text,days) :
    now = timezone.now()
    date = now + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=date)

class QuestionIndexViewTests(TestCase) :
    def test_no_questions(self) :
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
    
    def test_past_questions(self) :
        question = create_question("Past Question.",days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question'],['<Question: Past Question.>'])
    
    def test_futu