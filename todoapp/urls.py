from django.urls import path

from .views import CustomLoginView, Detail, TaskDelete, TaskUpdate, Tasklist,TaskCreate,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('',Tasklist.as_view(),name='tasks'),
    path("task/<int:pk>/", Detail.as_view(), name="detailview"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    path("register/", RegisterPage.as_view(), name="register")
   
    
]
