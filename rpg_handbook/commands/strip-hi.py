import logging
from pathlib import Path

import click
from subtitle_filter import Subtitles
from tqdm import tqdm


@click.command(name="strip-hi")
@click.argument("path", type=Path)
@click.option("-f", "--fonts", is_flag=True, default=False,
              help="Do not remove font tags and text contained within.")
@click.option("-a", "--ast", is_flag=True, default=False,
              help="Do not remove captions containing asterisks: (*).")
@click.option("-m", "--music", is_flag=True, default=False,
              help="Do not remove captions containing 1 or more \"♪\" or \"#\" symbols.")
@click.option("-e", "--effects", is_flag=True, default=False,
              help="Do not remove captions between and including parenthesis \"()\" or brackets \"[]\".")
@click.option("-n", "--names", is_flag=True, default=False,
              help="Do not replace names in captions with \"-\".")
@click.option("-c", "--credit", is_flag=True, default=False,
              help="Do not remove captions with author tags, e.g., `Subtitles by PwnedDude967`.")
def strip_hi(path: Path, fonts: bool, ast: bool, music: bool, effects: bool, names: bool, credit: bool) -> None:
    """
    \b
    Batch strip text for Hearing Impaired from SRT subtitles.
    You may provide either a Folder containing .SRT subtitles, or a direct
    path to a single .SRT subtitle.

    \b
    All filtering is done by mattlyon93's subtitle-filter:
    https://github.com/mattlyon93/filter-subs

    \b
    All parameters specify filtering to keep. All filtering is enabled by
    default. Filters are applied in the order listed.

    \b
    The following filters and fixes are also applied at the very end:
    - Erroneous comma spacing, e.g., `Hey , what's up? Nothing,my man.`
    - Lone symbols such as `?`, `-`, `#`, `_`.
    These cannot be disabled.

    \b
    The `--ast` filter may need to be disabled depending on the captioning.
    Some services or captions may use `*` for non-Hearing-Impaired uses.
    Adversely, some use it as a censorship symbol, e.g. `F*** you!`. The
    asterisk may also be used for effects instead of brackets.

    \b
    The `--credit` parameter is useful to remove annoying old P2P or DDL
    Subtitle Author captions, but is not extensive. General fair authorship is
    not filtered, e.g. `Captioning sponsored by NICKELODEON.` is not removed.
    """
    log = logging.getLogger("strip-hi")
    if not path.exists():
        log.error(f"Provided path does not exist: {path}")

    if path.is_file():
        subtitles = [path]
    else:
        subtitles = list(path.glob("*.srt"))

    log.info(f"Found {len(subtitles)} SRT subtitle{['s', ''][len(subtitles) == 1]}")

    for subtitle in tqdm(subtitles, unit="subs"):
        sub = Subtitles(subtitle)
        sub.filter(
            rm_fonts=not fonts,
            rm_ast=not ast,
            rm_music=not music,
            rm_effects=not effects,
            rm_names=not names,
            rm_author=not credit
        )
        sub.save()

    log.info("Done! All subtitles have been filtered.")
