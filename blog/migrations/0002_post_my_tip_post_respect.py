# Generated by Django 4.0.6 on 2022-09-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='my_tip',
            field=models.CharField(default=0, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='respect',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
    ]