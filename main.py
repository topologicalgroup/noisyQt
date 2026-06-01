from PIL import Image
from src.denoiser import Denoiser

if __name__ == "__main__":
    print("Hello, World!")
    denoiser = Denoiser("models/color_swinir_noise50.pth")
    img = Image.open("data/frog.png")
    denoised_image = denoiser.denoise_image(img)
    denoised_image.save("denoised_frog.png")
