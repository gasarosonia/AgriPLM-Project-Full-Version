# Generated by Django 5.0.7 on 2024-07-23 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofiles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_profile',
        ),
    ]
