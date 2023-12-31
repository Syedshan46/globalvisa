# Generated by Django 4.2.6 on 2023-10-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('contact_subject', models.CharField(max_length=200)),
                ('contact_message', models.CharField(max_length=200)),
            ],
        ),
    ]
