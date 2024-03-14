from clingo.social_media.providers.base import SocialMediaProvider
from clingo.social_media.providers.xhs import XiaohongshuProvider

PROVIDERS: list[type[SocialMediaProvider]] = [
    XiaohongshuProvider,
]

PROVIDER_CHOICES = [(p.code, p.name) for p in PROVIDERS]
