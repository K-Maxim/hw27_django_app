# Generated by Django 4.1 on 2022-08-19 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_location_id_alter_user_role_and_more'),
        ('ads', '0012_rename_author_ad_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
