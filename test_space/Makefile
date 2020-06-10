image_name := env

volume_name ?= Volume

container_name ?= $(volume_name)_test

where ?= docker # or local

ifeq ($(where), docker)
ifeq ($(volume_name),rCore_libc-test)
run:
	docker run \
	-v $(shell pwd)/${volume_name}:/root/${volume_name} \
	--privileged \
	--cpuset-cpus="0,1,2,3,4,6,7" \
	--name ${container_name} \
	-it ${image_name} sh ${volume_name}/start.sh
	make clean
else ifeq ($(volume_name), zCore_linux_libc-test)
run:
	docker run \
	-v $(shell pwd)/${volume_name}:/root/${volume_name} \
	--privileged \
	--cpuset-cpus="0,1,2,3,4,6,7" \
	--name ${container_name} \
	-it ${image_name} sh ${volume_name}/start.sh
	make clean

into:
	docker run \
	-v $(shell pwd)/${volume_name}:/root/${volume_name} \
	--privileged \
	--cpuset-cpus="0,1,2,3,4,6,7" \
	--name ${container_name} \
	-it ${image_name}

reinto:
	docker start ${container_name}
	docker exec -it ${container_name} /bin/bash

else 
run:
	docker run \
	-v $(shell pwd)/${volume_name}:/root/${volume_name} \
	--privileged \
	--cpuset-cpus="0,1,2,3,4,6,7" \
	--name ${container_name} \
	-it ${image_name} sh ${volume_name}/start.sh
	make clean
endif
else ifeq ($(where), local)
ifeq ($(volume_name),rCore_libc-test)
run:
	cd $(volume_name) && sh local_start.sh
else ifeq ($(volume_name), zCore_linux_libc-test)
run:
	cd $(volume_name) && sh local_start.sh
else
run:
	echo run nothing
endif
endif

# run:
# 	docker run \
# 	-v $(shell pwd)/${volume_name}:/root/Volume \
# 	--privileged \
# 	--cpuset-cpus="0,1,2,3,4,6,7" \
# 	--name ${container_name} \
# 	-it ${image_name} sh ${volume_name}/start.sh
# 	make clean

clean:
	@docker rm -v ${container_name} || echo no need clean