# Generated by Django 4.2.7 on 2023-11-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('zip_code', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=90)),
            ],
        ),
    ]