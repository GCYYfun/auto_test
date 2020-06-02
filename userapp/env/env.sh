arch=x86_64
musl_dir=/root/user/env/musl

# out_dir=/root/build/$arch

tarball=x86_64-linux-musl-cross.tgz

musl=x86_64-linux-musl-cross

echo 环境配置...

echo 换源...
mv /etc/apt/sources.list /etc/apt/sources.list.bak
echo deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse > /etc/apt/sources.list
apt upgrade
apt update

echo 配置 tzdata...
export DEBIAN_FRONTEND=noninteractive
apt install -y tzdata
ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
dpkg-reconfigure -f noninteractive tzdata

echo install expect...
apt install expect -y

echo install make...
apt install make -y

echo install gcc...
apt install gcc -y

echo install cmake...
apt install cmake -y

echo install g++...
apt install g++ -y

echo install git...
apt install git -y

echo install musl...

cd $musl_dir;wget "https://musl.cc/${tarball}"
cd $musl_dir;tar xvf $tarball 
cd $musl_dir;cp -r $musl/* /usr/


echo 转去执行userapp...
cd /root/user/userapp/libc-test
make clean
make | grep FAIL|wc -l
