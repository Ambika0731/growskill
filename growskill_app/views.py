from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.core.mail import send_mail
from .permissions import IsInstructorOrReadOnly


@api_view(["POST"])
def user_registration_api_view(request):
    if request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            is_instructor = request.data.get("is_instructor", False)
            speciality = request.data.get("speciality", None)
            user_profile_data = {
                "user": user.id,
                "is_instructor": is_instructor,
                "speciality": speciality,
            }
            user_profile_serializer = UserProfileSerializer(data=user_profile_data)
            if user_profile_serializer.is_valid():
                user_profile_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response(
                    user_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def class_create_api_view(request):
    if request.method == "POST":
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def course_create_api_view(request):
    if request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def course_list_api_view(request):
    if request.method == "GET":
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def course_detail_api_view(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)


@api_view(["POST"])
def enrollment_create_api_view(request):
    if request.method == "POST":
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def class_list_api_view(request, course_id):
    if request.method == "GET":
        queryset = Class.objects.filter(course_id=course_id)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def class_detail_api_view(request, id):
    try:
        instance = Class.objects.get(id=id)
    except Class.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ClassSerializer(instance)
        return Response(serializer.data)


@api_view(["GET"])
def class_recordings_list_api_view(request, course_id):
    if request.method == "GET":
        queryset = Class.objects.filter(course_id=course_id, is_completed=True)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def class_recording_detail_api_view(request, id):
    try:
        instance = Class.objects.get(id=id, is_completed=True)
    except Class.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ClassSerializer(instance)
        return Response(serializer.data)


@api_view(["GET"])
def certificate_download_api_view(request, user_id):
    try:
        certificate = Certificate.objects.get(user_id=user_id, is_generated=True)
    except Certificate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)
