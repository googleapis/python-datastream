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
# Snippet for CreateConnectionProfile
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-datastream


# [START datastream_v1_generated_Datastream_CreateConnectionProfile_sync]
from google.cloud import datastream_v1


def sample_create_connection_profile():
    # Create a client
    client = datastream_v1.DatastreamClient()

    # Initialize request argument(s)
    connection_profile = datastream_v1.ConnectionProfile()
    connection_profile.oracle_profile.hostname = "hostname_value"
    connection_profile.oracle_profile.username = "username_value"
    connection_profile.oracle_profile.password = "password_value"
    connection_profile.oracle_profile.database_service = "database_service_value"
    connection_profile.display_name = "display_name_value"

    request = datastream_v1.CreateConnectionProfileRequest(
        parent="parent_value",
        connection_profile_id="connection_profile_id_value",
        connection_profile=connection_profile,
    )

    # Make the request
    operation = client.create_connection_profile(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END datastream_v1_generated_Datastream_CreateConnectionProfile_sync]
