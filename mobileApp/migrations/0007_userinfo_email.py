# Generated by Django 3.0.8 on 2021-02-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileApp', '0006_members_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]