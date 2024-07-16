from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home",views.home,name="home"),
    path("addStudent", views.addStudentPage, name="addStudent"),
    path("addStudentDetails",views.addStudent,name="addStudentDetails"),
    path("viewDetails/<student_id>",views.getDetails,name="viewDetails"),
    path("deleteStudent/<student_id>",views.deleteStudent, name="deleteStudent"),
    path("editStudent/<student_id>",views.editStudent, name="editStudent"),
    path("updateData/<id>",views.updateData,name="updateData"),
]
