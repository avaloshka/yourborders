# Generated by Django 4.0.5 on 2022-07-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
