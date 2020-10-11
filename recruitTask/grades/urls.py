from django.urls import path
from .views import GradingView, CadidatesView

urlpatterns = [path('summary', CadidatesView.as_view()),
               path('api/add-mark', GradingView.as_view())]
