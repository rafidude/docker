docker swarm init
docker stack deploy -c docker-compose.yml getstartedlab
docker stack ps getstartedlab
curl http://localhost

Remove:
docker stack rm getstartedlab
docker swarm leave --force
