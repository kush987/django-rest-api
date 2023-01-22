# Generated by Django 4.1.4 on 2023-01-21 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_todo_uid_timingtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9374410d-1326-4428-83c0-86a153ece807'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9374410d-1326-4428-83c0-86a153ece807'), editable=False, primary_key=True, serialize=False),
        ),
    ]