# Generated by Django 5.0.2 on 2024-02-16 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The last update time')),
                ('is_updated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The last update time')),
                ('is_updated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The last update time')),
                ('is_updated', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=70)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='blog.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
