# Generated by Django 5.1.4 on 2025-01-25 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_chead0_blogpost_chead1_blogpost_chead2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='price',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='subcategory',
        ),
    ]
