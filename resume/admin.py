from django.contrib import admin
from .models import Profile, Attribute, Biography, Experience, Skill, Service, ServiceTab, \
    Portfolio, Recommendation, Reference, Client, Article, SentenceIntroduction,\
    DynamicSentence


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['mini_profile_photo', 'first_name', 'phone_number', 'email', 'is_active']
    list_display_links = ['mini_profile_photo', 'first_name']
    list_editable = ['is_active']
    readonly_fields = ['profile_photo']
    fieldsets = [
        ('', {
            'fields': (
                ('photo', 'profile_photo'),
                ('first_name', 'last_name'),
                ('phone_number', 'email'),
                'address',
                'about_me',
            ),
        }),
        ('Social', {
            'classes': ('collapse', 'expanded'),
            'fields': (
                ('twitter', 'facebook'),
                ('instagram', 'pinterest'),
                'youtube',
            )
        }),
        ('', {
            'fields': (
                'is_active',
            )
        })
    ]


@admin.register(SentenceIntroduction)
class SentenceIntroductionAdmin(admin.ModelAdmin):
    list_display = ['mini_profile_photo', 'static_sentence']
    list_display_links = ['mini_profile_photo', 'static_sentence']
    readonly_fields = ['profile_photo']

    fieldsets = [
        ('', {
            'fields': (
                ('photo', 'profile_photo'),
                'static_sentence'
            ),
        }),
        ('Social', {
            'classes': ('collapse', 'expanded'),
            'fields': (
                'dynamic_sentences',
            )
        }),
    ]


@admin.register(DynamicSentence)
class DynamicSentenceAdmin(admin.ModelAdmin):
    list_display = ['sentence', 'is_active']
    list_editable = ['is_active']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ['short_description']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['organization', 'position', 'type']
    list_display_links = ['organization', 'position']
    list_editable = ['type']

    fieldsets = [
        ('', {
            'fields': (
                'organization',
                ('position', 'type'),
                ('since', 'until'),
                'description',
            ),
        }),
    ]


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_price']

    fieldsets = [
        ('', {
            'fields': (
                ('title', 'start_price'),
                'description',
            ),
        }),
    ]


@admin.register(ServiceTab)
class ServiceTabAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['mini_cover_photo', 'title']
    list_display_links = ['mini_cover_photo', 'title']
    readonly_fields = ['cover_photo']

    fieldsets = [
        ('',
         {
            'fields': (
                ('cover', 'cover_photo'),
                'category',
                'title',
            ),
         }),
    ]


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['mini_cover_photo', 'name', 'short_description']
    list_display_links = ['mini_cover_photo', 'name', 'short_description']
    readonly_fields = ['cover_photo']

    fieldsets = [
        ('',
         {
             'fields': (
                 ('photo', 'cover_photo'),
                 ('name', 'rate'),
                 'description',
             ),
         }),
    ]


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['mini_cover_photo', 'photo']
    readonly_fields = ['cover_photo']

    fieldsets = [
        ('',
         {
             'fields': (
                 ('photo', 'cover_photo'),
             ),
         }),
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['mini_cover_photo', 'title', 'short_description', 'is_active']
    list_display_links = ['mini_cover_photo', 'title', 'short_description']
    list_editable = ['is_active']
