from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'username', 'age',
                  'type', 'status', 'country', 'city']


class ItSerializer(serializers.ModelSerializer):
    class Meta:
        model = It
        fields = ['title', 'description', 'image']


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'image', 'title', 'created_date']


class ArticlesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['title', 'created_date', 'image', 'description', 'created_date']


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ['image']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificate', 'description']


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True, read_only=True)
    about_us = CertificateSerializer()

    class Meta:
        model = AboutUs
        fields = ['title', 'description', 'images', 'about_us']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'question']


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'question', 'description']


class AboutCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCourses
        fields = ['description']


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'description']


class CoursesDetailSerializer(serializers.ModelSerializer):
    question_course = QuestionListSerializer(many=True, read_only=True)
    about_courses = AboutCoursesSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'access', 'about_courses', 'question_course']


class MasterClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = ['id', 'title', 'description']


class MasterClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = ['title', 'description']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class PaketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paket
        fields = ['id', 'time', 'status', 'price', 'choices']


class PaketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paket
        fields = ['title', 'time', 'status', 'price',
                  'choices', 'description']


class AboutSchoolSerializer(serializers.ModelSerializer):
    courses = CoursesListSerializer(many=True, read_only=True)
    master_class = MasterClassListSerializer(many=True, read_only=True)
    packets =PaketListSerializer(many=True, read_only=True)

    class Meta:
        model = AboutSchool
        fields = ['name', 'description', 'courses',
                  'master_class', 'packets']
