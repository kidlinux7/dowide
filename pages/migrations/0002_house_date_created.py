# Generated by Django 3.2 on 2022-08-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]