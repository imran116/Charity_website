# Generated by Django 4.2.3 on 2023-08-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0037_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='custom_amount',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
