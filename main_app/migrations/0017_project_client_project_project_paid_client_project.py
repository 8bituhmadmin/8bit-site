# Generated by Django 4.2.15 on 2024-10-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_project_deploy_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client_project',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='paid_client_project',
            field=models.BooleanField(default=False),
        ),
    ]