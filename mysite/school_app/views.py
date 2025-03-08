from rest_framework import viewsets, generics
from .serilaizers import *
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ItListApiView(generics.ListAPIView):
    queryset = It.objects.all()
    serializer_class = ItSerializer


class ArticlesListView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesListSerializer


class ArticlesDetailView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesDetailSerializer


class AboutUsApiView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsImageViewSet(viewsets.ModelViewSet):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CoursesListAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesListSerializer


class CoursesDetailAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesDetailSerializer


class QuestionListApiView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionDetailAPIlView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer


class MasterClassListAPIView(generics.ListAPIView):
    queryset = MasterClass.objects.all()
    serializer_class = MasterClassListSerializer


class MasterClassDetailAPIView(generics.RetrieveAPIView):
    queryset = MasterClass.objects.all()
    serializer_class = MasterClassDetailSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class AboutCoursesAPiView(generics.ListAPIView):
    queryset = AboutCourses.objects.all()
    serializer_class = AboutCoursesSerializer


class PaketListAPIView(generics.ListAPIView):
    queryset = Paket.objects.all()
    serializer_class = PaketListSerializer


class PaketDetailAPIView(generics.RetrieveAPIView):
    queryset = Paket.objects.all()
    serializer_class = PaketDetailSerializer


class AboutSchoolAPIView(generics.ListAPIView):
    queryset = AboutSchool.objects.all()
    serializer_class = AboutSchoolSerializer