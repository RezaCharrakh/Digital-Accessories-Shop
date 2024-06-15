# Generated by Django 5.0.6 on 2024-06-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_link_banner_button_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='name',
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_type',
            field=models.CharField(choices=[('head_banner', 'HeadBanner'), ('ad_banner', 'AdBanner')], default='null', max_length=50),
        ),
    ]