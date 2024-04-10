# DMDTC
Dual-domain Mean-reverting Diffusion Model-enhanced Temporal Compressive Coherent Diffraction Imaging
## Abstract
Temporal compressive coherent diffraction imaging is a lensless imaging technique with the capability to capture fast-moving small objects. However, the accuracy of imaging reconstruction is often hindered by the loss of frequency domain information, a critical factor limiting the quality of the reconstructed images. To improve the quality of these reconstructed images, a method dual-domain mean-reverting diffusion model-enhanced temporal compressive coherent diffraction imaging (DMDTC) has been introduced. DMDTC leverages the mean-reverting diffusion model to acquire prior information in both frequency and spatial domain through sample learning. The frequency domain mean-reverting diffusion model is employed to recover missing information, while hybrid input-output algorithm is carried out to reconstruct the spatial domain image. The spatial domain mean-reverting diffusion model is utilized for denoising and image restoration. DMDTC has demonstrated a significant enhancement in the quality of the reconstructed images. The results indicate that the structural similarity and peak signal-to-noise ratio of images reconstructed by DMDTC surpass those obtained through conventional methods. DMDTC enables high time frame rates and high spatial resolution in coherent diffraction imaging. 

## Main procedure
![Main procedure](/Figures/Fig3.png "Main proceduce")
## Requirements and Dependencies
  ```
  einops==0.6.0
  lmdb==1.3.0
  lpips==0.1.4
  numpy==1.23.5
  opencv-python==4.6.0.66
  Pillow==9.3.0
  PyYAML==6.0
  scipy==1.9.3
  tensorboardX==2.5.1
  timm==0.6.12
  torch==1.13.0
  torchsummaryX==1.3.0
  torchvision==0.14.0
  tqdm
  gradio
  ```
## Checkpoints
We provide the pre-trained model. Click [pre-trained model](https://pan.baidu.com/s/1733UrbTN1syOTkZh7eGksw?pwd=DMDT) to download the pre-trained model.(Extraction code: DMDT)
## Dataset
We provide the training dataset. Click [datasets](https://pan.baidu.com/s/12zrsjyG96VHLZP47njlAqw?pwd=DMDT) to download the dateset for training in our paper.(Extraction code: DMDT)
## Training
  Before start to training, the config file needs modifiction. The config path is `Code/prior_learning/config/deblurring/options/train/ir-sde.yml`.

  Once you have modified the config file, run the following code to train your own model

  `python train.py -opt=options/train/ir-sde.yml`
## Reconstruction
  Before conducting reconstruction, a [pre-trained model](https://pan.baidu.com/s/1733UrbTN1syOTkZh7eGksw?pwd=DMDT) or self-trained model is needed. Config file (whose path is `Code/prior_learning/config/deblurring/options/test/ir-sde.yml`) is needed to be modified for the model.

  
  First in `Code/Time_domain_unfolding`, run `python test.py` to decompress a sapshot into multiple frames.

  To supplement the frequency domain information, in path `Code/prior_learning/config/deblurring` run `python test.py -opt=options/test/ir-sde.yml`.

  Then run `python Code/HIO-DNN/PR_HIO_FFDNet.py` to obtain the spatial domain images. After that, simply run again `python test.py -opt=options/test/ir-sde.yml` to obtain the final results.(Change the pre-trained model from frequency to spatial!)
## Acknowledgement
  Thanks to these repositories for providing us with method code and experimental data: https://github.com/Algolzw/image-restoration-sde , https://github.com/zsm1211/TC-CDI
## Other Related Projects
  * Lens-less imaging via score-based generative model  
[<font size=5>**[Paper]**</font>](https://www.opticsjournal.net/M/Articles/OJf1842c2819a4fa2e/Abstract)   [<font size=5>**[Code]**</font>](https://github.com/yqx7150/LSGM)

  * Multi-phase FZA Lensless Imaging via Diffusion Model  
[<font size=5>**[Paper]**</font>](https://opg.optica.org/oe/fulltext.cfm?uri=oe-31-12-20595&id=531211)   [<font size=5>**[Code]**</font>](https://github.com/yqx7150/MLDM)    
  * Diffusion Models for Medical Imaging    
[<font size=5>**[Paper]**</font>](https://github.com/yqx7150/Diffusion-Models-for-Medical-Imaging)   [<font size=5>**[Code]**</font>](https://github.com/yqx7150/Diffusion-Models-for-Medical-Imaging)   [<font size=5>**[PPT]**</font>](https://github.com/yqx7150/HKGM/tree/main/PPT)  
