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

### [**Neural Networks**](./images/neural-networks/Dockerfile) - neural networks for inference and training
### [**Labeling**](./images/neural-networks/Dockerfile) - labeling tools
### [**Collaboration**](./images/neural-networks/Dockerfile) - collaboration tools

Unique deps:

```text
supervisely==6.72.70
```

### [**Synthetic Data**](./images/synthetic-data/Dockerfile) - synthetic data generation tools

Unique deps:

```text
supervisely==6.72.70
supervisely[augs]==6.72.70
opencv-python==4.5.5.62
albumentations==1.1.0
```

### [**Data Operations**](./images/data-operations/Dockerfile) - data operations tools

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
``````
### [**Visualization & Stats**](./images/visualization-stats/Dockerfile) - visualization and statistics tools

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
aniso8601==9.0.1
certifi==2021.10.8
charset-normalizer==2.0.10
click==8.0.3
cycler==0.11.0
Flask==2.0.2
fonttools==4.28.5
idna==3.3
imageio==2.13.5
itsdangerous==2.0.1
kiwisolver==1.3.2
networkx==2.6.3
packaging==21.3
pyparsing==3.0.6
python-dateutil==2.8.2
pytz==2021.3
PyWavelets==1.2.0
six==1.16.0
tenacity==8.0.1
tifffile==2021.11.2
websocket-client==1.2.3
Cython
pycocotools
open3d==0.15.2
```

### [**Development**](./images/development/Dockerfile) - development tools
### [**Utilities**](./images/utils/Dockerfile) - Utilities
