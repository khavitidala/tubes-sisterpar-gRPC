from serverapp.services import PendudukService
from serverapp_proto import penduduk_pb2_grpc

def grpc_handlers(server):
    penduduk_pb2_grpc.add_PendudukControllerServicer_to_server(PendudukService.as_servicer(), server)
