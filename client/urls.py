from django.urls import path
from client.views import *




urlpatterns = [
    path('index/',index,name="index"),
    path('', ClientLogin.as_view(), name = 'login'),
    path('search/',search,name='search'),
    path('delete/<int:id>/',delete,name='delete'),
    path('bohsqa/', ClientLogin.as_view(), name = 'loginn'),
    path('logout/', clinet_logout, name = 'logout'),
    path('registration/', ClientRegistration.as_view(), name='registration'),
]