from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clinics/create/', views.ClinicCreate.as_view(), name='create_clinic'),
    path('clinics/<int:pk>/', views.ClinicDetail.as_view(), name='detail_clinic'),
    path('clinics/<int:pk>/update/', views.ClinicUpdate.as_view(), name='update_clinic'),
    path('clinics/<int:pk>/delete/', views.ClinicDelete.as_view(), name='delete_clinic')
]