# Generated by Django 3.2.6 on 2021-11-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=30)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.TextField(blank='True', null='True')),
            ],
        ),
    ]
