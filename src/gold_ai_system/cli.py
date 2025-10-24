"""Command-line helpers for running the trading system."""

from __future__ import annotations

import argparse
import textwrap

from .config import load_settings


def build_parser() -> argparse.ArgumentParser:
    description = textwrap.dedent(
        """
        Gold AI System bootstrap utility.

        This command currently validates that required environment variables are present
        and prints the active configuration. It is a placeholder for the future
        scheduler/runner entrypoint.
        """
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Print the resolved configuration and exit.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    settings = load_settings()

    if args.show_config:
        masked_webhook = _mask_webhook(settings.discord_webhook_url)
        print("Active configuration:")
        print(f"  Discord webhook URL: {masked_webhook}")
        print(f"  Stage1 model: {settings.stage1_model}")
        print(f"  Stage2 model: {settings.stage2_model}")
    else:
        print("Configuration loaded successfully. Use --show-config to inspect values.")

    return 0


def _mask_webhook(url: str) -> str:
    """Mask the webhook URL so secrets are not leaked to the console."""

    if len(url) <= 10:
        return "********"

    prefix = url[:5]
    suffix = url[-4:]
    return f"{prefix}********{suffix}"


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())