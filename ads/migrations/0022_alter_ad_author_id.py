# Generated by Django 4.1 on 2022-09-09 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0021_alter_ad_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
