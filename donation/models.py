from django.db import models


# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_display = models.BooleanField(default=True)
    section_id = models.CharField(max_length=10)

    def __str__(self):
        return self.menu_name

    def get_submenu(self):
        return self.submenu_set.all()


class Submenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    sub_menu_name = models.CharField(help_text='without .html eg. home, index, contact ', max_length=20)
    sub_menu_page_name = models.CharField(max_length=20)
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

# about section start
