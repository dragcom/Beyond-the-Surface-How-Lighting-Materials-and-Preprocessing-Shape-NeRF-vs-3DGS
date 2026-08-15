# Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS

## Overview

3D reconstruction can be sensitive to challenging conditions such as low illumination and reflective surfaces. This project investigates how material and lighting intensity affect reconstruction quality using Nerfacto and Splatfacto, and whether background removal preprocessing can improve reconstruction.

## Research Questions

1. How does object material affect 3D reconstruction quality?
2. How does lighting intensity affect reconstruction quality?
3. How do Nerfacto and Splatfacto perform under different material and lighting conditions?
4. Can background removal improve reconstruction quality under challenging conditions?

## Experimental Design

A 2 × 3 factorial design was used:

| Material | High | Medium | Low |
|---|---|---|---|
| Solid | ✓ | ✓ | ✓ |
| Transparent | ✓ | ✓ | ✓ |

### Independent Variables
- **Material:** Solid and transparent plastic
- **Lighting:** High, medium, and low intensity

### Dependent Variables
- PSNR
- SSIM
- LPIPS

## Methodology

### Data Collection

Videos were captured using an iPhone with the Blackmagic Camera application. Camera settings, including exposure, focus, and white balance, were fixed across recordings.

A 360° orbital trajectory was used to capture each object under the six experimental conditions.

### Reconstruction Pipeline

```text
Video
  ↓
Frame Extraction
  ↓
Quality Filtering
  ↓
COLMAP
  ↓
Camera Pose Estimation
  ↓
Nerfacto / Splatfacto
```
## Background Removal Preprocessing
To investigate whether background removal can improve reconstruction quality under challenging conditions (e.g., low lighting or transparent materials), we applied a preprocessing step to remove the background from all input images before feeding them into the reconstruction pipeline.

Preprocessing Pipeline
We used rembg with the birefnet-general model to segment and remove the background from each extracted frame. The preprocessing workflow is as follows:
```text
Extracted Frames
       ↓
Background Removal (rembg)
       ↓
Background-Removed Frames
       ↓
COLMAP + Nerfacto / Splatfacto
```
Implementation Details
Tool: rembg with the birefnet-general pretrained model
Input: Extracted video frames (.png, .jpg, .jpeg, .webp, .bmp)
Output: Same filename with background removed, saved to a separate output directory
Error Handling: Each image is processed individually with exception catching to prevent pipeline interruption
Example usage
python removebg_birefnet-general.py -i input_frames -o output_frames -m birefnet-general

Rationale
Background clutter can introduce noise during COLMAP feature matching and camera pose estimation, especially under low-light conditions where feature points are already sparse. By removing the background, we aim to:

Reduce irrelevant feature points

Improve feature matching accuracy on the object itself

Enhance reconstruction quality for transparent objects where background bleed-through is prominent.
The results of this comparison will be presented in the following section.

## Results

This repository contains COLMAP training image previews and rendering results for Reflective and Matted Rubik's Cubes captured under low, medium, and high lighting conditions.

The datasets are shown in the following order:

- Reflective Low
- Reflective Medium
- Reflective High
- Solid Low
- Solid Medium
- Solid High

## COLMAP Training Image Previews

| Dataset | COLMAP Preview |
|---|---|
| Reflective Low | ![Reflective Low COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Reflective%20Low.jpeg) |
| Reflective Medium | ![Reflective Medium COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Reflective%20Medium.jpeg) |
| Reflective High | ![Reflective High COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Reflective%20High.jpeg) |
| Solid Low | ![Solid Low COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Solid%20Low.jpeg) |
| Solid Medium | ![Solid Medium COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Solid%20Medium.jpeg) |
| Solid High | ![Solid High COLMAP](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/COLMAP/Solid%20High.jpeg) |

## Main Results: Original Background

### Nerfacto

| Dataset | Interpolated Video | Nerfstudio Render | Training / Result Image |
|---|---|---|---|
| Reflective Low | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Low/Reflective%20Low%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Low/Reflective%20Low%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Reflective Low Nerfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Low/results.jpeg) |
| Reflective Medium | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Medium/Reflective%20Medium%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Medium/Reflective%20Medium%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Reflective Medium Nerfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20Medium/results.jpeg) |
| Reflective High | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20High/Reflective%20High%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20High/Reflective%20High%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Reflective High Nerfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Reflective%20High/results.jpeg) |
| Solid Low | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Low/Solid%20Low%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Low/Solid%20Low%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid Low Nerfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Low/training%20results.jpeg) |
| Solid Medium | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Medium/Solid%20Medium%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Medium/Solid%20Medium%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid Medium Nerfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20Medium/training%20results.jpeg) |
| Solid High | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20High/Solid%20High%20interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20High/Solid%20High%20Nerfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid High Nerfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/nerfacto/Solid%20High/training%20results.jpeg) |

