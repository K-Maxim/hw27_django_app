# Generated by Django 4.1 on 2022-09-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]