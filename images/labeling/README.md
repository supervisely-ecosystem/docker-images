# List of labeling applications:

- [mark-reference-objects-for-retail](https://github.com/supervisely-ecosystem/mark-reference-objects-for-retail)
- [retail-tagging](https://github.com/supervisely-ecosystem/retail-tagging)
- [nn-image-labeling annotation tool](https://github.com/supervisely-ecosystem/nn-image-labeling/tree/master/annotation-tool)
- [nn-image-labeling project dataset](https://github.com/supervisely-ecosystem/nn-image-labeling/tree/master/project-dataset)
- [review-retail-tags](https://github.com/supervisely-ecosystem/review-retail-tags)
- [visual-tagging](https://github.com/supervisely-ecosystem/visual-tagging)
- [ai-assisted-classification](https://github.com/supervisely-ecosystem/ai-assisted-classification)
- [review-labels-side-by-side](https://github.com/supervisely-ecosystem/review-labels-side-by-side)
- [action-recognition-labeling](https://github.com/supervisely-ecosystem/action-recognition-labeling)
- [mark-segments-on-synced-videos](https://github.com/supervisely-ecosystem/mark-segments-on-synced-videos)
- [mark-segments-on-synced-videos-2](https://github.com/supervisely-ecosystem/mark-segments-on-synced-videos-2)
- [object-tags-redactor](https://github.com/supervisely-ecosystem/object-tags-redactor)
- [apply-nn-to-videos-project](https://github.com/supervisely-ecosystem/apply-nn-to-videos-project)
- [gl-metric-learning](https://github.com/supervisely-ecosystem/gl-metric-learning)
- [dev-smart-tool-batched](https://github.com/supervisely-ecosystem/dev-smart-tool-batched)
- [batched-smart-tool-for-videos](https://github.com/supervisely-ecosystem/batched-smart-tool-for-videos)

## Custom docker images:

- [apply-nn-to-videos-project](https://github.com/supervisely-ecosystem/apply-nn-to-videos-project)

## Dependencies per application:

```text
# mark-reference-objects-for-retail
# retail-tagging                   
# nn-image-labeling                
# review-retail-tags               
# nn-image-labeling                
# visual-tagging                   
# ai-assisted-classification       
# review-labels-side-by-side       
# action-recognition-labeling      
# mark-segments-on-synced-videos   
# mark-segments-on-synced-videos-2 
# object-tags-redactor             
supervisely==6.35.0


# apply-nn-to-videos-project
supervisely==6.72.65
Cython
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=3.4.10.35
Pillow
PyYAML>=5.3
scipy>=1.4.1
tensorboard>=2.2
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
seaborn>=0.11.0
pandas
ftfy==6.0.3
regex
git+https://github.com/supervisely-ecosystem/depends-CLIP.git
ffmpeg-python==0.2.0
PyYAML==5.4.1

# gl-metric-learning
albumentations==1.1.0
timm==0.4.12 
numpy==1.19.1
opencv_python_headless==4.4.0.44
pytorch_lightning==0.9.0
transformers==3.3.1
scipy==1.5.2
apex==0.9.10dev
scikit_learn==0.23.2
python-dotenv==0.19.2
torch==1.11.0
supervisely==6.35.0
supervisely[apps]==6.35.0

# dev-smart-tool-batched
# batched-smart-tool-for-videos
supervisely[apps]==6.35.0
imutils==0.5.4
loguru==0.6.0
```