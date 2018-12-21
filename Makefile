.PHONY: build-garage-release run-garage-release

GARAGE_RELEASE="v2018.10.0"

build-garage-release: docker/Dockerfile.release docker/mjkey.txt
	docker build \
		-f docker/Dockerfile.release \
		--build-arg RELEASE="${GARAGE_RELEASE}" \
		-t rlworkgroup/garage:release .

build-garage-local: docker/Dockerfile.local
	docker build \
		-f docker/Dockerfile.local \
		-t rlworkgroup/garage:local .

run-garage-release: build-garage-release
	xhost +local:docker
	docker run \
		-it \
		--rm \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		-v $(shell pwd)/data:/root/code/garage/data \
		-e DISPLAY="${DISPLAY}" \
		rlworkgroup/garage:release ${RUN_CMD}

run-garage-local: build-garage-local
	xhost +local:docker
	docker run \
		-it \
		--rm \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		-v $(shell pwd)/data:/root/code/garage/data \
		-e DISPLAY="${DISPLAY}" \
		rlworkgroup/garage:local ${RUN_CMD}
