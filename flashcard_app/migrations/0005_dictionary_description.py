# Generated by Django 4.2 on 2023-12-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard_app', '0004_dictionary_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='description',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
