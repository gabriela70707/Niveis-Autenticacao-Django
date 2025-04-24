from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UsuarioSerializer, ProdutoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Usuario, Produto
from .permissions import IsCliente, IsGestor, IsFuncionario #nosso permissions
from rest_framework import permissions # permissions do rest_framework
#Uma boa prática é importar somente aquilo que você vai usar para não pesar a aplicação

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    # o query set é como se fosse um select * from usuario
    serializer_class = UsuarioSerializer 
    permission_classes = [IsGestor] #classes que tem a permissão para executar essa ação

class UsuarioRetriverUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):     #get especifico put patch delete 
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 
    permission_classes = [IsGestor]
    lookup_field = 'pk' #por qual atributo voce quer procurar(no caso aqui a chave primaria que por padrao é o id)

class ProdutoListCreateAPIView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    #permissões diferentes de funcionario e gestor para cliente, por isso vamo mecher nas permissões
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        
        # se não for get vai ser post
        return [IsFuncionario()]
