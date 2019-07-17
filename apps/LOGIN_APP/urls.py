from django.conf.urls import url
from apps.LOGIN_APP import views
                    
urlpatterns = [
    url(r'^process/registration$', views.processRegistration), 
    url(r'^process/login$', views.processLogin), 
    url(r'^user(?P<userID>\d+)$', views.userPage), # should refer to things specific to a user
    url(r'^success/$', views.success), 
    url(r'^logout/$', views.logout), 
    url(r'^$', views.index),
]