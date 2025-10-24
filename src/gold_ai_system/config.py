"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load variables from a local `.env` file if present.
load_dotenv()


@dataclass(slots=True)
class Settings:
    """Centralised configuration for the trading system."""

    discord_webhook_url: str
    stage1_model: str = "lightgbm"
    stage2_model: str = "lstm"

    @classmethod
    def from_env(cls) -> "Settings":
        """Construct settings from environment variables.

        Raises:
            ValueError: If a required environment variable is missing.
        """

        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        if not webhook_url:
            raise ValueError(
                "DISCORD_WEBHOOK_URL is not set. Export it or define it in a .env file."
            )

        stage1_model = os.getenv("STAGE1_MODEL", cls.stage1_model)
        stage2_model = os.getenv("STAGE2_MODEL", cls.stage2_model)
        return cls(
            discord_webhook_url=webhook_url.strip(),
            stage1_model=stage1_model.strip().lower(),
            stage2_model=stage2_model.strip().lower(),
        )


def load_settings() -> Settings:
    """Retrieve configuration settings with validation."""

    return Settings.from_env()