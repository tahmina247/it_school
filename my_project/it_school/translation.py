from .models import (It, Articles, AboutUs, AboutSchool, Courses, Question,
                     MasterClass, Rating, AboutCourses, Paket, AboutSecond,)
from modeltranslation.translator import TranslationOptions,register


@register(It)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Articles)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutUs)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutSchool)
class ProductTranslationOptions(TranslationOptions):
    fields = ('about_school', )


@register(Courses)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','course_name', 'description', 'access', 'included')


@register(MasterClass)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','master_name', 'description', 'access', 'included')


@register(Question)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Rating)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AboutCourses)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','about','description')


@register(AboutSecond)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description')


@register(Paket)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')