# Generated by Django 5.1.6 on 2025-02-13 21:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stoves',
            fields=[
                ('stove_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stove_url', models.URLField()),
                ('dimensions', models.CharField(verbose_name=255)),
                ('experience', models.CharField(choices=[('Beginner', 'Beginner'), ('Expert', 'Expert')], max_length=8)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('climate', models.CharField(choices=[('Cold', 'Cold'), ('Hot', 'Hot'), ('Mixed', 'Mixed')], max_length=5)),
                ('stove_location', models.CharField(choices=[('Int', 'Interior'), ('Ext', 'Exterior')], max_length=3)),
                ('use', models.CharField(choices=[('Cooking', 'Cooking'), ('Heating', 'Heating'), ('Other', 'Other')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions_set', to='auth.permission')),
            ],
            options={
                'permissions': [('can_view_admin_page', 'Can view admin page'), ('can_view_user_page', 'Can view user page')],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=2)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stove_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucca_web.stoves')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('material_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('material_name', models.CharField(verbose_name=255)),
                ('stove_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucca_web.stoves')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stove_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ucca_web.stoves')),
            ],
        ),
    ]
