#!/usr/bin/env python3
import os
import re
import random

themes = ['blue', 'red', 'green', 'yellow', 'orange']
theme_colors = {
    'blue': ['#2274a5', '#c7dce8', '#e8f1f7', '#617682'],
    'red': ['#fa003f', '#fc5c84', '#f00699', '#fe4a49'],
    'green': ['#88d18a', '#00513c', '#007d55', '#74c368'],
    'yellow': ['#ffcf00', '#ffa500', '#ec8421'],
    'orange': ['#ee6123', '#7b2d26', '#f4a261', '#f8dfa0'],
}

random.seed(54321)
comps_dir = '/Users/justintse/Desktop/hyperframes/hyperframe-templates/compositions'
comps = sorted([f for f in os.listdir(comps_dir) if f.endswith('.html')])

for i, fname in enumerate(comps):
    theme = themes[i % len(themes)]
    colors = theme_colors[theme]
    primary = colors[0]
    path = os.path.join(comps_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace gradient backgrounds
    content = re.sub(r'background:\s*linear-gradient\([^)]+\);', 'background: #ffffff;', content)
    content = re.sub(r'background:\s*radial-gradient\([^)]+\);', 'background: #ffffff;', content)
    
    # Set default text to black
    content = content.replace('color: #121212;', 'color: #000000;')
    content = content.replace('color:#121212;', 'color:#000000;')
    # Replace other dark grays that were used as body text
    content = content.replace('color: #131d23;', 'color: #000000;')
    content = content.replace('color: #00513c;', 'color: #000000;')
    
    # Replace accent colors with theme primary for highlights/titles/borders
    content = content.replace('#8A6D00', primary)
    content = content.replace('#B08A00', primary)
    content = content.replace('#C2185B', primary)
    content = content.replace('#C0392B', primary)
    content = content.replace('#7fa8e9', primary)
    content = content.replace('#77a3b9', primary)
    content = content.replace('#bcabb3', colors[-1] if len(colors) > 1 else primary)
    
    # Keep tints for fills where appropriate
    # Replace old tints
    if len(colors) > 1:
        content = content.replace('#FFF3A8', colors[1])
        content = content.replace('#FFE34F', colors[1] if theme != 'yellow' else '#ffcf00')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fname} with {theme} (primary {primary})')

