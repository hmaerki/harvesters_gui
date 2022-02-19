#!/bin/bash

set -e
set -x

cd src

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_harvesters.proto
