from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "This is the january challenge.",
    "february": "This is the february challenge.",
    "march": "This is the march challenge.",
    "april": "This is the april challenge.",
    "may": "This is the may challenge.",
    "june": "This is the june challenge.",
    "july": "This is the july challenge.",
    "august": "This is the august challenge.",
    "september": "This is the september challenge.",
    "october": "This is the october challenge.",
    "november": "This is the november challenge.",
    "december": "This is the december challenge.",
}

def index(request_):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Error: Invalid Month")

    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")
    