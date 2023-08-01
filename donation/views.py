from django.shortcuts import render
from django.views.generic import TemplateView

from donation.models import Menu, Submenu, Slider, Charity, About, AboutOurMissionList, AboutSectionMember


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(is_active=True, is_display=True)
        context['menus_get_section_id'] = Menu.objects.all()
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['charity'] = Charity.objects.filter(is_active=True)
        context['abouts'] = About.objects.first()
        context['abouts_mission_list'] = AboutOurMissionList.objects.all()
        context['abouts_section_member'] = AboutSectionMember.objects.get()

        return context
