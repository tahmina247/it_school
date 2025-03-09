from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'username', 'age',
                  'type', 'status', 'country', 'city']


class ArticlesListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Articles
        fields = ['id', 'image', 'title', 'created_date']


class ArticlesDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Articles
        fields = ['id','title', 'image', 'description', 'created_date']


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ['image']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name','certificate', 'description']


class QuestionSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSecond
        fields = ['id', 'question', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    all_question = QuestionSecondSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        fields = ['id','title','all_question']


class ItSerializer(serializers.ModelSerializer):
    articles = ArticlesListSerializer(many=True, read_only=True)
    question_it = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = It
        fields = ['title', 'description', 'image', 'articles', 'question_it']


class AboutSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSecond
        fields = ['id', 'title', 'description']


class AboutCoursesSerializer(serializers.ModelSerializer):
    about_second = AboutSecondSerializer(read_only=True, many=True)
    class Meta:
        model = AboutCourses
        fields = ['title', 'about','description', 'about_second']


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name','course_name', 'description']


class CoursesDetailSerializer(serializers.ModelSerializer):
    question_course = QuestionSerializer(many=True, read_only=True)
    about_courses = AboutCoursesSerializer(many=True, read_only=True)
    class Meta:
        model = Courses
        fields = [ 'access','included', 'about_courses', 'question_course']


class MasterClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = ['id','name','master_name', 'description']


class MasterClassDetailSerializer(serializers.ModelSerializer):
    about_master_class = AboutCoursesSerializer(read_only=True, many=True)
    question_master = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = MasterClass
        fields = ['about_master_class', 'access', 'included','question_master' ]


class RatingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingUser
        fields = ['id','name', 'description', 'image']


class RatingSerializer(serializers.ModelSerializer):
    rating_user = RatingUserSerializer(many=True, read_only=True)
    class Meta:
        model = Rating
        fields = ['title', 'rating_user']


class PaketSecondSerializer(serializers.ModelSerializer):
    class Meta:
     model = PaketSecond
     fields = ['id', 'time', 'price', 'choices', 'status']


class PaketSerializer(serializers.ModelSerializer):
    paket  = PaketSecondSerializer(read_only=True, many=True)
    question_paket = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Paket
        fields = ['title','paket','description', 'question_paket']


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True, read_only=True)
    certificate = CertificateSerializer(read_only=True, many=True)
    rating_about = RatingSerializer(read_only=True, many=True)
    class Meta:
        model = AboutUs
        fields = ['title', 'description', 'images', 'certificate', 'rating_about']


class AboutSchoolSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSchoolSecond
        fields = ['title', 'school_description']


class AboutSchoolSerializer(serializers.ModelSerializer):
    courses = CoursesListSerializer(many=True, read_only=True)
    master_class = MasterClassListSerializer(many=True, read_only=True)
    packets =PaketSerializer(many=True, read_only=True)
    school_rating = RatingSerializer(read_only=True, many=True)
    school = AboutSchoolSecondSerializer(read_only=True, many=True)
    class Meta:
        model = AboutSchool
        fields = ['about_school', 'school', 'courses',
                  'master_class', 'packets', 'school_rating']


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['id', 'network_name', 'network_url']


class ContactInfoSerializer(serializers.ModelSerializer):
    contact = SocialNetworkSerializer(read_only=True, many=True)
    class Meta:
        model = ContactInfo
        fields = ['id', 'contact_number', 'email', 'contact']