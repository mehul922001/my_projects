from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    path('log_out/',views.log_out.as_view(),name='log_out'),
    path('all_clients/',views.all_clients.as_view(),name='all_clients'),
    path('add_client/',views.add_client.as_view(),name='add_client'),
    path('update_client/<int:pk>',views.update_client.as_view(),name='update_client'),
    path('delete/<int:pk>',views.delete.as_view(),name='delete'),
    path('client_details/<int:pk>',views.client_details.as_view(),name='client_details'),
    path('add_project/<int:pk>',views.add_project.as_view(),name='add_project'),
    path('projects/',views.projects.as_view(),name='projects'),
    






]