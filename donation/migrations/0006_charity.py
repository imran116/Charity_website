# Generated by Django 4.2.3 on 2023-08-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_image', models.ImageField(upload_to='charity-image')),
                ('charity_title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
