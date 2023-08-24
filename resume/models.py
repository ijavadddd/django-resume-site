from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.template.defaultfilters import truncatechars
import mimetypes


class Profile(models.Model):
    photo = models.ImageField(upload_to='static/img/profile/')
    first_name = models.CharField(max_length=40,)
    last_name = models.CharField(max_length=40)
    about_me = models.TextField(max_length=300,)
    address = models.CharField(max_length=200,)
    phone_number = models.CharField(max_length=15,)
    email = models.EmailField(max_length=150, null=True, blank=True)
    twitter = models.URLField(null=True, blank=True,)
    facebook = models.URLField(null=True, blank=True,)
    instagram = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True,)
    youtube = models.URLField(null=True, blank=True,)
    is_active = models.BooleanField(default=True)

    def mini_profile_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:50px; max-height:50px;" />')

    def profile_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:100px; max-height:100px;" />')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DynamicSentence(models.Model):
    sentence = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sentence


class SentenceIntroduction(models.Model):
    photo = models.ImageField(upload_to='static/img/profile/')
    static_sentence = models.CharField(max_length=40,)
    dynamic_sentences = models.ManyToManyField(to=DynamicSentence)

    def mini_profile_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:50px; max-height:50px;" />')

    def profile_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:100px; max-height:100px;" />')

    def __str__(self):
        return self.static_sentence


class Attribute(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True,)
    value = models.CharField(max_length=40,)

    def __str__(self):
        if self.title:
            return f'{self.title}: {self.value}'
        return f'{self.value}'


class Biography(models.Model):
    description = RichTextField()
    attributes = models.ManyToManyField(to=Attribute,)

    def short_description(self):
        return truncatechars(mark_safe(self.description), 40)

    def __str__(self):
        return self.short_description()

    class Meta:
        verbose_name = 'Biography'
        verbose_name_plural = 'Biographies'


class Experience(models.Model):
    organization = models.CharField(max_length=100,)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=70,)
    description = RichTextField()
    TYPE_LIST = [
        ('0', 'education'),
        ('1', 'experience'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_LIST)

    def __str__(self):
        return f'{self.organization} - {self.position}'


class Skill(models.Model):
    title = models.CharField(max_length=70,)
    percent = models.IntegerField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_price = models.CharField(max_length=10,)

    def __str__(self):
        return self.title


class ServiceTab(models.Model):
    description = RichTextField()
    services = models.ManyToManyField(to=Service,)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return truncatechars(mark_safe(self.description), 40)


class Portfolio(models.Model):
    cover = models.ImageField(upload_to='static/img/portfolio/')
    title = models.CharField(max_length=50,)

    def mini_cover_photo(self):
        return mark_safe(f'<img src="{self.cover.url}" style="max-width:50px; max-height:50px;" />')

    def cover_photo(self):
        return mark_safe(f'<img src="{self.cover.url}" style="max-width:100px; max-height:100px;" />')

    def __str__(self):
        return self.title


class Recommendation(models.Model):
    photo = models.ImageField(upload_to='static/img/reference/recommendation/')
    name = models.CharField(max_length=40,)
    description = models.TextField(max_length=500,)
    rate = models.IntegerField()

    def mini_cover_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:50px; max-height:50px;" />')

    def cover_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:100px; max-height:100px;" />')

    def short_description(self):
        return truncatechars(self.description, 40)

    def __str__(self):
        return f'{self.name} - {truncatechars(self.description,40)}'


class Reference(models.Model):
    description = RichTextField()
    recommends = models.ManyToManyField(to=Recommendation)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return truncatechars(mark_safe(self.description), 40)


class Client(models.Model):
    photo = models.ImageField(upload_to='static/img/reference/client//')

    def mini_cover_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:50px; max-height:50px;" />')

    def cover_photo(self):
        return mark_safe(f'<img src="{self.photo.url}" style="max-width:100px; max-height:100px;" />')

    def __str__(self):
        return self.photo.url


class Article(models.Model):
    title = models.CharField(max_length=250,)
    cover = models.ImageField(upload_to='static/img/articles/')
    description = RichTextField()
    published_at = models.DateTimeField(auto_created=True,)
    is_active = models.BooleanField(default=True,)

    def mini_cover_photo(self):
        return mark_safe(f'<img src="{self.cover.url}" style="max-width:200px; max-height:50px;" />')

    def cover_photo(self):
        return mark_safe(f'<img src="{self.cover.url}" style="max-width:300px; max-height:100px;" />')

    def short_description(self):
        return truncatechars(mark_safe(self.description) , 40)

    def __str__(self):
        return self.title
