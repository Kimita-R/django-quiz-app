# Generated by Django 4.1.7 on 2023-03-12 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='quiz_id',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='user_id',
            new_name='user',
        ),
    ]
