# Generated by Django 4.2.3 on 2023-08-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0008_about_about_image_alter_about_total_donations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='total_donations',
            field=models.CharField(max_length=20),
        ),
    ]
