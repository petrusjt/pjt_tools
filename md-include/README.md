# md-include

This python script provides an include mechanism for text files. Intended to be used with markdown and pandoc.

## What this does

The script looks for lines beginning with `#![` and ending with `]!#` and recursively inserts the content of the linked file. The linked file can be of any type.

## Usage

### CLI usage
```
python3 md_include.py <input file>
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

### Parametrization

Includes now can have parameters that will be interpolated into the included file.

- Parameters must be specified after the `---` following the file path
- In the includee file the parameters can be referenced by `¤<number>`
##### Note
- `¤<number>` is zero-indexed
- In `¤<number>` number must be lower than number of parameters given 
  - **NOTE:** When `---` are **not** present in the include statement(?), no parameter interpolation is done, 
    so it won't be an issue
- Parametrization is only active when `---` are present in the include statement(?)

#### Example

Includer:
```markdown
# Title

#![includee.md --- arg1 arg2]!#
```

Includee:
```markdown
## ¤0 ¤1

- ¤0
```

Output:
```markdown
# Title

## arg1 arg2

- arg1
```