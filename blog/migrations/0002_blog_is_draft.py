# Generated by Django 5.0.2 on 2024-02-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
