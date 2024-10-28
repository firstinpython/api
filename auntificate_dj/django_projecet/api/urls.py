from django.urls import path,include
from . import views

urlpatterns = [
    path("videos/",views.VideoList.as_view()),
    path("create_videos/",views.VideoCreate.as_view()),
    path("auth/",include("rest_framework.urls"))
]