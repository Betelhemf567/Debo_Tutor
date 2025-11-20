from django.shortcuts import render
from discussions.models import Question
from resources.models import Resource
from django.contrib.auth.models import User


def home(request):
    # Get recent activity
    recent_questions = Question.objects.all()[:5]
    recent_resources = Resource.objects.all()[:5]
    total_users = User.objects.count()
    total_questions = Question.objects.count()
    total_resources = Resource.objects.count()

    context = {
        'recent_questions': recent_questions,
        'recent_resources': recent_resources,
        'total_users': total_users,
        'total_questions': total_questions,
        'total_resources': total_resources,
    }
    return render(request, 'home.html', context)
