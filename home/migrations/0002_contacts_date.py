# Generated by Django 3.2.6 on 2021-11-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='date',
            field=models.DateField(default='27-11-2021'),
        ),
    ]
