Base_Path="/home/own/Work Realm/AutoTest"

BIOS_UEFI=Kernel/x86_64/OVMF.fd

EFI_System_Partition=Kernel/x86_64/esp

FileSystem=FileSystem/x86_64.qcow2

echo Start Qemu

echo $BIOS_UEFI

qemu-system-x86_64\
  	-smp cores=4\
 	-bios $BIOS_UEFI\
 	-drive format=raw,file=fat:rw:$EFI_System_Partition\
 	-serial mon:stdio\
 	-m 4G\
 	-device isa-debug-exit\
 	-drive format=qcow2,file=$FileSystem,media=disk,cache=writeback,id=sfsimg,if=none \
	-device ahci,id=ahci0\
 	-device ide-drive,drive=sfsimg,bus=ahci0.0\
 	-nographic