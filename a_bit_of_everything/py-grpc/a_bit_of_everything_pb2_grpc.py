# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import a_bit_of_everything_pb2 as a__bit__of__everything__pb2
from examples.sub import message_pb2 as examples_dot_sub_dot_message__pb2
from examples.sub2 import message_pb2 as examples_dot_sub2_dot_message__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ABitOfEverythingServiceStub(object):
  """ABitOfEverything service is used to validate that APIs with complicated
  proto messages and URL templates are still processed correctly.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Create',
        request_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
        response_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
        )
    self.CreateBody = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/CreateBody',
        request_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
        response_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
        )
    self.Lookup = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Lookup',
        request_serializer=examples_dot_sub2_dot_message__pb2.IdMessage.SerializeToString,
        response_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
        )
    self.Update = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Update',
        request_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Delete',
        request_serializer=examples_dot_sub2_dot_message__pb2.IdMessage.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetQuery = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/GetQuery',
        request_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Echo = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Echo',
        request_serializer=examples_dot_sub_dot_message__pb2.StringMessage.SerializeToString,
        response_deserializer=examples_dot_sub_dot_message__pb2.StringMessage.FromString,
        )
    self.DeepPathEcho = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/DeepPathEcho',
        request_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
        response_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
        )
    self.NoBindings = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/NoBindings',
        request_serializer=google_dot_protobuf_dot_duration__pb2.Duration.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Timeout = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/Timeout',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ErrorWithDetails = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/ErrorWithDetails',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetMessageWithBody = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/GetMessageWithBody',
        request_serializer=a__bit__of__everything__pb2.MessageWithBody.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.PostWithEmptyBody = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.ABitOfEverythingService/PostWithEmptyBody',
        request_serializer=a__bit__of__everything__pb2.Body.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ABitOfEverythingServiceServicer(object):
  """ABitOfEverything service is used to validate that APIs with complicated
  proto messages and URL templates are still processed correctly.
  """

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateBody(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Lookup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Echo(self, request, context):
    """Echo allows posting a StringMessage value.

    It also exposes multiple bindings.

    This makes it useful when validating that the OpenAPI v2 API
    description exposes documentation correctly on all paths
    defined as additional_bindings in the proto.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeepPathEcho(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NoBindings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Timeout(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ErrorWithDetails(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMessageWithBody(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostWithEmptyBody(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ABitOfEverythingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
          response_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
      ),
      'CreateBody': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBody,
          request_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
          response_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
      ),
      'Lookup': grpc.unary_unary_rpc_method_handler(
          servicer.Lookup,
          request_deserializer=examples_dot_sub2_dot_message__pb2.IdMessage.FromString,
          response_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=examples_dot_sub2_dot_message__pb2.IdMessage.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetQuery': grpc.unary_unary_rpc_method_handler(
          servicer.GetQuery,
          request_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=examples_dot_sub_dot_message__pb2.StringMessage.FromString,
          response_serializer=examples_dot_sub_dot_message__pb2.StringMessage.SerializeToString,
      ),
      'DeepPathEcho': grpc.unary_unary_rpc_method_handler(
          servicer.DeepPathEcho,
          request_deserializer=a__bit__of__everything__pb2.ABitOfEverything.FromString,
          response_serializer=a__bit__of__everything__pb2.ABitOfEverything.SerializeToString,
      ),
      'NoBindings': grpc.unary_unary_rpc_method_handler(
          servicer.NoBindings,
          request_deserializer=google_dot_protobuf_dot_duration__pb2.Duration.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Timeout': grpc.unary_unary_rpc_method_handler(
          servicer.Timeout,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ErrorWithDetails': grpc.unary_unary_rpc_method_handler(
          servicer.ErrorWithDetails,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetMessageWithBody': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessageWithBody,
          request_deserializer=a__bit__of__everything__pb2.MessageWithBody.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'PostWithEmptyBody': grpc.unary_unary_rpc_method_handler(
          servicer.PostWithEmptyBody,
          request_deserializer=a__bit__of__everything__pb2.Body.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.gateway.examples.examplepb.ABitOfEverythingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class camelCaseServiceNameStub(object):
  """camelCase and lowercase service names are valid but not recommended (use TitleCase instead)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Empty = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.camelCaseServiceName/Empty',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class camelCaseServiceNameServicer(object):
  """camelCase and lowercase service names are valid but not recommended (use TitleCase instead)
  """

  def Empty(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_camelCaseServiceNameServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Empty': grpc.unary_unary_rpc_method_handler(
          servicer.Empty,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.gateway.examples.examplepb.camelCaseServiceName', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AnotherServiceWithNoBindingsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NoBindings = channel.unary_unary(
        '/grpc.gateway.examples.examplepb.AnotherServiceWithNoBindings/NoBindings',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AnotherServiceWithNoBindingsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NoBindings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AnotherServiceWithNoBindingsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NoBindings': grpc.unary_unary_rpc_method_handler(
          servicer.NoBindings,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.gateway.examples.examplepb.AnotherServiceWithNoBindings', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
