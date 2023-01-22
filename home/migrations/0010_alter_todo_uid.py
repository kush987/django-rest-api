# Generated by Django 4.1.4 on 2023-01-21 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('0d59b8dd-6b28-4027-99ca-92046f587d9c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
