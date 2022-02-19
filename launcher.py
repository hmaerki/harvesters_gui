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
from PyQt5.QtWidgets import QApplication
from harvesters_gui.frontend.pyqt5 import Harvester


if __name__ == "__main__":
    app = QApplication(sys.argv)
    h = Harvester()

    # Add interface file
    cti ='/home/hansm/.pyenv/versions/3.8.9/envs/venv_harvesters/lib/python3.8/site-packages/genicam/TLSimu.cti'
    h.harvester_core.reset()
    h.harvester_core.add_file(file_path=cti, check_existence=True, check_validity=True)
    h.harvester_core.update()

    # Update the device list in the gui
    h.device_list.update()

    # Update the enabled state
    h.button_select_file.update()
    h.button_select_file.update_observers()

    h.action_on_connect()
    h.button_connect.update()
    h.button_connect.update_observers()

    # Start the application
    h.show()
    sys.exit(app.exec_())
    