from django.db.models import F
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
"""The render() function takes the request object as its first argument, 
a template name as its second argument and a dictionary as its optional 
third argument. It returns an HttpResponse object of the given template rendered with the given co"""
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Question, Choice

# Create your views here.

""" def index(request):
    return HttpResponse("Hello, world. You're at the polls index.") """

""" def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output) """

""" def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(template.render(context, request)) """

""" def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render(request, "polls/index.html", context) """

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published
        questions."""
        return Question.objects.order_by("-pub_date")[:5]
    


""" def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id) """

"""def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, "polls/detail.html", { "question" : question}) """

""" def detail(request, question_id):
    '''
    The get_object_or_404() function takes a Django model 
    as its first argument and an arbitrary number of keyword arguments,
    which it passes to the get() function of the model’s manager. 
    It raises Http404 if the object doesn’t exist.

    There’s also a get_list_or_404() function, which works just as 
    get_object_or_404() – except using filter() instead of get(). 
    It raises Http404 if the list is empty.
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", { "question" : question}) """

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


""" def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) """

""" def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 
                  "polls/results.html", {"question": question}) """

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



""" def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id) """

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html", 
                      {'question': question,
                       "error_message" : "You didn't select a choice.",
                       }
                )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))