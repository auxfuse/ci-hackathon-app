# Generated by Django 3.1.1 on 2020-10-25 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('theme', models.CharField(max_length=264)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackathons', to=settings.AUTH_USER_MODEL)),
                ('judges', models.ManyToManyField(blank=True, related_name='hackathon_judges', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackathon_organisation', to='accounts.organisation')),
                ('organiser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackathon_organiser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HackProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('github_url', models.URLField(default='', max_length=255)),
                ('deployed_url', models.URLField(default='', max_length=255)),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('speaker_name', models.CharField(default='', max_length=225)),
                ('share_permission', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackproject', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hackproject_mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HackTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(default='', max_length=254)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackteams', to=settings.AUTH_USER_MODEL)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='hackathon.hackathon')),
                ('participants', models.ManyToManyField(related_name='hackteam', to=settings.AUTH_USER_MODEL)),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hackathon.hackproject')),
            ],
        ),
        migrations.CreateModel(
            name='HackProjectScoreCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(default='', max_length=255)),
                ('min_score', models.IntegerField(default=1)),
                ('max_score', models.IntegerField(default=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojectscorecategories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hack project score categories',
            },
        ),
        migrations.CreateModel(
            name='HackProjectScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojectscores', to=settings.AUTH_USER_MODEL)),
                ('hack_project_score_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.hackprojectscorecategory')),
                ('judge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='hackathon.hackproject')),
            ],
        ),
        migrations.CreateModel(
            name='HackAwardCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackawardcategories', to=settings.AUTH_USER_MODEL)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='hackathon.hackathon')),
                ('winning_project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hackathon.hackproject')),
            ],
            options={
                'verbose_name_plural': 'Hack award categories',
            },
        ),
    ]
