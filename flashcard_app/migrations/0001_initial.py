# Generated by Django 4.2 on 2023-10-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('source', models.URLField(blank=True, default=True, max_length=400, null=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
