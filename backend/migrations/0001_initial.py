# Generated by Django 3.0.5 on 2021-04-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=15)),
                ('user_pw', models.CharField(max_length=20)),
            ],
        ),
    ]
