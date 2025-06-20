# Generated by Django 5.2.3 on 2025-06-12 01:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.UUID('6c264779-b9ba-4ff8-8425-5e995ecc56c5'), editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('todo_title', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
