# Generated by Django 4.2.5 on 2023-10-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_contact_send_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Xabar', 'verbose_name_plural': 'Xabarlar'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
    ]
