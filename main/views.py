
from .models import Menu, Review,MenuUser, AdminCustomer
from .serializers import MenuSerializer, ReviewSerializer, UserSerializer,ReviewDetailSerializer,MenuDetailSerializer,AdminCustomerDetailSerializer
from  django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from rest_framework import viewsets,generics




@csrf_exempt
def admincustomer_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')


    email = request.POST.get('email')


    username = request.POST.get('username')


    password = request.POST.get('password')


    mobile = request.POST.get('mobile')

    account_type = request.POST.get('account_type')



    try:


        # Create a new user


        user = User.objects.create_user(


            username=username, email=email, password=password, first_name=first_name, last_name=last_name)


        if user:


            try:

                customer = AdminCustomer.objects.create(user=user, phone=mobile, account_type=account_type)


                msg = {


                    'bool': True,


                    'user': user.id,


                    'customer': customer.id,


                    'msg': 'You have successfully registered.You can now login.'


                }


            except:


                msg = {


                    'bool': False,


                    'msg': 'mobile already exists'


                }


        else:


            msg = {


                'bool': False,


                'msg': 'Oops! Something went wrong. Please try again later.'


            }


    except IntegrityError:


        msg = {


            'bool': False,


            'msg': 'username already exist'


        }


    return JsonResponse(msg)




    first_name = request.POST.get('first_name')


    last_name = request.POST.get('last_name')


    email = request.POST.get('email')


    username = request.POST.get('username')


    password = request.POST.get('password')


    mobile = request.POST.get('mobile')

    account_type = request.POST.get('account_type')



    try:


        # Create a new user


        user = User.objects.create_user(


            username=username, email=email, password=password, first_name=first_name, last_name=last_name)


        if user:
            try:
                customer = AdminCustomer.objects.create(user=user, phone=mobile, account_type=account_type)
                msg = {

                    'bool': True,
                    'user': user.id,
                    'customer': customer.id,
                    'msg': 'You have successfully registered. You can now login.'
                }
            except IntegrityError:
                msg = {
                    'bool': False,
                    'msg': 'Mobile already exists'
                }
        else:
            msg = {
                'bool': False,
                'msg': 'Oops! Something went wrong. Please try again later.'
            }
    except IntegrityError:
        msg = {
            'bool': False,
            'msg': 'Username already exists'
        }
    return JsonResponse(msg)



@csrf_exempt
def admincustomer_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
        customer = AdminCustomer.objects.get(user=user)
        msg = {
            'bool': True,
            'user': user.username,
            'id': customer.id,
        }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid username or password'
        }
    return JsonResponse(msg)





@csrf_exempt
def AdminCustomerChangePassword(request, pk):
    password = request.POST.get('password')
    customer = AdminCustomer.objects.get(id=pk)
    user = customer.user
    user.password = make_password(password)
    user.save()
    msg = {
        'bool': True,
        'msg': 'Password changed successfully'

    }
    return JsonResponse(msg)





class AdminCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminCustomer.objects.all()
    serializer_class = AdminCustomerDetailSerializer




class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class MenuUserViewSet(generics.ListCreateAPIView):
    queryset = MenuUser.objects.all()
    serializer_class = UserSerializer
   



class MenuViewSet(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuListViewSet(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer = self.kwargs['pk']
        qs = qs.filter(customer__id=customer)
        return qs




class MenuDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = MenuDetailSerializer
    def get_queryset(self):
        menu_id = self.kwargs['pk']
        return Menu.objects.filter(id=menu_id)



class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ReviewDetailViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        menu_id = self.kwargs['pk']
        qs = qs.filter(menu__id=menu_id)
        return qs




class ReviewDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    def get_queryset(self):
        review_id = self.kwargs['pk']
        return Review.objects.filter(id=review_id)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = MenuUser.objects.all()
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user




class MenuListandViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuReviewListandViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


