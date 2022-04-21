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
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.datastream.v1",
    manifest={
        "OracleProfile",
        "MysqlProfile",
        "GcsProfile",
        "StaticServiceIpConnectivity",
        "ForwardSshTunnelConnectivity",
        "VpcPeeringConfig",
        "PrivateConnection",
        "PrivateConnectivity",
        "Route",
        "MysqlSslConfig",
        "ConnectionProfile",
        "OracleColumn",
        "OracleTable",
        "OracleSchema",
        "OracleRdbms",
        "OracleSourceConfig",
        "MysqlColumn",
        "MysqlTable",
        "MysqlDatabase",
        "MysqlRdbms",
        "MysqlSourceConfig",
        "SourceConfig",
        "AvroFileFormat",
        "JsonFileFormat",
        "GcsDestinationConfig",
        "DestinationConfig",
        "Stream",
        "StreamObject",
        "SourceObjectIdentifier",
        "BackfillJob",
        "Error",
        "ValidationResult",
        "Validation",
        "ValidationMessage",
    },
)


class OracleProfile(proto.Message):
    r"""Oracle database profile.

    Attributes:
        hostname (str):
            Required. Hostname for the Oracle connection.
        port (int):
            Port for the Oracle connection, default value
            is 1521.
        username (str):
            Required. Username for the Oracle connection.
        password (str):
            Required. Password for the Oracle connection.
        database_service (str):
            Required. Database for the Oracle connection.
        connection_attributes (Mapping[str, str]):
            Connection string attributes
    """

    hostname = proto.Field(
        proto.STRING,
        number=1,
    )
    port = proto.Field(
        proto.INT32,
        number=2,
    )
    username = proto.Field(
        proto.STRING,
        number=3,
    )
    password = proto.Field(
        proto.STRING,
        number=4,
    )
    database_service = proto.Field(
        proto.STRING,
        number=5,
    )
    connection_attributes = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )


class MysqlProfile(proto.Message):
    r"""MySQL database profile.

    Attributes:
        hostname (str):
            Required. Hostname for the MySQL connection.
        port (int):
            Port for the MySQL connection, default value
            is 3306.
        username (str):
            Required. Username for the MySQL connection.
        password (str):
            Required. Input only. Password for the MySQL
            connection.
        ssl_config (google.cloud.datastream_v1.types.MysqlSslConfig):
            SSL configuration for the MySQL connection.
    """

    hostname = proto.Field(
        proto.STRING,
        number=1,
    )
    port = proto.Field(
        proto.INT32,
        number=2,
    )
    username = proto.Field(
        proto.STRING,
        number=3,
    )
    password = proto.Field(
        proto.STRING,
        number=4,
    )
    ssl_config = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MysqlSslConfig",
    )


class GcsProfile(proto.Message):
    r"""Cloud Storage bucket profile.

    Attributes:
        bucket (str):
            Required. The Cloud Storage bucket name.
        root_path (str):
            The root path inside the Cloud Storage
            bucket.
    """

    bucket = proto.Field(
        proto.STRING,
        number=1,
    )
    root_path = proto.Field(
        proto.STRING,
        number=2,
    )


class StaticServiceIpConnectivity(proto.Message):
    r"""Static IP address connectivity."""


class ForwardSshTunnelConnectivity(proto.Message):
    r"""Forward SSH Tunnel connectivity.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hostname (str):
            Required. Hostname for the SSH tunnel.
        username (str):
            Required. Username for the SSH tunnel.
        port (int):
            Port for the SSH tunnel, default value is 22.
        password (str):
            Input only. SSH password.

            This field is a member of `oneof`_ ``authentication_method``.
        private_key (str):
            Input only. SSH private key.

            This field is a member of `oneof`_ ``authentication_method``.
    """

    hostname = proto.Field(
        proto.STRING,
        number=1,
    )
    username = proto.Field(
        proto.STRING,
        number=2,
    )
    port = proto.Field(
        proto.INT32,
        number=3,
    )
    password = proto.Field(
        proto.STRING,
        number=100,
        oneof="authentication_method",
    )
    private_key = proto.Field(
        proto.STRING,
        number=101,
        oneof="authentication_method",
    )


