.PHONY: build run rerun into reinto clean

where ?= docker



image_dir = ./image_env

test_dir = ./test_space

build:
	cd $(image_dir) && make build

run:
	cd $(test_dir) && make run

run_rcore_test_docker:
	cd $(test_dir) && make run where=docker volume_name=rCore_libc-test

run_rcore_test_local:
	cd $(test_dir) && make run where=local volume_name=rCore_libc-test

# run_zcore_linux_test_docker:
# 	cd $(test_dir) && make into where=docker volume_name=zCore_linux_libc-test
# 	cd zCore_linux_libc-test
# 	sh local_start.sh

run_zcore_linux_test_local:
	cd $(test_dir) && make run where=local volume_name=zCore_linux_libc-test

