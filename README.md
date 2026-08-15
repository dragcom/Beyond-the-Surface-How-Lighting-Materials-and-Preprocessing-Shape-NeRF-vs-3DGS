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

Background Removal Preprocessing
BiRefNet
BiRefNet was used to remove background regions while preserving the target object.
Background removal may allow the reconstruction model to focus on relevant object features and reduce background-related artifacts.
The background-removed images were reconstructed using the same COLMAP camera poses as the baseline reconstruction. This allows the effect of preprocessing to be evaluated while keeping camera pose estimation consistent.
Images
  ↓
BiRefNet
  ↓
Background Removal
  ↓
Background-Removed Images
  ↓
Nerfacto / Splatfacto
The baseline and preprocessed pipelines therefore differ only in the image preprocessing step:
Baseline:
Original Images + Same COLMAP Poses
              ↓
       Nerfacto / Splatfacto

Preprocessed:
Background-Removed Images + Same COLMAP Poses
              ↓
       Nerfacto / Splatfacto
