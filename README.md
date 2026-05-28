# Gendiff

Compares two configuration files and shows a difference.

### Hexlet tests and linter status

[![Python CI](https://github.com/Geogrigri/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/Geogrigri/python-project-50/actions/workflows/main.yml)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Geogrigri_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Geogrigri_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Geogrigri_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Geogrigri_python-project-50)

### Installation

```bash
uv tool install .
```

### Usage

```bash
gendiff file1.json file2.json
```

### JSON comparison

```bash
gendiff tests/test_data/file1.json tests/test_data/file2.json
```

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### YAML comparison

```bash
gendiff tests/test_data/file1.yml tests/test_data/file2.yml
```

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### Plain format

```bash
gendiff --format plain tests/test_data/nested_file1.json tests/test_data/nested_file2.json
```

```text
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

### JSON format

```bash
gendiff --format json tests/test_data/nested_file1.json tests/test_data/nested_file2.json
```

```json
[
    {
        "key": "common",
        "type": "nested",
        "children": [
            {
                "key": "follow",
                "type": "added",
                "value": false
            }
        ]
    }
]
```
### Demo

#### Help output

[![asciicast](https://asciinema.org/a/HNGkIvHymTlsf7md.svg)](https://asciinema.org/a/HNGkIvHymTlsf7md)

#### JSON comparison

[![asciicast](https://asciinema.org/a/LGeLhRrc4GKSPNmw.svg)](https://asciinema.org/a/LGeLhRrc4GKSPNmw)

#### YAML comparison

[![asciicast](https://asciinema.org/a/Zy8cRUnwGAoioDmA.svg)](https://asciinema.org/a/Zy8cRUnwGAoioDmA)

#### Recursive comparison

[![asciicast](https://asciinema.org/a/ttB7D0rctf0y66en.svg)](https://asciinema.org/a/ttB7D0rctf0y66en)

#### Plain and JSON formats

[![asciicast](https://asciinema.org/a/ELZj74XfIt5Xyll7.svg)](https://asciinema.org/a/ELZj74XfIt5Xyll7)