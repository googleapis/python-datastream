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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.datastream_v1alpha1.types import datastream
from google.cloud.datastream_v1alpha1.types import datastream_resources
from google.longrunning import operations_pb2  # type: ignore

from .base import DatastreamTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class DatastreamRestInterceptor:
    """Interceptor for Datastream.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DatastreamRestTransport.

    .. code-block:: python
        class MyCustomDatastreamInterceptor(DatastreamRestInterceptor):
            def pre_create_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_discover_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_discover_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_errors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_errors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_static_ips(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_static_ips(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connection_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connection_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DatastreamRestTransport(interceptor=MyCustomDatastreamInterceptor())
        client = DatastreamClient(transport=transport)


    """
    def pre_create_connection_profile(self, request: datastream.CreateConnectionProfileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.CreateConnectionProfileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_connection_profile(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_connection_profile

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_create_private_connection(self, request: datastream.CreatePrivateConnectionRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.CreatePrivateConnectionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_private_connection(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_private_connection

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_create_route(self, request: datastream.CreateRouteRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.CreateRouteRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_route(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_route

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_create_stream(self, request: datastream.CreateStreamRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.CreateStreamRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_stream(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_stream

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_delete_connection_profile(self, request: datastream.DeleteConnectionProfileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.DeleteConnectionProfileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_connection_profile(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_connection_profile

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_delete_private_connection(self, request: datastream.DeletePrivateConnectionRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.DeletePrivateConnectionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_private_connection(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_private_connection

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_delete_route(self, request: datastream.DeleteRouteRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.DeleteRouteRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_route(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_route

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_delete_stream(self, request: datastream.DeleteStreamRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.DeleteStreamRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_stream(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_stream

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_discover_connection_profile(self, request: datastream.DiscoverConnectionProfileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.DiscoverConnectionProfileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for discover_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_discover_connection_profile(self, response: datastream.DiscoverConnectionProfileResponse) -> datastream.DiscoverConnectionProfileResponse:
        """Post-rpc interceptor for discover_connection_profile

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_fetch_errors(self, request: datastream.FetchErrorsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.FetchErrorsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for fetch_errors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_fetch_errors(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for fetch_errors

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_fetch_static_ips(self, request: datastream.FetchStaticIpsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.FetchStaticIpsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for fetch_static_ips

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_fetch_static_ips(self, response: datastream.FetchStaticIpsResponse) -> datastream.FetchStaticIpsResponse:
        """Post-rpc interceptor for fetch_static_ips

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_get_connection_profile(self, request: datastream.GetConnectionProfileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.GetConnectionProfileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_connection_profile(self, response: datastream_resources.ConnectionProfile) -> datastream_resources.ConnectionProfile:
        """Post-rpc interceptor for get_connection_profile

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_get_private_connection(self, request: datastream.GetPrivateConnectionRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.GetPrivateConnectionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_private_connection(self, response: datastream_resources.PrivateConnection) -> datastream_resources.PrivateConnection:
        """Post-rpc interceptor for get_private_connection

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_get_route(self, request: datastream.GetRouteRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.GetRouteRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_route(self, response: datastream_resources.Route) -> datastream_resources.Route:
        """Post-rpc interceptor for get_route

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_get_stream(self, request: datastream.GetStreamRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.GetStreamRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_stream(self, response: datastream_resources.Stream) -> datastream_resources.Stream:
        """Post-rpc interceptor for get_stream

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_list_connection_profiles(self, request: datastream.ListConnectionProfilesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.ListConnectionProfilesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_connection_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_connection_profiles(self, response: datastream.ListConnectionProfilesResponse) -> datastream.ListConnectionProfilesResponse:
        """Post-rpc interceptor for list_connection_profiles

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_list_private_connections(self, request: datastream.ListPrivateConnectionsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.ListPrivateConnectionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_private_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_private_connections(self, response: datastream.ListPrivateConnectionsResponse) -> datastream.ListPrivateConnectionsResponse:
        """Post-rpc interceptor for list_private_connections

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_list_routes(self, request: datastream.ListRoutesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.ListRoutesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_routes(self, response: datastream.ListRoutesResponse) -> datastream.ListRoutesResponse:
        """Post-rpc interceptor for list_routes

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_list_streams(self, request: datastream.ListStreamsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.ListStreamsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_streams(self, response: datastream.ListStreamsResponse) -> datastream.ListStreamsResponse:
        """Post-rpc interceptor for list_streams

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_update_connection_profile(self, request: datastream.UpdateConnectionProfileRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.UpdateConnectionProfileRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_update_connection_profile(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_connection_profile

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response
    def pre_update_stream(self, request: datastream.UpdateStreamRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[datastream.UpdateStreamRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_update_stream(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_stream

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DatastreamRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DatastreamRestInterceptor


class DatastreamRestTransport(DatastreamTransport):
    """REST backend transport for Datastream.

    Datastream service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'datastream.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[DatastreamRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DatastreamRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1alpha1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _CreateConnectionProfile(DatastreamRestStub):
        def __hash__(self):
            return hash("CreateConnectionProfile")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
            "connectionProfileId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.CreateConnectionProfileRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create connection profile method over HTTP.

            Args:
                request (~.datastream.CreateConnectionProfileRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/connectionProfiles',
                'body': 'connection_profile',
            },
            ]
            request, metadata = self._interceptor.pre_create_connection_profile(request, metadata)
            pb_request = datastream.CreateConnectionProfileRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_connection_profile(resp)
            return resp

    class _CreatePrivateConnection(DatastreamRestStub):
        def __hash__(self):
            return hash("CreatePrivateConnection")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
            "privateConnectionId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.CreatePrivateConnectionRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create private connection method over HTTP.

            Args:
                request (~.datastream.CreatePrivateConnectionRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/privateConnections',
                'body': 'private_connection',
            },
            ]
            request, metadata = self._interceptor.pre_create_private_connection(request, metadata)
            pb_request = datastream.CreatePrivateConnectionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_private_connection(resp)
            return resp

    class _CreateRoute(DatastreamRestStub):
        def __hash__(self):
            return hash("CreateRoute")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
            "routeId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.CreateRouteRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create route method over HTTP.

            Args:
                request (~.datastream.CreateRouteRequest):
                    The request object. route creation request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes',
                'body': 'route',
            },
            ]
            request, metadata = self._interceptor.pre_create_route(request, metadata)
            pb_request = datastream.CreateRouteRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_route(resp)
            return resp

    class _CreateStream(DatastreamRestStub):
        def __hash__(self):
            return hash("CreateStream")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
            "streamId" : "",        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.CreateStreamRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create stream method over HTTP.

            Args:
                request (~.datastream.CreateStreamRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/streams',
                'body': 'stream',
            },
            ]
            request, metadata = self._interceptor.pre_create_stream(request, metadata)
            pb_request = datastream.CreateStreamRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_stream(resp)
            return resp

    class _DeleteConnectionProfile(DatastreamRestStub):
        def __hash__(self):
            return hash("DeleteConnectionProfile")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.DeleteConnectionProfileRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete connection profile method over HTTP.

            Args:
                request (~.datastream.DeleteConnectionProfileRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_connection_profile(request, metadata)
            pb_request = datastream.DeleteConnectionProfileRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_connection_profile(resp)
            return resp

    class _DeletePrivateConnection(DatastreamRestStub):
        def __hash__(self):
            return hash("DeletePrivateConnection")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.DeletePrivateConnectionRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete private connection method over HTTP.

            Args:
                request (~.datastream.DeletePrivateConnectionRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1alpha1/{name=projects/*/locations/*/privateConnections/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_private_connection(request, metadata)
            pb_request = datastream.DeletePrivateConnectionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_private_connection(resp)
            return resp

    class _DeleteRoute(DatastreamRestStub):
        def __hash__(self):
            return hash("DeleteRoute")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.DeleteRouteRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete route method over HTTP.

            Args:
                request (~.datastream.DeleteRouteRequest):
                    The request object. route deletion request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_route(request, metadata)
            pb_request = datastream.DeleteRouteRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_route(resp)
            return resp

    class _DeleteStream(DatastreamRestStub):
        def __hash__(self):
            return hash("DeleteStream")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.DeleteStreamRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete stream method over HTTP.

            Args:
                request (~.datastream.DeleteStreamRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1alpha1/{name=projects/*/locations/*/streams/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_stream(request, metadata)
            pb_request = datastream.DeleteStreamRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_stream(resp)
            return resp

    class _DiscoverConnectionProfile(DatastreamRestStub):
        def __hash__(self):
            return hash("DiscoverConnectionProfile")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.DiscoverConnectionProfileRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.DiscoverConnectionProfileResponse:
            r"""Call the discover connection
        profile method over HTTP.

            Args:
                request (~.datastream.DiscoverConnectionProfileRequest):
                    The request object. Request message for 'discover'
                ConnectionProfile request.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.DiscoverConnectionProfileResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/connectionProfiles:discover',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_discover_connection_profile(request, metadata)
            pb_request = datastream.DiscoverConnectionProfileRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.DiscoverConnectionProfileResponse()
            pb_resp = datastream.DiscoverConnectionProfileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_discover_connection_profile(resp)
            return resp

    class _FetchErrors(DatastreamRestStub):
        def __hash__(self):
            return hash("FetchErrors")

        def __call__(self,
                request: datastream.FetchErrorsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the fetch errors method over HTTP.

            Args:
                request (~.datastream.FetchErrorsRequest):
                    The request object. Request message for 'FetchErrors'
                request.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1alpha1/{stream=projects/*/locations/*/streams/*}:fetchErrors',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_fetch_errors(request, metadata)
            pb_request = datastream.FetchErrorsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fetch_errors(resp)
            return resp

    class _FetchStaticIps(DatastreamRestStub):
        def __hash__(self):
            return hash("FetchStaticIps")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.FetchStaticIpsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.FetchStaticIpsResponse:
            r"""Call the fetch static ips method over HTTP.

            Args:
                request (~.datastream.FetchStaticIpsRequest):
                    The request object. Request message for 'FetchStaticIps'
                request.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.FetchStaticIpsResponse:
                    Response message for a
                'FetchStaticIps' response.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{name=projects/*/locations/*}:fetchStaticIps',
            },
            ]
            request, metadata = self._interceptor.pre_fetch_static_ips(request, metadata)
            pb_request = datastream.FetchStaticIpsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.FetchStaticIpsResponse()
            pb_resp = datastream.FetchStaticIpsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fetch_static_ips(resp)
            return resp

    class _GetConnectionProfile(DatastreamRestStub):
        def __hash__(self):
            return hash("GetConnectionProfile")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.GetConnectionProfileRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream_resources.ConnectionProfile:
            r"""Call the get connection profile method over HTTP.

            Args:
                request (~.datastream.GetConnectionProfileRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream_resources.ConnectionProfile:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_connection_profile(request, metadata)
            pb_request = datastream.GetConnectionProfileRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream_resources.ConnectionProfile()
            pb_resp = datastream_resources.ConnectionProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_connection_profile(resp)
            return resp

    class _GetPrivateConnection(DatastreamRestStub):
        def __hash__(self):
            return hash("GetPrivateConnection")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.GetPrivateConnectionRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream_resources.PrivateConnection:
            r"""Call the get private connection method over HTTP.

            Args:
                request (~.datastream.GetPrivateConnectionRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream_resources.PrivateConnection:
                    The PrivateConnection resource is
                used to establish private connectivity
                between Datastream and a customer's
                network.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{name=projects/*/locations/*/privateConnections/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_private_connection(request, metadata)
            pb_request = datastream.GetPrivateConnectionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream_resources.PrivateConnection()
            pb_resp = datastream_resources.PrivateConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_private_connection(resp)
            return resp

    class _GetRoute(DatastreamRestStub):
        def __hash__(self):
            return hash("GetRoute")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.GetRouteRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream_resources.Route:
            r"""Call the get route method over HTTP.

            Args:
                request (~.datastream.GetRouteRequest):
                    The request object. route get request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream_resources.Route:
                    The Route resource is the child of
                the PrivateConnection resource. It used
                to define a route for a
                PrivateConnection setup.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_route(request, metadata)
            pb_request = datastream.GetRouteRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream_resources.Route()
            pb_resp = datastream_resources.Route.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_route(resp)
            return resp

    class _GetStream(DatastreamRestStub):
        def __hash__(self):
            return hash("GetStream")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.GetStreamRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream_resources.Stream:
            r"""Call the get stream method over HTTP.

            Args:
                request (~.datastream.GetStreamRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream_resources.Stream:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{name=projects/*/locations/*/streams/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_stream(request, metadata)
            pb_request = datastream.GetStreamRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream_resources.Stream()
            pb_resp = datastream_resources.Stream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_stream(resp)
            return resp

    class _ListConnectionProfiles(DatastreamRestStub):
        def __hash__(self):
            return hash("ListConnectionProfiles")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.ListConnectionProfilesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.ListConnectionProfilesResponse:
            r"""Call the list connection profiles method over HTTP.

            Args:
                request (~.datastream.ListConnectionProfilesRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.ListConnectionProfilesResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/connectionProfiles',
            },
            ]
            request, metadata = self._interceptor.pre_list_connection_profiles(request, metadata)
            pb_request = datastream.ListConnectionProfilesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.ListConnectionProfilesResponse()
            pb_resp = datastream.ListConnectionProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_connection_profiles(resp)
            return resp

    class _ListPrivateConnections(DatastreamRestStub):
        def __hash__(self):
            return hash("ListPrivateConnections")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.ListPrivateConnectionsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.ListPrivateConnectionsResponse:
            r"""Call the list private connections method over HTTP.

            Args:
                request (~.datastream.ListPrivateConnectionsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.ListPrivateConnectionsResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/privateConnections',
            },
            ]
            request, metadata = self._interceptor.pre_list_private_connections(request, metadata)
            pb_request = datastream.ListPrivateConnectionsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.ListPrivateConnectionsResponse()
            pb_resp = datastream.ListPrivateConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_private_connections(resp)
            return resp

    class _ListRoutes(DatastreamRestStub):
        def __hash__(self):
            return hash("ListRoutes")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.ListRoutesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.ListRoutesResponse:
            r"""Call the list routes method over HTTP.

            Args:
                request (~.datastream.ListRoutesRequest):
                    The request object. route list request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.ListRoutesResponse:
                    route list response
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes',
            },
            ]
            request, metadata = self._interceptor.pre_list_routes(request, metadata)
            pb_request = datastream.ListRoutesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.ListRoutesResponse()
            pb_resp = datastream.ListRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_routes(resp)
            return resp

    class _ListStreams(DatastreamRestStub):
        def __hash__(self):
            return hash("ListStreams")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.ListStreamsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> datastream.ListStreamsResponse:
            r"""Call the list streams method over HTTP.

            Args:
                request (~.datastream.ListStreamsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastream.ListStreamsResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1alpha1/{parent=projects/*/locations/*}/streams',
            },
            ]
            request, metadata = self._interceptor.pre_list_streams(request, metadata)
            pb_request = datastream.ListStreamsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastream.ListStreamsResponse()
            pb_resp = datastream.ListStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_streams(resp)
            return resp

    class _UpdateConnectionProfile(DatastreamRestStub):
        def __hash__(self):
            return hash("UpdateConnectionProfile")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.UpdateConnectionProfileRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update connection profile method over HTTP.

            Args:
                request (~.datastream.UpdateConnectionProfileRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1alpha1/{connection_profile.name=projects/*/locations/*/connectionProfiles/*}',
                'body': 'connection_profile',
            },
            ]
            request, metadata = self._interceptor.pre_update_connection_profile(request, metadata)
            pb_request = datastream.UpdateConnectionProfileRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_connection_profile(resp)
            return resp

    class _UpdateStream(DatastreamRestStub):
        def __hash__(self):
            return hash("UpdateStream")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: datastream.UpdateStreamRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update stream method over HTTP.

            Args:
                request (~.datastream.UpdateStreamRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1alpha1/{stream.name=projects/*/locations/*/streams/*}',
                'body': 'stream',
            },
            ]
            request, metadata = self._interceptor.pre_update_stream(request, metadata)
            pb_request = datastream.UpdateStreamRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_stream(resp)
            return resp

    @property
    def create_connection_profile(self) -> Callable[
            [datastream.CreateConnectionProfileRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnectionProfile(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_private_connection(self) -> Callable[
            [datastream.CreatePrivateConnectionRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateConnection(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_route(self) -> Callable[
            [datastream.CreateRouteRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRoute(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_stream(self) -> Callable[
            [datastream.CreateStreamRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStream(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_connection_profile(self) -> Callable[
            [datastream.DeleteConnectionProfileRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnectionProfile(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_private_connection(self) -> Callable[
            [datastream.DeletePrivateConnectionRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateConnection(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_route(self) -> Callable[
            [datastream.DeleteRouteRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRoute(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_stream(self) -> Callable[
            [datastream.DeleteStreamRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStream(self._session, self._host, self._interceptor) # type: ignore

    @property
    def discover_connection_profile(self) -> Callable[
            [datastream.DiscoverConnectionProfileRequest],
            datastream.DiscoverConnectionProfileResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DiscoverConnectionProfile(self._session, self._host, self._interceptor) # type: ignore

    @property
    def fetch_errors(self) -> Callable[
            [datastream.FetchErrorsRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchErrors(self._session, self._host, self._interceptor) # type: ignore

    @property
    def fetch_static_ips(self) -> Callable[
            [datastream.FetchStaticIpsRequest],
            datastream.FetchStaticIpsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchStaticIps(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_connection_profile(self) -> Callable[
            [datastream.GetConnectionProfileRequest],
            datastream_resources.ConnectionProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnectionProfile(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_private_connection(self) -> Callable[
            [datastream.GetPrivateConnectionRequest],
            datastream_resources.PrivateConnection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateConnection(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_route(self) -> Callable[
            [datastream.GetRouteRequest],
            datastream_resources.Route]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRoute(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_stream(self) -> Callable[
            [datastream.GetStreamRequest],
            datastream_resources.Stream]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStream(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_connection_profiles(self) -> Callable[
            [datastream.ListConnectionProfilesRequest],
            datastream.ListConnectionProfilesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnectionProfiles(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_private_connections(self) -> Callable[
            [datastream.ListPrivateConnectionsRequest],
            datastream.ListPrivateConnectionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateConnections(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_routes(self) -> Callable[
            [datastream.ListRoutesRequest],
            datastream.ListRoutesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRoutes(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_streams(self) -> Callable[
            [datastream.ListStreamsRequest],
            datastream.ListStreamsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStreams(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_connection_profile(self) -> Callable[
            [datastream.UpdateConnectionProfileRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnectionProfile(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_stream(self) -> Callable[
            [datastream.UpdateStreamRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStream(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'DatastreamRestTransport',
)