class VpcPeeringConfig(proto.Message):
    r"""The VPC Peering configuration is used to create VPC peering
    between Datastream and the consumer's VPC.

    Attributes:
        vpc (str):
            Required. Fully qualified name of the VPC that Datastream
            will peer to. Format:
            ``projects/{project}/global/{networks}/{name}``
        subnet (str):
            Required. A free subnet for peering. (CIDR of
            /29)
    """

    vpc = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivateConnection(proto.Message):
    r"""The PrivateConnection resource is used to establish private
    connectivity between Datastream and a customer's network.

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (Mapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        state (google.cloud.datastream_v1.types.PrivateConnection.State):
            Output only. The state of the Private
            Connection.
        error (google.cloud.datastream_v1.types.Error):
            Output only. In case of error, the details of
            the error in a user-friendly format.
        vpc_peering_config (google.cloud.datastream_v1.types.VpcPeeringConfig):
            VPC Peering Config.
    """

    class State(proto.Enum):
        r"""Private Connection state."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        FAILED = 3
        DELETING = 4
        FAILED_TO_DELETE = 5

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    state = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    error = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Error",
    )
    vpc_peering_config = proto.Field(
        proto.MESSAGE,
        number=100,
        message="VpcPeeringConfig",
    )


class PrivateConnectivity(proto.Message):
    r"""Private Connectivity

    Attributes:
        private_connection (str):
            Required. A reference to a private connection resource.
            Format:
            ``projects/{project}/locations/{location}/privateConnections/{name}``
    """

    private_connection = proto.Field(
        proto.STRING,
        number=1,
    )


class Route(proto.Message):
    r"""The route resource is the child of the private connection
    resource, used for defining a route for a private connection.

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (Mapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        destination_address (str):
            Required. Destination address for connection
        destination_port (int):
            Destination port for connection
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    destination_address = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_port = proto.Field(
        proto.INT32,
        number=7,
    )


class MysqlSslConfig(proto.Message):
    r"""MySQL SSL configuration information.

    Attributes:
        client_key (str):
            Input only. PEM-encoded private key associated with the
            Client Certificate. If this field is used then the
            'client_certificate' and the 'ca_certificate' fields are
            mandatory.
        client_key_set (bool):
            Output only. Indicates whether the client_key field is set.
        client_certificate (str):
            Input only. PEM-encoded certificate that will be used by the
            replica to authenticate against the source database server.
            If this field is used then the 'client_key' and the
            'ca_certificate' fields are mandatory.
        client_certificate_set (bool):
            Output only. Indicates whether the client_certificate field
            is set.
        ca_certificate (str):
            Input only. PEM-encoded certificate of the CA
            that signed the source database server's
            certificate.
        ca_certificate_set (bool):
            Output only. Indicates whether the ca_certificate field is
            set.
    """

    client_key = proto.Field(
        proto.STRING,
        number=1,
    )
    client_key_set = proto.Field(
        proto.BOOL,
        number=2,
    )
    client_certificate = proto.Field(
        proto.STRING,
        number=3,
    )
    client_certificate_set = proto.Field(
        proto.BOOL,
        number=4,
    )
    ca_certificate = proto.Field(
        proto.STRING,
        number=5,
    )
    ca_certificate_set = proto.Field(
        proto.BOOL,
        number=6,
    )


class ConnectionProfile(proto.Message):
    r"""A set of reusable connection configurations to be used as a
    source or destination for a stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (Mapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        oracle_profile (google.cloud.datastream_v1.types.OracleProfile):
            Oracle ConnectionProfile configuration.

            This field is a member of `oneof`_ ``profile``.
        gcs_profile (google.cloud.datastream_v1.types.GcsProfile):
            Cloud Storage ConnectionProfile
            configuration.

            This field is a member of `oneof`_ ``profile``.
        mysql_profile (google.cloud.datastream_v1.types.MysqlProfile):
            MySQL ConnectionProfile configuration.

            This field is a member of `oneof`_ ``profile``.
        static_service_ip_connectivity (google.cloud.datastream_v1.types.StaticServiceIpConnectivity):
            Static Service IP connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        forward_ssh_connectivity (google.cloud.datastream_v1.types.ForwardSshTunnelConnectivity):
            Forward SSH tunnel connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        private_connectivity (google.cloud.datastream_v1.types.PrivateConnectivity):
            Private connectivity.

            This field is a member of `oneof`_ ``connectivity``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    oracle_profile = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="profile",
        message="OracleProfile",
    )
    gcs_profile = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="profile",
        message="GcsProfile",
    )
    mysql_profile = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="profile",
        message="MysqlProfile",
    )
    static_service_ip_connectivity = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="connectivity",
        message="StaticServiceIpConnectivity",
    )
    forward_ssh_connectivity = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="connectivity",
        message="ForwardSshTunnelConnectivity",
    )
    private_connectivity = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="connectivity",
        message="PrivateConnectivity",
    )


class OracleColumn(proto.Message):
    r"""Oracle Column.

    Attributes:
        column (str):
            Column name.
        data_type (str):
            The Oracle data type.
        length (int):
            Column length.
        precision (int):
            Column precision.
        scale (int):
            Column scale.
        encoding (str):
            Column encoding.
        primary_key (bool):
            Whether or not the column represents a
            primary key.
        nullable (bool):
            Whether or not the column can accept a null
            value.
        ordinal_position (int):
            The ordinal position of the column in the
            table.
    """

    column = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type = proto.Field(
        proto.STRING,
        number=2,
    )
    length = proto.Field(
        proto.INT32,
        number=3,
    )
    precision = proto.Field(
        proto.INT32,
        number=4,
    )
    scale = proto.Field(
        proto.INT32,
        number=5,
    )
    encoding = proto.Field(
        proto.STRING,
        number=6,
    )
    primary_key = proto.Field(
        proto.BOOL,
        number=7,
    )
    nullable = proto.Field(
        proto.BOOL,
        number=8,
    )
    ordinal_position = proto.Field(
        proto.INT32,
        number=9,
    )


class OracleTable(proto.Message):
    r"""Oracle table.

    Attributes:
        table (str):
            Table name.
        oracle_columns (Sequence[google.cloud.datastream_v1.types.OracleColumn]):
            Oracle columns in the schema.
            When unspecified as part of inclue/exclude
            lists, includes/excludes everything.
    """

    table = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_columns = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OracleColumn",
    )


class OracleSchema(proto.Message):
    r"""Oracle schema.

    Attributes:
        schema (str):
            Schema name.
        oracle_tables (Sequence[google.cloud.datastream_v1.types.OracleTable]):
            Tables in the schema.
    """

    schema = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_tables = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OracleTable",
    )


class OracleRdbms(proto.Message):
    r"""Oracle database structure.

    Attributes:
        oracle_schemas (Sequence[google.cloud.datastream_v1.types.OracleSchema]):
            Oracle schemas/databases in the database
            server.
    """

    oracle_schemas = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OracleSchema",
    )


class OracleSourceConfig(proto.Message):
    r"""Oracle data source configuration

    Attributes:
        include_objects (google.cloud.datastream_v1.types.OracleRdbms):
            Oracle objects to include in the stream.
        exclude_objects (google.cloud.datastream_v1.types.OracleRdbms):
            Oracle objects to exclude from the stream.
    """

    include_objects = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OracleRdbms",
    )
    exclude_objects = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OracleRdbms",
    )


class MysqlColumn(proto.Message):
    r"""MySQL Column.

    Attributes:
        column (str):
            Column name.
        data_type (str):
            The MySQL data type. Full data types list can
            be found here:
            https://dev.mysql.com/doc/refman/8.0/en/data-types.html
        length (int):
            Column length.
        collation (str):
            Column collation.
        primary_key (bool):
            Whether or not the column represents a
            primary key.
        nullable (bool):
            Whether or not the column can accept a null
            value.
        ordinal_position (int):
            The ordinal position of the column in the
            table.
    """

    column = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type = proto.Field(
        proto.STRING,
        number=2,
    )
    length = proto.Field(
        proto.INT32,
        number=3,
    )
    collation = proto.Field(
        proto.STRING,
        number=4,
    )
    primary_key = proto.Field(
        proto.BOOL,
        number=5,
    )
    nullable = proto.Field(
        proto.BOOL,
        number=6,
    )
    ordinal_position = proto.Field(
        proto.INT32,
        number=7,
    )


class MysqlTable(proto.Message):
    r"""MySQL table.

    Attributes:
        table (str):
            Table name.
        mysql_columns (Sequence[google.cloud.datastream_v1.types.MysqlColumn]):
            MySQL columns in the database.
            When unspecified as part of include/exclude
            lists, includes/excludes everything.
    """

    table = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_columns = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MysqlColumn",
    )


class MysqlDatabase(proto.Message):
    r"""MySQL database.

    Attributes:
        database (str):
            Database name.
        mysql_tables (Sequence[google.cloud.datastream_v1.types.MysqlTable]):
            Tables in the database.
    """

    database = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_tables = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MysqlTable",
    )


class MysqlRdbms(proto.Message):
    r"""MySQL database structure

    Attributes:
        mysql_databases (Sequence[google.cloud.datastream_v1.types.MysqlDatabase]):
            Mysql databases on the server
    """

    mysql_databases = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MysqlDatabase",
    )


class MysqlSourceConfig(proto.Message):
    r"""MySQL source configuration

    Attributes:
        include_objects (google.cloud.datastream_v1.types.MysqlRdbms):
            MySQL objects to retrieve from the source.
        exclude_objects (google.cloud.datastream_v1.types.MysqlRdbms):
            MySQL objects to exclude from the stream.
    """

    include_objects = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MysqlRdbms",
    )
    exclude_objects = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MysqlRdbms",
    )


class SourceConfig(proto.Message):
    r"""The configuration of the stream source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_connection_profile (str):
            Required. Source connection profile resoource. Format:
            ``projects/{project}/locations/{location}/connectionProfiles/{name}``
        oracle_source_config (google.cloud.datastream_v1.types.OracleSourceConfig):
            Oracle data source configuration

            This field is a member of `oneof`_ ``source_stream_config``.
        mysql_source_config (google.cloud.datastream_v1.types.MysqlSourceConfig):
            MySQL data source configuration

            This field is a member of `oneof`_ ``source_stream_config``.
    """

    source_connection_profile = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_source_config = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="source_stream_config",
        message="OracleSourceConfig",
    )
    mysql_source_config = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="source_stream_config",
        message="MysqlSourceConfig",
    )


class AvroFileFormat(proto.Message):
    r"""AVRO file format configuration."""


class JsonFileFormat(proto.Message):
    r"""JSON file format configuration.

    Attributes:
        schema_file_format (google.cloud.datastream_v1.types.JsonFileFormat.SchemaFileFormat):
            The schema file format along JSON data files.
        compression (google.cloud.datastream_v1.types.JsonFileFormat.JsonCompression):
            Compression of the loaded JSON file.
    """

    class SchemaFileFormat(proto.Enum):
        r"""Schema file format."""
        SCHEMA_FILE_FORMAT_UNSPECIFIED = 0
        NO_SCHEMA_FILE = 1
        AVRO_SCHEMA_FILE = 2

    class JsonCompression(proto.Enum):
        r"""Json file compression."""
        JSON_COMPRESSION_UNSPECIFIED = 0
        NO_COMPRESSION = 1
        GZIP = 2

    schema_file_format = proto.Field(
        proto.ENUM,
        number=1,
        enum=SchemaFileFormat,
    )
    compression = proto.Field(
        proto.ENUM,
        number=2,
        enum=JsonCompression,
    )


class GcsDestinationConfig(proto.Message):
    r"""Google Cloud Storage destination configuration

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        path (str):
            Path inside the Cloud Storage bucket to write
            data to.
        file_rotation_mb (int):
            The maximum file size to be saved in the
            bucket.
        file_rotation_interval (google.protobuf.duration_pb2.Duration):
            The maximum duration for which new events are
            added before a file is closed and a new file is
            created.
        avro_file_format (google.cloud.datastream_v1.types.AvroFileFormat):
            AVRO file format configuration.

            This field is a member of `oneof`_ ``file_format``.
        json_file_format (google.cloud.datastream_v1.types.JsonFileFormat):
            JSON file format configuration.

            This field is a member of `oneof`_ ``file_format``.
    """

    path = proto.Field(
        proto.STRING,
        number=1,
    )
    file_rotation_mb = proto.Field(
        proto.INT32,
        number=2,
    )
    file_rotation_interval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    avro_file_format = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="file_format",
        message="AvroFileFormat",
    )
    json_file_format = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="file_format",
        message="JsonFileFormat",
    )


class DestinationConfig(proto.Message):
    r"""The configuration of the stream destination.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_connection_profile (str):
            Required. Destination connection profile resource. Format:
            ``projects/{project}/locations/{location}/connectionProfiles/{name}``
        gcs_destination_config (google.cloud.datastream_v1.types.GcsDestinationConfig):
            A configuration for how data should be loaded
            to Cloud Storage.

            This field is a member of `oneof`_ ``destination_stream_config``.
    """

    destination_connection_profile = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_destination_config = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="destination_stream_config",
        message="GcsDestinationConfig",
    )


class Stream(proto.Message):
    r"""A resource representing streaming data from a source to a
    destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The stream's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the stream.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            stream.
        labels (Mapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        source_config (google.cloud.datastream_v1.types.SourceConfig):
            Required. Source connection profile
            configuration.
        destination_config (google.cloud.datastream_v1.types.DestinationConfig):
            Required. Destination connection profile
            configuration.
        state (google.cloud.datastream_v1.types.Stream.State):
            The state of the stream.
        backfill_all (google.cloud.datastream_v1.types.Stream.BackfillAllStrategy):
            Automatically backfill objects included in
            the stream source configuration. Specific
            objects can be excluded.

            This field is a member of `oneof`_ ``backfill_strategy``.
        backfill_none (google.cloud.datastream_v1.types.Stream.BackfillNoneStrategy):
            Do not automatically backfill any objects.

            This field is a member of `oneof`_ ``backfill_strategy``.
        errors (Sequence[google.cloud.datastream_v1.types.Error]):
            Output only. Errors on the Stream.
        customer_managed_encryption_key (str):
            Immutable. A reference to a KMS encryption
            key. If provided, it will be used to encrypt the
            data. If left blank, data will be encrypted
            using an internal Stream-specific encryption key
            provisioned through KMS.

            This field is a member of `oneof`_ ``_customer_managed_encryption_key``.
    """

    class State(proto.Enum):
        r"""Stream state."""
        STATE_UNSPECIFIED = 0
        NOT_STARTED = 1
        RUNNING = 2
        PAUSED = 3
        MAINTENANCE = 4
        FAILED = 5
        FAILED_PERMANENTLY = 6
        STARTING = 7
        DRAINING = 8

    class BackfillAllStrategy(proto.Message):
        r"""Backfill strategy to automatically backfill the Stream's
        objects. Specific objects can be excluded.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            oracle_excluded_objects (google.cloud.datastream_v1.types.OracleRdbms):
                Oracle data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            mysql_excluded_objects (google.cloud.datastream_v1.types.MysqlRdbms):
                MySQL data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
        """

        oracle_excluded_objects = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="excluded_objects",
            message="OracleRdbms",
        )
        mysql_excluded_objects = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="excluded_objects",
            message="MysqlRdbms",
        )

    class BackfillNoneStrategy(proto.Message):
        r"""Backfill strategy to disable automatic backfill for the
        Stream's objects.

        """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    source_config = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SourceConfig",
    )
    destination_config = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DestinationConfig",
    )
    state = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    backfill_all = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="backfill_strategy",
        message=BackfillAllStrategy,
    )
    backfill_none = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="backfill_strategy",
        message=BackfillNoneStrategy,
    )
    errors = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Error",
    )
    customer_managed_encryption_key = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


class StreamObject(proto.Message):
    r"""A specific stream object (e.g a specific DB table).

    Attributes:
        name (str):
            Output only. The object resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the object.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            object.
        display_name (str):
            Required. Display name.
        errors (Sequence[google.cloud.datastream_v1.types.Error]):
            Output only. Active errors on the object.
        backfill_job (google.cloud.datastream_v1.types.BackfillJob):
            The latest backfill job that was initiated
            for the stream object.
        source_object (google.cloud.datastream_v1.types.SourceObjectIdentifier):
            The object identifier in the data source.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    errors = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
    )
    backfill_job = proto.Field(
        proto.MESSAGE,
        number=7,
        message="BackfillJob",
    )
    source_object = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SourceObjectIdentifier",
    )


