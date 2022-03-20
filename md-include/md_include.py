import codecs
import sys

from typing import List

INCLUDE_START = "#!["
INCLUDE_END = "]!#"


def interpolate_content(content: List[str], path: str = "") -> str:
    interpolated_content: List[str] = []
    for row in content:
        if row.startswith(INCLUDE_START) and row.endswith(INCLUDE_END):
            interpolated_content += include_recursive(row[3:-3], path)
        else:
            interpolated_content.append(row)
    return interpolated_content


def include_recursive(filename: str, path: str = "") -> List[str]:
    with codecs.open(path + filename, encoding="utf-8-sig") as file:
        new_path = f"{path}/{'/'.join(filename.split('/')[:-1])}/" if '/' in filename else path
        if len(new_path) > 0 and new_path[0] == "/":
            new_path = new_path[1:]
        return interpolate_content(read_lines(file), new_path)


def read_lines(file: codecs.StreamReaderWriter) -> List[str]:
    return [line.rstrip() for line in file.readlines()]

if __name__ == "__main__":
    with codecs.open(sys.argv[1], encoding="utf-8-sig") as file:
        content = read_lines(file)

    with codecs.open(f"{sys.argv[1][:-3]}_out.md", "w", encoding="utf-8-sig") as file:
        for line in interpolate_content(content):
            print(line, file=file)