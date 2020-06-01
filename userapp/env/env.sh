arch=x86_64
# build_dir=build/$arch
out_dir=/root/build/$arch

tarball=musl/x86_64-linux-musl-cross.tgz

musl_dir=musl/x86_64-linux-musl-cross

echo 环境配置...

echo 换源...
mv /etc/apt/sources.list /etc/apt/sources.list.bak
echo deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse > /etc/apt/sources.list
apt upgrade
apt update

echo install make...
apt install make -y

echo install gcc...
apt install gcc -y

echo install cmake...
apt install cmake -y

echo install g++...
apt install g++ -y

echo install musl...

tar xvf $tarball
cp -r $musl_dir/* /usr/

