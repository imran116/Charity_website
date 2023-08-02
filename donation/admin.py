from django.contrib import admin

from donation.models import Menu, Submenu, Slider, Charity, About, AboutOurMissionList, AboutSectionMember, Cause, \
    Volunteer, VolunteerMember, NewsCategory, Tag, AddNews

# Register your models here.
admin.site.register(Menu)
admin.site.register(Submenu)
admin.site.register(Slider)
admin.site.register(Charity)
admin.site.register(About)
admin.site.register(AboutOurMissionList)
admin.site.register(AboutSectionMember)
admin.site.register(Cause)
admin.site.register(Volunteer)
admin.site.register(VolunteerMember)
admin.site.register(NewsCategory)
admin.site.register(Tag)
admin.site.register(AddNews)
