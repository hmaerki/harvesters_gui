#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
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


# Standard library imports

# Related third party imports
from PyQt5.QtWidgets import QComboBox

# Local application/library specific imports
from harvesters_gui._private.frontend.pyqt5.helper import get_system_font


class ComboBoxDisplayRateList(QComboBox):
    #
    _list_disp_rates = [10, 30, 60, 300]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(get_system_font())
        for disp_rate in self._list_disp_rates:
            self.addItem(f"{disp_rate} fps")
        self.setCurrentIndex(0)
        self.currentIndexChanged.connect(self._set_display_rate)

    def _set_display_rate(self, idx):
        display_rate = float(self._list_disp_rates[idx])
        self.parent().parent().canvas.display_rate = display_rate

