# Generated by Django 4.0 on 2023-02-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_studentform'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]