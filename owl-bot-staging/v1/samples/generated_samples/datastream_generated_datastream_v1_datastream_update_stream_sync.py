# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateStream
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datastream


# [START datastream_generated_datastream_v1_Datastream_UpdateStream_sync]
from google.cloud import datastream_v1


def sample_update_stream():
    # Create a client
    client = datastream_v1.DatastreamClient()

    # Initialize request argument(s)
    stream = datastream_v1.Stream()
    stream.display_name = "display_name_value"
    stream.source_config.source_connection_profile = "source_connection_profile_value"
    stream.destination_config.destination_connection_profile = "destination_connection_profile_value"

    request = datastream_v1.UpdateStreamRequest(
        stream=stream,
    )

    # Make the request
    operation = client.update_stream(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END datastream_generated_datastream_v1_Datastream_UpdateStream_sync]
