# Generated by Django 3.2.7 on 2021-09-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictcancer',
            name='breast',
            field=models.CharField(choices=[('left', 'left'), ('right', 'right')], max_length=50),
        ),
        migrations.AlterField(
            model_name='predictcancer',
            name='breast_quad',
            field=models.CharField(choices=[('central', 'central'), ('left low', 'left low'), ('left up', 'left up'), ('right low', 'right low'), ('right up', 'right up')], max_length=50),
        ),
        migrations.AlterField(
            model_name='predictcancer',
            name='irradiat',
            field=models.CharField(choices=[('no', 'no'), ('yes', 'yes')], max_length=50),
        ),
        migrations.AlterField(
            model_name='predictcancer',
            name='node_caps',
            field=models.CharField(choices=[('no', 'no'), ('yes', 'yes')], max_length=50),
        ),
    ]