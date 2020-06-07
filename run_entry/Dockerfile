FROM ubuntu:20.04

# 换源

WORKDIR /root

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && echo deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse > /etc/apt/sources.list\ 
    && apt-get upgrade && apt-get update

# 依赖软件 
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install git cpu-checker gcc python3.8 python3-pip make pkg-config libglib2.0-dev libpixman-1-dev qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y

# 安装Qemu

## 网络方式

# RUN git clone https://mirrors.tuna.tsinghua.edu.cn/git/qemu.git
# RUN cd qemu
# RUN git submodule init
# RUN git submodule update --recursive

## 压缩包方式

COPY qemu-5.0.0.tar.xz /root/qemu-5.0.0.tar.xz
RUN tar xvJf qemu-5.0.0.tar.xz \
    && cd qemu-5.0.0 \
    && ./configure --target-list=x86_64-softmmu,riscv64-softmmu --python=python3.8 \
    && make -j4 && make install

## 环境变量
RUN echo 'export PATH=$PWD/x86_64-softmmu:$PWD/riscv64-softmmu:$PATH' >> /root/.bashrc \
    && /bin/bash -c "source /root/.bashrc"

# 添加运行脚本支持

RUN pip3 install pexpect

# 换到root下[也许多余]

WORKDIR /root