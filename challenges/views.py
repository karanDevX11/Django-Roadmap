from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect  #imported http module
from django.urls import reverse

challenges = {  #dictionary to store challenges
    "january": "Learn the basics of Data Structures and Algorithms.",
    "february": "Build a simple CRUD application using Django.",
    "march": "Master advanced Python concepts like decorators and generators.",
    "april": "Solve 30 competitive programming problems on a popular platform like LeetCode.",
    "may": "Build a personal portfolio website using HTML, CSS, and JavaScript.",
    "june": "Learn the basics of SQL and practice queries on sample datasets.",
    "july": "Understand REST APIs and integrate one into a Python project.",
    "august": "Develop a small AI-powered project, such as a chatbot or recommendation system.",
    "september": "Contribute to an open-source project on GitHub.",
    "october": "Master Git and GitHub workflows, including branching and pull requests.",
    "november": "Prepare for technical interviews by practicing 50 coding problems.",
    "december": "Review and document all the projects completed throughout the year."
}

# Create your views here.

def monthly_challenges_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):     #checking month is greater than given keys
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month-1]  #index starts from 0 

    redirect_path = reverse("month-challenge", args= [redirect_month])  #reverse function to redirect path challenges/january

    return HttpResponseRedirect(redirect_path)  #redirects this to monthly_challenges view's url

def monthly_challenges(request, month):  #this is a function based view processing request
    try:   #try block to catch any exception
        challenge_text = challenges[month]    #accessing value from dictionary
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Page not found!") #returns a response to the server after processing the view