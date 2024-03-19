from django.urls import path
from . import views


urlpatterns = [


    path("", views.emp),
    path("stu",views.stu),

]
