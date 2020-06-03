arch ?= x86_64

out_dir ?= fs/$(arch)
out_img ?= fs/$(arch).img
out_qcow2 ?= fs/$(arch).qcow2

prebuilt_version ?= 0.1.2

rcore_fs_fuse_revision ?= 7f5eeac

.PHONY: build prebuilt sfsimg libc-test

libc-test:
	@echo Building libc-test
	@mkdir -p $(out_dir)
	@cp -r libc-test $(out_dir)/libc-test


build: prebuilt libc-test 

prebuilt:
	@wget https://github.com/rcore-os/rcore-user/releases/download/v$(prebuilt_version)/$(arch).tar.gz
	@tar -xzf $(arch).tar.gz -C fs

sfsimg: $(out_qcow2)

$(out_qcow2): $(out_img)
	@echo Generating sfsimg
	@qemu-img convert -f raw $< -O qcow2 $@
	@qemu-img resize $@ +1G

$(out_img): build rcore-fs-fuse
	@rcore-fs-fuse $@ $(out_dir) zip

rcore-fs-fuse:
ifneq ($(shell rcore-fs-fuse dir image git-version), $(rcore_fs_fuse_revision))
	@echo Installing rcore-fs-fuse
	@cargo install rcore-fs-fuse --git https://github.com/rcore-os/rcore-fs --rev $(rcore_fs_fuse_revision) --force
endif
