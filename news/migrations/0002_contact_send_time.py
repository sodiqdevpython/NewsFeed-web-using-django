# Generated by Django 4.2.5 on 2023-09-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='send_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
