# Generated by Django 4.1.4 on 2023-01-21 09:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('47c0dba4-7c9e-4440-8d1d-713dda9d5df7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
