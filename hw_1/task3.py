import sys

import click


def utf8len(s):
    return len(s.encode('utf-8'))


def print_out(lines, words, bytes, filepath):
    click.echo(f"{' ' * (8 - len(str(lines)))}{lines}{' ' * (8 - len(str(words)))}{words}{' ' * (8 - len(str(bytes)))}{bytes} {filepath}")


@click.command()
@click.argument("filepaths", nargs=-1, type=click.Path())
def main(filepaths):
    total_lines_count = 0
    total_words_count = 0
    total_bytes_count = 0
    if not filepaths:
        for line in sys.stdin:
            total_lines_count += 1
            total_words_count += len(line.split())
            total_bytes_count += utf8len(line)

        print_out(total_lines_count, total_words_count, total_bytes_count, "")
    else:
        for filepath in filepaths:
            lines_count = 0
            words_count = 0
            bytes_count = 0
            try:
                f = open(filepath, 'r')
            except IOError:
                click.echo('wc: %s: open: No such file or directory' %
                           filepath)
                continue

            for line in f.readlines():
                lines_count += 1
                words_count += len(line.split())
                bytes_count += utf8len(line)

                total_lines_count += 1
                total_words_count += len(line.split())
                total_bytes_count += utf8len(line)
            f.close()

            print_out(lines_count, words_count, bytes_count, filepath)
        if len(filepaths) > 1:
            print_out(total_lines_count, total_words_count,
                      total_bytes_count, "total")


if __name__ == "__main__":
    main()
