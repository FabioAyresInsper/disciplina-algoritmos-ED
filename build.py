import subprocess
import pathlib
import os.path as osp
import functools
import glob
import sys

DEBUG=True

sh = functools.partial(subprocess.run, check=True, shell=True, capture_output=not DEBUG)
DATE_CMD = 'date +\"%d/%m/%Y %H:%M\"'
PANDOC_HANDOUT = 'pandoc -f markdown+pipe_tables+backtick_code_blocks+fenced_divs+raw_html --lua-filter=filters/message.lua --lua-filter=filters/spacer.lua --lua-filter=filters/graphviz.lua --lua-filter=filters/side-by-side.lua  -s --template templates/tufte-handout.tex '
PANDOC_PAGE = 'pandoc -f markdown+pipe_tables+backtick_code_blocks+fenced_divs+raw_html --toc --toc-depth=1 -s --template templates/template-index.html '
PANDOC_VARS = f'-V date="$({DATE_CMD})" -V versao="2025/02"'


def find_chrome():
    """Locate the Chrome installed by the devcontainer's `@puppeteer/browsers`."""
    candidates = sorted(glob.glob(osp.expanduser('~/chrome/*/chrome-linux64/chrome')))
    if candidates:
        return candidates[-1]
    raise RuntimeError(
        'No Chrome install found under ~/chrome. '
        'Run: npx @puppeteer/browsers install chrome@stable'
    )


MARP_CMD = f'npx @marp-team/marp-cli --browser-path {find_chrome()}  --theme templates/slides.css  --allow-local-files --html '


src = pathlib.Path('src')

if len(sys.argv) > 1:
    all_files = [pathlib.Path(f) for f in sys.argv[1:]]
    show_file_list = True
else:
    all_files = src.rglob('*')
    show_file_list = False
sh('mkdir -p temp')

for f in all_files:
    dir, fname = osp.split(f)
    without_src = "docs" / f.relative_to('src')
    

    if osp.isdir(f):
        if not show_file_list:
            print('Creating dir', without_src)
        sh(f'mkdir -p {without_src}')
    elif fname.endswith('.md') and 'handout' in fname:
        resname = without_src.parent / fname.replace('.md', '.pdf')
        if show_file_list:
            print(resname)
        else:
            print('Handout', f)
        sh(f'{PANDOC_HANDOUT} {PANDOC_VARS} --resource-path {dir} {f} -o {resname}')
    elif fname.endswith('.md') and 'slide' in fname:
        resname = without_src.parent / fname.replace('.md', '.pdf')
        if show_file_list:
            print(resname)
        else:
             print('Slides', f)
        sh(f'{MARP_CMD} -o {resname} {f}')
    elif fname.endswith('.md'):
        resname = without_src.parent / fname.replace('.md', '.html')
        if show_file_list:
            print(resname)
        else:
            print('Page', f)
        sh(f'{PANDOC_PAGE} {PANDOC_VARS} --resource-path {dir} {f} -o {resname}')
    else:
        if show_file_list:
            print(f)
        else:
            print('copy', f)
        sh(f'cp {f} {without_src}')
