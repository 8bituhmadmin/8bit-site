# Generated by Django 4.2.9 on 2024-04-20 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_contactperson_remove_client_client_name_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
