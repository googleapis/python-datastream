# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Snippet for CreateStream
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datastream


# [START datastream_v1_generated_Datastream_CreateStream_async]
from google.cloud import datastream_v1


async def sample_create_stream():
    # Create a client
    client = datastream_v1.DatastreamAsyncClient()

    # Initialize request argument(s)
    stream = datastream_v1.Stream()
    stream.display_name = "display_name_value"
    stream.source_config.source_connection_profile = "source_connection_profile_value"
    stream.destination_config.destination_connection_profile = "destination_connection_profile_value"

    request = datastream_v1.CreateStreamRequest(
        parent="parent_value",
        stream_id="stream_id_value",
        stream=stream,
    )

    # Make the request
    operation = client.create_stream(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END datastream_v1_generated_Datastream_CreateStream_async]
