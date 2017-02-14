from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    objects = QuestionManager()

    def get_url(self):
        return "/question/{}/".format(self.pk)

class AnswerManager(models.Manager):
    def getAnswerWithQuestionId(self, question_id):
        return self.filter(question=question_id).order_by('-added_at')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, default=1)
    objects = AnswerManager()
