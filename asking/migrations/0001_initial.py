# Generated by Django 2.0.5 on 2018-05-27 16:48

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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_question', models.CharField(max_length=50, verbose_name='Can I have your name, genius?')),
                ('name_asker', models.CharField(max_length=50, verbose_name='Ask me anything babe!')),
                ('content', models.TextField()),
                ('answer', models.TextField(blank=True, null=True)),
                ('asking_day', models.DateTimeField(verbose_name='date published')),
                ('id_user_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
