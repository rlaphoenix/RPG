import logging

import click

from rpg_handbook.commands import Commands
from rpg_handbook.constants import click_context


@click.command(cls=Commands, context_settings=click_context)
@click.option("-d", "--debug", is_flag=True, default=False, help="Enable DEBUG level logs.")
def main(debug: bool) -> None:
    """Utilities for use with the RPG Handbook."""
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)


if __name__ == "__main__":
    main()