### Splatfacto

| Dataset | Interpolated Video | Nerfstudio Render | Training Result Image |
|---|---|---|---|
| Reflective Low | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Low/Reflective%20Low%20Interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Low/Reflective%20Low%20Splatfacto%20Method%20Nerfstudio%20Render.mp4) | ![Reflective Low Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Low/training%20results.jpeg) |
| Reflective Medium | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Medium/Reflective%20Medium%20Interpolated%20Video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Medium/Reflective%20Medium%20Splatfacto%20Method%20Nerfstudio%20Rendering.mp4) | ![Reflective Medium Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20Medium/training%20results.jpeg) |
| Reflective High | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20High/Reflective%20High%20Interpolated%20Video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20High/Reflective%20High%20Splatfacto%20Method%20Nerfstudio%20Rendering.mp4) | ![Reflective High Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Reflective%20High/training%20results.jpeg) |
| Solid Low | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Low/Solid%20Low%20Interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Low/Solid%20Low%20Splatfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid Low Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Low/training%20results.jpeg) |
| Solid Medium | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Medium/Solid%20Medium%20Interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Medium/Solid%20Medium%20Splatfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid Medium Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20Medium/training%20results.jpeg) |
| Solid High | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20High/Solid%20High%20Interpolated%20video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20High/Solid%20High%20Splatfacto%20Method%20Nerfstudio%20Render.mp4) | ![Solid High Splatfacto training results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/splatfacto/Solid%20High/training%20results.jpeg) |

## Background-Removed Results

The following results use the modified datasets where the background was removed before training.

### Reflective High 500

| Method | Interpolated Video | Nerfstudio Render | Result Image |
|---|---|---|---|
| Nerfacto | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/nerfacto/interpolated.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/nerfacto/nerfstudio_render.mp4) | ![Reflective High background-removed Nerfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/nerfacto/results.jpg) |
| Splatfacto | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/splatfecto/splatfacto_interpolate_video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/splatfecto/nerfstudio_render.mp4) | ![Reflective High background-removed Splatfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Reflective_High_500/splatfecto/results.jpg) |

### Solid Low 500

| Method | Interpolated Video | Nerfstudio Render | Result Image |
|---|---|---|---|
| Nerfacto | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/nerfacto/nerfacto_interpolate_video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/nerfacto/nerfstudio_render.mp4) | ![Solid Low background-removed Nerfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/nerfacto/results.jpg) |
| Splatfacto | [Open interpolated video](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/splatfecto/splatfacto_interpolate_video.mp4) | [Open Nerfstudio render](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/splatfecto/nerfstudio_render.mp4) | ![Solid Low background-removed Splatfacto results](https://raw.githubusercontent.com/dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS/main/Video%20%26%20Results/removed_background/Solid_Low_500/splatfecto/results.jpg) |

## Citation

```text
@inproceedings{nerfstudio,
	title        = {Nerfstudio: A Modular Framework for Neural Radiance Field Development},
	author       = {
		Tancik, Matthew and Weber, Ethan and Ng, Evonne and Li, Ruilong and Yi, Brent
		and Kerr, Justin and Wang, Terrance and Kristoffersen, Alexander and Austin,
		Jake and Salahi, Kamyar and Ahuja, Abhik and McAllister, David and Kanazawa,
		Angjoo
	},
	year         = 2023,
	booktitle    = {ACM SIGGRAPH 2023 Conference Proceedings},
	series       = {SIGGRAPH '23}
}

@software{gatis_rembg,
  author = {Daniel Gatis},
  title = {rembg: Rembg is a tool to remove image backgrounds},
  url = {https://github.com/danielgatis/rembg},
  license = {MIT}
}
```

## Contributors

<a href="https://github.com/OWNER/REPO/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dragcom/Beyond-the-Surface-How-Lighting-Materials-and-Preprocessing-Shape-NeRF-vs-3DGS"/>
</a>
