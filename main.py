# entry point

import numpy as np
from PIL import Image
from src.denoiser import Denoiser
from src.config import DEFAULT_MODEL_WEIGHT_PATH

if __name__ == "__main__":
    denoiser = Denoiser(DEFAULT_MODEL_WEIGHT_PATH)
    img = Image.open("data/dog.png")
    arr = np.asarray(img).copy()
    result_arr = denoiser.denoise_array(arr)
    denoised_image = Image.fromarray(result_arr)
    denoised_image.save("denoised_dog.png")
