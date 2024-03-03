import sys

import click


@click.command()
@click.argument("filepath", type=click.Path(), default="")
def main(filepath):
    num = 0

    if not filepath:
        for line in sys.stdin:
            num += 1
            click.echo('    %2d  %s' % (num, line.strip()))
    else:
        try:
            f = open(filepath, 'r')
        except IOError:
            sys.exit('nl: %s: No such file or directory' % filepath)

        for line in f.readlines():
            num += 1
            click.echo('    %2d  %s' % (num, line.strip()))
    f.close()


if __name__ == "__main__":
    main()
