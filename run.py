import pexpect

BIOS_UEFI="kernel/x86_64/OVMF.fd"

EFI_System_Partition="kernel/x86_64/esp"

FileSystem="file_system/x86_64.qcow2"

def main():

    child = pexpect.spawn('qemu-system-x86_64 -smp cores=4 -bios '+ BIOS_UEFI +' -drive format=raw,file=fat:rw:'+ EFI_System_Partition +'  -serial mon:stdio -m 4G -device isa-debug-exit -drive format=qcow2,file='+FileSystem +',media=disk,cache=writeback,id=sfsimg,if=none -device ahci,id=ahci0 -device ide-drive,drive=sfsimg,bus=ahci0.0 -nographic')
    result = open('result/result.txt','wb')
    child.logfile = result
    child.expect('.*#')
    child.sendline('ls -l')
    child.sendline('cd /usr/bin')
    child.sendline('ls')
    child.sendline('Done')
    child.expect('Done',timeout=None)


if __name__ == "__main__":
    main()

