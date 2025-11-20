from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Reply
from .forms import QuestionForm, ReplyForm


def question_list(request):
    """Display all questions with optional subject filtering"""
    questions = Question.objects.all()
    subject_filter = request.GET.get('subject')

    if subject_filter:
        questions = questions.filter(subject=subject_filter)

    # Get subject choices for filter dropdown
    subjects = Question.SUBJECT_CHOICES

    context = {
        'questions': questions,
        'subjects': subjects,
        'current_subject': subject_filter
    }
    return render(request, 'discussions/question_list.html', context)


def question_detail(request, pk):
    """Display question details and replies"""
    question = get_object_or_404(Question, pk=pk)
    replies = question.replies.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to post a reply.')
            return redirect('login')

        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.question = question
            reply.author = request.user
            reply.save()
            messages.success(request, 'Your reply has been posted!')
            return redirect('question_detail', pk=pk)
    else:
        form = ReplyForm()

    context = {
        'question': question,
        'replies': replies,
        'form': form
    }
    return render(request, 'discussions/question_detail.html', context)


@login_required
def question_create(request):
    """Create a new question"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Your question has been posted!')
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, 'discussions/question_form.html', {'form': form})
