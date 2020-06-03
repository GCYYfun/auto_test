import pexpect

#===============Must Config========================

BaseFile = "diy_file/"

BIOS_UEFI = BaseFile + "kernel/x86_64/OVMF.fd"

EFI_System_Partition = BaseFile + "kernel/x86_64/esp"

FileSystem = BaseFile + "file_system/x86_64.qcow2"

Result = BaseFile + "result/result.txt"

Config = BaseFile + "work/libc-test.v1"

#==============================================

def main():

    # 读取 文件 
        # 文件内容 测试 命令
    lines = []
    with open(Config, "r") as f:
        lines = f.readlines()

    
    # 循环测试
        # 预期 测试结果 反馈 信息
    for line in lines:
        child = pexpect.spawn('qemu-system-x86_64 -smp cores=4 -bios '+ BIOS_UEFI 
                                +' -drive format=raw,file=fat:rw:'+ EFI_System_Partition 
                                +' -serial mon:stdio -m 4G -device isa-debug-exit -drive format=qcow2,file='+FileSystem 
                                +',media=disk,cache=writeback,id=sfsimg,if=none -device ahci,id=ahci0 -device ide-drive,drive=sfsimg,bus=ahci0.0 -nographic')
        result = open(Result,'wb')

        child.logfile = result

        child.expect('.*#')
        child.sendline('cd libc-test')
        child.sendline(line)
        child.sendline('Done')
        child.expect('Done',timeout=None)




if __name__ == "__main__":
    main()

