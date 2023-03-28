from django.urls import path
from . import views

urlpatterns = [
    # Example: /polls/
    path('', views.index, name='index'),
    # Example: /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # Example: /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # Example: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]