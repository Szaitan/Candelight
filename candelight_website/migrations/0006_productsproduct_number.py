# Generated by Django 5.0 on 2024-01-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candelight_website', '0005_productssubgroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsproduct',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
