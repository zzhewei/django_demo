# FROM：基底映像檔
FROM python:3.7-bullseye

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# WORKDI：建立 working directory
WORKDIR /django_demo

# ADD：將檔案加到 images 內
ADD . /django_demo

# 只有build 時使用，會執行此命令
RUN pip install -r requirements.txt

# run container 時要執行的命令
#CMD python app.py

COPY dbsetup.sh ./
RUN chmod u+x ./dbsetup.sh
ENTRYPOINT ["./dbsetup.sh"]