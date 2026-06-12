import torch
import numpy as np
from PIL import Image
from .models.network_swinir import SwinIR

class Denoiser:
    """ Denoiser
        A wrapper around SwinIR for denoising images.

    Args:
        model_weights_path (str): path to SwinIR .pth checkpoint

    Methods:
        denoise_array(arr) -> np.ndarray
    """

    def __init__(self, model_weights_path: str):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Configuration settings taken from
        # https://github.com/JingyunLiang/SwinIR/blob/main/main_test_swinir.py
        model = SwinIR(upscale=1, in_chans=3, img_size=128, window_size=8,
                    img_range=1., depths=[6, 6, 6, 6, 6, 6], embed_dim=180, num_heads=[6, 6, 6, 6, 6, 6],
                    mlp_ratio=2, upsampler='', resi_connection='1conv').to(device)
        param_key_g = "params"
        checkpoint = torch.load(model_weights_path, map_location=device)
        model.load_state_dict(checkpoint[param_key_g] if param_key_g in checkpoint.keys() else checkpoint, strict=True)

        self.device = device
        self.model = model
        self.model.eval()

    def denoise_image(self, data: np.ndarray | Image.Image) -> Image.Image:
        if isinstance(data, Image.Image):
            arr = np.asarray(data)
        else:
            arr = data
        # A copy must be made to suppress writable warning
        denoised_arr = self.denoise_array(arr.copy())
        denoised_image = Image.fromarray(denoised_arr)
        return denoised_image

    def denoise_array(self, arr: np.ndarray) -> np.ndarray:
        """Denoise an HxWx3 (height, width, channels) uint8 RGB numpy array."""
        if arr.ndim != 3 or arr.shape[2] != 3:
            raise ValueError("denoise_array expects HxWx3 RGB array")

        if arr.dtype != np.uint8:
            arr_uint8 = (255 * np.clip(arr, 0.0, 1.0)).astype(np.uint8)
        else:
            arr_uint8 = arr

        inp = torch.from_numpy(arr_uint8).permute(2,0,1)   # CxHxW
        inp = inp.unsqueeze(0).float().to(self.device) / 255.0  # 1xCxHxW, normalized in [0.0, 1.0]
        # Oh no! The treated CUDA out of memory error can occur on larger images ;_;
        # Got the error on raytraced_original.png
        with torch.no_grad():
            out_t = self.model(inp)

        out = (out_t.clamp(0, 1).squeeze(0).permute(1, 2, 0).cpu().numpy() * 255.0)
        out = np.clip(out, 0, 255).astype(np.uint8)
        return out
