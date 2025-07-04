# Downscaling-Precipitation-using-WGAN-Models
This repository contains the source code for my undergraduate thesis project titled:
**“Development of Downscaling Wasserstein Generative Adversarial Networks (WGAN) to Improve the Spatial Resolution of Low Rainfall Projections over Java Island Using NEX-GDDP-CMIP6 MIROC6 GCM Data.”**

The Python scripts in this repository demonstrate the implementation of the project. In this GAN model, I used two different generator architectures:
1. U-Net architecture:
![image](https://github.com/user-attachments/assets/7194704d-f85e-45a2-a4da-60d9179a795b)

2. U-Net++ architecture:
![image](https://github.com/user-attachments/assets/195930e4-456e-468e-8c63-cbc8ba30e66a)

The dataset used for training is the MSWEP (Multi-Source Weighted-Ensemble Precipitation) dataset, which is available from the official MSWEP website: https://www.gloh2o.org/mswep/

Once trained, the models can take low-resolution GCM data as input and perform downscaling to produce high-resolution outputs at 0.1° (approximately 11.1 km).

The image below shows a comparison of the downscaling results produced by the models:
![image](https://github.com/user-attachments/assets/1e72af3b-a74a-4e27-83b5-352edca2b252)


