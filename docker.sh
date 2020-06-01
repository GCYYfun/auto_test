echo docker...

container_name=env

exit=Exited

# docker rm -v $container_name

if [ $(docker ps -a |grep $container_name|wc -l) -eq 1 ]; then
	if [ $(docker ps -a |grep $container_name|grep $exit|wc -l) -eq 1 ]; then
		docker start $container_name
		docker exec -it $container_name bin/bash
		
	else
		docker exec -it $container_name bin/bash
	fi
else 
	docker run -v /home/own/test:/root/user --name ${container_name} -it ubuntu sh /root/user/env/env.sh
fi

# "sh /root/user/env/env.sh"
