from django.urls import path
from appli1 import views
urlpatterns = [
    path('details/',views.details,name = 'team_details'),
    path('detail/<int:pk>',views.detail,name='team_detail'),
    path('add/',views.create,name = 'create_team'),
    path('ud/<int:pk>',views.update,name= 'update_team'),
    path('dele/<int:pk>',views.delete,name='delete_team'),
]