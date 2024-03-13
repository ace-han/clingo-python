from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class RawPickup(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    downloaded_at = models.DateTimeField(null=True)
    video_file = models.FileField(upload_to="pickups", null=True)
    obsolete = models.BooleanField(default=False)


class PreProcessing(models.Model):
    pickup = models.ForeignKey(RawPickup, on_delete=models.SET_NULL, null=True)
    margin_top = models.PositiveSmallIntegerField(default=0)
    margin_bottom = models.PositiveSmallIntegerField(default=0)
    start_sec = models.PositiveSmallIntegerField(default=0)
    end_sec = models.PositiveSmallIntegerField(default=0)
    video_file = models.FileField(upload_to="processings", null=True)
    remark = models.CharField(max_length=128)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["pickup", "start_sec", "end_sec"],
                name="unique_material_preprocessing",
            )
        ]


class ProofReading(models.Model):
    processing = models.ForeignKey(RawPickup, on_delete=models.CASCADE)
    source_language = models.CharField(
        max_length=16, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE
    )
    target_language = models.CharField(
        max_length=16, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    raw_source_subtitle_file = models.FileField(upload_to="proofreadings", null=True)
    raw_subtitle_file = models.FileField(upload_to="proofreadings", null=True)
    downloaded_at = models.DateTimeField(null=True)
    source_subtitles = models.TextField()
    target_subtitles = models.TextField()
    edited_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    edited_at = models.DateTimeField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["processing", "source_language", "target_language"],
                name="unique_material_proofreading",
            )
        ]


class VideoClip(models.Model):
    proofreading = models.ForeignKey(RawPickup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to="videoclips")
    cover_image = models.ImageField(upload_to="coverimages")
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    topic = models.CharField(max_length=128)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "proofreading",
                    "title",
                ],
                name="unique_material_videoclip",
            )
        ]
