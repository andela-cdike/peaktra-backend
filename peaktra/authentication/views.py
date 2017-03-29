from rest_framework.views import APIView
from rest_framework.response import Response


class ProtectedView(APIView):
    '''Dummy view to confirm only users with token have access'''

    def get(self, request, **kwargs):
        return Response({'message': 'YOU ARE GOOD. HALLELUJAH! YOU ARE GOOD!'})
