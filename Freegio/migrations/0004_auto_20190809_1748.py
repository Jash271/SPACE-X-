# Generated by Django 2.2.2 on 2019-08-09 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Freegio', '0003_auto_20190809_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launches',
            name='Mission_Patch_Link',
        ),
        migrations.RemoveField(
            model_name='launches',
            name='Mission_Video_Link',
        ),
    ]
