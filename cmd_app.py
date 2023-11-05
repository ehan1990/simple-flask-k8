#!/usr/bin/env python
import click
from libs.health_cmd import health_cmd


@click.group()
def cli():
    pass


cli.add_command(health_cmd)


if __name__ == "__main__":
    cli()
