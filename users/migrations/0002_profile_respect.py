# Generated by Django 4.0.6 on 2022-10-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='respect',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
    ]
