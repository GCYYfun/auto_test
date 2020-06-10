# AutoTest

自动测试 0.0.2

## 环境要求

OS : ubuntu 20.04  

docker 运行  
有安装docker

本地运行  
有安装qemu、kvm、python3.8、pexpect

## 下载

```

```

## 运行 

在auto_test 目录下

[如使用docker 先 make build]

1. docker 执行 rcore 测试

```sh
make run_rcore_test_docker
```

2. 本地执行rcore测试 [对本地环境配置有要求]

```sh
make run_rcore_test_local
```
>要求有：  
qemu 且支持 kvm 、有python3.8 且有 安装pexpect

3. ~~docker 执行 zcore 测试~~ 

```sh
make run_zcore_linux_test_docker
```

4. 本地 执行 zcore 测试 

```sh
make run_zcore_linux_test_local:
```
>要求有：  
有python3.8 且有 安装pexpect
