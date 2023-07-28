FROM supervisely/base-py-sdk:6.72.82

RUN pip install Cython==3.0.0
RUN pip install scikit-learn==1.3.0 umap-learn==0.5.3 
RUN pip install transformers==4.31.0 timm==0.9.2
RUN pip install open3d==0.15.2 pycocotools==2.0.6 
RUN pip install diskcache==5.2.1 seaborn==0.11.0
RUN pip install supervisely==6.72.82 supervisely[apps]==6.72.82



FROM supervisely/base-py-sdk:6.72.82

RUN pip install Cython==3.0.0 scikit-learn==1.3.0 
RUN pip install open3d==0.15.2 pycocotools==2.0.6 diskcache==5.2.1 seaborn==0.11.0
RUN pip install supervisely==6.72.82 supervisely[apps]==6.72.82


# No space left on device
# embeddings-app
# RUN pip install torch==2.0.1
# RUN pip install scikit-learn==1.3.0 umap-learn==0.5.3 transformers==4.31.0 timm==0.9.2
# RUN pip install supervisely==6.72.82
