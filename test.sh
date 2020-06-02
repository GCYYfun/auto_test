container_name=main_test

docker build -t core:test .

docker run \
    -v $(pwd)/file_system:/root/file_system \
    -v $(pwd)/kernel:/root/kernel \
    -v $(pwd)/run.py:/root/run.py \
    --name ${container_name} \
    -it core:test python3.8 run.py
