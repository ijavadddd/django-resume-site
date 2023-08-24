from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile, SentenceIntroduction, Biography, Experience, Skill, ServiceTab, Portfolio, Reference,\
    Client, Article


class ResumeView(TemplateView):
    template_name = 'resume/index.html'


class ProfileView(TemplateView):
    template_name = 'resume/profile_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['profile'] = Profile.objects.get(is_active=True)
        except:
            pass
        return context


class SentenceIntroductionView(TemplateView):
    template_name = 'resume/sentence_into_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['sentence_introduction'] = SentenceIntroduction.objects.get()
        except:
            pass
        return context


class BiographyView(TemplateView):
    template_name = 'resume/biography_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['biography'] = Biography.objects.get()
        except:
            pass
        return context


class EducationView(TemplateView):
    template_name = 'resume/experience_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience'] = Experience.objects.filter(type='0')
        context['type'] = 'Education'
        return context


class ExperienceView(TemplateView):
    template_name = 'resume/experience_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience'] = Experience.objects.filter(type='1')
        context['type'] = 'Experience'
        return context


class SkillsView(TemplateView):
    template_name = 'resume/skills_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.filter()
        return context


class ServicesView(TemplateView):
    template_name = 'resume/services_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['service_tab'] = ServiceTab.objects.get(is_active=True)
        except:
            pass
        return context


class PortfolioView(TemplateView):
    template_name = 'resume/portfolio_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['portfolios'] = Portfolio.objects.all()
        except:
            pass
        return context


class ReferencesView(TemplateView):
    template_name = 'resume/references_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['reference'] = Reference.objects.get(is_active=True)
        except:
            pass
        return context


class ClientsView(TemplateView):
    template_name = 'resume/clients_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['clients'] = Client.objects.all()
        except:
            pass
        return context


class ArticlesView(TemplateView):
    template_name = 'resume/articles_include.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['articles'] = Article.objects.filter(is_active=True)
        except:
            pass
        return context


class ProfileAjaxAdminView(TemplateView):
    template_name = 'resume/admin/profile_ajax.html'
