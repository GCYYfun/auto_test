
container_name:=main_test

image_name:=autotest

image_name_kvm:=autotest-kvm

.PHONY: build_docker_image run clean

build_docker_image:
	docker build -t ${image_name} .

build_docker_kvm_image:
	docker build -t ${image_name_kvm} .

into:
	docker run \
    -v $(shell pwd)/diy_file:/root/diy_file \
	--privileged \
	--cpuset-cpus="0,1,2,3,4,6,7" \
    --name ${container_name} \
    -it ${image_name_kvm}
	
reinto:
	docker start ${container_name}
	docker exec -it ${container_name} /bin/bash

run:
	@docker run \
    -v $(shell pwd)/diy_file:/root/diy_file \
    --name ${container_name} \
    -it ${image_name_kvm} sh diy_file/start.sh
	make clean

clean:
	@docker rm -v ${container_name} || echo no need clean
