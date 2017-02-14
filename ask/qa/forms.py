from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "text"]

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer