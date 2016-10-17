from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .models import Book,Question,Choice

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:2]
    heading = ['Home','Contestants','Register','Login','Contact']
    return render(request, 'website2/index2.html', {'heading':heading, 'book_list':book_list,'title_head':'Vote', 'title_header':'Voting centre'})


'''def vote(request, question_id):
    #handle voting dor a particular choice in a particular question
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'website/detail.html', {'question':question,
                      'error_message':"You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('website:results',
                                            args=(question.id,)))'''
