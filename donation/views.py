from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from donation.models import Menu, Submenu, Slider, Charity, About, AboutOurMissionList, AboutSectionMember, Cause, \
    Volunteer, VolunteerMember, NewsCategory, Tag, AddNews, HappyCustomer, GetInTouch, WebsiteSetting, \
    AddDonationAmount, AddDonationPaymentMethod, Comment
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
        context['add_news'] = AddNews.objects.filter(is_draft=False)[:2]
        context['happy_customers'] = HappyCustomer.objects.all()
        context['get_in_touch'] = GetInTouch.objects.get()
        context['website_settings'] = WebsiteSetting.objects.get()

        return context


def volunteer_form_submit(request):
    if request.method == 'POST':
        volunteer_name = request.POST['volunteer_name']
        volunteer_email = request.POST['volunteer_email']
        volunteer_subject = request.POST['volunteer_subject']
        volunteer_message = request.POST['volunteer_message']
        volunteer_file = request.FILES.get('volunteer_file')

        volunteer = Volunteer(volunteer_name=volunteer_name, volunteer_email=volunteer_email,
                              volunteer_subject=volunteer_subject, volunteer_file=volunteer_file,
                              volunteer_message=volunteer_message)
        volunteer.save()
        messages.success(request, "Your Form Submitted.")
        return redirect('home')
    else:
        messages.error(request, "Try Again.")

    return render(request, 'index.html')


# news section start
def all_news_list(request):
    menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
    submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)
    website_settings = WebsiteSetting.objects.get()
    add_news = AddNews.objects.filter(is_draft=False)
    news_category = NewsCategory.objects.all()
    news_tags = Tag.objects.all()
    context = {
        'obj': add_news,
        'menus': menus,
        'submenus': submenus,
        'website_settings': website_settings,
        'news_category': news_category,
        'news_tags': news_tags,
    }
    return render(request, 'news-list.html', context=context)


def get_news_details(request, news_id):
    menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
    submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)

    news = AddNews.objects.get(id=news_id)
    news_category = NewsCategory.objects.all()
    news_tags = Tag.objects.all()
    website_settings = WebsiteSetting.objects.get()

    context = {
        'newsObj': news,
        'news_category': news_category,
        'news_tags': news_tags,
        'menus': menus,
        'submenus': submenus,
        'website_settings': website_settings,

    }
    return render(request, 'news-detail.html', context=context)


# news section end

# category items show start
def get_specific_category(request, category_id):
    menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
    submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)

    news_category = NewsCategory.objects.all()
    news_tags = Tag.objects.all()
    category = NewsCategory.objects.get(pk=category_id)
    obj = AddNews.objects.filter(category=category)
    website_settings = WebsiteSetting.objects.get()
    context = {
        'obj': obj,
        'news_category': news_category,
        'news_tags': news_tags,
        'website_settings': website_settings,
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, 'news-list.html', context=context)


# category item show end

# tag item show start

def get_specific_tag_item(request, tag_id):
    menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
    submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)

    news_category = NewsCategory.objects.all()
    news_tags = Tag.objects.all()
    tag_name = Tag.objects.get(pk=tag_id)
    obj = AddNews.objects.filter(tags=tag_name)
    website_settings = WebsiteSetting.objects.get()
    context = {
        'obj': obj,
        'news_category': news_category,
        'news_tags': news_tags,
        'website_settings': website_settings,
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, 'news-list.html', context=context)


# tag item show end

# newsletter section start
class NewsLetterView(View):
    def post(self, request):
        form = forms.NewsLetterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribe Complete.")
            return redirect('home')
        else:
            messages.error(request, "Try Again.f")
            return redirect('home')


# newsletter section end


# contact section start

class ContactView(View):
    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message Send.")
            return redirect('home')
        else:
            messages.error(request, "Please Try Again.")
            return redirect('home')


# contact section end


# donation section start

def donation_view(request):
    donation_amount = AddDonationAmount.objects.all()
    payment_method = AddDonationPaymentMethod.objects.all()
    menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
    submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)
    website_settings = WebsiteSetting.objects.get()

    context = {
        'donation_amount': donation_amount,
        'payment_method': payment_method,
        'website_settings': website_settings,
        'menus': menus,
        'submenus': submenus,
    }

    return render(request, 'donate.html', context=context)


class DonationPayment(View):

    def get(self, request):
        return render(request, 'donate.html')

    def post(self, request):
        donation_amount = AddDonationAmount.objects.all()
        payment_method = AddDonationPaymentMethod.objects.all()
        menus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=False)
        submenus = Menu.objects.filter(is_active=True, is_display=True, is_dropdown_menu=True)
        website_settings = WebsiteSetting.objects.get()
        form = forms.DonationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Donation Data Submit")
            return redirect('donation')
        else:
            messages.error(request, "Try Again!")
            print(form.errors)
            return render(request, 'donate.html', {'form': form,
                                                   'website_settings': website_settings,
                                                   'menus': menus,
                                                   'submenus': submenus,
                                                   })


# donation section end

# Register section start

class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = forms.RegisterForm(data=request.POST)
        password = form.data['password']
        confirm_password = form.data['confirm_password']
        if password == confirm_password:
            if form.is_valid():
                password = form.data['password']
                user = form.save()
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                messages.error(request, "Username Already Exists")
                return render(request, 'register.html', {'form': form})
        else:
            messages.error(request, "Password Don't Match.")
            return render(request, 'register.html', {'form': form})


# Register section end


# login section start

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']

            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    messages.success(request, "Login Successful.")
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "User Not Found!")
                    return render(request, 'login.html', {'form': form})
            except ObjectDoesNotExist:
                messages.error(request, "Invalid Credentials!")
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, "Invalid Credentials!")
            return render(request, 'login.html', {'form': form})


# login section end

# logout section start
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


# logout section end


# comment section start

class CommentView(View):
    def post(self, request, news_id):
        form = forms.CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.data['comment']
            Comment.objects.create(

                user=self.request.user,
                add_news_id=news_id,
                comment=comment

            ).save()
        else:
            messages.error(request, "Invalid Data!")

        return redirect(f"/news-details/{news_id}/")

# comment section end
