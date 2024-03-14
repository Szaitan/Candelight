# Generated by Django 5.0 on 2024-01-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candelight_website', '0009_alter_productssubgroup_main_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realisationsproject',
            old_name='title',
            new_name='arrangement',
        ),
        migrations.RemoveField(
            model_name='realisationsproject',
            name='description',
        ),
        migrations.AddField(
            model_name='realisationsproject',
            name='design_office',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realisationsproject',
            name='object',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realisationsproject',
            name='photo',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]