FROM ubuntu:20.04

# 换源

WORKDIR /root

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN echo deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse > /etc/apt/sources.list
RUN apt upgrade && apt update

# 依赖软件 
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt install git 
RUN apt install python3.8
RUN apt install make
RUN apt istall gcc
RUN apt install pkg-config
RUN apt install libglib2.0-dev
RUN apt install libpixman-1-dev

# 安装Qemu
RUN git clone https://mirrors.tuna.tsinghua.edu.cn/git/qemu.git
RUN cd qemu
RUN git submodule init
RUN git submodule update --recursive
RUN ./configure --target-list=x86_64-softmmu,riscv64-softmmu --python=python3.8
RUN make

RUN export PATH=$PWD/x86_64-softmmu:$PWD/riscv64-softmmu:$PATH

# 挂载 文件

# 运行