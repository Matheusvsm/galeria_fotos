from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Foto, Comentario
from .api.serializers import UsuarioSerializer, FotoSerializer, ComentarioSerializer

class UsuarioView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FotoListView(APIView):
    def get(self, request):
        fotos = Foto.objects.all()
        serializer = FotoSerializer(fotos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FotoDetailView(APIView):
    def get_object(self, pk):
        try:
            return Foto.objects.get(pk=pk)
        except Foto.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        foto = self.get_object(pk)
        serializer = FotoSerializer(foto)
        return Response(serializer.data)

    def put(self, request, pk):
        foto = self.get_object(pk)
        serializer = FotoSerializer(foto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        foto = self.get_object(pk)
        foto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FotoAprovacaoView(APIView):
    def put(self, request, pk):
        foto = Foto.objects.get(pk=pk)
        # Verifique a autoridade do amigo e cônjuge aqui
        # Se aprovado, atualize o campo 'aprovada' da foto e salve-a
        foto.aprovada = True
        foto.save()
        serializer = FotoSerializer(foto)
        return Response(serializer.data)

class ComentarioListView(APIView):
    def get(self, request):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
