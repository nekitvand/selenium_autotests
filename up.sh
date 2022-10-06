#!/bin/bash

docker-compose up -d
sleep 5
if [[ "$OSTYPE" == "darwin"* ]]; then
  docker exec -i ui-autotests python load.py --arm
  echo "docker pull dumbdumbych/selenium_vnc_chrome_arm64:91.0.b" >> selenoid_images.sh
else
  docker exec -i ui-autotests python load.py
fi
while [ ! -f selenoid_images.sh ]; do sleep 1; done
sh selenoid_images.sh