# NoisyQt

![Comparison of a noisy, and a denoised image using SwinIR](.github/res/cmp_raytraced.png)

Welcome! This is a Qt implementation of the paper [SwinIR: Image Restoration Using Swin Transformer](https://arxiv.org/abs/2108.10257) by Liang et al. This is a simple wrapper around the authors' model and denoise model weights, using a [Swin Transformer](https://arxiv.org/abs/2103.14030).

## Usage

Cloning the repository will not automatically download the necessary model weights for SwinIR. The weights we used can be found from the [authors' repository](https://github.com/JingyunLiang/SwinIR) and can be retrieved using the script below:

```bash
./download_weights.sh
```

Install the program as a package using `pip`

```bash
pip install -e .
```

And run it via `python`
```bash
python -m noisyqt
```
