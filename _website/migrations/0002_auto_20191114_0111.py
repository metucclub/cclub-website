# Generated by Django 2.2.6 on 2019-11-13 22:11

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='custom_js',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='content_en',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='content_tr',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='content_en',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='content_tr',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_en',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content_tr',
            field=martor.models.MartorField(),
        ),
    ]