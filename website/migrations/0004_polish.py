# Generated by Django 4.0.5 on 2022-07-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_borders_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('lorries', models.CharField(max_length=100)),
                ('buses', models.CharField(max_length=100)),
                ('cars', models.CharField(max_length=100)),
                ('time', models.TimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
