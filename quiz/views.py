from django.shortcuts import render, get_object_or_404
from .models import Question, Option, Quiz, Result
from datetime import datetime
"""
This module contains the view functions for myquizsite django web application

Each view function corresponds to a different URL endpoint in the application, and is responsible for handling incoming
HTTP requests and returning an HTTP response.

Functions:
    index(request):
        Renders the home page of the application.

    topic(request, quiz_id):
        Renders a topic page for each available quiz in the app.

    results(request, quiz_id):
        Renders the results of a submitted quiz

"""

# Create your views here.
def index(request):
    """This method renders the home page of the app
        Each available topic that corresponds to a 
        quiz is displayed. 

        :param HttpRequest request
        
        :returns: Rendered index.html (home) page

        :rtype: HttpResponse object
    """
    quiz_list = Quiz.objects.order_by('pub_date')[:5]
    return render(request, 'quiz/index.html', {'quiz_list': quiz_list})

def topic(request, quiz_id):
    """This method renders the topic page that 
        corresponds to the given quiz_id. 
        The content that relates to the quiz is 
        displayed as well as the quiz for the user 
        to test their knowledge. 

        :param HttpRequest request
        :param int quiz_id
        
        :returns: Rendered topic.html page

        :rtype: HttpResponse object
    """
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    user = request.user
    results = Result.objects.filter(quiz=quiz_id, user=user)
    return render(request, 'quiz/topic.html', {'quiz': quiz, 'results': results})

def results(request, quiz_id):
    """This method renders the results page once 
        a user has answered a quiz and submitted their answers.

        If the user is completing the quiz for the first time 
        or achieves a new high score this score is saved 
        to the database.

        :param HttpRequest request
        :param int quiz_id
        
        :returns: Rendered results.html page

        :rtype: HttpResponse object
    """
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    user = request.user
    # Get list of questions associated with current quiz
    questions=Question.objects.filter(quiz=quiz_id)
    num_questions = len(questions)
    perc_score = 0
    passed = False
    score = 0

    if request.method == "POST":
        user_input = request.POST.items()
        user_input_dict = dict((x, y) for x, y in user_input)
        user_input_dict.pop("csrfmiddlewaretoken")
        
        # Iterate through the user_input (stored in user_input_dict)
        # If the user input is True they have selected the correct answer 
        # Else they have selected an incorrect answer
        for x in user_input_dict:
            if user_input_dict[x] == 'True':
                score+=1
        
        #Calculate score in % and check if user has met the required_score_to_pass
        perc_score = int(round((score/num_questions) * 100,0))

        if perc_score >= quiz.required_score_to_pass: 
            passed = True

    # Update or add the users result to the Results table
    
    last_result_list = Result.objects.filter(quiz=quiz, user=user).values('score_in_percentage')

    if not last_result_list:
        Result.objects.update_or_create(quiz=quiz, user=user, defaults={'passed': passed, 'score_in_percentage': perc_score},)
    
    # Only update the result if the new score is higher than the previous score
    else:
        last_result = last_result_list[0]['score_in_percentage']
        if int(last_result) < perc_score:
            Result.objects.update_or_create(quiz=quiz, user=user, defaults={'passed': passed, 'score_in_percentage': perc_score},)

    return render(request, 'quiz/results.html', {'score': f"{score}/{num_questions}", 'perc_score': perc_score, 'passed' : passed, 'quiz': quiz})
    