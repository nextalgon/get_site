from django.urls import path
from .views import get_site
urlpatterns = [
    path('get/', get_site),

]
