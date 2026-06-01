from PIL import Image
from src.denoiser import Denoiser
from src.db import Database

if __name__ == "__main__":
    print("Hello, World!")
    # denoised_image.save("denoised_frog.png")
    denoiser = Denoiser("models/color_swinir_noise50.pth")
    img = Image.open("data/frog.png")
    denoised_image = denoiser.denoise_image(img)
    db = Database("images.db")
    # db.insert("frog.png", img, denoised_image)
    db.read("frog.png", img, denoised_image)
