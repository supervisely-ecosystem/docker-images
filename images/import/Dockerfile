FROM supervisely/supervisely/base-py-sdk:6.72.70


# base
RUN echo "Installing base dependencies"
RUN pip install supervisely==6.72.70 black isort

# Images
RUN echo "Installing import dependencies for images"

# import DICOM studies
# install in Volumes section
# RUN pip install gdcm==1.1 pylibjpeg==1.4.0 pylibjpeg-libjpeg==1.3.1

# remote import
RUN pip install htmllistparse==0.6.0

# import from google cloud storage
RUN pip install google-cloud-storage==1.35.0

# import coco
# import coco keypoints
RUN pip install pycocotools==2.0.6

# Videos
RUN echo "Installing import dependencies for videos"

# improt youtube videos
RUN pip install yt-dlp==2023.3.4

# import-videos-team-files
RUN pip install moviepy==1.0.3

# youtube downloader
# moviepy==1.0.3
RUN pip install google-api-python-client==2.81.0 yt-dlp==2023.3.4

# Point clouds
RUN echo "Installing import dependencies for point clouds"

# import pointcloud ply
# import kitti 3d
RUN pip install open3d==0.15.2

# import las format
RUN pip install scikit-learn==0.24.1
RUN pip install laspy==2.0.1 lazrs==0.3.0

# import kitti 360
RUN pip install git+https://github.com/autonomousvision/kitti360Scripts.git transforms3d==0.3.1
# open3d==0.14.1

# Volumes
RUN echo "Installing import dependencies for volumes"

# import DICOM studies
RUN pip install gdcm==1.1 pylibjpeg==1.4.0 pylibjpeg-libjpeg==1.3.1

