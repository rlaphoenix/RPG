from typing import Optional, Any

import click

from rpg_handbook.constants import Folder


class Commands(click.MultiCommand):
    """Lazy-loaded command group of project commands."""
    COMMANDS_DIR = Folder.package_root / "commands"

    def list_commands(self, ctx: click.Context) -> list[str]:
        """Returns a list of command names from the command filenames."""
        rv = []
        for cmd in self.COMMANDS_DIR.iterdir():
            if cmd.stem.lower() != "__init__" and cmd.suffix.lower() == ".py":
                rv.append(cmd.stem)
        rv.sort()
        return rv

    def get_command(self, ctx: click.Context, name: str) -> Optional[click.Command]:
        """Load the command code and return the main click command function."""
        scope: dict[str, Any] = {}
        fn = self.COMMANDS_DIR / f"{name}.py"
        with fn.open() as f:
            code = compile(f.read(), fn, "exec")
            eval(code, scope, scope)
        return scope[name.replace("-", "_")]


# Hide direct access to commands from quick import form, they shouldn't be accessed directly
__ALL__ = (Commands,)
