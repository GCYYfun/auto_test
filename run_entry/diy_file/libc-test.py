import pexpect

#===============Must Config========================

BaseFile = "diy_file/"

BIOS_UEFI = BaseFile + "kernel/x86_64/OVMF.fd"

EFI_System_Partition = BaseFile + "kernel/x86_64/esp"

FileSystem = BaseFile + "file_system/x86_64.qcow2"

LogFile = BaseFile + "result/logfile.txt"
Result = BaseFile + "result/result.txt"

Config = BaseFile + "work/libc-test"

#==============================================

# qeme 的 参数

args=["-smp","cores=4","-bios",BIOS_UEFI,"-drive","format=raw,file=fat:rw:"+ EFI_System_Partition,
                                "-serial","mon:stdio","-m","4G",
                                "-device","isa-debug-exit","-drive","format=qcow2,file="+FileSystem+",media=disk,cache=writeback,id=sfsimg,if=none",
                                "-device","ahci,id=ahci0","-device","ide-drive,drive=sfsimg,bus=ahci0.0","-nographic"]

def main():

    # 读取 文件 
        # 文件内容 测试 命令
    lines = []
    with open(Config, "r") as f:
        lines = f.readlines()

    logfile = open(LogFile,"wb")
    with open(Result,"w",encoding='utf-8',errors='ignore'):
        pass
    #     lines = f.readlines()
    # result = open(Result,"w",encoding='utf-8',errors='ignore')

    num = 0
    # 循环测试
        # 预期 测试结果 反馈 信息
    for line in lines:
        
        if line == '\n':
            continue

        num+=1
        # child = pexpect.spawn("qemu-system-x86_64 -smp cores=4 -bios "+ BIOS_UEFI 
        #                         +" -drive format=raw,file=fat:rw:"+ EFI_System_Partition 
        #                         +" -serial mon:stdio -m 4G -device isa-debug-exit -drive format=qcow2,file="+FileSystem 
        #                         +" ,media=disk,cache=writeback,id=sfsimg,if=none -device ahci,id=ahci0 -device ide-drive,drive=sfsimg,bus=ahci0.0 -nographic",
        child = pexpect.spawn("qemu-system-x86_64",args,timeout=10)
        

        child.logfile = logfile


        child.expect(".*#")
        child.sendline("cd libc-test")
        child.expect(".*#")
        child.sendline(line)
        
        index = child.expect(["successed","failed",pexpect.EOF,pexpect.TIMEOUT,"/libc-test #","Hangup","=== BEGIN rCore stack trace ==="]) 
        if index == 0: 
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" successed\n")
        elif index == 1:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" failed\n")
        elif index == 2:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" EOF\n")
        elif index == 3:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" 10s_timeout\n")
        elif index == 4:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" successed\n")
        elif index == 5:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" Hangup\n")
        elif index == 6:
            with open(Result,"a",encoding='utf-8',errors='ignore') as f:
                f.writelines(str(num)+" "+line.split("/")[4].split(".")[0]+" Panic\n")

if __name__ == "__main__":
    main()

