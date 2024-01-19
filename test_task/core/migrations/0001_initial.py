# Generated by Django 5.0.1 on 2024-01-19 20:27

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('decription', models.CharField(max_length=200)),
                ('count', models.IntegerField(validators=[core.models.validate_count])),
                ('delivery_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
            ],
        ),
    ]