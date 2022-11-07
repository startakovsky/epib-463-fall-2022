
import json
import uuid

from itertools import repeat, zip_longest

def read_json(filename):
    with open(filename) as f:
        whole_ipynb = json.loads(f.read())
    return whole_ipynb

def get_boilerplate_ipynb():
    with open('boilerplate_ipynb.json') as f:
        boilerplate_ipynb = json.loads(f.read())
    return boilerplate_ipynb

def get_markdown_cell(text):
    """Return whole_notebook_json['cells'] json value."""
    
    return {
        'cell_type': 'markdown',
        'id': str(uuid.uuid4()),
        'source': text.splitlines(),
        'metadata': {},
    }

def get_code_cell(text=None):
    return   {
        "cell_type": "code",
        "execution_count": None,
        "id": str(uuid.uuid4()),
        "metadata": {},
        "outputs": [],
        "source": []
    }

def get_code_cells_interleaved(cells):
    interleaved_cells = []
    for markdown_cell, _ in zip_longest(cells, ''):
        interleaved_cells.append(markdown_cell)
        interleaved_cells.append(get_code_cell())
    return interleaved_cells
        
def get_whole_ipynb(text, is_interleave):
    """Return ipynb"""
    whole_ipynb = {'cells': [get_markdown_cell(s) for s in text.splitlines()]}
    if is_interleave:
        whole_ipynb['cells'] = get_code_cells_interleaved(whole_ipynb['cells'])
    whole_ipynb.update(get_boilerplate_ipynb())
    return whole_ipynb

def get_whole_json(text, is_interleave):
    whole_ipynb = get_whole_ipynb(text, is_interleave)
    return json.dumps(whole_ipynb, indent=4)
