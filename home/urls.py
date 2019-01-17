from django.urls import path
from . import views
from .views import Event_Create,Event_delete,Event_list

app_name = 'event'

urlpatterns = [
    path('list/',Event_list.as_view(),name = 'list'),
    path('create/',Event_Create.as_view(),name = 'event_create'),
    path('delete/<pk>',Event_delete.as_view(),name = 'delete')
] 