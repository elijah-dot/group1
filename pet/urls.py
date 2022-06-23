from django.urls import path
from . import views

urlpatterns = [





  path('appointments/',views.user_appointments, name='user_appointments'),
  path('book/',views.available, name='available'),
  path('confirm/<vetName>',views.booking, name='booking'),
  path('del/<appointment>',views.delete_appointment, name='delete_appointment'),

    
    
]