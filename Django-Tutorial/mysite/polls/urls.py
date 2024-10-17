
from django.urls import path #importing pathing/paths from django.urls library

from . import views # importing our content from views.py (?)

app_name = "polls"
 # set url pattern and pathing to be set as index
urlpatterns = [
    #ex : /polls/
    path("", views.IndexView.as_view(), name= "index"),
    # polls/5/ (where we are on question 5)
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    # polls/5/results/
    path("<int:pk>/results", views.ResultsView.as_view(), name = "results"),
    # polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name = "vote"),
    
]
    
