
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, JsonResponse

from django.core.exceptions import ObjectDoesNotExist

from website.models import Skill
from website.models import Work
from website.models import Link
from website.models import Image
from website.models import Background
from website.models import Contact
from website.models import Page

from website.forms import ContactForm

from website.lines import send

# Create your views here.
def home_page(request):
    skill_list = Skill.objects.all()
    work_list = Work.objects.all()
    link_list = Link.objects.all()
    gackground_list = Background.objects.all()

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
