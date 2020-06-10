
image_name := zcore_linux_syscall

container_name := zcore_linux_syscall_test

build:
	docker build -t ${image_name} .

reinto:
	docker start ${container_name}
	docker exec \
	-it ${container_name} /bin/bash

rerun:
	docker start ${container_name}
	docker exec \
	-it ${container_name} sh Volume/start.sh

into:
	docker run \
	-v $(shell pwd)/Volume:/root/Volume \
	--name ${container_name} \
	-it ${image_name}

run:
	docker run \
	-v $(shell pwd)/Volume:/root/Volume \
	--name ${container_name} \
	-it ${image_name} sh Volume/start.sh

clean:
	@docker rm -v ${container_name} || echo no need clean