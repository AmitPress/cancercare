# Generated by Django 3.2.9 on 2022-01-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
