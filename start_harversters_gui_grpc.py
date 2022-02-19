#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2021 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


import sys
import pathlib
from concurrent import futures
import grpc

from PyQt5.QtWidgets import QApplication

from harvesters_gui.frontend.pyqt5 import Harvester

import grpc_harvesters_pb2
import grpc_harvesters_pb2_grpc


class GprcHarvesters(grpc_harvesters_pb2_grpc.HarvestersServicer):
    def __init__(self, harvester: Harvester) -> None:
        super().__init__()
        self._harvester = harvester

    def Acquire(self, request, context):
        message = self._harvester.acquire(filename=request.filename)
        return grpc_harvesters_pb2.AcquireReply(message=message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    h = Harvester()

    # Add interface file
    cti_files = (
        # r"C:\Program Files\Basler\pylon 6\Runtime\x64\ProducerGEV.cti",
        r"C:\Program Files\Basler\pylon 6\Runtime\x64\ProducerU3V.cti",
        "/home/hansm/.pyenv/versions/3.8.9/envs/venv_harvesters/lib/python3.8/site-packages/genicam/TLSimu.cti",
        r"C:\Program Files\Python38\Lib\site-packages\genicam\TLSimu.cti",
    )
    h.harvester_core.reset()
    for cti in cti_files:
        if pathlib.Path(cti).exists():
            print(f"Add {cti}")
            h.harvester_core.add_file(
                file_path=cti, check_existence=True, check_validity=True
            )
    h.harvester_core.update()

    # Update the device list in the gui
    h.device_list.update()

    # Update the enabled state
    h.button_select_file.update()
    h.button_select_file.update_observers()

    if False:
        h.action_on_connect()
        h.button_connect.update()
        h.button_connect.update_observers()

    if True:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        grpc_harvesters_pb2_grpc.add_HarvestersServicer_to_server(
            GprcHarvesters(harvester=h), server
        )
        server.add_insecure_port("[::]:50051")
        server.start()

    # Start the application
    h.show()
    sys.exit(app.exec_())
