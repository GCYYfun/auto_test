# AutoTest

自动测试

## 环境要求 

docker

qemu[可选]

[注意] 确保路径全英文小写

## 目录结构

```
auto-test
    ├── run_entry               // 进行 测试运行的 入口
    │   ├── diy_file               // docker 挂载目录
    │   │   ├── kerlnel               // 放置内核的地方
    │   │   ├── file_system           // 放置文件系统的地方
    │   │   ├── result                // 测试结果放置的地方
    │   │   ├── diy_test.py           // 自定义的测试执行命令文件
    │   │   └── start.sh              // 开始入口
    │   ├── Dockerfile             // 测试环境构建的文件
    │   ├── Makefile               // Makefile
    │   └── README.md              // 读我?                          
    ├── build_entry             // 构建 镜像文件 入口
    │   ├── diy_file               // docker 挂载目录
    │   │   ├── test_app1             // 用户测试程序 1
    │   │   ├── test_app1             // 用户测试程序 2
    │   │   │   ···
    │   │   ├── test_app1             // 用户测试程序 n
    │   │   ├── Makefile.py           // Makefile
    │   │   └── result                // 开始入口
    │   ├── Dockerfile             // build环境构建的文件
    │   ├── Makefile               // Makefile
    │   └── README.md              // 读我?
    ├── Makefile
    └── README.md
    ···
```

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



## 用户程序 测试

sh docker.sh
