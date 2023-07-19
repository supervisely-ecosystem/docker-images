# List of import applications:

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

## Dependencies per application:

```text
#base
supervisely==6.72.70
black
isort

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
git+https://github.com/autonomousvision/kitti360Scripts.git transforms3d==0.3.1
open3d==0.14.1


# import DICOM studies
supervisely==6.72.70
gdcm==1.1
pylibjpeg==1.4.0
pylibjpeg-libjpeg==1.3.1
```
