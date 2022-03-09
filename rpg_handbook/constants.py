import tempfile
from pathlib import Path

from appdirs import AppDirs


class Folder:
    app_dirs = AppDirs("rpg-handbook", False)
    package_root = Path(__file__).resolve().parent
    configs = Path(app_dirs.user_config_dir)
    data = Path(app_dirs.user_data_dir)
    temp = Path(tempfile.gettempdir(), "rpg-handbook")
    cache = Path(app_dirs.user_cache_dir)
    logs = Path(app_dirs.user_log_dir)


class File:
    log = Folder.logs / "rpg-handbook_{name}_{time}.log"


click_context = dict(
    help_option_names=["-?", "-h", "--help"],  # default only has --help
    max_content_width=116,  # max PEP8 line-width, -4 to adjust for initial indent
)
