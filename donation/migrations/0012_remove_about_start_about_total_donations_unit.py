# Generated by Django 4.2.3 on 2023-08-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0011_alter_about_founded_year_alter_about_total_donations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='start',
        ),
        migrations.AddField(
            model_name='about',
            name='total_donations_unit',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
