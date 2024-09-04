# DEFECT-YOLO: Enhanced Metal Surface Defect Detection

## Overview
DEFECT-YOLO is an advanced model designed to improve the detection of metal surface defects, addressing the challenges posed by inter-class similarity and intra-class variance. Based on the YOLOv8s model, DEFECT-YOLO introduces several enhancements to boost accuracy and efficiency in multi-metal defect detection.

## Key Features
- **Effective Multi-scale Downsampling Convolution Module (EMDCM):** Improves detection accuracy while minimizing parameters.
- **Atrous Spatial Pyramid Pooling with Efficient Multiscale Attention (ASPPE):** Enhances the model's ability to capture local information.
- **Multi-branch Coordinate Attention (MCA):** Strengthens feature extraction for defects.
- **Normalized Wasserstein Distance (NWD) Loss Function:** Combines localization and Complete Intersection over Union (CIoU) losses for better detection of small target defects.

## Performance
- **Mean Average Precision (mAP@0.5):** Achieves a 3.6% improvement over baseline models.
- **Parameter Increase:** Only 1.64M additional parameters.
- **Inference Speed:** Meets real-time detection requirements for industrial applications.

## Installation
To install DEFECT-YOLO, clone the repository and install dependencies:

```bash
git clone https://github.com/your-repo/DEFECT-YOLO.git
cd DEFECT-YOLO
pip install -r requirements.txt
```

## Dataset Source

```

[1] Tianchi Platform (2023) Aluminum Defect Dataset. https://tianchi.aliyun.com (accessed August 2, 2023).

[2] Huang YB, Qiu CY, Guo Y, Wang XN, Yuan K (2018) Surface Defect Saliency of Magnetic Tile. In **2018 IEEE 14th International Conference on Automation Science and Engineering (CASE)**, Munich, Germany, pp. 612-617. https://doi.org/10.1109/COASE.2018.8560423

[3] Lv XM, Duan FJ, Jiang JJ, Fu X, Gan L (2020) Deep Metallic Surface Defect Detection: The New Benchmark and Detection Network. In **Sensors**, 20(6), 1562. https://doi.org/10.3390/s20061562

[4] Song KC, Yan YH (2013) A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects. In **Applied Surface Science**, 285(21), 858–864.  https://doi.org/10.1016/j.apsusc.2013.09.002
```

