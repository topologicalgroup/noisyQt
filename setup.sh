#!/bin/bash

pip install -r requirements.txt

if [ ! -d "models" ]; then
    mkdir models
fi
wget -O models/color_swinir_noise50.pth https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/005_colorDN_DFWB_s128w8_SwinIR-M_noise50.pth
