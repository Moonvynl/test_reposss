# Generated by Django 5.0.1 on 2024-02-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_tasks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "ADMIN"), ("user", "USER")],
                default="user",
                max_length=63,
            ),
        ),
    ]