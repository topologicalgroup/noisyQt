from PIL import Image
import os

# Create side by side comparison of noisy and denoised images
# Noisy in data, denoised in result. File names have to match

inp = "data"
out = "result"
pairs = []
for f in sorted(os.listdir(inp)):
    if f.lower().endswith((".png",".jpg",".jpeg")) and os.path.exists(os.path.join(out,f)):
        pairs.append(f)

for f in pairs:
    a = Image.open(os.path.join(inp,f)).convert("RGB")
    b = Image.open(os.path.join(out,f)).convert("RGB")
    # create side-by-side
    w,h = a.size
    canvas = Image.new("RGB", (w*2, h))
    canvas.paste(a, (0,0))
    canvas.paste(b, (w,0))
    canvas.save(os.path.join(out, "cmp_"+f))
    print("Saved", "cmp_"+f)
