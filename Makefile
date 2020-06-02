
container_name:=main_test

all:

run:



build_image:
	docker build -t autotest .

run_test:
	docker run \
    -v $(shell pwd)/file_system:/root/file_system \
    -v $(shell pwd)/kernel:/root/kernel \
	-v $(shell pwd)/result:/root/result \
    -v $(shell pwd)/run.py:/root/run.py \
	-v $(shell pwd)/start.sh:/root/start.sh \
    --name ${container_name} \
    -it autotest sh start.sh

clean:
	docker rm -v main_test