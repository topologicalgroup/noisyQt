#!/bin/bash

pip install -r requirements.txt

if [ ! -d "models" ]; then
    mkdir models
fi

printf "Downloading monochromatic denoising model weights...\n"
wget -O models/monochrome_swinir_noise15.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/004_grayDN_DFWB_s128w8_SwinIR-M_noise15.pth
wget -O models/monochrome_swinir_noise25.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/004_grayDN_DFWB_s128w8_SwinIR-M_noise25.pth
wget -O models/monochrome_swinir_noise50.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/004_grayDN_DFWB_s128w8_SwinIR-M_noise50.pth
printf "Downloading colored denoising model weights...\n"
wget -O models/color_swinir_noise15.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/005_colorDN_DFWB_s128w8_SwinIR-M_noise15.pth
wget -O models/color_swinir_noise25.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/005_colorDN_DFWB_s128w8_SwinIR-M_noise25.pth
wget -O models/color_swinir_noise50.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/005_colorDN_DFWB_s128w8_SwinIR-M_noise50.pth
printf "Done!\n"
