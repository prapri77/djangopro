from django.urls import path
from . import views


urlpatterns = [

    path("stu",views.stu),
    path("",views.home, name="home"),
    path("adddata",views.adddata, name="adddata"),
    path("updatedata/<int:id>",views.updatedata, name="updatedata"),
    path("deletedata/<int:id>", views.deletedata, name="deletedata"),


]
