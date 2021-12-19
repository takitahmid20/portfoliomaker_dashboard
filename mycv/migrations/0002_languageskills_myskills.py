# Generated by Django 3.2.8 on 2021-12-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, max_length=200, null=True)),
                ('skill_percentage', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mycv.profile')),
            ],
        ),
        migrations.CreateModel(
            name='languageSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(blank=True, max_length=200, null=True)),
                ('language_percentage', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mycv.profile')),
            ],
        ),
    ]