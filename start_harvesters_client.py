import pathlib
import logging

import grpc

import grpc_harvesters_pb2
import grpc_harvesters_pb2_grpc

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = grpc_harvesters_pb2_grpc.HarvestersStub(channel)

        filename = str(DIRECTORY_OF_THIS_FILE / "tmp_snap.bmp")
        response = stub.Acquire(grpc_harvesters_pb2.AcquireRequest(filename=filename))
    print(
        f"Harvesters client received: {response.message}."
    )


if __name__ == "__main__":
    logging.basicConfig()
    run()
