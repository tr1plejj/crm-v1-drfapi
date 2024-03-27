from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


class ProductsListApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        output = [{'id': output.id, 'user': output.user_id, 'title': output.title, 'description': output.description,
                   'price': output.price} for output in Product.objects.filter(user=self.request.user)]
        return Response(output)

    def post(self, request):
        serializer = ProductSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(serializer.data)


class ProductGetApi(APIView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        output = {'id': product.id, 'user': product.user_id, 'title': product.title, 'description': product.description, 'price': product.price}
        return Response(output)


# i am not deleting some products right now
# class ProductDeleteApi(APIView):
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#
#     def delete(self, request, pk):
#         Product.objects.get(pk=pk, user=self.request.user).delete()
#         return Response('200')


class OrderCreateApi(APIView):

    def post(self, request):
        serializer = OrderSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            user_id = serializer.validated_data.get('user')
            serializer.save(user=user_id)
            return Response(serializer.data)


class UserOrdersListApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        output = [{'id': output.id, 'user': output.user_id, 'product': output.product_id,
                   'buyer_id': output.buyer_id, 'address': output.address} for output in Order.objects.filter(user=self.request.user)]
        return Response(output)


class OrderApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, pk):
        order = Order.objects.get(pk=pk, user=self.request.user)
        output = {'id': order.id, 'user': order.user_id, 'product': order.product_id, 'buyer_id': order.buyer_id}
        return Response(output)

    def delete(self, request, pk):
        Order.objects.get(pk=pk, user=self.request.user).delete()
        return Response('200')
