#!/usr/bin/env python3
#
# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
CI-Dice:  A simple tool to randomly pass or fail.  It is useful as a
command or module to simulate, debug or build out CI pipelines.
"""

from copy import deepcopy
import random
import sys

# TODO(beisner): Expose config as cli parameters.
DEFAULT_CONFIG = {
    'dice': 2,         # Quantity of dice to roll
    'fatal': True,     # Exit non-zero when match condition is met
    'invert': False,   # Invert the behavior and odds
    'symbols': False,  # Print dice symbols to the output
    'numerals': True,  # Print numerals to the output
    'exit': 127,       # Exit code for simulated fails
}

DIE_SYMBOLS = ('⚀', '⚁', '⚂', '⚃', '⚄', '⚅')


def roll(**kwargs):
    """
    Roll the dice.
    """
    config = deepcopy(DEFAULT_CONFIG)
    config.update(kwargs)

    rolls = []
    for die in range(config['dice']):
        rolls.append(random.randint(1, 6))

    match = len(set(rolls)) == 1
    fail = match if not config['invert'] else not match

    msg = ''
    for roll in rolls:
        if config['numerals']:
            msg += ' [{}]'.format(roll)
        if config['symbols']:
            msg += ' {} '.format(DIE_SYMBOLS[roll-1])

    msg += ' FAIL' if fail else ' OK'

    print(msg)
    if fail:
        sys.exit(config['exit'])
