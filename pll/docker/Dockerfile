FROM amazonlinux:latest

RUN echo 'alias ll="ls -ltha"' >> ~/.bashrc

RUN yum -y update && \
    yum -y install \
      wget \
      zip \
      gcc \
      openssl-devel \
      bzip2-devel

# Install Python3 and Pip
RUN wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
RUN tar xzf Python-3.6.5.tgz
RUN cd Python-3.6.5 && ./configure --enable-optimizations
RUN cd Python-3.6.5 && make altinstall
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.6 get-pip.py

# Create app directory and add current directory on host into container
ENV APP_HOME='/app'
ENV APP_TMP='/tmp/app'
ENV APP_VENV="$APP_TMP/venv"
ENV APP_PACKAGES="$APP_TMP/build/site-packages"
ENV APP_CACHE="$APP_TMP/build/pip-cache"
ENV ZIP="$APP_TMP/dist/docker.zip"
RUN mkdir -p "$APP_HOME"
RUN mkdir -p "$APP_TMP/dist"

RUN pip install --upgrade pip virtualenv && virtualenv --python=python3.6 $APP_VENV

# This is what is run by the container as a "one shot"
ADD startup-build.sh /opt/
RUN chmod +x /opt/startup-build.sh
CMD /opt/startup-build.sh