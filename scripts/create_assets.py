#!/usr/bin/env python3
"""Build favicons from the approved Rakushiru logo (requires Pillow)."""
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
source=root/'public/images/approved-rakushiru-logo.jpg'
if not source.exists(): source=root/'public/images/approved-rakushiru-logo.png'
if not source.exists(): source=Path('/mnt/data/teal_katakana_ra_logo_with_sparkle.png')
if not source.exists():
 raise SystemExit('Original approved logo not available at this path: adapt source before running')
source_img=Image.open(source).convert('RGB')
# Exact reference image is preserved for future adjustment.
if source.resolve() != (root/'public/images/approved-rakushiru-logo.png').resolve():
 source_img.save(root/'public/images/approved-rakushiru-logo.png', optimize=True)
p=source_img.load(); w,h=source_img.size
pixels=[]
for y in range(0,h,3):
 for x in range(0,w,3):
  r,g,b=p[x,y]
  if g>r*1.12 and g>b*1.04 and r<170:
   pixels.append((x,y))
if not pixels:raise SystemExit('Could not identify logo foreground')
box=(max(0,min(x for x,_ in pixels)-4),max(0,min(y for _,y in pixels)-4),min(w,max(x for x,_ in pixels)+5),min(h,max(y for _,y in pixels)+5))
cropped=source_img.crop(box)
canvas=Image.new('RGB',(512,512),'white')
cropped.thumbnail((425,425),Image.Resampling.LANCZOS)
canvas.paste(cropped,((512-cropped.width)//2,(512-cropped.height)//2))
for size,path in [(32,'favicon-32.png'),(48,'favicon-48.png'),(180,'apple-touch-icon.png'),(192,'icon-192.png'),(512,'icon-512.png')]:
 canvas.resize((size,size),Image.Resampling.LANCZOS).save(root/'public'/path,optimize=True)
canvas.save(root/'public/favicon.ico',format='ICO',sizes=[(16,16),(32,32),(48,48),(64,64)])
(root/'public/favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="ラクしる">
<rect x="0" y="0" width="100" height="100" fill="#fff"/>
<g fill="none" stroke="#09bd9b" stroke-linecap="round" stroke-linejoin="round">
<path stroke-width="10" d="M25 29H70"/>
<path stroke-width="11" d="M23 45H70C67 67 48 79 28 84"/>
</g><path d="M80 14 Q82 22 90 24 Q82 26 80 34 Q78 26 70 24 Q78 22 80 14Z" fill="#09bd9b"/>
</svg>''',encoding='utf8')
# Open Graph graphic with Japanese font if available, no external dependencies.
from subprocess import check_output
fontfile=check_output(['fc-match','-f','%{file}','Noto Sans CJK JP']).decode().strip()
W,H=1200,630
im=Image.new('RGB',(W,H),'#f5f7f3');draw=ImageDraw.Draw(im)
draw.rounded_rectangle((44,44,1156,586),radius=30,fill='#ffffff',outline='#ddeae2',width=2)
icon=canvas.resize((155,155),Image.Resampling.LANCZOS);im.paste(icon,(115,190))
title=ImageFont.truetype(fontfile,94)
tag=ImageFont.truetype(fontfile,34)
small=ImageFont.truetype(fontfile,24)
draw.text((308,196),'ラクしる',font=title,fill='#183c39')
draw.text((309,355),'毎日の暮らしを、もっとラクに。',font=tag,fill='#183c39')
draw.text((310,484),'便利なサービスの選び方と、暮らしのヒント',font=small,fill='#597168')
im.save(root/'public/og-default.png',optimize=True)
print('Brand assets written:',box)
