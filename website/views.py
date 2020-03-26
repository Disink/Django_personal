
from django.shortcuts import render

from website.models import SkillGroup
from website.models import Work
from website.models import Link
from website.models import Article
from website.models import Image

from website.forms import ContactForm

from website.lines import send

# Create your views here.
def home_page(request):
    skill_group_list = SkillGroup.objects.all()
    work_list = Work.objects.all()
    link_list = Link.objects.all()

    head_right_article = Article.objects.get(title='head-right-article').content
    head_right_select = Article.objects.get(title='head-right-select').content
    head_left_image = Image.objects.get(name='head-left-image').image

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():

            contact_form.save()
            send(request.POST)

    return render(request, 'home.html', {'skill_group_list': skill_group_list,
                                          'work_list': work_list,
                                          'link_list': link_list,
                                          'head_left_image': head_left_image,
                                          'head_right_article': head_right_article,
                                          'head_right_select': head_right_select,
                                          'comment_form': contact_form,})

