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
# Snippet for StartBackfillJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datastream


# [START datastream_generated_datastream_v1_Datastream_StartBackfillJob_async]
from google.cloud import datastream_v1


async def sample_start_backfill_job():
    # Create a client
    client = datastream_v1.DatastreamAsyncClient()

    # Initialize request argument(s)
    request = datastream_v1.StartBackfillJobRequest(
        object_="object__value",
    )

    # Make the request
    response = await client.start_backfill_job(request=request)

    # Handle response
    print(response)

# [END datastream_generated_datastream_v1_Datastream_StartBackfillJob_async]
