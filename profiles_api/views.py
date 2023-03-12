from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions



class HelloApiView(APIView):
    """ Test API View """

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """ Returns a list of API View features """
        an_apiview=[
            'Uses HTTP methods as function (get , post , patch , delete )',
            'Is similar to a traditional Django View ',
            'Gives you the most control over your application logic ',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,pk=None):
        """Handle updating an object """

        return Response({'message':'PUT'})


    def patch(self ,request,pk=None):
        """Handle a patial update of an object"""
        return Response({'message':'PATCH'})


    def delete(self ,request,pk=None):
        """Delete an object """
        return Response({'message':'DELETE'})




class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset """
    serializer_class=serializers.HelloSerializer

    def list(self ,request):
        """Return a hello message"""

        a_viewset=[
            'Uses Actions (list ,create , retrieve , update , partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code '

        ]

        return Response({'message':'Hello ! ','a_viewset':a_viewset})



    def create(self,request):
        """Create a hello message """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})


        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self ,request,pk=None):
        """Handle getting an object by Its ID"""
        return Response({'HTTP_methode':'GET'})


    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'HTTP_mthode':'PUT'})


    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'HTTP_methode':'PATCH'})


    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'HTTP_mthode':'DELETE'})




class UserProfilesViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
