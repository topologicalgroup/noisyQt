# from PIL import Image
from src.denoiser import Denoiser
# from src.db import Database
# from io import BytesIO

if __name__ == "__main__":
    print("[INFO] Hi, This is a simple application that tests out image denoising using transformers.")
    print("""[INFO] The model used comes from the paper "SwinIR: Image Restoration Using Swin Transformer" by Liang et al.""")
    print("[INFO] https://arxiv.org/abs/2108.10257")

    denoiser_50 = Denoiser("models/color_swinir_noise50.pth")
    denoiser_25 = Denoiser("models/color_swinir_noise25.pth")
    denoiser_15 = Denoiser("models/color_swinir_noise15.pth")

    # img = Image.open("data/frog.png")
    # denoised_image = denoiser.denoise_image(img)
    # db = Database("images.db")
    # db.insert("frog.png", img, denoised_image)

    # Database read works
    # row = db.read(1)
    # res = row["denoised"]
    # img = Image.open(BytesIO(res))
    # img.save("res.png")
