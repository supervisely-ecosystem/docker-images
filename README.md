# Base images for Supervisely applications

## Categories

### [**Import**](./images/import/Dockerfile)

Unique deps:

```text
supervisely
black
isort
htmllistparse==0.6.0
google-cloud-storage==1.35.0
pycocotools==2.0.6
yt-dlp==2023.3.4
moviepy==1.0.3
google-api-python-client==2.81.0
yt-dlp==2023.3.4
open3d==0.15.2
scikit-learn==0.24.1
laspy==2.0.1
lazrs==0.3.0
git+https://github.com/autonomousvision/kitti360Scripts.git
transforms3d==0.3.1
gdcm==1.1
pylibjpeg==1.4.0
pylibjpeg-libjpeg==1.3.1
```

### [**Export**](./images/export/Dockerfile)

Unique deps:

```text
supervisely==6.72.55
lxml==4.6.3
open3d==0.15.2
scikit-image==0.18.3
```

### [**Neural Networks**](./images/neural-networks/Dockerfile)
### [**Labeling**](./images/neural-networks/Dockerfile)
### [**Collaboration**](./images/neural-networks/Dockerfile)
Unique deps:

```text
supervisely==6.72.70
```

### [**Synthetic Data**](./images/synthetic-data/Dockerfile)

Unique deps:

```text
supervisely==6.72.70
supervisely[augs]==6.72.70
opencv-python==4.5.5.62
albumentations==1.1.0
```

### [**Data Operations**](./images/data-operations/Dockerfile)
Unique deps:

```text
supervisely==6.72.70
supervisely[docs]==6.72.70
black
isort
imutils
pyzbar==0.1.9
moviepy==1.0.3
imageio-ffmpeg==0.4.7
```

### [**Visualization & Stats**](./images/visualization-stats/Dockerfile)

Unique deps:

```text
supervisely==6.72.55
diskcache==5.2.1
seaborn==0.11.0
opencv-python==4.6.0.66
transformers
timm
torch
scikit-learn
umap-learn
Cython                      
pycocotools
open3d==0.15.2
```

### [**Development**](./images/development/Dockerfile) - development tools
### [**Utilities**](./images/utils/Dockerfile) - Utilities
