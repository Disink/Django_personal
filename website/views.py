from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, JsonResponse

from html.parser import HTMLParser

from django.core.exceptions import ObjectDoesNotExist

from django import template

from website.models import Skill
from website.models import Work
from website.models import Link
from website.models import Image
from website.models import Background
from website.models import Contact
from website.models import Page
from website.models import Style
from website.models import Script
from website.models import Template

from website.forms import ContactForm

from website.lines import send

def home_page(request):
    skill_list = Skill.objects.all()
    work_list = Work.objects.all()
    link_list = Link.objects.all()
    gackground_list = Background.objects.all()
    style_list = Style.objects.all()
    script_list = Script.objects.all()

    head_left_image = Image.objects.get(name='head-left-image').image
    head_background = Image.objects.get(name='head-background').image

    contact_form = ContactForm()

#    if request.method == 'POST':
#        contact_form = ContactForm(data=request.POST)
#        if contact_form.is_valid():
#
#            contact_form.save()

    return render(request, 'home.html', {'skill_list': skill_list,
                                         'work_list': work_list,
                                         'link_list': link_list,
                                         'background_list': gackground_list,
                                         'head_left_image': head_left_image,
                                         'head_background': head_background,
                                         'comment_form': contact_form,})

def template_page(request, page_type, page):
    template_content = Template.objects.get(name=page).content

    skill_list = Skill.objects.all()
    work_list = Work.objects.all()
    link_list = Link.objects.all()
    gackground_list = Background.objects.all()
    style_list = Style.objects.all()
    script_list = Script.objects.all()

    context_list = template.RequestContext(request,{'skill_list': skill_list,
                                                    'work_list': work_list,
                                                    'link_list': link_list,
                                                    'background_list': gackground_list,
                                                    'style_list': style_list,
                                                    'script_list': script_list,})

    first_template = template.Template(template_content)
    first_render =  HTMLParser().unescape(first_template.render(context_list))

    second_template = template.Template(first_render)
    second_render = second_template.render(context_list)

    response_type = 'text/' + page_type

    return HttpResponse(second_render, content_type=response_type)

@require_http_methods(['POST'])
def contact_api_page(request):
    response = {}
    try:
        name_text = request.POST['name']
        email_text = request.POST['email']
        title_text = request.POST['title']
        message_text = request.POST['message']
        contact_ = Contact.objects.create(name=name_text,
                                          email=email_text,
                                          title=title_text,
                                          message=message_text)
        send(request.POST)
        response['msg'] = 'Ok'
    except ObjectDoesNotExist:
        response['msg'] = 'Error'

    return JsonResponse(response)

@require_http_methods(['GET'])
def page_api_page(request):
    response = {}
    try:
        response['page'] = list(Page.objects.all().values())
    except ObjectDoesNotExist:
        response['msg'] = 'Error'

    return JsonResponse(response)

@require_http_methods(['GET'])
def page_data_api_page(request):
    response = {}
    try:
        response['skill'] = list(Skill.objects.all().values())
        response['work'] = list(Work.objects.all().values())
        response['link'] = list(Link.objects.all().values())
    except ObjectDoesNotExist:
        response['msg'] = 'Error'

    return JsonResponse(response)
