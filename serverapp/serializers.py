from django_grpc_framework import proto_serializers
from rest_framework import serializers
from serverapp.models import Penduduk, NIK
from serverapp_proto import penduduk_pb2

class PendudukProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Penduduk
        proto_class = penduduk_pb2.Penduduk
        fields = '__all__'

    def validate(self, attrs):
        cek_nik = NIK.objects.filter(nik=attrs["nik_pelapor"])
        if cek_nik:
            return attrs
        else:
            return proto_serializers.ValidationError()

