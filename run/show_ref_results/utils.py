import csv
from pathlib import Path

from tabulate import tabulate


def parse_files(base_dir: Path) -> None:
    csv_paths = sorted(list(base_dir.rglob("*.csv")))
    for path in csv_paths:
        print_table(csv_path=path)


def print_table(csv_path: Path, fmt=".3f") -> None:
    with open(csv_path, newline="") as f:
        rows = list(csv.reader(f))

    table_lines = tabulate(
        rows[1:], headers=rows[0], tablefmt="mixed_outline", floatfmt=fmt
    ).splitlines()

    sep = next(line for line in table_lines if line.startswith("┝"))

    # insert that divider right before the last data-row (the “average”)
    table_lines.insert(-2, sep)

    print()
    print(f"{csv_path.name}:")
    print("\n".join(table_lines))
    print()
