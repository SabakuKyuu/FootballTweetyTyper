# Generated by Django 4.0.6 on 2022-10-03 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_my_tip_post_respect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='respect',
        ),
    ]