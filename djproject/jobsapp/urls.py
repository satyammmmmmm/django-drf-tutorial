
from django.urls import path 
from .import views

urlpatterns = [
 
    path('hyderabad/',views.hyderabad_jobs_view),
    path('blr/',views.banglore_jobs_view),
    path('ncr/',views.ncr_jobs_view),
]
