# Generated by Django 4.2.6 on 2023-10-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=200)),
                ('reg_pass', models.IntegerField()),
            ],
        ),
    ]
