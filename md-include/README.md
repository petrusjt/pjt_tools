# md-include

This python script provides an include mechanism for text files. Intended to be used with markdown and pandoc.

## What this does

The script looks for lines beginning with `#![` and ending with `]!#` and recursively inserts the content of the linked file. The linked file can be of any type.

## Usage

### CLI usage
```
python3 md_include <input file>
```

The output is saved as `<input file>_out.md`.

### Markdown example usage

```markdown
# Title

#![topic_one.md]!#

#![topic_two.md]!#
```

#### Note:

Includes can be nested. So topic_one.md can include topic_one_one.md for example.

### Warning

Includes from parent directories may not work. Haven't tested it, and probably won't.
