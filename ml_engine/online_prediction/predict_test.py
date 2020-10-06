# Copyright 2017 Google Inc. All Rights Reserved.
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

import json
import socket

import pytest

import predict

MODEL = 'census'
JSON_VERSION = 'v2json'
PROJECT = 'python-docs-samples-tests'
EXPECTED_OUTPUT = {
    u'confidence': 0.7760370969772339,
    u'predictions': u' <=50K'
}

# Raise the socket timeout. The requests involved in the sample can take
# a long time to complete.
socket.setdefaulttimeout(60)


with open('resources/census_test_data.json') as f:
    JSON = json.load(f)


@pytest.mark.flaky
def test_predict_json():
    result = predict.predict_json(
        PROJECT, MODEL, [JSON, JSON], version=JSON_VERSION)
    assert [EXPECTED_OUTPUT, EXPECTED_OUTPUT] == result


@pytest.mark.flaky
def test_predict_json_error():
    with pytest.raises(RuntimeError):
        predict.predict_json(
            PROJECT, MODEL, [{"foo": "bar"}], version=JSON_VERSION)
