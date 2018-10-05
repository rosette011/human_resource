# Generated by Django 2.0.7 on 2018-09-28 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='avatar.jpg', upload_to='profile_pics')),
                ('summary', models.CharField(max_length=1000)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Role')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]