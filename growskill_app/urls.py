from django.urls import path
from .views import *

urlpatterns = [
    path("user/register/", user_registration_api_view, name="user_register"),
    path("class/create/", class_create_api_view, name="class_create"),
    path("course/create/", course_create_api_view, name="course_create"),
    path("courses/", course_list_api_view, name="course_list"),
    path("courses/<int:id>/", course_detail_api_view, name="course_detail"),
    path("enrollment/create/", enrollment_create_api_view, name="enrollment_create"),
    path("courses/<int:course_id>/classes/", class_list_api_view, name="class_list"),
    path("classes/<int:id>/", class_detail_api_view, name="class_detail"),
    path(
        "courses/<int:course_id>/recordings/",
        class_recordings_list_api_view,
        name="class_recordings_list",
    ),
    path(
        "recordings/<int:id>/",
        class_recording_detail_api_view,
        name="class_recording_detail",
    ),
    path(
        "certificate/<int:user_id>/",
        certificate_download_api_view,
        name="certificate_download",
    ),
]
