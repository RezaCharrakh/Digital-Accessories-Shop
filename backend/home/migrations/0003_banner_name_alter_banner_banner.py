# Generated by Django 5.0.6 on 2024-06-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner',
            field=models.ImageField(upload_to='home/static/src/banners/'),
        ),
    ]