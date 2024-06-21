#!/bin/bash

docker network create postgres

/bin/bash ${PWD}/on_startup/run_master.sh&
/bin/bash ${PWD}/on_startup/run_slave.sh&
