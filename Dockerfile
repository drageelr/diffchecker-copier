FROM selenium/standalone-chrome:114.0-chromedriver-114.0-grid-4.10.0-20230614

USER root

WORKDIR /root
SHELL ["/bin/bash", "-c"]

# Install Pip Dependencies
RUN sudo apt update && \
    sudo apt install -y python3-distutils

# Install Pip
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

# COPY . .

# RUN pip install -r requirements.txt