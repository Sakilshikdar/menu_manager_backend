from rest_framework import serializers

from .models import  Menu, Review,MenuUser, AdminCustomer

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','last_name',  'email']  
    




class AdminCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminCustomer
        fields = ['id', 'user', 'account_type','phone', 'profile_img']

        
        def __init__(self, *args, **kwargs):
            super(CustomerSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1
    



class AdminCustomerDetailSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
            response = super().to_representation(instance)
            response['user'] = UserSerializer(instance.user).data
            return response


    class Meta:
        model = AdminCustomer
        fields = ['id', 'user', 'phone', 'account_type','profile_img']


    def __init__(self, *args, **kwargs):
        super(AdminCustomerDetailSerializer, self).__init__(*args, **kwargs)


class MenuSerializer(serializers.ModelSerializer):
    menu_ratings = serializers.StringRelatedField(

        many=True, read_only=True)

    class Meta:

        model = Menu

        fields = ['id','customer','description','slug' ,'image','title', 'cook', 'published_date', 'price','menu_ratings']



        #


class MenuDetailSerializer(serializers.ModelSerializer):

    menu_ratings = serializers.StringRelatedField(

        many=True, read_only=True)

    class Meta:

        many=True

        model = Menu

        fields = ['id','customer','description' ,'image','slug','title', 'cook', 'published_date', 'price','menu_ratings']


    def __init__(self, *args, **kwargs):

            super(MenuDetailSerializer, self).__init__(*args, **kwargs)

            self.Meta.depth = 1


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review

        fields = ['id', 'customer','menu', 'rating', 'comment', 'created_date']




class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review

        fields = ['id', 'customer','menu', 'rating', 'comment', 'created_date']

    

        def to_representation(self, instance):
            response = super().to_representation(instance)

            response['customer'] = CustomerSerializer(instance.customer).data

            response['menu'] = MenuSerializer(instance.menu).data
            return response


