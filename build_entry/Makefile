container_name:=user_env

image_name:=env

.PHONY: build_docker_image run clean

build_docker_image:
	docker build -t ${image_name} .

run:
	docker run \
    -v $(shell pwd)/diy_file:/root/diy_file \
    --name ${container_name} \
    -it ${image_name}

clean:
	docker rm -v ${container_name}