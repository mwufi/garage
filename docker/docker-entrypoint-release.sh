#!/usr/bin/env bash
# Dockerfile entrypoint
set -e

source ~/.bashrc

# Activate conda environment
source activate garage

# Fixes Segmentation Fault
# See: https://github.com/openai/mujoco-py/pull/145#issuecomment-356938564
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/x86_64-linux-gnu/mesa/libGL.so.1

export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${HOME}/.mujoco/mjpro150/bin"

exec "$@"
