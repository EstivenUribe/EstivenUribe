"""Refresh the in-page Spanish edition after editing README.es.md."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MARKER = '<!-- Spanish edition generated from README.es.md with tools/sync_spanish.py -->'
END = '<!-- End of the in-page Spanish edition -->'


def main():
    english_file = ROOT / 'README.md'
    english = english_file.read_text(encoding='utf-8')
    if english.startswith(MARKER):
        _, end_marker, english = english.partition(END)
        if not end_marker:
            raise ValueError('The generated section has no end marker.')
    spanish = (ROOT / 'README.es.md').read_text(encoding='utf-8')
    # Use the cover and all subsequent sections. The standalone language switch is replaced below.
    _, cover, rest = spanish.partition('<h1>')
    if not cover:
        raise ValueError('The Spanish cover is missing its h1 heading.')
    edition = (cover + rest).replace('<h1>', '<h2>', 1).replace('</h1>', '</h2>', 1)
    # Inline Spanish reference links so the two editions can use different reference definitions.
    definitions = dict(re.findall(r'^\[([\w-]+)\]: (\S+)$', edition, re.M))
    edition = re.sub(r'^\[[\w-]+\]: \S+\n?', '', edition, flags=re.M)
    edition = re.sub(r'\]\[([\w-]+)\]', lambda m: '](' + definitions[m[1]] + ')', edition)
    # Each language has its own project jump links on the combined page.
    edition = re.sub(r'\]\(#([\w-]+)\)', r'](#es-\1)', edition)
    def project_heading(match):
        slug = re.sub(r'[^\w]+', '-', match[1].lower()).strip('-')
        return f'<a name="es-{slug}"></a>\n\n### <samp>{match[1]}</samp> · {match[2]}\n\n'
    edition = re.sub(r'^### <samp>([^<]+)</samp>\n\n\*\*([^\n]+?)\*\*<br>', project_heading, edition, flags=re.M)
    block = f'''{MARKER}
<details lang="es">
<summary align="right"><samp>Leer en español</samp></summary>

[English](#english) · [Abrir el archivo en español](./README.es.md)

{edition.strip()}

</details>
{END}
'''
    english_file.write_text(f'{block}\n{english.lstrip()}', encoding='utf-8')


if __name__ == '__main__':
    main()
