from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(),name='detail'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('ajax-chat/',views.ajax_chat_add,name='ajax_chat_add'),
    path('junle/<int:pk>',views.JunleView.as_view(),name="junle"),

]
