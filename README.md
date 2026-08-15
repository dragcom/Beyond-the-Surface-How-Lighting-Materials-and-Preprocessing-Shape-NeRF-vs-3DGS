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