class SourceObjectIdentifier(proto.Message):
    r"""Represents an identifier of an object in the data source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oracle_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.OracleObjectIdentifier):
            Oracle data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        mysql_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.MysqlObjectIdentifier):
            Mysql data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
    """

    class OracleObjectIdentifier(proto.Message):
        r"""Oracle data source object identifier.

        Attributes:
            schema (str):
                Required. The schema name.
            table (str):
                Required. The table name.
        """

        schema = proto.Field(
            proto.STRING,
            number=1,
        )
        table = proto.Field(
            proto.STRING,
            number=2,
        )

    class MysqlObjectIdentifier(proto.Message):
        r"""Mysql data source object identifier.

        Attributes:
            database (str):
                Required. The database name.
            table (str):
                Required. The table name.
        """

        database = proto.Field(
            proto.STRING,
            number=1,
        )
        table = proto.Field(
            proto.STRING,
            number=2,
        )

    oracle_identifier = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source_identifier",
        message=OracleObjectIdentifier,
    )
    mysql_identifier = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source_identifier",
        message=MysqlObjectIdentifier,
    )


class BackfillJob(proto.Message):
    r"""Represents a backfill job on a specific stream object.

    Attributes:
        state (google.cloud.datastream_v1.types.BackfillJob.State):
            Backfill job state.
        trigger (google.cloud.datastream_v1.types.BackfillJob.Trigger):
            Backfill job's triggering reason.
        last_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Backfill job's start time.
        last_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Backfill job's end time.
        errors (Sequence[google.cloud.datastream_v1.types.Error]):
            Output only. Errors which caused the backfill
            job to fail.
    """

    class State(proto.Enum):
        r"""State of the stream object's backfill job."""
        STATE_UNSPECIFIED = 0
        NOT_STARTED = 1
        PENDING = 2
        ACTIVE = 3
        STOPPED = 4
        FAILED = 5
        COMPLETED = 6
        UNSUPPORTED = 7

    class Trigger(proto.Enum):
        r"""Triggering reason for a backfill job."""
        TRIGGER_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    state = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    trigger = proto.Field(
        proto.ENUM,
        number=2,
        enum=Trigger,
    )
    last_start_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_end_time = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    errors = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Error",
    )


