from importlib.metadata import metadata

import click


@click.command()
def version():
    """Check what version you have installed."""
    meta = metadata("rpg-handbook")
    print(f"RPG Handbook version {meta['version']} Copyright (c) 2022 rlaphoenix")
    print(meta["home-page"])
