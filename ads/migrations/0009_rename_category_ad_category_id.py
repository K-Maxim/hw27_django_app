# Generated by Django 4.1 on 2022-08-18 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_alter_ad_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='category',
            new_name='category_id',
        ),
    ]