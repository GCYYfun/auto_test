FROM ubuntu:20.04

# 换源

WORKDIR /root

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && echo deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse > /etc/apt/sources.list\ 
    && apt-get upgrade && apt-get update

# 依赖软件

#### list ####
# 编译用
# make
# gcc
# g++
# cmake

# 库用
# musl-tools
# musl-dev

# 工具用
# git
# curl
# wget
# vim

# qemu 用
# libglib2.0-dev 
# libpixman-1-dev 
# pkg-config 

# KVM 用
# cpu-checker
# qemu-kvm 
# libvirt-daemon-system 
# libvirt-clients 
# bridge-utils

# lang用
# python3.8
# python3-pip

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install make gcc g++ cmake -y \
    && apt-get install git curl wget vim -y \
    && apt-get install libglib2.0-dev libpixman-1-dev pkg-config -y \
    && apt-get install cpu-checker qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y \
    && apt-get install musl-tools musl-dev -y \ 
    && apt-get install python3.8 python3-pip -y

RUN pip3 install pexpect

## 安装 Rust
RUN echo export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup >> /root/.bashrc \
    && /bin/bash -c "source /root/.bashrc" \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && cat .cargo/env >> .bashrc \
    && /bin/bash -c "source /root/.bashrc" \
    && echo '[source.crates-io]' >> .cargo/config \
    && echo 'replace-with = "tuna"' >> .cargo/config \
    && echo '[source.tuna]' >> .cargo/config \
    && echo 'registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"' >> .cargo/config

## 手动安装muslcc [musl.cc](https://musl.cc)
# 同Dockerfile 目录下 需要有 muslcc和musl

# COPY musl-1.2.0.tar.gz /root/musl-1.2.0.tar.gz
# RUN tar zxf musl-1.2.0.tar.gz \
#     && cd musl-1.2.0 \
#     && ./configure --prefix=/root/musl-install/ \
#     && make && make install \
#     && cd /root/musl-install/bin \
#     && ln -s musl-gcc x86_64-linux-musl-gcc \
#     && cd /root

# COPY x86_64-linux-musl-cross.tgz /root/x86_64-linux-musl-cross.tgz
# RUN tar xvf x86_64-linux-musl-cross.tgz \
#     && cd x86_64-linux-musl-cross \
#     && cp -r * /usr/ 

## 压缩包方式 安装 qemu
#  同Dockerfile 目录下 需要有 qemu

COPY qemu-5.0.0.tar.xz /root/qemu-5.0.0.tar.xz
RUN tar xvJf qemu-5.0.0.tar.xz \
    && cd qemu-5.0.0 \
    && ./configure --target-list=x86_64-softmmu,riscv64-softmmu --python=python3.8 \
    && make -j8 && make install

## 环境变量
RUN echo 'export PATH=$PWD/x86_64-softmmu:$PWD/riscv64-softmmu:$PATH' >> /root/.bashrc \
    && /bin/bash -c "source /root/.bashrc"

WORKDIR /root