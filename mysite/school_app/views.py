from rest_framework import viewsets, generics
from .serilaizers import *
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ItViewSet(viewsets.ModelViewSet):
    queryset = It.objects.all()
    serializer_class = ItSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsImageViewSet(viewsets.ModelViewSet):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class MasterClassViewSet(viewsets.ModelViewSet):
    queryset = MasterClass.objects.all()
    serializer_class = MasterClassSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class AboutCoursesViewSet(viewsets.ModelViewSet):
    queryset = AboutCourses.objects.all()
    serializer_class = AboutCoursesSerializer


class PaketViewSet(viewsets.ModelViewSet):
    queryset = Paket.objects.all()
    serializer_class = PaketSerializer