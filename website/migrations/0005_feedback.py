# Generated by Django 4.0.5 on 2022-07-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_polish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=20000)),
            ],
        ),
    ]
