
from django.shortcuts import render

from website.models import Skill
from website.models import Work
from website.models import Link
from website.models import Image
from website.models import Background

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

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():

            contact_form.save()
            send(request.POST)

    return render(request, 'home.html', {'skill_list': skill_list,
                                          'work_list': work_list,
                                          'link_list': link_list,
                                          'background_list': gackground_list,
                                          'head_left_image': head_left_image,
                                          'head_background': head_background,
                                          'comment_form': contact_form,})

