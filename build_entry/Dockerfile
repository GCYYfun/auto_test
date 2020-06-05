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
    && apt-get install make gcc g++ cmake git wget -y

# 手动安装muslcc [musl.cc](https://musl.cc)

## From 网络

### TODO 

## From 本地

COPY musl-1.2.0.tar.gz /root/musl-1.2.0.tar.gz
RUN tar zxf musl-1.2.0.tar.gz \
    && cd musl-1.2.0 \
    && ./configure --prefix=/root/musl-install/ \
    && make && make install \
    && cd /root/musl-install/bin \
    && ln -s musl-gcc x86_64-linux-musl-gcc \
    && cd /root

COPY x86_64-linux-musl-cross.tgz /root/x86_64-linux-musl-cross.tgz
RUN tar xvf x86_64-linux-musl-cross.tgz \
    && cd x86_64-linux-musl-cross \
    && cp -r * /usr/ 


WORKDIR /root