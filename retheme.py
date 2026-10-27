#!/usr/bin/env python3
import os
import re
import random

themes = ['blue', 'red', 'green', 'yellow', 'orange']
theme_colors = {
    'blue': ['#2274a5', '#c7dce8', '#e8f1f7', '#131d23', '#617682'],
    'red': ['#fa003f', '#fc5c84', '#f00699', '#fe4a49'],
    'green': ['#88d18a', '#00513c', '#007d55', '#74c368'],
    'yellow': ['#ffcf00', '#ffa500', '#ec8421'],
    'orange': ['#ee6123', '#7b2d26', '#f4a261', '#f8dfa0'],
}

random.seed(12345)
comps_dir = '/Users/justintse/Desktop/hyperframes/hyperframe-templates/compositions'
comps = sorted([f for f in os.listdir(comps_dir) if f.endswith('.html')])

for i, fname in enumerate(comps):
    theme = themes[i % len(themes)]
    colors = theme_colors[theme]
    path = os.path.join(comps_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace gradient backgrounds
    content = re.sub(r'background:\s*linear-gradient\([^)]+\);', 'background: #ffffff;', content)
    content = re.sub(r'background:\s*radial-gradient\([^)]+\);', 'background: #ffffff;', content)
    
    # Replace specific old colors
    if len(colors) > 3:
        content = content.replace('#121212', colors[3])
    content = content.replace('#8A6D00', colors[0])
    content = content.replace('#B08A00', colors[0])
    if len(colors) > 1:
        content = content.replace('#C2185B', colors[1])
    content = content.replace('#C0392B', colors[0])
    if len(colors) > 1:
        content = content.replace('#FFF3A8', colors[-1])
        content = content.replace('#FFE34F', colors[1])
    else:
        content = content.replace('#FFF3A8', '#f0f0f0')
        content = content.replace('#FFE34F', colors[0])
    if len(colors) > 1:
        content = content.replace('#7fa8e9', colors[1])
        content = content.replace('#77a3b9', colors[1])
    if len(colors) > 4:
        content = content.replace('#bcabb3', colors[4])
    elif len(colors) > 1:
        content = content.replace('#bcabb3', colors[1])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fname} with {theme}')

