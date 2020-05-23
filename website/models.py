from django.db import models
from ordered_model.models import OrderedModel

class Skill(OrderedModel):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='skill_image')

    def __str__(self):
        return self.title


class Work(OrderedModel):
    name = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to='work_image')
    content = models.TextField()
    url = models.CharField(max_length=160, blank=True, default='')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    title = models.CharField(max_length=80)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Link(OrderedModel):
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=160)
    image = models.FileField(upload_to='link_image')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=80)
    image = models.FileField(upload_to='public_image')

    def __str__(self):
        return self.name


class Background(OrderedModel):
    name = models.CharField(max_length=80)
    image = models.FileField(upload_to='background_image', blank=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=80)
    line_id = models.CharField(max_length=80)
    token = models.CharField(max_length=200)

    def __str__(self):
        return self.name


STATUS = (
    (0, 'Hidden'),
    (1, 'Show')
)

class Page(OrderedModel):
    name = models.CharField(max_length=80)
    content = models.TextField()
    select_status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()

    def __str__(self):
        return self.name


class Script(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()

    def __str__(self):
        return self.name


class Dynamic(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()

    def __str__(self):
        return self.name
