# Generated by Django 3.2.8 on 2021-12-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0004_profile_who_are_you'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='project_details',
            field=models.TextField(blank=True),
        ),
    ]
