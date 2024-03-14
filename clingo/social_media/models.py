from django.contrib.auth import get_user_model
from django.db import models

from clingo.social_media.providers import PROVIDER_CHOICES

UserModel = get_user_model()


class SocialMediaGroup(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    code = models.SlugField()
    name = models.CharField(max_length=32)
    remark = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "code",
                ],
                name="unique_social_media_group",
            )
        ]


class SocialMediaAccount(models.Model):
    group = models.ForeignKey(SocialMediaGroup, on_delete=models.SET_NULL, null=True)
    provider = models.CharField(max_length=32, choices=PROVIDER_CHOICES)
    uid = models.CharField(max_length=256)
    nickname = models.CharField(max_length=128)
    avatar_url = models.URLField(max_length=256)
    remark = models.CharField(max_length=128)
    auth_validated_at = models.DateTimeField()
    auth_stacktrace = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["provider", "uid"],
                name="unique_social_media_account",
            )
        ]


class SocialMediaPost(models.Model):
    account = models.ForeignKey(
        SocialMediaAccount, on_delete=models.SET_NULL, null=True
    )
    videoclip = models.ForeignKey("material.VideoClip", on_delete=models.CASCADE)
    posted_at = models.DateTimeField()
    post_stacktrace = models.TextField()
    remark = models.CharField(max_length=128)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["account", "videoclip"],
                name="unique_social_media_post",
            )
        ]
