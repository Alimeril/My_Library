from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('SignUpPage/', views.SignUpPage.as_view(), name = 'SignUp'),
    path('ListPage/', views.ListPage.as_view(), name = 'ListPage'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('AddPage/', views.AddPage.as_view(), name = 'AddPage'),
    path('<int:pk>/EditPage', views.EditPage.as_view(), name = 'EditPage'),
    path('<int:pk>/DeletePage', views.DeletePage.as_view(), name='DeletePage'),
]