# Generated by Django 4.1.5 on 2023-02-01 19:24

import admin_panel_app.services.image_paths_builders
import admin_panel_app.services.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="greeting_image",
            field=models.ImageField(
                upload_to=admin_panel_app.services.image_paths_builders.greeting_image_path,
                validators=[admin_panel_app.services.model_validators.image_size_validator],
            ),
        ),
        migrations.AlterField(
            model_name="chat",
            name="greeting_text",
            field=models.TextField(max_length=1024),
        ),
    ]