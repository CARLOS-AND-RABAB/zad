# Generated by Django 3.1.4 on 2021-01-21 17:59

from django.db import migrations, models
import django.db.models.deletion
import zad.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_title', models.TextField(default='null', help_text='TITLE:', max_length=50, verbose_name='ad about:')),
                ('Ad_details', models.TextField(help_text='DETAILS:', max_length=500, verbose_name='ad about:')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date of publish  the advertice')),
                ('category', models.IntegerField(choices=[(1, 'product'), (2, 'service'), (3, 'course'), (4, 'store'), (5, 'other')])),
                ('photo', models.ImageField(help_text='PHOTO:', upload_to=zad.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('period', models.IntegerField(choices=[(24, 'day'), (48, 'tow days'), (72, 'three days')], help_text='PERIOD')),
                ('approved', models.BooleanField(blank=True, default=False)),
                ('unvalid', models.BooleanField(blank=True, default=False)),
                ('vote', models.IntegerField(blank=True, default=0, help_text='VOTE:')),
                ('AD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='zad.ad')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(help_text='add comment:', max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='zad.post')),
            ],
        ),
    ]
