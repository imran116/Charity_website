from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from donation.models import Menu, Submenu, Slider, Charity, About, AboutOurMissionList, AboutSectionMember, Cause, \
    Volunteer, VolunteerMember, NewsCategory, Tag, AddNews
from . import forms


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
        context['submenus'] = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['charity'] = Charity.objects.filter(is_active=True)
        context['abouts'] = About.objects.first()
        context['abouts_mission_list'] = AboutOurMissionList.objects.all()
        context['abouts_section_member'] = AboutSectionMember.objects.get()
        context['causes'] = Cause.objects.all()
        context['volunteer_members'] = VolunteerMember.objects.filter(is_active=True)
        context['news_category'] = NewsCategory.objects.all()
        context['news_tags'] = Tag.objects.all()
        context['add_news'] = AddNews.objects.filter(is_draft=False)


        return context


def news_list_view(request):
    return render(request, 'news-list.html')


def volunteer_form_submit(request):
    if request.method == 'POST':
        volunteer_name = request.POST['volunteer_name']
        volunteer_email = request.POST['volunteer_email']
        volunteer_subject = request.POST['volunteer_subject']
        volunteer_message = request.POST['volunteer_message']
        volunteer_file = request.FILES.get('volunteer_file')

        volunteer = Volunteer(volunteer_name=volunteer_name, volunteer_email=volunteer_email, volunteer_subject=volunteer_subject, volunteer_file=volunteer_file, volunteer_message=volunteer_message)
        volunteer.save()
        messages.success(request, "Your Form Submitted.")
        return redirect('home')
    else:
        messages.error(request, "Try Again.")

    return render(request, 'index.html')


# news section start

# news section end