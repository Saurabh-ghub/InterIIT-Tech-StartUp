# Generated by Django 4.0 on 2023-02-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_studentform_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='profession',
            field=models.CharField(default='Mentor', max_length=50),
            preserve_default=False,
        ),
    ]
