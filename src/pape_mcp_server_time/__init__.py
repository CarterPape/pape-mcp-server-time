"""MCP server init file."""

import argparse
import asyncio

from .server import serve


def main() -> None:
    """MCP Time Server - Time and timezone conversion functionality for MCP."""
    parser = argparse.ArgumentParser(
        description=(
            "give a model the ability to handle time queries "
            "and timezone conversions"
        ),
    )
    parser.add_argument("--local-timezone", type=str, help="Override local timezone")

    args = parser.parse_args()
    asyncio.run(serve(args.local_timezone))


if __name__ == "__main__":
    main()
