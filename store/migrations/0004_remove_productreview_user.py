# Generated by Django 4.2.1 on 2023-09-14 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='user',
        ),
    ]
