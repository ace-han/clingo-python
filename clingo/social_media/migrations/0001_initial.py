# Generated by Django 5.0.3 on 2024-03-14 23:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("material", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialMediaGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.SlugField()),
                ("name", models.CharField(max_length=32)),
                ("remark", models.CharField(max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialMediaAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "provider",
                    models.CharField(
                        choices=[("xiaohongshu", "Xiao Hong Shu")], max_length=32
                    ),
                ),
                ("uid", models.CharField(max_length=256)),
                ("nickname", models.CharField(max_length=128)),
                ("avatar_url", models.URLField(max_length=256)),
                ("remark", models.CharField(max_length=128)),
                ("auth_validated_at", models.DateTimeField()),
                ("auth_stacktrace", models.TextField()),
                (
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="social_media.socialmediagroup",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialMediaPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("posted_at", models.DateTimeField()),
                ("post_stacktrace", models.TextField()),
                ("remark", models.CharField(max_length=128)),
                (
                    "account",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="social_media.socialmediaaccount",
                    ),
                ),
                (
                    "videoclip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="material.videoclip",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="socialmediagroup",
            constraint=models.UniqueConstraint(
                fields=("code",), name="unique_social_media_group"
            ),
        ),
        migrations.AddConstraint(
            model_name="socialmediaaccount",
            constraint=models.UniqueConstraint(
                fields=("provider", "uid"), name="unique_social_media_account"
            ),
        ),
        migrations.AddConstraint(
            model_name="socialmediapost",
            constraint=models.UniqueConstraint(
                fields=("account", "videoclip"), name="unique_social_media_post"
            ),
        ),
    ]