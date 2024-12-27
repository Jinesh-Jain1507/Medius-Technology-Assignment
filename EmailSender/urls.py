from django.contrib import admin
from django.urls import path
from assignment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendemail/', views.send_email, name='send_email'),
]
