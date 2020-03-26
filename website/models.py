from django.db import models
from ordered_model.models import OrderedModel

class SkillGroup(OrderedModel):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Skill(OrderedModel):
    skill_group = models.ForeignKey(SkillGroup, on_delete= models.CASCADE, related_name='skills')
    name =  models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name



class Work(OrderedModel):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='work_image')
    content = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    title = models.CharField(max_length=80)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Link(OrderedModel):
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=160)
    image = models.FileField(upload_to='link_image')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(OrderedModel):
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='public_image')

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=80)
    line_id = models.CharField(max_length=80)
    token = models.CharField(max_length=200)

    def __str__(self):
        return self.name

