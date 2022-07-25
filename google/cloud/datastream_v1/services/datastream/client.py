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
from collections import OrderedDict
import os
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.datastream_v1.services.datastream import pagers
from google.cloud.datastream_v1.types import datastream, datastream_resources

from .transports.base import DEFAULT_CLIENT_INFO, DatastreamTransport
from .transports.grpc import DatastreamGrpcTransport
from .transports.grpc_asyncio import DatastreamGrpcAsyncIOTransport


class DatastreamClientMeta(type):
    """Metaclass for the Datastream client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[DatastreamTransport]]
    _transport_registry["grpc"] = DatastreamGrpcTransport
    _transport_registry["grpc_asyncio"] = DatastreamGrpcAsyncIOTransport

    def get_transport_class(
        cls,
        label: str = None,
    ) -> Type[DatastreamTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class DatastreamClient(metaclass=DatastreamClientMeta):
    """Datastream service"""

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "datastream.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DatastreamClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DatastreamClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DatastreamTransport:
        """Returns the transport used by the client instance.

        Returns:
            DatastreamTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def connection_profile_path(
        project: str,
        location: str,
        connection_profile: str,
    ) -> str:
        """Returns a fully-qualified connection_profile string."""
        return "projects/{project}/locations/{location}/connectionProfiles/{connection_profile}".format(
            project=project,
            location=location,
            connection_profile=connection_profile,
        )

    @staticmethod
    def parse_connection_profile_path(path: str) -> Dict[str, str]:
        """Parses a connection_profile path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/connectionProfiles/(?P<connection_profile>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def networks_path(
        project: str,
        network: str,
    ) -> str:
        """Returns a fully-qualified networks string."""
        return "projects/{project}/global/networks/{network}".format(
            project=project,
            network=network,
        )

    @staticmethod
    def parse_networks_path(path: str) -> Dict[str, str]:
        """Parses a networks path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/global/networks/(?P<network>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def private_connection_path(
        project: str,
        location: str,
        private_connection: str,
    ) -> str:
        """Returns a fully-qualified private_connection string."""
        return "projects/{project}/locations/{location}/privateConnections/{private_connection}".format(
            project=project,
            location=location,
            private_connection=private_connection,
        )

    @staticmethod
    def parse_private_connection_path(path: str) -> Dict[str, str]:
        """Parses a private_connection path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateConnections/(?P<private_connection>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def route_path(
        project: str,
        location: str,
        private_connection: str,
        route: str,
    ) -> str:
        """Returns a fully-qualified route string."""
        return "projects/{project}/locations/{location}/privateConnections/{private_connection}/routes/{route}".format(
            project=project,
            location=location,
            private_connection=private_connection,
            route=route,
        )

    @staticmethod
    def parse_route_path(path: str) -> Dict[str, str]:
        """Parses a route path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateConnections/(?P<private_connection>.+?)/routes/(?P<route>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def stream_path(
        project: str,
        location: str,
        stream: str,
    ) -> str:
        """Returns a fully-qualified stream string."""
        return "projects/{project}/locations/{location}/streams/{stream}".format(
            project=project,
            location=location,
            stream=stream,
        )

    @staticmethod
    def parse_stream_path(path: str) -> Dict[str, str]:
        """Parses a stream path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/streams/(?P<stream>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def stream_object_path(
        project: str,
        location: str,
        stream: str,
        object: str,
    ) -> str:
        """Returns a fully-qualified stream_object string."""
        return "projects/{project}/locations/{location}/streams/{stream}/objects/{object}".format(
            project=project,
            location=location,
            stream=stream,
            object=object,
        )

    @staticmethod
    def parse_stream_object_path(path: str) -> Dict[str, str]:
        """Parses a stream_object path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/streams/(?P<stream>.+?)/objects/(?P<object>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DatastreamTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the datastream client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, DatastreamTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, DatastreamTransport):
            # transport is a DatastreamTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=client_options.api_audience,
            )

    def list_connection_profiles(
        self,
        request: Union[datastream.ListConnectionProfilesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConnectionProfilesPager:
        r"""Use this method to list connection profiles created
        in a project and location.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_list_connection_profiles():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.ListConnectionProfilesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_connection_profiles(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.ListConnectionProfilesRequest, dict]):
                The request object. Request message for listing
                connection profiles.
            parent (str):
                Required. The parent that owns the
                collection of connection profiles.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.ListConnectionProfilesPager:
                Response message for listing
                connection profiles.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.ListConnectionProfilesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.ListConnectionProfilesRequest):
            request = datastream.ListConnectionProfilesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_connection_profiles]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListConnectionProfilesPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_connection_profile(
        self,
        request: Union[datastream.GetConnectionProfileRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.ConnectionProfile:
        r"""Use this method to get details about a connection
        profile.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_get_connection_profile():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.GetConnectionProfileRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_connection_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.GetConnectionProfileRequest, dict]):
                The request object. Request message for getting a
                connection profile.
            name (str):
                Required. The name of the connection
                profile resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.ConnectionProfile:
                A set of reusable connection
                configurations to be used as a source or
                destination for a stream.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.GetConnectionProfileRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.GetConnectionProfileRequest):
            request = datastream.GetConnectionProfileRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_connection_profile]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_connection_profile(
        self,
        request: Union[datastream.CreateConnectionProfileRequest, dict] = None,
        *,
        parent: str = None,
        connection_profile: datastream_resources.ConnectionProfile = None,
        connection_profile_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to create a connection profile in a
        project and location.

        .. code-block:: python

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

        Args:
            request (Union[google.cloud.datastream_v1.types.CreateConnectionProfileRequest, dict]):
                The request object. Request message for creating a
                connection profile.
            parent (str):
                Required. The parent that owns the
                collection of ConnectionProfiles.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connection_profile (google.cloud.datastream_v1.types.ConnectionProfile):
                Required. The connection profile
                resource to create.

                This corresponds to the ``connection_profile`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connection_profile_id (str):
                Required. The connection profile
                identifier.

                This corresponds to the ``connection_profile_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.datastream_v1.types.ConnectionProfile` A set of reusable connection configurations to be used as a source or
                   destination for a stream.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, connection_profile, connection_profile_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.CreateConnectionProfileRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.CreateConnectionProfileRequest):
            request = datastream.CreateConnectionProfileRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if connection_profile is not None:
                request.connection_profile = connection_profile
            if connection_profile_id is not None:
                request.connection_profile_id = connection_profile_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_connection_profile
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.ConnectionProfile,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_connection_profile(
        self,
        request: Union[datastream.UpdateConnectionProfileRequest, dict] = None,
        *,
        connection_profile: datastream_resources.ConnectionProfile = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to update the parameters of a
        connection profile.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_update_connection_profile():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                connection_profile = datastream_v1.ConnectionProfile()
                connection_profile.oracle_profile.hostname = "hostname_value"
                connection_profile.oracle_profile.username = "username_value"
                connection_profile.oracle_profile.password = "password_value"
                connection_profile.oracle_profile.database_service = "database_service_value"
                connection_profile.display_name = "display_name_value"

                request = datastream_v1.UpdateConnectionProfileRequest(
                    connection_profile=connection_profile,
                )

                # Make the request
                operation = client.update_connection_profile(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.UpdateConnectionProfileRequest, dict]):
                The request object. Connection profile update message.
            connection_profile (google.cloud.datastream_v1.types.ConnectionProfile):
                Required. The connection profile to
                update.

                This corresponds to the ``connection_profile`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the ConnectionProfile resource by the
                update. The fields specified in the update_mask are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.datastream_v1.types.ConnectionProfile` A set of reusable connection configurations to be used as a source or
                   destination for a stream.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([connection_profile, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.UpdateConnectionProfileRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.UpdateConnectionProfileRequest):
            request = datastream.UpdateConnectionProfileRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if connection_profile is not None:
                request.connection_profile = connection_profile
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_connection_profile
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("connection_profile.name", request.connection_profile.name),)
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.ConnectionProfile,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_connection_profile(
        self,
        request: Union[datastream.DeleteConnectionProfileRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to delete a connection profile.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_delete_connection_profile():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.DeleteConnectionProfileRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_connection_profile(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.DeleteConnectionProfileRequest, dict]):
                The request object. Request message for deleting a
                connection profile.
            name (str):
                Required. The name of the connection
                profile resource to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.DeleteConnectionProfileRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.DeleteConnectionProfileRequest):
            request = datastream.DeleteConnectionProfileRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_connection_profile
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def discover_connection_profile(
        self,
        request: Union[datastream.DiscoverConnectionProfileRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream.DiscoverConnectionProfileResponse:
        r"""Use this method to discover a connection profile.
        The discover API call exposes the data objects and
        metadata belonging to the profile. Typically, a request
        returns children data objects of a parent data object
        that's optionally supplied in the request.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_discover_connection_profile():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                connection_profile = datastream_v1.ConnectionProfile()
                connection_profile.oracle_profile.hostname = "hostname_value"
                connection_profile.oracle_profile.username = "username_value"
                connection_profile.oracle_profile.password = "password_value"
                connection_profile.oracle_profile.database_service = "database_service_value"
                connection_profile.display_name = "display_name_value"

                request = datastream_v1.DiscoverConnectionProfileRequest(
                    connection_profile=connection_profile,
                    full_hierarchy=True,
                    parent="parent_value",
                )

                # Make the request
                response = client.discover_connection_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.DiscoverConnectionProfileRequest, dict]):
                The request object. Request message for 'discover'
                ConnectionProfile request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.DiscoverConnectionProfileResponse:
                Response from a discover request.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.DiscoverConnectionProfileRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.DiscoverConnectionProfileRequest):
            request = datastream.DiscoverConnectionProfileRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.discover_connection_profile
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_streams(
        self,
        request: Union[datastream.ListStreamsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListStreamsPager:
        r"""Use this method to list streams in a project and
        location.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_list_streams():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.ListStreamsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_streams(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.ListStreamsRequest, dict]):
                The request object. Request message for listing streams.
            parent (str):
                Required. The parent that owns the
                collection of streams.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.ListStreamsPager:
                Response message for listing streams.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.ListStreamsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.ListStreamsRequest):
            request = datastream.ListStreamsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_streams]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListStreamsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_stream(
        self,
        request: Union[datastream.GetStreamRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.Stream:
        r"""Use this method to get details about a stream.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_get_stream():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.GetStreamRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_stream(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.GetStreamRequest, dict]):
                The request object. Request message for getting a
                stream.
            name (str):
                Required. The name of the stream
                resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.Stream:
                A resource representing streaming
                data from a source to a destination.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.GetStreamRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.GetStreamRequest):
            request = datastream.GetStreamRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_stream]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_stream(
        self,
        request: Union[datastream.CreateStreamRequest, dict] = None,
        *,
        parent: str = None,
        stream: datastream_resources.Stream = None,
        stream_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to create a stream.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_create_stream():
                # Create a client
                client = datastream_v1.DatastreamClient()

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

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.CreateStreamRequest, dict]):
                The request object. Request message for creating a
                stream.
            parent (str):
                Required. The parent that owns the
                collection of streams.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            stream (google.cloud.datastream_v1.types.Stream):
                Required. The stream resource to
                create.

                This corresponds to the ``stream`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            stream_id (str):
                Required. The stream identifier.
                This corresponds to the ``stream_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.datastream_v1.types.Stream` A
                resource representing streaming data from a source to a
                destination.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, stream, stream_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.CreateStreamRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.CreateStreamRequest):
            request = datastream.CreateStreamRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if stream is not None:
                request.stream = stream
            if stream_id is not None:
                request.stream_id = stream_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_stream]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.Stream,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_stream(
        self,
        request: Union[datastream.UpdateStreamRequest, dict] = None,
        *,
        stream: datastream_resources.Stream = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to update the configuration of a
        stream.

        .. code-block:: python

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

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.UpdateStreamRequest, dict]):
                The request object. Request message for updating a
                stream.
            stream (google.cloud.datastream_v1.types.Stream):
                Required. The stream resource to
                update.

                This corresponds to the ``stream`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the stream resource by the update. The
                fields specified in the update_mask are relative to the
                resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then all fields will be overwritten.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.datastream_v1.types.Stream` A
                resource representing streaming data from a source to a
                destination.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([stream, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.UpdateStreamRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.UpdateStreamRequest):
            request = datastream.UpdateStreamRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if stream is not None:
                request.stream = stream
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_stream]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("stream.name", request.stream.name),)
            ),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.Stream,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_stream(
        self,
        request: Union[datastream.DeleteStreamRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to delete a stream.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_delete_stream():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.DeleteStreamRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_stream(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.DeleteStreamRequest, dict]):
                The request object. Request message for deleting a
                stream.
            name (str):
                Required. The name of the stream
                resource to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.DeleteStreamRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.DeleteStreamRequest):
            request = datastream.DeleteStreamRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_stream]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_stream_object(
        self,
        request: Union[datastream.GetStreamObjectRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.StreamObject:
        r"""Use this method to get details about a stream object.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_get_stream_object():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.GetStreamObjectRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_stream_object(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.GetStreamObjectRequest, dict]):
                The request object. Request for fetching a specific
                stream object.
            name (str):
                Required. The name of the stream
                object resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.StreamObject:
                A specific stream object (e.g a
                specific DB table).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.GetStreamObjectRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.GetStreamObjectRequest):
            request = datastream.GetStreamObjectRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_stream_object]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def lookup_stream_object(
        self,
        request: Union[datastream.LookupStreamObjectRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.StreamObject:
        r"""Use this method to look up a stream object by its
        source object identifier.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_lookup_stream_object():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                source_object_identifier = datastream_v1.SourceObjectIdentifier()
                source_object_identifier.oracle_identifier.schema = "schema_value"
                source_object_identifier.oracle_identifier.table = "table_value"

                request = datastream_v1.LookupStreamObjectRequest(
                    parent="parent_value",
                    source_object_identifier=source_object_identifier,
                )

                # Make the request
                response = client.lookup_stream_object(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.LookupStreamObjectRequest, dict]):
                The request object. Request for looking up a specific
                stream object by its source object identifier.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.StreamObject:
                A specific stream object (e.g a
                specific DB table).

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.LookupStreamObjectRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.LookupStreamObjectRequest):
            request = datastream.LookupStreamObjectRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.lookup_stream_object]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_stream_objects(
        self,
        request: Union[datastream.ListStreamObjectsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListStreamObjectsPager:
        r"""Use this method to list the objects of a specific
        stream.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_list_stream_objects():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.ListStreamObjectsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_stream_objects(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.ListStreamObjectsRequest, dict]):
                The request object. Request for listing all objects for
                a specific stream.
            parent (str):
                Required. The parent stream that owns
                the collection of objects.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.ListStreamObjectsPager:
                Response containing the objects for a
                stream.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.ListStreamObjectsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.ListStreamObjectsRequest):
            request = datastream.ListStreamObjectsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_stream_objects]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListStreamObjectsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def start_backfill_job(
        self,
        request: Union[datastream.StartBackfillJobRequest, dict] = None,
        *,
        object_: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream.StartBackfillJobResponse:
        r"""Use this method to start a backfill job for the
        specified stream object.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_start_backfill_job():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.StartBackfillJobRequest(
                    object_="object__value",
                )

                # Make the request
                response = client.start_backfill_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.StartBackfillJobRequest, dict]):
                The request object. Request for manually initiating a
                backfill job for a specific stream object.
            object_ (str):
                Required. The name of the stream
                object resource to start a backfill job
                for.

                This corresponds to the ``object_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.StartBackfillJobResponse:
                Response for manually initiating a
                backfill job for a specific stream
                object.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([object_])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.StartBackfillJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.StartBackfillJobRequest):
            request = datastream.StartBackfillJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if object_ is not None:
                request.object_ = object_

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.start_backfill_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("object", request.object_),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def stop_backfill_job(
        self,
        request: Union[datastream.StopBackfillJobRequest, dict] = None,
        *,
        object_: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream.StopBackfillJobResponse:
        r"""Use this method to stop a backfill job for the
        specified stream object.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_stop_backfill_job():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.StopBackfillJobRequest(
                    object_="object__value",
                )

                # Make the request
                response = client.stop_backfill_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.StopBackfillJobRequest, dict]):
                The request object. Request for manually stopping a
                running backfill job for a specific stream object.
            object_ (str):
                Required. The name of the stream
                object resource to stop the backfill job
                for.

                This corresponds to the ``object_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.StopBackfillJobResponse:
                Response for manually stop a backfill
                job for a specific stream object.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([object_])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.StopBackfillJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.StopBackfillJobRequest):
            request = datastream.StopBackfillJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if object_ is not None:
                request.object_ = object_

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.stop_backfill_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("object", request.object_),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def fetch_static_ips(
        self,
        request: Union[datastream.FetchStaticIpsRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.FetchStaticIpsPager:
        r"""The FetchStaticIps API call exposes the static IP
        addresses used by Datastream.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_fetch_static_ips():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.FetchStaticIpsRequest(
                    name="name_value",
                )

                # Make the request
                page_result = client.fetch_static_ips(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.FetchStaticIpsRequest, dict]):
                The request object. Request message for 'FetchStaticIps'
                request.
            name (str):
                Required. The resource name for the location for which
                static IPs should be returned. Must be in the format
                ``projects/*/locations/*``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.FetchStaticIpsPager:
                Response message for a
                'FetchStaticIps' response.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.FetchStaticIpsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.FetchStaticIpsRequest):
            request = datastream.FetchStaticIpsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.fetch_static_ips]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.FetchStaticIpsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_private_connection(
        self,
        request: Union[datastream.CreatePrivateConnectionRequest, dict] = None,
        *,
        parent: str = None,
        private_connection: datastream_resources.PrivateConnection = None,
        private_connection_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to create a private connectivity
        configuration.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_create_private_connection():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                private_connection = datastream_v1.PrivateConnection()
                private_connection.display_name = "display_name_value"

                request = datastream_v1.CreatePrivateConnectionRequest(
                    parent="parent_value",
                    private_connection_id="private_connection_id_value",
                    private_connection=private_connection,
                )

                # Make the request
                operation = client.create_private_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.CreatePrivateConnectionRequest, dict]):
                The request object. Request for creating a private
                connection.
            parent (str):
                Required. The parent that owns the
                collection of PrivateConnections.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_connection (google.cloud.datastream_v1.types.PrivateConnection):
                Required. The Private Connectivity
                resource to create.

                This corresponds to the ``private_connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_connection_id (str):
                Required. The private connectivity
                identifier.

                This corresponds to the ``private_connection_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.datastream_v1.types.PrivateConnection` The PrivateConnection resource is used to establish private connectivity
                   between Datastream and a customer's network.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, private_connection, private_connection_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.CreatePrivateConnectionRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.CreatePrivateConnectionRequest):
            request = datastream.CreatePrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if private_connection is not None:
                request.private_connection = private_connection
            if private_connection_id is not None:
                request.private_connection_id = private_connection_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_private_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.PrivateConnection,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_private_connection(
        self,
        request: Union[datastream.GetPrivateConnectionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.PrivateConnection:
        r"""Use this method to get details about a private
        connectivity configuration.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_get_private_connection():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.GetPrivateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_private_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.GetPrivateConnectionRequest, dict]):
                The request object. Request to get a private connection
                configuration.
            name (str):
                Required. The name of the  private
                connectivity configuration to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.PrivateConnection:
                The PrivateConnection resource is
                used to establish private connectivity
                between Datastream and a customer's
                network.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.GetPrivateConnectionRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.GetPrivateConnectionRequest):
            request = datastream.GetPrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_private_connection]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_private_connections(
        self,
        request: Union[datastream.ListPrivateConnectionsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPrivateConnectionsPager:
        r"""Use this method to list private connectivity
        configurations in a project and location.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_list_private_connections():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.ListPrivateConnectionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_private_connections(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.ListPrivateConnectionsRequest, dict]):
                The request object. Request for listing private
                connections.
            parent (str):
                Required. The parent that owns the
                collection of private connectivity
                configurations.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.ListPrivateConnectionsPager:
                Response containing a list of private
                connection configurations.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.ListPrivateConnectionsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.ListPrivateConnectionsRequest):
            request = datastream.ListPrivateConnectionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_private_connections]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPrivateConnectionsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_private_connection(
        self,
        request: Union[datastream.DeletePrivateConnectionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to delete a private connectivity
        configuration.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_delete_private_connection():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.DeletePrivateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_private_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.DeletePrivateConnectionRequest, dict]):
                The request object. Request to delete a private
                connection.
            name (str):
                Required. The name of the private
                connectivity configuration to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.DeletePrivateConnectionRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.DeletePrivateConnectionRequest):
            request = datastream.DeletePrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_private_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_route(
        self,
        request: Union[datastream.CreateRouteRequest, dict] = None,
        *,
        parent: str = None,
        route: datastream_resources.Route = None,
        route_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to create a route for a private
        connectivity configuration in a project and location.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_create_route():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                route = datastream_v1.Route()
                route.display_name = "display_name_value"
                route.destination_address = "destination_address_value"

                request = datastream_v1.CreateRouteRequest(
                    parent="parent_value",
                    route_id="route_id_value",
                    route=route,
                )

                # Make the request
                operation = client.create_route(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.CreateRouteRequest, dict]):
                The request object. Route creation request.
            parent (str):
                Required. The parent that owns the
                collection of Routes.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            route (google.cloud.datastream_v1.types.Route):
                Required. The Route resource to
                create.

                This corresponds to the ``route`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            route_id (str):
                Required. The Route identifier.
                This corresponds to the ``route_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.datastream_v1.types.Route` The route resource is the child of the private connection resource,
                   used for defining a route for a private connection.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, route, route_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.CreateRouteRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.CreateRouteRequest):
            request = datastream.CreateRouteRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if route is not None:
                request.route = route
            if route_id is not None:
                request.route_id = route_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_route]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            datastream_resources.Route,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_route(
        self,
        request: Union[datastream.GetRouteRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datastream_resources.Route:
        r"""Use this method to get details about a route.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_get_route():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.GetRouteRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_route(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.GetRouteRequest, dict]):
                The request object. Route get request.
            name (str):
                Required. The name of the Route
                resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.types.Route:
                The route resource is the child of
                the private connection resource, used
                for defining a route for a private
                connection.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.GetRouteRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.GetRouteRequest):
            request = datastream.GetRouteRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_route]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_routes(
        self,
        request: Union[datastream.ListRoutesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRoutesPager:
        r"""Use this method to list routes created for a private
        connectivity configuration in a project and location.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_list_routes():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.ListRoutesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_routes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.ListRoutesRequest, dict]):
                The request object. Route list request.
            parent (str):
                Required. The parent that owns the
                collection of Routess.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datastream_v1.services.datastream.pagers.ListRoutesPager:
                Route list response.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.ListRoutesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.ListRoutesRequest):
            request = datastream.ListRoutesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_routes]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListRoutesPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_route(
        self,
        request: Union[datastream.DeleteRouteRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Use this method to delete a route.

        .. code-block:: python

            from google.cloud import datastream_v1

            def sample_delete_route():
                # Create a client
                client = datastream_v1.DatastreamClient()

                # Initialize request argument(s)
                request = datastream_v1.DeleteRouteRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_route(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.datastream_v1.types.DeleteRouteRequest, dict]):
                The request object. Route deletion request.
            name (str):
                Required. The name of the Route
                resource to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a datastream.DeleteRouteRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, datastream.DeleteRouteRequest):
            request = datastream.DeleteRouteRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_route]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=datastream.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-datastream",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DatastreamClient",)
