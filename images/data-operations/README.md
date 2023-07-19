# List of data operations applications:

- [sys-clone-project](https://github.com/supervisely-ecosystem/sys-clone-project)
- [merge-datasets](https://github.com/supervisely-ecosystem/merge-datasets)
- [convert-class-shape](https://github.com/supervisely-ecosystem/convert-class-shape)
- [turn-video-project-into-images](https://github.com/supervisely-ecosystem/turn-video-project-into-images)
- [tag-train-val-test](https://github.com/supervisely-ecosystem/tag-train-val-test)
- [extract-frames-from-videos](https://github.com/supervisely-ecosystem/extract-frames-from-videos)
- [create-trainset-for-smarttool](https://github.com/supervisely-ecosystem/create-trainset-for-smarttool)
- [merge-classes](https://github.com/supervisely-ecosystem/merge-classes)
- [filter-images](https://github.com/supervisely-ecosystem/filter-images)
- [imgaug-studio](https://github.com/supervisely-ecosystem/imgaug-studio)
- [diff-merge-images-projects](https://github.com/supervisely-ecosystem/diff-merge-images-projects)
- [diff-merge-project-meta](https://github.com/supervisely-ecosystem/diff-merge-project-meta)
- [sliding-window/tree/master/split](https://github.com/supervisely-ecosystem/sliding-window/tree/master/split)
- [resize-images](https://github.com/supervisely-ecosystem/resize-images)
- [images-project-to-videos-project](https://github.com/supervisely-ecosystem/images-project-to-videos-project)
- [crop-objects-on-images](https://github.com/supervisely-ecosystem/crop-objects-on-images)
- [unpack-anyshape](https://github.com/supervisely-ecosystem/unpack-anyshape)
- [rasterize-objects-on-images](https://github.com/supervisely-ecosystem/rasterize-objects-on-images)
- [rasterize-objects-on-images](https://github.com/supervisely-ecosystem/rasterize-objects-on-images)
- [object-tags-redactor](https://github.com/supervisely-ecosystem/object-tags-redactor)
- [split-dataset](https://github.com/supervisely-ecosystem/split-dataset)
- [compare-models-predictions-on-demo-video](https://github.com/supervisely-ecosystem/compare-models-predictions-on-demo-video)
- [convert-to-semantic-segmentation](https://github.com/supervisely-ecosystem/convert-to-semantic-segmentation)
- [render-video-from-images](https://github.com/supervisely-ecosystem/render-video-from-images)
- [unpack-key-value-tags](https://github.com/supervisely-ecosystem/unpack-key-value-tags)
- [create-foreground-mask](https://github.com/supervisely-ecosystem/create-foreground-mask)
- [sliding-window/tree/master/merge](https://github.com/supervisely-ecosystem/sliding-window/tree/master/merge)
- [convert-labels-to-rotated-bboxes](https://github.com/supervisely-ecosystem/convert-labels-to-rotated-bboxes)
- [tag-by-dataset-name](https://github.com/supervisely-ecosystem/tag-by-dataset-name)
- [rotate-images](https://github.com/supervisely-ecosystem/rotate-images)
- [tags-to-image-urls](https://github.com/supervisely-ecosystem/tags-to-image-urls)
- [copy-image-tags-to-objects](https://github.com/supervisely-ecosystem/copy-image-tags-to-objects)
- [perspective-transform-using-qr-code](https://github.com/supervisely-ecosystem/perspective-transform-using-qr-code)
- [bind-nested-objects-into-groups](https://github.com/supervisely-ecosystem/bind-nested-objects-into-groups)
- [dev-assets-transfer](https://github.com/supervisely-ecosystem/dev-assets-transfer)
- [tag-to-object-class](https://github.com/supervisely-ecosystem/tag-to-object-class)
- [slice-volumes](https://github.com/supervisely-ecosystem/slice-volumes)
- [object-class-to-tag](https://github.com/supervisely-ecosystem/object-class-to-tag)
- [merge-tags](https://github.com/supervisely-ecosystem/merge-tags)
- [compare-models-predictions-on-demo-video](https://github.com/supervisely-ecosystem/compare-models-predictions-on-demo-video)
- [take-fragment-from-video](https://github.com/supervisely-ecosystem/take-fragment-from-video)
- [interpolation-tracker-v1](https://github.com/supervisely-ecosystem/interpolation-tracker-v1)
- [change-video-framerate](https://github.com/supervisely-ecosystem/change-video-framerate)
- [convert-video-class-shape](https://github.com/supervisely-ecosystem/convert-video-class-shape)
- [convert-video-class-shape](https://github.com/supervisely-ecosystem/convert-video-class-shape)
- [youtube-downloader](https://github.com/supervisely-ecosystem/youtube-downloader)
- [synthetic-videos-for-tracking](https://github.com/supervisely-ecosystem/synthetic-videos-for-tracking)
- [convert_ptc_to_ptc_episodes](https://github.com/supervisely-ecosystem/convert_ptc_to_ptc_episodes)
- [slice-volumes](https://github.com/supervisely-ecosystem/slice-volumes)




## Custom docker images:

**supervisely/perspective-transform-using-qr-code:1.0.0**

- [perspective-transform-using-qr-code](https://github.com/supervisely-ecosystem/perspective-transform-using-qr-code)


## Dependencies per application:

```text
# sys-clone-project
# merge-datasets
# convert-class-shape
# turn-video-project-into-images
# tag-train-val-test
# extract-frames-from-videos
# create-trainset-for-smarttool
# merge-classes
# filter-images
# diff-merge-images-projects
# diff-merge-project-meta
# sliding-window/tree/master/split
# resize-images
# images-project-to-videos-project
# crop-objects-on-images
# unpack-anyshape
# rasterize-objects-on-images
# object-tags-redactor
# split-dataset
# compare-models-predictions-on-demo-vi
# convert-to-semantic-segmentation
# render-video-from-images
# unpack-key-value-tags
# create-foreground-mask
# sliding-window/tree/master/merge
# convert-labels-to-rotated-bboxes
# tag-by-dataset-name
# rotate-images
# tags-to-image-urls
# copy-image-tags-to-objects
# bind-nested-objects-into-groups
# dev-assets-transfer
# tag-to-object-class
# slice-volumes
# object-class-to-tag
# merge-tags
supervisely==6.72.70


# imgaug-studio
supervisely==6.72.70
supervisely[docs]==6.72.70

# perspective-transform-using-qr-code
used to print cool text to stdout
art==5.7 
black==22.6.0 
python-dotenv
supervisely==6.68.26
imutils
pyzbar==0.1.9


# compare-models-predictions-on-demo-video
# interpolation-tracker-v1
# convert-video-class-shape
# convert-video-class-shape
# youtube-downloader
# synthetic-videos-for-tracking
# convert_ptc_to_ptc_episodes
# slice-volumes
supervisely==6.72.70

# take-fragment-from-video
supervisely==6.72.70
moviepy==1.0.3
imageio-ffmpeg==0.4.7

# change-video-framerate
supervisely==6.72.70
ffmpeg_python==0.2.0
```