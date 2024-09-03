# Generated by Django 2.2.7 on 2019-12-08 15:40

import chunked_upload.models
import chunked_upload.settings
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChunkedUpload",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "upload_id",
                    models.CharField(
                        default=chunked_upload.models.generate_upload_id,
                        editable=False,
                        max_length=32,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=255, upload_to=chunked_upload.settings.UPLOAD_TO
                    ),
                ),
                ("filename", models.CharField(max_length=255)),
                ("offset", models.BigIntegerField(default=0)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Uploading"), (2, "Complete")], default=1
                    ),
                ),
                ("completed_on", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=chunked_upload.settings.DEFAULT_MODEL_USER_FIELD_BLANK,
                        null=chunked_upload.settings.DEFAULT_MODEL_USER_FIELD_NULL,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chunked_uploads",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
