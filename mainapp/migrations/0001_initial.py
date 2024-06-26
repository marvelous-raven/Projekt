# Generated by Django 5.0.6 on 2024-06-17 23:45

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_end', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('muscles', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('difficulty', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='workout_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeGoal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goal', models.IntegerField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.challenge')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExerciseHighscore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('highscore', models.IntegerField()),
                ('date_got', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalHighscore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('highscore', models.IntegerField(default=0)),
                ('date_got', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserChallengeProgress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('progress_value', models.IntegerField(default=0)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.challenge')),
                ('goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.challengegoal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sets', models.IntegerField(blank=True, null=True)),
                ('reps', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.workout')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExerciseLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('reps', models.IntegerField(blank=True, null=True)),
                ('sets', models.IntegerField(blank=True, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.workoutexercise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
