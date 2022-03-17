# Generated by Django 2.2.26 on 2022-03-15 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievementName', models.CharField(blank=True, max_length=30)),
                ('achievementDescription', models.CharField(blank=True, max_length=256)),
                ('achievementImage', models.ImageField(blank=True, upload_to='achievement_images')),
                ('achievementType', models.CharField(default='currency', max_length=10)),
                ('achievementCriteriaExpectedVal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prizeName', models.CharField(blank=True, max_length=30, unique=True)),
                ('prizeImage', models.ImageField(blank=True, upload_to='prize_images')),
                ('prizeValue', models.IntegerField(default=0)),
                ('prizeRarity', models.CharField(blank=True, choices=[('ULTRA_RARE', 'ULTRA RARE!'), ('COMMON', 'Common!'), ('RARE_ISH', 'Rare-ish'), ('RARE', 'Rare')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImage', models.ImageField(blank=True, default='profile_images/none.jpg', upload_to='profile_images')),
                ('currency', models.IntegerField(default=100)),
                ('username_slug', models.CharField(blank=True, max_length=30)),
                ('achievements', models.ManyToManyField(blank=True, to='CR8.Achievement')),
                ('prizes', models.ManyToManyField(blank=True, to='CR8.Prize')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
