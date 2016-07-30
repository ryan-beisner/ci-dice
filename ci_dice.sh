#!/bin/bash -e
# CI-Dice:  A simple tool to randomly pass or fail.  It is useful as a
# command or module to simulate, debug or build out CI pipelines. Seeds
# with PID.  Rolls a pair of dice.  Fails if the pair matches.
# ~16.666% probability.
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

symbols="⚀
⚁
⚂
⚃
⚄
⚅"

faces=($symbols)
num_faces=${#faces[*]}

RANDOM=$$
val_1=$((RANDOM%num_faces))
val_2=$((RANDOM%num_faces))

die_1=${faces[$val_1]}
die_2=${faces[$val_2]}

echo "  $((val_1+1))    $((val_2+1))"
echo "  ${die_1}    ${die_2}"

if [[ "$val_1" != "$val_2" ]]; then
  echo "   Pass"
else
  echo "!! Fail !!"
  exit 127
fi
