# List of visualization and stats applications:

## Images

- [classes-stats-for-images](https://github.com/supervisely-ecosystem/classes-stats-for-images)
- [object-size-stats](https://github.com/supervisely-ecosystem/object-size-stats)
- [objects-thumbnails-preview-by-class](https://github.com/supervisely-ecosystem/objects-thumbnails-preview-by-class)
- [classes-co-occurrence-matrix](https://github.com/supervisely-ecosystem/classes-co-occurrence-matrix)
- [interactive-objects-distribution](https://github.com/supervisely-ecosystem/interactive-objects-distribution)
- [thumbnails-preview](https://github.com/supervisely-ecosystem/thumbnails-preview)
- [embeddings-app](https://github.com/supervisely-ecosystem/embeddings-app)
- [compare-models-predictions-on-demo-video](https://github.com/supervisely-ecosystem/compare-models-predictions-on-demo-video)
- [labels-spatial-distribution](https://github.com/supervisely-ecosystem/labels-spatial-distribution)
- [classification-metrics](https://github.com/supervisely-ecosystem/classification-metrics)
- [tags-co-occurrence-matrix](https://github.com/supervisely-ecosystem/tags-co-occurrence-matrix)
- [consensus](https://github.com/supervisely-ecosystem/consensus)
- [instance-segmentation-metrics](https://github.com/supervisely-ecosystem/instance-segmentation-metrics)

## Videos

- [render-video-labels-to-mp4](https://github.com/supervisely-ecosystem/render-video-labels-to-mp4)
- [video-objects-stats-for-every-class](https://github.com/supervisely-ecosystem/video-objects-stats-for-every-class)
- [compare-models-predictions-on-demo-video](https://github.com/supervisely-ecosystem/compare-models-predictions-on-demo-video)
- [action-recognition-stats](https://github.com/supervisely-ecosystem/action-recognition-stats)

## Point cloud

- [project-3d-stats](https://github.com/supervisely-ecosystem/project-3d-stats)

## Custom docker images:

**supervisely/thumbnails-preview:1.0.0**

- [thumbnails-preview](https://github.com/supervisely-ecosystem/thumbnails-preview)
- [objects-thumbnails-preview-by-class](https://github.com/supervisely-ecosystem/objects-thumbnails-preview-by-class)


**supervisely/labels-spatial-distribution:1.0.0**

- [labels-spatial-distribution](https://github.com/supervisely-ecosystem/labels-spatial-distribution)
Fixed - base-py-sdk

**instance-segmentation-metrics:1.0.0**

- [instance-segmentation-metrics](https://github.com/supervisely-ecosystem/instance-segmentation-metrics)


## Dependencies per application:

```text
# render-video-labels-to-mp4
# video-objects-stats-for-every-class
# compare-models-predictions-on-demo-video
# action-recognition-stats
# classes-stats-for-images
# interactive-objects-distribution
# compare-models-predictions-on-demo-video
# tags-co-occurrence-matrix
# consensus
# labels-spatial-distribution
supervisely==6.72.55

# objects-thumbnails-preview-by-class
supervisely==6.72.55
diskcache==5.2.1

# classes-co-occurrence-matrix
supervisely==6.35.0
supervisely[apps]==6.35.0
seaborn==0.11.0

# thumbnails-preview
supervisely==6.72.55
diskcache==5.2.1

# embeddings-app
supervisely==6.70.15
opencv-python==4.6.0.66
transformers
timm
torch
scikit-learn
umap-learn

# classification-metrics
supervisely==6.69.76
scikit-learn

# instance-segmentation-metrics
supervisely==6.72.2
scikit-learn
pycocotools
Cython

# project-3d-stats
supervisely==6.72.55
open3d==0.15.2
```