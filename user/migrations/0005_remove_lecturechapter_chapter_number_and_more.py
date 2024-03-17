# Generated by Django 5.0.2 on 2024-03-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_lecturechapter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturechapter',
            name='chapter_number',
        ),
        migrations.AddField(
            model_name='lecturechapter',
            name='chapter_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