class Error(proto.Message):
    r"""Represent a user-facing Error.

    Attributes:
        reason (str):
            A title that explains the reason for the
            error.
        error_uuid (str):
            A unique identifier for this specific error,
            allowing it to be traced throughout the system
            in logs and API responses.
        message (str):
            A message containing more information about
            the error that occurred.
        error_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the error occurred.
        details (Mapping[str, str]):
            Additional information about the error.
    """

    reason = proto.Field(
        proto.STRING,
        number=1,
    )
    error_uuid = proto.Field(
        proto.STRING,
        number=2,
    )
    message = proto.Field(
        proto.STRING,
        number=3,
    )
    error_time = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    details = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class ValidationResult(proto.Message):
    r"""Contains the current validation results.

    Attributes:
        validations (Sequence[google.cloud.datastream_v1.types.Validation]):
            A list of validations (includes both executed
            as well as not executed validations).
    """

    validations = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Validation",
    )


class Validation(proto.Message):
    r"""A validation to perform on a stream.

    Attributes:
        description (str):
            A short description of the validation.
        state (google.cloud.datastream_v1.types.Validation.State):
            Validation execution status.
        message (Sequence[google.cloud.datastream_v1.types.ValidationMessage]):
            Messages reflecting the validation results.
        code (str):
            A custom code identifying this validation.
    """

    class State(proto.Enum):
        r"""Validation execution state."""
        STATE_UNSPECIFIED = 0
        NOT_EXECUTED = 1
        FAILED = 2
        PASSED = 3

    description = proto.Field(
        proto.STRING,
        number=1,
    )
    state = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    message = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ValidationMessage",
    )
    code = proto.Field(
        proto.STRING,
        number=4,
    )


class ValidationMessage(proto.Message):
    r"""Represent user-facing validation result message.

    Attributes:
        message (str):
            The result of the validation.
        level (google.cloud.datastream_v1.types.ValidationMessage.Level):
            Message severity level (warning or error).
        metadata (Mapping[str, str]):
            Additional metadata related to the result.
        code (str):
            A custom code identifying this specific
            message.
    """

    class Level(proto.Enum):
        r"""Validation message level."""
        LEVEL_UNSPECIFIED = 0
        WARNING = 1
        ERROR = 2

    message = proto.Field(
        proto.STRING,
        number=1,
    )
    level = proto.Field(
        proto.ENUM,
        number=2,
        enum=Level,
    )
    metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    code = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
