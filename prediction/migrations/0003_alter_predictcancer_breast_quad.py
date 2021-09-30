# Generated by Django 3.2.7 on 2021-09-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20210929_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictcancer',
            name='breast_quad',
            field=models.CharField(choices=[('central', 'central'), ('left low', 'left_low'), ('left up', 'left_up'), ('right low', 'right_low'), ('right up', 'right_up')], max_length=50),
        ),
    ]