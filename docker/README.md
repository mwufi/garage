# Garage Docker

Currently there's three versions of garage containers:
  - ci: used for the continuous integration of garage in TravisCI and not
    intended for final users.
  - release: it's a published image based on the latest official release of
    garage.
  - local: it's an image built on top of the release with a copy of the files
    in your local repository.

## Release image

The release image is published to be downloaded without the need of having
a local repository. The command to run in the corresponding container can be
specified through the argument RUN_CMD. To run an example launcher in the
container, execute:
```
docker run --rm rlworkgroup/garage:release RUN_CMD="python examples/tf/trpo_cartpole.py"
```
This image does not come with a MuJoCo key, so it's not possible to run MuJuCo
environments with it. To enable MuJoCo, you need to build a local image and
set a valid key in the image.

If you want to build the release image, follow this steps:
  1. Clone this repository
  2. Copy a valid MuJoCo key in `docker/mjkey.txt` inside the cloned repository
  3. Move to the root folder of your cloned repository and run
    ```
    make build-garage-release
    ```

You can also build a specific release based on the release tag, for example:
```
make build-garage-release GARAGE_RELEASE="v2018.10.0"
```

The release version can also be ran with the command:
```
make run-garage-release
```

To run a command in the container, for example a garage launcher example,
execute:
```
make run-garage-release RUN_CMD="python examples/tf/trpo_cartpole.py"
```

This previous command adds a volume from the data folder inside your cloned
garage repository to the garage-release container, so any experiment results
ran in the container will be saved in the data folder inside your cloned
repository.

## Local image

The local image is built on top of the release image and it includes the
changes in your cloned repository as well as configuring the MuJoCo key
(optionally).

If you want to build the local image, follow this steps:
  1. Clone this repository
  2. Copy a valid MuJoCo key in `docker/mjkey.txt` inside the cloned repository
  3. Move to the root folder of your cloned repository and run
    ```
    make build-garage-local
    ```

The local version can also be ran with the command:
```
make run-garage-local
```

To run a command in the container, for example a garage launcher example,
execute:
```
make run-garage-local RUN_CMD="python examples/tf/trpo_cartpole.py"
```

This previous command adds a volume from the data folder inside your cloned
garage repository to the garage-release container, so any experiment results
ran in the container will be saved in the data folder inside your cloned
repository.
