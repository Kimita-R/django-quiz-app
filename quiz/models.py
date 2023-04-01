from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# Holds a table of quizes for the app
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    required_score_to_pass = models.IntegerField(help_text="Score to pass in %")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizes'

# Table holding questions - each question is related to a Quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

# Every question has a selection of Options, i.e. each option therefore is related to a question
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    # From the list of options select the answer that is correct - to check users score at the end of the quiz
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
    
# Holds a table of results, consisting of the users score of their last attempt of a quiz
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    score_in_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quiz}, {self.user}, {self.passed}, {self.score_in_percentage}"


