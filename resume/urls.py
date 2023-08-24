from django.urls import path
from .views import ResumeView, ProfileAjaxAdminView


app_name = 'resume'
urlpatterns = [
    path('', ResumeView.as_view(), name='index'),
    path('admin/profile-ajax', ProfileAjaxAdminView.as_view()),
]
