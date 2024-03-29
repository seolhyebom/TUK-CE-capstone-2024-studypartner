from django.urls import path
from .views import lecture_list_view
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path('lecture_list/', views.lecture_list_view, name='lecture_list'),
    path('lecture/', views.lecture_view, name='lecture'),
    path('add_lecture_chapter/', views.add_lecture_chapter_view, name='add_lecture_chapter'),
    
    # lecture에 대한 URL 패턴
    path('lecture_detail/<str:lecture_name>/', views.lecture_detail_view, name='lecture_detail'),  # lecture_detail_view
    # chapter에 대한 URL 패턴
    # path('chapter_detail/<str:lecture_name>/<str:chapter_name>/', views.chapter_detail_view, name='chapter_detail'),  # chapter_detail_view

  
]





