# Generated by Django 4.2.11 on 2024-05-01 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0016_lesson_form_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='form_link',
            new_name='quiz',
        ),
    ]
