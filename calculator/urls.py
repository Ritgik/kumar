from django.urls import path
from .views import calculator_view

urlpatterns = [
    path('', calculator_view, name='calculator'),  # Root URL of the calculator app
]