# Generated by Django 3.2.4 on 2021-06-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantappapi', '0002_light'),
    ]

    operations = [
        migrations.CreateModel(
            name='water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_needs', models.CharField(max_length=50)),
            ],
        ),
    ]
