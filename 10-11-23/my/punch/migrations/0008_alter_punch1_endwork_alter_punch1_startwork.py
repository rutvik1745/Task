# Generated by Django 4.2.7 on 2023-11-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punch', '0007_alter_punch1_endwork_alter_punch1_startwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punch1',
            name='endWork',
            field=models.DateTimeField(max_length=60),
        ),
        migrations.AlterField(
            model_name='punch1',
            name='startWork',
            field=models.DateTimeField(max_length=60),
        ),
    ]
