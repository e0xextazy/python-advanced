import sys

import click


@click.command()
@click.argument("filepaths", nargs=-1, type=click.Path())
@click.option("--number", "-n", type=int, default=10)
def main(filepaths, number):
    if not filepaths:
        cache = list()
        
        for line in sys.stdin:
            cache.append(line)
        
        click.echo("".join(cache[-17:]).rstrip())
    else:
        for i, filepath in enumerate(filepaths):
            try:
                f = open(filepath, 'r')
            except IOError:
                click.echo('tail: %s: No such file or directory' % filepath)
                continue

            if i != 0:
                click.echo("")
            if len(filepaths) > 1:
                click.echo(f"==> {filepath} <==")
            for line in f.readlines()[-number:]:
                click.echo(line.rstrip())
            f.close()

if __name__ == "__main__":
    main()
