#!/usr/bin/env python3
"""Package the preserved PowerPoint source; requires only Python 3."""
import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=root / 'from-slack-to-shipped.pptx')
    args = parser.parse_args()
    source = root / 'source'
    files = sorted(p for p in source.rglob('*') if p.is_file() and p.name != '.DS_Store')
    for required in ('[Content_Types].xml', '_rels/.rels', 'ppt/presentation.xml'):
        if not (source / required).is_file():
            parser.error(f'Missing source part: {required}')
    for path in files:
        if path.suffix in ('.xml', '.rels'):
            ET.parse(path)
    output = args.output.resolve()
    if output == source or source in output.parents:
        parser.error('Output must be outside source/')
    output.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=output.parent, suffix='.pptx', delete=False) as temp:
        temporary = Path(temp.name)
    try:
        with ZipFile(temporary, 'w', compression=ZIP_DEFLATED) as package:
            for path in files:
                package.write(path, path.relative_to(source).as_posix())
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'Built {output}')


if __name__ == '__main__':
    main()
