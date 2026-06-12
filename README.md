# NoisyQt

<!-- ![Placeholder for UI showcase](placeholder url) -->

Welcome! This is a simple, Qt implementation of the paper [SwinIR: Image Restoration Using Swin Transformer](https://arxiv.org/abs/2108.10257) by Liang et al. This is a simple wrapper around the authors' model for restoring noisy images using a Transformer.

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
