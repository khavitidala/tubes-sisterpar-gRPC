import grpc
import random
from datetime import datetime
from django_grpc_framework.services import Service
from serverapp.models import Penduduk
from serverapp.serializers import PendudukProtoSerializer

class PendudukService(Service):
    def Create(self, request, context):
        random.seed()
        nama = ["Ryan", "Azriel", "Faiz"]
        rnama = random.randint(0, 2)
        jml = random.randint(1, 10)
        tmp = datetime.now()
        tgl = str(tmp.day)+"-"+str(tmp.month)+"-"+str(tmp.year)+", "+str(tmp.hour+3)+":"+"00"
        serializer = PendudukProtoSerializer(message=request)
        #try:
        serializer.is_valid(raise_exception=True)
        serializer.save(nama_petugas=nama[rnama], tgl_jemput=tgl, jumlah=jml)
        return serializer.message
        #except:
            #self.context.abort(grpc.StatusCode.NOT_FOUND, 'NIK tidak valid!')

    #def Destroy(self, request, context)
        #post = self.get_object(request.id)


