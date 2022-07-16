import codecs
import sys
import re

from typing import List

INCLUDE_START = "#!["
INCLUDE_END = "]!#"

FILE_ARG_SEP = "---"
ARG_PREFIX = "¤"
ARG_PATTERN = re.compile(ARG_PREFIX + r"\d+")


def interpolate_content(content: List[str], path: str = "") -> List[str]:
    interpolated_content: List[str] = []
    for row in content:
        if row.startswith(INCLUDE_START) and row.endswith(INCLUDE_END):
            interpolated_content += include_recursive(row[3:-3], path)
        else:
            interpolated_content.append(row)
    return interpolated_content


def include_recursive(filename_args: str, path: str = "") -> List[str]:
    filename = filename_args.split(FILE_ARG_SEP)[0].strip()
    with codecs.open(path + filename, encoding="utf-8-sig") as file:
        new_path = f"{path}/{'/'.join(filename_args.split('/')[:-1])}/" if '/' in filename else path
        if len(new_path) > 0 and new_path[0] == "/":
            new_path = new_path[1:]

        asd = read_lines(file)
        if FILE_ARG_SEP in filename_args:
            asd = interpolate_arguments(asd, filename_args.split(FILE_ARG_SEP)[1].strip().split())
        return interpolate_content(asd, new_path)


def read_lines(file: codecs.StreamReaderWriter) -> List[str]:
    return [line.rstrip() for line in file.readlines()]


def interpolate_arguments(lines: List[str], args: List[str]) -> List[str]:
    return [interpolate_into_line(line, args) for line in lines]


def interpolate_into_line(line: str, args: List[str]) -> str:
    asd = ARG_PATTERN.findall(line)
    interpolated_line = line
    for match in asd:
        interpolated_line = interpolated_line.replace(match, args[int(match[len(ARG_PREFIX):])])
    return interpolated_line


def main():
    with codecs.open(sys.argv[1], encoding="utf-8-sig") as file:
        content = read_lines(file)

    with codecs.open(f"{sys.argv[1][:-3]}_out.md", "w", encoding="utf-8-sig") as file:
        for line in interpolate_content(content):
            print(line, file=file)


if __name__ == "__main__":
    main()
