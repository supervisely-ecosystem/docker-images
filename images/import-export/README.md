# List of import applications:

kitti360 - failed
## Images
- [import-images](https://github.com/supervisely-ecosystem/import-images)
- [import-images-in-sly-format](https://github.com/supervisely-ecosystem/import-images-in-sly-format)
- [convert-yolov5-to-supervisely-format](https://github.com/supervisely-ecosystem/convert-yolov5-to-supervisely-format)
- [import-images-from-cloud-storage](https://github.com/supervisely-ecosystem/import-images-from-cloud-storage)
- [import-images-from-csv](https://github.com/supervisely-ecosystem/import-images-from-csv)
- [import-images-with-masks](https://github.com/supervisely-ecosystem/import-images-with-masks)
- [import-dicom-studies](https://github.com/supervisely-ecosystem/import-dicom-studies)
- [import-pascal-voc](https://github.com/supervisely-ecosystem/import-pascal-voc)
- [remote-import](https://github.com/supervisely-ecosystem/remote-import)
- [import-from-google-cloud-storage](https://github.com/supervisely-ecosystem/import-from-google-cloud-storage)
- [import-coco](https://github.com/supervisely-ecosystem/import-coco)
- [copy-project-between-instances](https://github.com/supervisely-ecosystem/copy-project-between-instances)
- [import-csv-catalog](https://github.com/supervisely-ecosystem/import-csv-catalog)
- [import-cityscapes](https://github.com/supervisely-ecosystem/import-cityscapes)
- [import-metadata](https://github.com/supervisely-ecosystem/import-metadata)
- [import-images-groups](https://github.com/supervisely-ecosystem/import-images-groups)
- [pexels-downloader](https://github.com/supervisely-ecosystem/pexels-downloader)
- [add-properties-to-image-from-csv](https://github.com/supervisely-ecosystem/add-properties-to-image-from-csv)
- [import-coco-keypoints](https://github.com/supervisely-ecosystem/import-coco-keypoints)
- [import-movie-genre-from-its-poster](https://github.com/supervisely-ecosystem/import-movie-genre-from-its-poster)
- [flickr-downloader](https://github.com/supervisely-ecosystem/flickr-downloader)
- [import-images-in-sly-format-from-cloud-storage](https://github.com/supervisely-ecosystem/import-images-in-sly-format-from-cloud-storage)

## Videos
- [import-videos-supervisely](https://github.com/supervisely-ecosystem/import-videos-supervisely)
- [import-videos-from-cloud-storage](https://github.com/supervisely-ecosystem/import-videos-from-cloud-storage)
- [import-videos-in-sly-format](https://github.com/supervisely-ecosystem/import-videos-in-sly-format)
- [import-videos-by-urls-from-txt](https://github.com/supervisely-ecosystem/import-videos-by-urls-from-txt)
- [import-youtube-videos](https://github.com/supervisely-ecosystem/import-youtube-videos)
- [import-videos-team-files](https://github.com/supervisely-ecosystem/import-videos-team-files)
- [youtube-downloader](https://github.com/supervisely-ecosystem/youtube-downloader)

## Point clouds
- [import-pointcloud-pcd](https://github.com/supervisely-ecosystem/import-pointcloud-pcd)
- [import-pointcloud-episode](https://github.com/supervisely-ecosystem/import-pointcloud-episode)
- [import-pointcloud-ply](https://github.com/supervisely-ecosystem/import-pointcloud-ply)
- [import-pointcloud-project](https://github.com/supervisely-ecosystem/import-pointcloud-project)
- [import-kitti-3d](https://github.com/supervisely-ecosystem/import-kitti-3d)
- [import-las-format](https://github.com/supervisely-ecosystem/import-las-format)
- [import-kitti-360](https://github.com/supervisely-ecosystem/import-kitti-360/tree/master/supervisely_app)

## DICOM
- [import-dicom-studies](https://github.com/supervisely-ecosystem/import-dicom-studies)
- [import-dicom-volumes](https://github.com/supervisely-ecosystem/import-dicom-volumes)
- [import-volumes-with-anns](https://github.com/supervisely-ecosystem/import-volumes-with-anns)

## Custom docker images:

**supervisely/remote-import:1.1.0**

- [remote-import](https://github.com/supervisely-ecosystem/remote-import)

**supervisely/coco-dataset:1.0.0"**

- [import-coco](https://github.com/supervisely-ecosystem/import-coco)
- [import-coco-keypoints](https://github.com/supervisely-ecosystem/import-coco-keypoints)

**supervisely/pointcloud:1.0.0**

- [import-pointcloud-pcd](https://github.com/supervisely-ecosystem/import-pointcloud-pcd)
- [import-pointcloud-ply](https://github.com/supervisely-ecosystem/import-pointcloud-ply)

**supervisely/import-export-kitty:1.0.2**

- [import-kitti-3d](https://github.com/supervisely-ecosystem/import-kitti-3d)

- import-kitti-360
- import-dicom-studies
- import-from-google-cloud-storage

## Dependencies per application:

```text
#base
supervisely==6.72.70
black
isort


# import-images
# import-images-in-sly-format
# convert-yolov5-to-supervisely-format
# import-images-from-csv
# import-images-with-masks
# import-pascal-voc
# copy-project-between-instances
# import-csv-catalog
# import-cityscapes
# import-metadata
# import-images-groups
# pexels-downloader
# add-properties-to-image-from-csv
# import-movie-genre-from-its-poster
# flickr-downloader
# import-images-in-sly-format-from-cloud-storage
# import-videos-supervisely
# import-videos-from-cloud-storage
# import-videos-in-sly-format
# import-videos-by-urls-from-txt
# import-youtube-videos
# import-videos-team-files
# youtube-downloader
# import-pointcloud-episode
# import-pointcloud-project
# import-las-format
# import-dicom-volumes
# import-volumes-with-anns
supervisely==6.72.70

# import DICOM studies
gdcm==1.1
pylibjpeg==1.4.0
pylibjpeg-libjpeg==1.3.1

# remote import
supervisely==6.72.70
htmllistparse==0.6.0

# import from google cloud storage
supervisely==6.72.70
google-cloud-storage==1.35.0

# import coco
supervisely==6.72.70
pycocotools==2.0.6

# import coco keypoints
supervisely==6.72.70
pycocotools==2.0.6

# improt youtube videos
supervisely==6.72.70
yt-dlp==2023.3.4

# import-videos-team-files
supervisely==6.72.70
moviepy==1.0.3

# youtube downloader
supervisely==6.72.70
moviepy==1.0.3
google-api-python-client==2.81.0
yt-dlp==2023.3.4

# import pointcloud ply
supervisely==6.72.70
open3d==0.15.2

# import kitti 3d
supervisely==6.72.70
open3d==0.15.2

# import las format
supervisely==6.72.70
scikit-learn==0.24.1
laspy==2.0.1
lazrs==0.3.0

# import kitti 360
supervisely==6.72.70
git+https://github.com/autonomousvision/kitti360Scripts.git
transforms3d==0.3.1
open3d==0.14.1


# import DICOM studies
supervisely==6.72.70
gdcm==1.1
pylibjpeg==1.4.0
pylibjpeg-libjpeg==1.3.1
```

# List of export applications:

## Images

- [export-as-masks](https://github.com/supervisely-ecosystem/export-as-masks)
- [export-to-supervisely-format](https://github.com/supervisely-ecosystem/export-to-supervisely-format)
- [convert-supervisely-to-yolov5-format](https://github.com/supervisely-ecosystem/convert-supervisely-to-yolov5-format)
- [export-to-coco](https://github.com/supervisely-ecosystem/export-to-coco)
- [export-only-labeled-items](https://github.com/supervisely-ecosystem/export-only-labeled-items)
- [export-to-pascal-voc](https://github.com/supervisely-ecosystem/export-to-pascal-voc)
- [export-activity-as-csv](https://github.com/supervisely-ecosystem/export-activity-as-csv)
- [export-to-dota](https://github.com/supervisely-ecosystem/export-to-dota)
- [export-to-cityscapes](https://github.com/supervisely-ecosystem/export-to-cityscapes)
- [export-to-yolov8](https://github.com/supervisely-ecosystem/export-to-yolov8)
- [export-metadata](https://github.com/supervisely-ecosystem/export-metadata)
- [download-images](https://github.com/supervisely-ecosystem/download-images)
- [render-video-from-images](https://github.com/supervisely-ecosystem/render-video-from-images)
- [export-project-to-cloud-storage](https://github.com/supervisely-ecosystem/export-project-to-cloud-storage)
- [create-json-with-reference-items](https://github.com/supervisely-ecosystem/create-json-with-reference-items)
- [download-images-csv](https://github.com/supervisely-ecosystem/download-images-csv)
- [tags-to-image-urls](https://github.com/supervisely-ecosystem/tags-to-image-urls)
- [export-items-after-labeling-job-review](https://github.com/supervisely-ecosystem/export-items-after-labeling-job-review)
- [export-to-coco-mask](https://github.com/supervisely-ecosystem/export-to-coco-mask)

## Videos

- [export-videos-project-in-supervisely-format](https://github.com/supervisely-ecosystem/export-videos-project-in-supervisely-format)
- [export-only-labeled-items](https://github.com/supervisely-ecosystem/export-only-labeled-items)
- [render-video-labels-to-mp4](https://github.com/supervisely-ecosystem/render-video-labels-to-mp4)
- [render-video-from-images](https://github.com/supervisely-ecosystem/render-video-from-images)
- [export-items-after-labeling-job-review](https://github.com/supervisely-ecosystem/export-items-after-labeling-job-review)

## Point clouds

- [export-pointclouds-project-in-supervisely-format](https://github.com/supervisely-ecosystem/export-pointclouds-project-in-supervisely-format)
- [export-only-labeled-items](https://github.com/supervisely-ecosystem/export-only-labeled-items)
- [export-pointcloud-episode](https://github.com/supervisely-ecosystem/export-pointcloud-episode)
- [export-to-kitti-3d](https://github.com/supervisely-ecosystem/export-to-kitti-3d)
- [export-items-after-labeling-job-review](https://github.com/supervisely-ecosystem/export-items-after-labeling-job-review)

## DICOM
- [export-volume-project](https://github.com/supervisely-ecosystem/export-volume-project)
- [export-volume-project-to-cloud-storage](https://github.com/supervisely-ecosystem/export-volume-project-to-cloud-storage)

## Custom docker images:

**supervisely/import-export-kitty:1.0.3**

- [export-to-kitti-3d](https://github.com/supervisely-ecosystem/export-to-kitti-3d)

## Dependencies per application:

```text
#export-as-masks
#export-to-supervisely-format
#convert-supervisely-to-yolov5-format
#export-to-coco
#export-only-labeled-items
#export-activity-as-csv
#export-to-dota
#export-to-cityscapes
#export-to-yolov8
#export-metadata
#download-images
#render-video-from-images
#export-project-to-cloud-storage
#create-json-with-reference-items
#download-images-csv
#tags-to-image-urls
#export-items-after-labeling-job-review
#export-to-coco-mask
supervisely==6.72.55

#export-to-pascal-voc
supervisely==6.68.109
lxml==4.6.3

# Videos

#export-videos-project-in-supervisely-format
#export-only-labeled-items
#render-video-labels-to-mp4
#render-video-from-images
#export-items-after-labeling-job-review
supervisely==6.72.55


# Point cloud
# export-pointclouds-project-in-supervisely-format
# export-only-labeled-items
# export-pointcloud-episode
# export-items-after-labeling-job-review
supervisely==6.72.55

# export-to-kitti-3d
supervisely==6.72.55
open3d==0.13.0
scikit-image==0.18.3

# DICOM
# export-volume-project
# export-volume-project-to-cloud-storage
supervisely==6.72.55
```
