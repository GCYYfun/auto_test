# AutoTest

自动测试

## 环境要求 

docker

qemu[可选]

## 本地运行 [需要qemu] 

材料放置
```
    // 内核镜像放置位置 kernel/x86_64/esp/EFI/rCore 下
    例：kernel/x86_64/esp/EFI/rCore/kernel.elf

    // 用户文件系统放置位置 userapp/file_system 下
    例：file_system/x86_64.qcow2
```
在 auto_test 目录下 运行

    sh x.sh

## 在docker里测试

TODO

## 用户程序 编译

sh docker.sh
