#!/usr/bin/env python3
"""Offline content and local-link integrity checks; not a replacement for Astro build."""
import re,sys,datetime
from pathlib import Path
try:import yaml
except ImportError:
 print('PyYAML missing. Install with pip install PyYAML',file=sys.stderr);sys.exit(2)
root=Path(__file__).resolve().parents[1]
files=list((root/'src/content/blog').glob('*.md'))
errors=[]
slugs={p.stem for p in files}
cats={'meal','housework','cleaning','subscriptions'}
seen_titles=set()
for p in files:
 s=p.read_text(encoding='utf-8')
 match=re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$',s,re.S)
 if not match:errors.append(f'{p.name}: missing YAML frontmatter');continue
 try:data=yaml.safe_load(match.group(1))
 except Exception as e:errors.append(f'{p.name}: YAML error: {e}');continue
 for k in ['title','description','publishedAt','category','readingMinutes']:
  if k not in data:errors.append(f'{p.name}: missing {k}')
 if data.get('category') not in cats:errors.append(f'{p.name}: unknown category')
 if data.get('title') in seen_titles:errors.append(f'{p.name}: duplicate title')
 seen_titles.add(data.get('title'))
 if len(match.group(2))<850:errors.append(f'{p.name}: body appears too short')
 if not re.search(r'^## ',match.group(2),re.M):errors.append(f'{p.name}: missing H2')
 for link in re.findall(r'\]\((/[^)]+)\)',match.group(2)):
  m=re.fullmatch(r'/articles/([a-z0-9-]+)/',link)
  if m and m.group(1) not in slugs:errors.append(f'{p.name}: broken article link {link}')
  if not m:errors.append(f'{p.name}: unexpected internal link {link}')
 for source in data.get('sources',[]):
  if not source.get('url','').startswith('https://'):errors.append(f'{p.name}: non-HTTPS source')
print(f'Checked {len(files)} Japanese articles, {len(seen_titles)} titles, internal article links and required fields.')
if errors:
 for e in errors:print('FAIL:',e)
 sys.exit(1)
print('PASS: offline content validation')
