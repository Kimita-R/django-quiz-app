from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# Holds a table of quizes for the app
class Quiz(models.Model):
    """
    Represents a Quiz object

    Attributes:
        name (CharField): The name of the Quiz.
        require_score_pass (IntegerField): The minimum score a user needs to pass/complete the quiz and topic module.
        pub_date (DateTimeField): The date and time the quiz was published.
    """
    name = models.CharField(max_length=200)
    required_score_to_pass = models.IntegerField(help_text="Score to pass in %")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizes'

# Table holding questions - each question is related to a Quiz
class Question(models.Model):
    """
    Represents a Question object - each question corresponds to a Quiz object
    
    Attributes:
        quiz (ForeignKey): The quiz the question corresponds to , represented as a foreign key to the Quiz model.
        question_text (CharField): The question.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

# Every question has a selection of Options, i.e. each option therefore is related to a question
class Option(models.Model):
    """
    Represents a Option object - each option corresponds to a Question object
    
    Attributes:
        question (ForeignKey): The question the option corresponds to , represented as a foreign key to the Question model.
        option_text (CharField): The option.
        correct_answer (BooleanField): Is the answer the correct answer to the corresponding question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    # From the list of options select the answer that is correct - to check users score at the end of the quiz
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
    
# Holds a table of results, consisting of the users score of their last attempt of a quiz
class Result(models.Model):
    """
    Represents the results of users for a specific quiz
    
    Attributes:
        quiz (ForeignKey): The quiz, represented as a foreign key to the Quiz model
        user (ForeignKey): The user, represented as a foreign key to the User model.
        passed (BooleanField): Did the user meet the minimum score to pass?
        score_in_percentage (IntegerField): The users score in percentage 
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    score_in_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quiz}, {self.user}, {self.passed}, {self.score_in_percentage}"


