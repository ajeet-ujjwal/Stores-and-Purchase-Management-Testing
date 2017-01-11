# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 06:37
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', message=b'Only alphanumeric characters are allowed')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name=b'email address')),
                ('name', models.CharField(max_length=20)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
                ('dueDate', models.DateField()),
                ('type', models.CharField(choices=[(b'Table', b'Table'), (b'Chair', b'Chair'), (b'CupBoard', b'CupBoard')], max_length=30)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('r_object', models.CharField(choices=[(b'Table', b'Table'), (b'Chair', b'Chair'), (b'CupBoard', b'CupBoard')], max_length=15)),
                ('status', models.CharField(choices=[(b'P', b'Pending'), (b'A', b'Approved'), (b'D', b'Denied'), (b'C', b'Completed')], max_length=15)),
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_request', models.DateField()),
                ('date_of_completion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('login.user',),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(choices=[(b'Assistant Professor', b'Assistant Professor'), (b'Associate Professor', b'Associate Professor'), (b'Visiting Faculty', b'Visiting Faculty'), (b'Head of Department', b'Head of Department')], max_length=25)),
                ('department', models.CharField(choices=[(b'CS', b'Computer Science'), (b'ME', b'Mechanical Engineering'), (b'EE', b'Electrical Engineering'), (b'SS', b'Systems Science')], max_length=2)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Admin')),
            ],
            options={
                'abstract': False,
            },
            bases=('login.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('year', models.CharField(choices=[(b'B1', b'B.Tech. First Year'), (b'B2', b'B.Tech Second Year'), (b'B3', b'B.Tech Third Year'), (b'B2', b'B.Tech Fourth Year'), (b'M1', b'M.Tech First Year'), (b'M2', b'M.Tech Second Year')], max_length=2)),
                ('department', models.CharField(choices=[(b'CS', b'Computer Science'), (b'ME', b'Mechanical Engineering'), (b'EE', b'Electrical Engineering'), (b'SS', b'Systems Science')], max_length=2)),
                ('roll_no', models.CharField(max_length=12)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Faculty')),
            ],
            options={
                'abstract': False,
            },
            bases=('login.user',),
        ),
        migrations.AddField(
            model_name='request',
            name='r_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_username', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='request',
            name='requested_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='object',
            name='currentOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificationfaculty',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Request'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='notificationfaculty',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Faculty'),
        ),
    ]