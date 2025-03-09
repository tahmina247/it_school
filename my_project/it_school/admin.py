from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 1


class AboutSchoolInline(admin.TabularInline):
    model = AboutSchoolSecond
    extra = 1


class RatingUserInline(admin.TabularInline):
    model = RatingUser
    extra = 1


class PaketSecondInline(admin.TabularInline):
    model = PaketSecond
    extra = 1


class QuestionSecondInline( admin.TabularInline):
    model = QuestionSecond
    extra = 1


class AboutSecondInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = AboutSecond
    extra = 1


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 1


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    inlines = [AboutUsImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Rating)
class RatingAdmin(TranslationAdmin):
    inlines = [RatingUserInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Paket)
class PaketAdmin(TranslationAdmin):
    inlines = [PaketSecondInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    inlines = [QuestionSecondInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AboutCourses)
class CourseAdmin(TranslationAdmin):
    inlines = [AboutSecondInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AboutSchool)
class CourseAdmin(TranslationAdmin):
    inlines = [AboutSchoolInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(It, Articles, Courses, MasterClass)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [SocialNetworkInline]


admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(ContactInfo, ContactInfoAdmin)
