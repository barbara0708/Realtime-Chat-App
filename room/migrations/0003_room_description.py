# Generated by Django 4.0 on 2023-04-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default='some description'),
            preserve_default=False,
        ),
    ]
