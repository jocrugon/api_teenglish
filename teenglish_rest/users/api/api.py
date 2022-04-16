from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from users.models import User
from users.api.serializers import UserSerializer


@api_view(['GET','POST'])
def user_api_view(request):

    #list
    if request.method == 'GET':
        #queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    #create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)

        #validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'usuario creado correctamente'})
        return Response(user_serializer.errors)