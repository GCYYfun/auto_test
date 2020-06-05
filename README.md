# AutoTest

自动测试

## 环境要求 

docker

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

## 使用

    下载 仓库 
    git clone https://github.com/GCYYfun/auto_test.git

    下载 大文件 
    git lfs https://github.com/GCYYfun/auto_test.git

## 本地运行 [过时 不可取]

材料放置
```
    // 内核镜像放置位置 kernel/x86_64/esp/EFI/rCore 下
    例：kernel/x86_64/esp/EFI/rCore/kernel.elf

    // 用户文件系统放置位置 userapp/file_system 下
    例：file_system/x86_64.qcow2
```
在 auto_test 目录下 运行

    sh x.sh

## 在docker里测试 [Done]

### 大致操作

1. 自己编译好的 内核镜像  
    以rcore 举例 应该是kernel/target/x86_64下的esp文件夹

    自己编译好的 文件系统镜像  
    以rcore 举例 应该是user/build/x86_64.qcow2 文件

2. 把esp 和 x86_64.qcow2 分别放在  
    run_entry/diy_file/kernel/x86_64/ 下  和  
    run_entry/diy_file/file_system/  下

3. 在 run_entry/diy_file/work 文件夹下建立希望执行的测试命令文件

4. 在 run_entry/diy_file/ 下 diy 自己的测试命令脚本

5. 在 run_entry/Makefile 里 添加自己的执行命令

### 目前已经完成

1. 有libc的测试脚本  只需完成 内核的装载就可进行测试内核syscall

    装载好内核后 run_entry 下
    ```
    制作docker image [仅一次]
    make build_docker_image

    运行
    make run

    ```
    在 run_entry/diy_file/result/result.txt 中查看运行结果 (可实时观测)
