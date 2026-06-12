import sys

# from .denoiser import Denoiser
# from .db import Database
# from PIL import Image
# from io import BytesIO

def main() -> int:
    print("Hi, This is a simple application that tests out image denoising using transformers.")
    print('The model used comes from the paper "SwinIR: Image Restoration Using Swin Transformer" by Liang et al.')
    print("https://arxiv.org/abs/2108.10257")

    """
    denoiser_50 = Denoiser("weights/color_swinir_noise50.pth")
    denoiser_25 = Denoiser("weights/color_swinir_noise25.pth")
    denoiser_15 = Denoiser("weights/color_swinir_noise15.pth")
    dn = denoiser_15
    db = Database("images.db")

    file_name = "pattern.png"
    img = Image.open("data/" + file_name).convert("RGB")
    denoised_image = dn.denoise_image(img)
    db.insert("pattern.png", img, denoised_image)

    # Database read works
    row = db.read(1)
    res = row["denoised"]
    img = Image.open(BytesIO(res))
    img.save("result/" + file_name)
    """

    return 0

if __name__ == "__main__":
    sys.exit(main())
