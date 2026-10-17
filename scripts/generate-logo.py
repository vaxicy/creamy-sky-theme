from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]; S=4
im=Image.new('RGBA',(128*S,128*S)); d=ImageDraw.Draw(im)
def b(v): return tuple(round(x*S) for x in v)
d.ellipse(b((57,15,111,69)),fill='#FFD164')
# One continuous cloud silhouette, flat blue, without outlines or small details.
d.ellipse(b((13,55,59,101)),fill='#9EDCF3')
d.ellipse(b((34,37,88,91)),fill='#9EDCF3')
d.ellipse(b((69,58,113,102)),fill='#9EDCF3')
d.rounded_rectangle(b((22,72,104,103)),radius=14*S,fill='#9EDCF3')
im=im.resize((128,128),Image.Resampling.LANCZOS); out=ROOT/'logo/logo128.png'; out.parent.mkdir(parents=True,exist_ok=True); im.save(out)
assert im.size==(128,128) and im.mode=='RGBA'; print('Generated logo/logo128.png: 128x128 transparent')
