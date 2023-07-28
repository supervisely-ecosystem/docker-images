FROM supervisely/base-py-sdk:6.72.82

RUN apt-get update -y
RUN apt-get install -y libzbar0

RUN pip install pyzbar==0.1.9
RUN pip install moviepy==1.0.3 imageio-ffmpeg==0.4.7
RUN pip install imutils==0.5.4 
RUN pip install supervisely==6.72.82 supervisely[docs]==6.72.82
