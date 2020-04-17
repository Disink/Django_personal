from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from website.models import Skill
from website.models import Work
from website.models import Contact
from website.models import Link
from website.models import Line
from website.models import Image
from website.models import Background


class SkillAdmin(OrderedModelAdmin):
    list_display = ['title', 'move_up_down_links']

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


class ImageAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Image, ImageAdmin)


class BackgroundAdmin(OrderedModelAdmin):
    list_display = ['name', 'move_up_down_links']

admin.site.register(Background, BackgroundAdmin)
