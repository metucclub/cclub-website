# Generated by Django 2.2.7 on 2019-11-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_website', '0006_auto_20191118_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='home_page_order',
            field=models.PositiveIntegerField(default=0, help_text='Make 0 to hide in home page'),
        ),
    ]
