# Generated by Django 2.1.7 on 2019-05-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_appeal_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='gamee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cAuthor', models.CharField(blank=True, max_length=50)),
                ('cContent', models.CharField(blank=True, default='', max_length=9999)),
                ('cTitle', models.CharField(blank=True, default='', max_length=100)),
                ('cLink', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]