# Generated by Django 3.2.9 on 2021-12-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeatures', '0002_druginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=512)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
