# Generated by Django 3.2.9 on 2021-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfeatures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugname', models.CharField(max_length=255)),
                ('drugprice', models.IntegerField()),
                ('availability', models.CharField(max_length=5)),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
    ]