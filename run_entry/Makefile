
container_name:=main_test

image_name:=autotest

.PHONY: build_docker_image run clean

build_docker_image:
	docker build -t ${image_name} .

into:
	docker run \
    -v $(shell pwd)/diy_file:/root/diy_file \
    --name ${container_name} \
    -it ${image_name}
	
reinto:
	docker start ${container_name}
	docker exec -it ${container_name} /bin/bash

run:
	@docker run \
    -v $(shell pwd)/diy_file:/root/diy_file \
    --name ${container_name} \
    -it ${image_name} sh diy_file/start.sh
	make clean

clean:
	@docker rm -v ${container_name} || echo no need clean