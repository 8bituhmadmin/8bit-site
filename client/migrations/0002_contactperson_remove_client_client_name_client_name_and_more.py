# Generated by Django 4.2.9 on 2024-04-20 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of contact person', max_length=255)),
                ('email', models.CharField(blank=True, help_text='Email of contact person', max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, help_text='phone_number of contact person', max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_name',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default='', help_text='Name of client', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short name for the project eg. Learning Emporium Website', max_length=255)),
                ('description', models.TextField(help_text="Short description of what the project is, what we're doing for the project", max_length=2000)),
                ('status', models.CharField(choices=[('NS', 'Have not started'), ('IP', 'In progrss'), ('CO', 'Project completed')], help_text='Status of the project', max_length=255)),
                ('client', models.ForeignKey(help_text='The client we are doing project for', on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
