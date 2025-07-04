# Downscaling-Precipitation-using-WGAN-Models
This is a source code for my undergraduate thesis project called Development of Downscaling Wasserstein Generative Adversarial  Networks (WGAN) to Improve Spatial Resolution of Java Island Low  Rainfall Projections Using NEX-GDDP-CMIP6 MIROC6 GCM Model.

The sample script used to do this project is contained in the Python file, in this GAN model I use 2 different Generator architectures, the first using the UNET architecture as follows:

![image](https://github.com/user-attachments/assets/7194704d-f85e-45a2-a4da-60d9179a795b)

and UNET++ architecture as follows:

![image](https://github.com/user-attachments/assets/195930e4-456e-468e-8c63-cbc8ba30e66a)

The dataset used to train the model is the MSWEP (Multi-Source Weighted-Ensemble Precipitation) dataset which can be obtained from the official MSWEP website below https://www.gloh2o.org/mswep/ .

Models that have been trained using the MSWEP dataset can then be given input GCM model data that has a low resolution and the model will perform dowscaling so as to produce a high resolution of 0.1° (11.1 km).

The following images is a comparison from the downscaling results of the model that has been made.
![image](https://github.com/user-attachments/assets/1e72af3b-a74a-4e27-83b5-352edca2b252)


