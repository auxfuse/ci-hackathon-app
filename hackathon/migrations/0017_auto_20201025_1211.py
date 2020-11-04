# Generated by Django 3.1.1 on 2020-10-25 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0016_merge_20201024_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackproject',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackproject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackprojectscore',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojectscores', to=settings.AUTH_USER_MODEL),
        ),
    ]
