# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.urls import path
from . import views

# Name-spacing URL names
app_name = "polls"


# path() argument: ROUTE
###############################
# When processing a request, Django starts at the first pattern 
#in urlpatterns and makes its way down the list, 
#comparing the requested URL against each pattern until 
#it finds one that matches.

# path() argument: VIEW
###############################
# When Django finds a matching pattern, 
#it calls the specified view function with an HttpRequest object 
#as the first argument and any “captured” values from the route as keyword arguments. 

# path() argument: KWARGS
###############################
# Arbitrary keyword arguments can be passed in a dictionary to the target view. 
#We aren’t going to use this feature of Django in the tutorial.

# path() argument: NAME
###############################
# Naming your URL lets you refer to it unambiguously from elsewhere in Django, 
#especially from within templates. This powerful feature allows you to make 
#global changes to the URL patterns of your project while only touching a single file.

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
