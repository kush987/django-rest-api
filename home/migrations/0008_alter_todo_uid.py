# Generated by Django 4.1.4 on 2023-01-21 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('706e4ab9-0454-460d-99de-1b9790239e3d'), editable=False, primary_key=True, serialize=False),
        ),
    ]