# Generated by Django 2.2.2 on 2019-08-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freegio', '0006_launches_mission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launches',
            name='Mission_name',
            field=models.TextField(null=True),
        ),
    ]
