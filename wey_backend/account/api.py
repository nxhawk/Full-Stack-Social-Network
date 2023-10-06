from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import FriendshipRequestSerializer, UserSerializer

from .forms import SignupForms
from .models import FriendshipRequest, User

@api_view(["GET"])
def me(request):
  return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
  data = request.data
  message = "success"

  form = SignupForms({
    'email': data.get('email'),
    'name': data.get('name'),
    'password1': data.get('password1'),
    'password2': data.get('password2'),    
  })

  if form.is_valid():
    form.save()
    # user = form.save()
    # user.is_active = False
    # user.save()
  else:
    message = form.errors.as_json()

  print(message)

  return JsonResponse({'message': message})

@api_view(['GET'])
def friends(request, pk):
  user = User.objects.get(pk=pk)
  requests = []

  if user == request.user:
    requests = FriendshipRequest.objects.filter(created_for=request.user, status = FriendshipRequest.SENT)
    requests = FriendshipRequestSerializer(requests, many=True)
    requests = requests.data

  friends = user.friends.all()

  return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)




@api_view(["POST"])
def send_friendship_request(request, pk):
  user = User.objects.get(pk=pk)

  check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
  check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

  if not check1 or not check2:
    friendrequest = FriendshipRequest.objects.create(created_for=user, created_by=request.user)

    return JsonResponse({'message': "friendship request created"})
  else:
    return JsonResponse({'message': 'request already sent'})


@api_view(["POST"])
def handle_request(request, pk, status):
  user = User.objects.get(pk=pk)
  friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
  friendship_request.status = status
  friendship_request.save()
  
  if status == FriendshipRequest.ACCEPTED:
    user.friends.add(request.user)
    user.friends_count = user.friends_count + 1
    user.save()

  request_user = request.user
  request_user.friends_count = request_user.friends_count + 1
  request_user.save()

  return JsonResponse({'message': "friendship request updated"})
  


