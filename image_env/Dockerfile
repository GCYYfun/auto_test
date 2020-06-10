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
# pkg-config 

# 库用
# musl-tools
# musl-dev

# 工具用
# git
# curl
# wget
# vim

# KVM 用
# cpu-checker
# libglib2.0-dev 
# libpixman-1-dev 
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
    && apt-get install make gcc g++ cmake pkg-config -y \
    && apt-get install git curl wget -y \
    && apt-get install musl-tools musl-dev -y \ 
    && apt-get install python3.8 python3-pip -y

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

RUN pip3 install pexpect

WORKDIR /root