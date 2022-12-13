#!/bin/bash
echo ECS_CLUSTER=${cluster_name} >> /etc/ecs/ecs.config 
echo ECS_BACKEND_HOST= >> /etc/ecs/ecs.config
echo 'vm.max_map_count = 262144' >> /etc/sysctl.conf
sysctl -p