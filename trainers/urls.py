from django.urls import path
from . import views
from .views import TrainerFormView, TrainersListView, TrainerDetailView

app_name = "trainers"
urlpatterns = [
    path('', views.TrainerFormView.as_view(), name='trainer_create'),
    # #trainer URLs
    path('', views.TrainersListView.as_view(), name='trainer'),
    path('trainers/', views.TrainersListView.as_view(), name='trainer_view'),
    path('trainers/add/', TrainerFormView.as_view(), name='add_trainer'),
    path('<str:trainer_id>', views.TrainerDetailView.as_view(), name='trainer_one'),
    path('toggle-status/<str:pk>/', views.TrainerToggleStatus.as_view(), name='trainer_toggle_status'),
     # Colleges URLs
    path('colleges/', views.colleges_view, name='colleges'),
    path('colleges/add/', views.add_college, name='add_college'),
    # Degree URLs
    path('degrees/', views.degrees_view, name='degrees'),
    path('degrees/add/', views.add_degree, name='add_degree'),
    # Organization URLs
    path('organizations/', views.organizations_view, name='organizations'),
    path('organizations/add/', views.add_organization, name='add_organization'),   
    # Qualification URLs
    path('qualifications/', views.qualifications_view, name='qualifications'),
    path('qualifications/add/', views.add_qualification, name='add_qualification'),  
    # Award URLs
    path('awards/', views.awards_view, name='awards'),
    path('awards/add/', views.add_award, name='add_award'),
    path('index/', views.index_page, name='index'),
    #trainer URLs
    # path('trainers/', views.trainers_view, name='trainers'),  
    # path('add_trainer/', views.add_trainer, name='add_trainer'),  
]
