# Generated by Django 4.2.11 on 2024-05-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0012_rename_name_tag_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('bg-danger', 'Required (Red)'), ('bg-success', 'Core (Green)'), ('bg-primary', 'Regular (Blue)')], default='bg-primary', max_length=50),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, to='learning.tag'),
        ),
    ]
