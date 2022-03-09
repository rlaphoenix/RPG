# RPG

[![Build Tests](https://img.shields.io/github/workflow/status/rlaphoenix/RPG/ci?label=Python%203.8%2B%20builds)](https://github.com/rlaphoenix/RPG/actions?query=workflow%3A%22ci%22)
[![License](https://img.shields.io/github/license/rlaphoenix/RPG?style=flat)](https://github.com/rlaphoenix/RPG/blob/master/LICENSE)

This repository contains Code and Documentation from the RPG release group.

## The Documentation

It's very much Work-in-Progress, but it is built on Sphinx with the Furo theme.
The documentation is auto deployed to <https://rpg-handbook.readthedocs.io>.

You can build the documentation in `/docs` using [Poetry].
Make sure you install the `docs` dependencies (`poetry install -E docs`).

## The Code

We have limited and niche software and scripts for specific purposes only. This is
because a lot of the software work is done for us with great tools like MakeMKV,
MKVToolNix, AnyDVD HD, and so on.

Again the code can be built in `/rpg_handbook` using [Poetry].
Once built and installed, you can run it by simply calling the `rpg` script.

## Poetry

Poetry is a Python dependency-management software. It focuses on virtualizing all
dependency installations to the project, similar to `node_modules` on NodeJS.

I recommend doing `poetry config virtualenvs.in-project true` so the `.venv` folder
is made alongside the project code, and not hidden away in `AppData`.

The gist is to install dependencies with `poetry install` and then use `poetry shell`
to activate the virtual-env. You can then run any command like normal, and the poetry
virtual-environment will be used over your normal system Python environment.

You should read the [documentation][Poetry] for any further information on usage.

  [Poetry]: <https://python-poetry.org>
