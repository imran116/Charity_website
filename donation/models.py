from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render


# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=20)
    id_or_href = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_display = models.BooleanField(default=True)
    is_dropdown_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.menu_name

    def get_submenu(self):
        return self.submenu_set.filter(is_active=True)


class Submenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, limit_choices_to={"is_dropdown_menu": True})
    sub_menu_name = models.CharField(help_text='without .html eg. home, index, contact ', max_length=20)
    id_or_href = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_menu_name


# slider section start

class Slider(models.Model):
    slider_image = models.ImageField(upload_to='slider-image')
    slider_title = models.CharField(max_length=100)
    slider_sub_title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.slider_title


# slider section end


# charity section start
class Charity(models.Model):
    charity_image = models.ImageField(upload_to='charity-image')
    charity_title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.charity_title


# charity section end

# about section start
class About(models.Model):
    about_image = models.ImageField(upload_to='about/')
    about_title = models.CharField(max_length=150)
    about_sub_title = models.CharField(max_length=150)
    about_description = models.TextField()
    founded_year = models.IntegerField(default=0)
    total_donations = models.IntegerField(default=0)
    total_donations_unit = models.CharField(max_length=20)
    our_mission_description = models.TextField()
    quote = models.CharField(max_length=50)

    def __str__(self):
        return self.about_title


class AboutOurMissionList(models.Model):
    mission_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mission_name


class AboutSectionMember(models.Model):
    image = models.ImageField(upload_to='about-section-member/')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    about = models.TextField()
    facebook_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    instagram_link = models.CharField(max_length=150)


# about section end

# cause section start
class Cause(models.Model):
    image = models.ImageField(upload_to='causes/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    raised_amount = models.IntegerField(default=0)
    goal_amount = models.IntegerField(default=0)
    raised_amount_percentage = models.PositiveIntegerField(default=0)


# cause section end


# volunteer section start
class Volunteer(models.Model):
    volunteer_name = models.CharField(max_length=50)
    volunteer_email = models.EmailField(unique=True)
    volunteer_subject = models.CharField(max_length=150)
    volunteer_message = models.TextField()
    volunteer_file = models.FileField(upload_to='volunteer-file/')


class VolunteerMember(models.Model):
    image = models.ImageField(upload_to='volunteer-member/')
    name = models.CharField(max_length=100)
    about = models.TextField()
    is_active = models.BooleanField(default=True)


# volunteer section end


# news section start

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class AddNews(models.Model):
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(NewsCategory)

    image_1 = models.ImageField(upload_to='news/')
    image_2 = models.ImageField(upload_to='news/')
    image_3 = models.ImageField(upload_to='news/')
    news_title = models.CharField(max_length=250)
    news_description = models.TextField()
    news_quote = models.CharField(max_length=200)
    news_author_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=False)

    @property
    def get_short_desc(self):
        return self.news_description[:150]

    def get_last_desc(self):
        return self.news_description[-250:]

    def get_recent_news(self):
        return AddNews.objects.filter(is_draft=False)[:2]

    def get_related_news(self):
        return AddNews.objects.filter(tags__in=self.tags.all())[:2]

    def __str__(self):
        return self.news_title

    def get_comment(self):
        return self.comment_set.all()


# news section end

# newsletter section start

class Newsletter(models.Model):
    news_letter_email = models.EmailField(unique=True)

    def __str__(self):
        return self.news_letter_email


# newsletter section end


# happy customer section start

class HappyCustomer(models.Model):
    customer_image = models.ImageField(upload_to='happy-customer/')
    customer_name = models.CharField(max_length=50)
    customer_quote = models.CharField(max_length=250)


# happy customer section end


# get_in_touch section start

class GetInTouch(models.Model):
    member_image = models.ImageField(upload_to='get-in-touch-member/')
    member_name = models.CharField(max_length=100)
    member_position = models.CharField(max_length=100)
    member_address = models.CharField(max_length=100)
    member_mobile_no = models.CharField(max_length=20)
    member_email = models.CharField(max_length=200)

    def __str__(self):
        return self.member_name


# get_in_touch section end

# contact form  section start

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.first_name


# contact form section end


# donation section start

class AddDonationAmount(models.Model):
    donation_amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.donation_amount)


class AddDonationPaymentMethod(models.Model):
    donation_payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.donation_payment_method


class Donation(models.Model):
    DonationFrequency = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    custom_amount = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# donation section end


# website setting start
class WebsiteSetting(models.Model):
    navbar_logo = models.ImageField(upload_to='logo/')
    footer_logo = models.ImageField(upload_to='logo/')
    copyright = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    facebook_link = models.CharField(max_length=250)
    youtube_link = models.CharField(max_length=250)
    instagram_link = models.CharField(max_length=250)
    twitter_link = models.CharField(max_length=250)
    linkedin_link = models.CharField(max_length=250)

    def __str__(self):
        return self.email


# website setting end

# comment section start

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_news = models.ForeignKey(AddNews, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}: {self.user.id}"

# comment section end
