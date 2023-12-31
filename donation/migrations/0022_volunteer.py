# Generated by Django 4.2.3 on 2023-08-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0021_alter_cause_raised_amount_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_name', models.CharField(max_length=50)),
                ('volunteer_email', models.EmailField(max_length=150)),
                ('volunteer_subject', models.CharField(max_length=150)),
                ('volunteer_message', models.TextField()),
                ('volunteer_file', models.FileField(upload_to='volunteer-file/')),
            ],
        ),
    ]
