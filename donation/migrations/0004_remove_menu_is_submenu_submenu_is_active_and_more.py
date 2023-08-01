# Generated by Django 4.2.3 on 2023-08-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_submenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='is_submenu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='sub_menu_page_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sub_menu_name',
            field=models.CharField(help_text='without .html eg. home, index, contact ', max_length=20),
        ),
    ]
