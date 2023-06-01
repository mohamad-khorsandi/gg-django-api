from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import GardenSerializer, GardenUpdateSerializer, GardenCreateSerializer, GardenByIDSerializer
from accounts.models import GardenOwnerProfile
from .models import Garden
from .permissions import GardenOwnerPerm
from scores.serializers import ScoreAddSerializer


class GardenGetIDAPI(RetrieveAPIView):
    serializer_class = GardenByIDSerializer
    permission_classes = [AllowAny]
    queryset = Garden.objects.filter(is_verified=True)
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context


class GardenAPI(RetrieveAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated, GardenOwnerPerm]

    def get_object(self):
        user = GardenOwnerProfile.objects.filter(user=self.request.user)[0]
        garden = user.garden
        return garden


class GardenUpdateAPI(UpdateAPIView):
    serializer_class = GardenUpdateSerializer
    permission_classes = [IsAuthenticated, GardenOwnerPerm]

    def get_object(self):
        user = GardenOwnerProfile.objects.filter(user=self.request.user)[0]
        garden = user.garden
        return garden

    def update(self, request, *args, **kwargs):
        garden = self.get_object()
        garden.is_verified = False
        garden.save()
        serializer = self.get_serializer(garden, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GardenCreateAPI(CreateAPIView):
    serializer_class = GardenCreateSerializer
    permission_classes = [IsAuthenticated, GardenOwnerPerm]

    def get_object(self):
        try:
            user = GardenOwnerProfile.objects.filter(user=self.request.user)[0]
            garden = user.garden
            return garden
        except Exception as e:
            print(repr(e))
            return None

    def create(self, request, *args, **kwargs):
        garden = self.get_object()
        data = request.data
        if garden is None:
            data['garden_owner'] = request.user.id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(data=data, status=status.HTTP_201_CREATED)

        data = self.get_serializer(garden).data
        return Response(data=data, status=status.HTTP_403_FORBIDDEN)


class GardenDeleteAPI(DestroyAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated, GardenOwnerPerm]

    def get_object(self):
        user = GardenOwnerProfile.objects.filter(user=self.request.user)[0]
        garden = user.garden
        return garden


class GardenAddScoreAPI(CreateAPIView):
    serializer_class = ScoreAddSerializer
    permission_classes = [IsAuthenticated]
    queryset = Garden.objects.all()
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        garden = self.get_object()
        data = request.data
        if garden is not None:
            data['user'] = request.user.id
            data['garden'] = kwargs['id']
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(data=data, status=status.HTTP_201_CREATED)

        data = self.get_serializer(data).data
        return Response(data=data, status=status.HTTP_403_FORBIDDEN)



