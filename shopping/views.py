from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerilaizer
from rest_framework.authentication import SessionAuthentication 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .mypagination import MyPageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication



#Add Product
class AddProduct(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerilaizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
    filterset_fields=['name']
    filter_backends=[OrderingFilter]
    pagination_class=MyPageNumberPagination






#Stripe Secert Key
# stripe.api_key = settings.STRIPE_SECRET_KEY

# #Home Page
# class Home(View):
#     def get(self,request):
#        data= Product.objects.all()
#        category= Category.objects.all()
#        return  render(request,'home.html',{'products':data,'categories':category})


# #Login User Page
# class LoginUserHome(LoginRequiredMixin,View):
#     def get(self,request):
#        data= Product.objects.all()
#        category= Category.objects.all()
#        return  render(request,'login_user_home.html',{'products':data,'categories':category})


# #Registration Form
# class Signup(View):

#     def post(self,request):
#         form = SignUp(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             email = form.cleaned_data["email"]
#             contact = form.cleaned_data["contact"]
#             address = form.cleaned_data["address"]
#             password = form.cleaned_data["password"]

#             # Check if a user with this email already exists
#             if AppUser.objects.filter(email=email).exists():
#                 return render(request, "signup.html", {"form": form, "error": "Email already exists"})
#             print('AFTER FILTER CONDITION')

#             user=User.objects.create(
#                 username=username,
#                 password=make_password(password),
#                 email=email,
#             )
            
#             # Create a new AppUser instance
#             AppUser.objects.create(
#                 user=user,
#                 username=username,
#                 email=email,
#                 contact=contact,
#                 address=address,
#             )
#             print('AFTER APPUser Creation')
#             subject='Welcome on shoppinglyx'
#             message=f"Hi,{user.username} thank you for joining india's best service provider group"
#             email_from=settings.EMAIL_HOST_USER
#             recepient_list=  [user.email]
#             send_mail(subject, message ,email_from ,recepient_list)
 
#             return redirect("user_login")

#         else:
#             return render(request,'signup.html',{"form": form ,"error":'Please correct the errors below.'})

#     def get(self ,request):
#         form=SignUp
#         return render(request,'signup.html',{'form':form})

# #Login 
# class UserLogin(View):

#     def post(self ,request):
#         form = CustomLoginForm()
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         data = Product.objects.all()
#         if user:
#             print("user authenticte successfully ")
#             auth_login(request, user)
#             #Welcome message on every time when user login
#             subject='Welcome on shoppinglyx'
#             message=f"Hi {username} Welcome to shoppinglyx"
#             email_from=settings.EMAIL_HOST_USER
#             recepient_list=  [request.user.appuser.email]
#             send_mail(subject, message ,email_from ,recepient_list)
#             return render(request, "login_user_home.html", {"products": data})
#         else:
#             return render(request, "login.html", {"form":form , "error": "Enter Correct Details"})
    
#     def get(self ,request):
#         form = CustomLoginForm()
#         print("inside login function")
#         return render(request, "login.html", {"form": form})
    

#Show Product with description 
# class ProductDetails(View):
#     def get(self,request,product_id):
#         product = get_object_or_404(Product, id=product_id)
#         category = Category.objects.all()
#         return render(request, "product_details.html", {"product": product,'categories':category})


# #Show Products by Category
# class ProductListByCategory(View):
#     def get(self ,request, category_id):
#         category = get_object_or_404(Category, id=category_id)
#         products = Product.objects.filter(category=category)
#         categories = Category.objects.all()
#         return render(request,"product_list.html",{"category": category, "products": products, "categories": categories})

# #Show user profile
# class UserProfile(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request):
#         try:
#             username1 = request.user.appuser
#             print("User is:", username1)
#             app_user = AppUser.objects.get(username=username1)
#             category = Category.objects.all()
#             return render(request, "user_profile.html", {"app_user": app_user ,'categories':category})
#         except:
#             return render(request, "user_profile.html", {"error": "Not Exists"})

# #Update User Profile
# class UpdateProfile(LoginRequiredMixin,View):
#         login_url='user_login'
#         def post(self,request):
#             username = request.POST.get("username")
#             contact = request.POST.get("contact")
#             address = request.POST.get("address")
#             email = request.POST.get("email")
#             print("Email is:", email)
#             update_data = AppUser.objects.get(email=email)
#             print("Update data :", update_data)
#             update_data.username = username
#             update_data.contact = contact
#             update_data.address = address
#             update_data.save()

#             user_model_data = User.objects.get(email=email)
#             user_model_data.username = username
#             user_model_data.save()

#             return redirect("user_profile")

#         def get(self ,request):
#             username = request.user
#             app_user = AppUser.objects.get(username=username)
#             category = Category.objects.all()
#             return render(request, "update_profile.html", {"app_user": app_user,'categories':category})


# # View Cart
# class ViewCart(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self ,request):
#         app_user = request.user.appuser
#         print("User inside view_Cart:", app_user)   
#         cart_items = CartItem.objects.filter(user=app_user)
#         category = Category.objects.all()
#         print("Catt_Item:", cart_items)
#         total_price = sum(item.product.price * item.quantity for item in cart_items)
#         return render(request, "view_cart.html",{"cart_items": cart_items, "total_price": total_price ,'categories':category})


# # Add to cart
# class AddToCart(LoginRequiredMixin ,View):
#     login_url='user_login'
#     def get(self,request, product_id):
#         user = request.user
#         product = get_object_or_404(Product, id=product_id)
#         # import pdb; pdb.set_trace()
#         app_user = AppUser.objects.filter(email=user.email).first()
#         print("Product is:", product)
#         cart_item, created = CartItem.objects.get_or_create(product=product, user=app_user)

#         if not created:
#             cart_item.quantity += 1
#         else:
#             cart_item.quantity = 1

#         cart_item.save()
#         return redirect("view_cart")


# # Remove Items from Cart
# class RemoveItems(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request, item_id):
#         try:
#             app_user = AppUser.objects.get(user=request.user)
#             print('APP_USER:',app_user)
#             cart_item = CartItem.objects.get(user=app_user, product_id=item_id)
#             print('CART_Item is:',cart_item)
#             cart_item.delete()
#             print('CartItem deleted successfully')  # Debugging line
#         except AppUser.DoesNotExist:
#             print('AppUser does not exist')  # Debugging line
#             return redirect("user_login")
#         except CartItem.DoesNotExist:
#             print('CartItem does not exist')  # Debugging line
#             return redirect("view_cart")
   
#         return redirect("view_cart")


# #Delete User Account
# class DeleteAccount(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self, request):
#         try:
#             print("inside try block")
#             user = request.user
#             app_user = AppUser.objects.get(username=user)
#             user.delete()
#             app_user.delete()
#             return redirect("logout_view")
#         except AppUser.DoesNotExist:
#             print("AppUser does not exist")
#             return redirect("login_user_home")
#         except Exception as e:
#             print("An error occurred: ", e)
#             return redirect("login_user_home")
    
# #Show Products based on filter
# class ShowProduct(View):
#     def get(self, request):
#         query=request.GET.get('search')
#         category = Category.objects.all()
#         print('Data Filter is:',query)
#         if query:
#             filter_data=Product.objects.filter(name__icontains=query)
#         else:
#             filter_data=Product.objects.all()
#         return render(request ,'filter_data.html',{'filter_data':filter_data ,'query':query ,'categories':category})
    

# #Buy Product
# class BuyNow(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request,product_id):
#         product =get_object_or_404(Product,id=product_id)
#         print("Product Id is:",product_id)
#         print('ProductL:',product)
#         app_user =  request.user.appuser
#         address=app_user.address
#         print('Address:',address)   
#         total_amount=product.price 
#         print('Total Amount:',total_amount)
#         shipping_amount=70
#         total_amount+= shipping_amount
#         return render(request, 'buy_now.html', {
#             'product': product,
#             'total_amount': total_amount,
#             'shipping_amount': shipping_amount,
#             'address':  address
#         })

# #Confirm Order
# class ConfirmOrder(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request ,product_id):
#         product =get_object_or_404(Product,id=product_id)
#         total_amount=product.price 
#         print('Total Amount:',total_amount)
#         shipping_amount=70
#         total_amount+= shipping_amount
#         return render(request ,'order_done.html',{'product':product ,'total_amount':total_amount})

# #Payment Getway
# class OrderDone(LoginRequiredMixin, View):
#     def post(self, request, product_id=None):
#         try:
#             if product_id:  # If product_id is provided
#                 product = get_object_or_404(Product, id=product_id)
                
#                 shipping_amount = 70
#                 OrderItem.objects.create(
#                     user=request.user.appuser,
#                     product=product,
#                     quantity=1,
#                     price=product.price,
#                 )
                
#                 # Create a Stripe Checkout Session
#                 session = stripe.checkout.Session.create(
#                     payment_method_types=['card'],
#                     line_items=[{
#                         'price_data': {
#                             'currency': 'inr',
#                             'product_data': {
#                                 'name': product.name,
#                             },
#                             'unit_amount': int(product.price * 100) + (shipping_amount * 100),
#                         },
#                         'quantity': 1,
#                     }],
#                     mode='payment',
#                     success_url=request.build_absolute_uri('/payment_success/'),
#                     cancel_url=request.build_absolute_uri('/payment_cancel/'),
#                 )
#                 return redirect(session.url, code=303)

#             else:  # Process all cart items
#                 items = CartItem.objects.filter(user=request.user.appuser)
#                 line_items = []
#                 shipping_amount = 70
#                 for item in items:
#                     OrderItem.objects.create(
#                         user=request.user.appuser,
#                         product=item.product,
#                         quantity=item.quantity,
#                         price=item.product.price,
#                     )
                    
#                     line_items.append({
#                         'price_data': {
#                             'currency': 'inr',
#                             'product_data': {
#                                 'name': item.product.name,
#                             },
#                             'unit_amount': int(item.product.price * 100) + (shipping_amount * 100),
#                         },
#                         'quantity': item.quantity,
#                     })

#                 # Create a Stripe Checkout Session with all cart items
#                 session = stripe.checkout.Session.create(
#                     payment_method_types=['card'],
#                     line_items=line_items,
#                     mode='payment',
#                     success_url=request.build_absolute_uri('/payment_success/'),
#                     cancel_url=request.build_absolute_uri('/payment_cancel/'),
#                 )
#                 return redirect(session.url, code=303)

#         except stripe.error.StripeError as e:
#             return JsonResponse({'error': f'Stripe error: {str(e)}'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': f'Error: {str(e)}'}, status=500)


# #Order Detail
# class OrderSummary(LoginRequiredMixin ,View):
#     login_url='user_login'
#     def get(self,request):
#         return render(request,'order_summary.html')

# #Payment Success
# class PaymentSuccess(LoginRequiredMixin ,View):
#     login_url='user_login'
#     def get(self,request):
#         # Handle successful payment here, like updating order status
#         app_user=request.user.appuser.email
#         print('Email :',app_user)
#         subject ='Order Successful'
#         message= '''Thank you for order please visit again..... ,have a nice day'''
#         email_from= settings.EMAIL_HOST_USER
#         recepient_list= [app_user]
#         send_mail(subject ,message ,email_from ,recepient_list)
#         category = Category.objects.all()
#         return render(request ,'order_summary.html',{'categories':category})

# #Payment Cancel
# class PaymentCancel(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request):
#         # Handle payment cancellation here
#         return redirect('login_user_home')


# #Show Order History
# class ShowOrderList(LoginRequiredMixin ,View):
#     login_url='user_login'
#     def get(self,request):
#         app_user=request.user.appuser
#         order_details=OrderItem.objects.filter(user=app_user) 
#         print('OrderItems :',order_details)
#         category = Category.objects.all()        
#         return render(request,'show_order_list.html',{'orders':order_details,'categories':category})

# #Cancel Order
# class CancelOrder(LoginRequiredMixin ,View):
#     login_url='user_login'
#     def get(self,request ,product_id):
#         order=get_object_or_404(OrderItem ,id =product_id)
#         order.delete()
#         return redirect('show_order_list')



# #Logout
# class Logout(LoginRequiredMixin,View):
#     login_url='user_login'
#     def get(self,request):
#         logout(request)
#         return redirect("home")
