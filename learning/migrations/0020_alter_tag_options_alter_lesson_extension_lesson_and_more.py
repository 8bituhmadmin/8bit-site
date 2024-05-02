# Generated by Django 4.2.11 on 2024-05-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0019_remove_lesson_skills_lesson_core_lesson_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': [models.Case(models.When(color='bg-primary', then=1), default=2, output_field=models.IntegerField())]},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='extension_lesson',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('bg-primary', 'Technical Skill (Blue)'), ('bg-secondary', 'Technical Concept (Grey)')], default='bg-primary', max_length=50),
        ),
    ]
