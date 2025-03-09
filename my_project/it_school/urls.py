from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('it/', ItListApiView.as_view(), name='it'),
    path('articles/', ArticlesListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', ArticlesDetailView.as_view(), name='articles_detail'),
    path('about_us/', AboutUsApiView.as_view(), name='about_us'),
    path('course/', CoursesListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CoursesDetailAPIView.as_view(), name='course_detail'),
    path('master_class/', MasterClassListAPIView.as_view(), name='master_class_list'),
    path('master_class/<int:pk>/', MasterClassDetailAPIView.as_view(), name='master_class_detail'),
    path('paket/', PaketListAPIView.as_view(), name='packet_list'),
    path('paket/<int:pk>/', PaketDetailAPIView.as_view(), name='paket_detail'),
    path('about_school/', AboutSchoolAPIView.as_view(), name='about_school'),
    path('questions/', QuestionApiView.as_view(), name='questions'),
    path('contact/', ContactInfoViewSet.as_view(), name='contact')
]