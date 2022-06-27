from rest_framework import views, generics, response, permissions, status

from address.models import Address
from .serializers import AddressSerializers


class GetUserAddress(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            address_qs = Address.objects.filter(user=user).first()
            if address_qs:
                serializer = AddressSerializers(address_qs)
                return response.Response({'user_address': serializer.data, 'user_have_address': True})
            else:
                return response.Response({'user_have_address': False})
        else:
            return response.Response({
                "msg": "auth error"
            }, status=status.HTTP_401_UNAUTHORIZED)


class CreateAddressApiView(generics.ListCreateAPIView):
    serializer_class = AddressSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        address_qs = Address.objects.filter(user=user).first()
        if address_qs:
            serializer = AddressSerializers(address_qs)
            return response.Response(serializer.data)
        return response.Response({"msg": "Not found"})

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        print(data)
        serializer = AddressSerializers(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            print(serializer.data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddressEditView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AddressSerializers
    lookup_field = 'id'


class SaveLocalCoordsToDB(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            data = request.data
            print(data["lat"])
            print(data["lng"])

            address_qs = Address.objects.filter(user=user).first()
            if address_qs:
                if address_qs.lattitude == data["lat"] and address_qs.longtitude == data["lng"]:
                    return response.Response(status=status.HTTP_200_OK)
                else:
                    address_qs.lattitude = data["lat"]
                    address_qs.longtitude == data["lng"]
                    address_qs.save()
                    return response.Response(status=status.HTTP_200_OK)
            else:
                Address.objects.create(
                    user=user,
                    lattitude=data["lat"],
                    longtitude=data["lng"]
                )
                return response.Response(status=status.HTTP_200_OK)
        else:
            print('errrrrrrrrrrrrrrrrrr')
            return response.Response({"msg": "User Unauthorized"}, status=status.HTTP_400_BAD_REQUEST)
