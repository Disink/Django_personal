from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from website.models import SkillGroup
from website.models import Skill
from website.models import Work
from website.models import Contact
from website.models import Link
from website.models import Line
from website.models import Article
from website.models import Image


class SkillGroupAdmin(OrderedModelAdmin):
    list_display = ['title', 'move_up_down_links']

admin.site.register(SkillGroup, SkillGroupAdmin)


class SkillAdmin(OrderedModelAdmin):
    list_display = ['name', 'skill_group', 'move_up_down_links']
    list_filter = ("skill_group",)

admin.site.register(Skill, SkillAdmin)


class WorkAdmin(OrderedModelAdmin):
    list_display = ['name', 'move_up_down_links']

admin.site.register(Work, WorkAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email')

admin.site.register(Contact, ContactAdmin)


class LinkAdmin(OrderedModelAdmin):
    list_display = ['name', 'move_up_down_links']

admin.site.register(Link, LinkAdmin)


class LineAdmin(OrderedModelAdmin):
    list_display = ['line_id', 'token']

admin.site.register(Line, LineAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Article, ArticleAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Image, ImageAdmin)
