# Generated by Django 3.2.6 on 2021-11-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contacts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateField(default='2021-11-26'),
        ),
    ]
