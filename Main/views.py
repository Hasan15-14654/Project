from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from . models import Product, Departments, Cart, BlogPost, Billing_Details, HomeCarousel, Delivery, Review, WishList, Coupon, Social, PaymentMethod, About, FAQ
from . forms import BillingDetailsForm, ReviewForm, CouponForm
from django.contrib.auth import authenticate
from django.utils.html import strip_tags
from django.db.models import Q
from django.contrib import messages
from django.db.models import F
from django.utils import timezone
from datetime import timedelta


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()[:12:-1]
        departments = Departments.objects.all()
        blog = BlogPost.objects.all()[0:3:-1]
        Carousel = HomeCarousel.objects.all()
        latest_product = Product.objects.all().order_by('-id')[:4]
        social = Social.objects.all()
        payment_method = PaymentMethod.objects.all()
        about = About.objects.all()
        
        wishlist = []
        if request.user.is_authenticated:
            wishlist = WishList.objects.filter(user=request.user).values_list('product', flat=True)

        # top_selling_products = Product.objects.all().order_by('-selles')[:16]
        current_date = timezone.now()
        fifteen_days_ago = current_date - timedelta(days=15)
        
        # Get top 16 trending products based on `selles` in the last 15 days
        trending_products = Product.objects.filter(updated_at__gte=fifteen_days_ago).order_by('-selles')[:8]

        context = {
            'products': products,
            'departments': departments,
            'blog':blog,
            'Carousel':Carousel,
            'latest':latest_product,
            'wishlist':wishlist,
            'top':trending_products,
            'social':social,
            'payment':payment_method,
            'about':about
        }
        return render(request, 'home.html', context) 
    

class ShopView(View):
    def get(self, request, pk=None):
        departments = Departments.objects.all()
        if pk:
        
            selected_department = get_object_or_404(Departments, pk=pk)
            products = Product.objects.filter(department=selected_department)
        else:
           
            products = Product.objects.all()
        
        context = {
            'department': departments,
            'products': products
        }
        return render(request, 'shop.html', context)



class ProductDetails(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        quantity = product.stock
        if quantity < 1:
            stoke = "Stoke out!"
        else:
            stoke = quantity

        department_description = product.department.description
        all = Product.objects.all()
        
        related_products = Product.objects.filter(department=product.department).exclude(pk=pk)

        review = Review.objects.filter(product = product)
        review_quantity = len(review)
        
        product_video = product.product_video

        product_video_embed = ""

        if product_video:  # Only proceed if there's a product_video
            product_video_embed = product_video.replace('https://youtu.be/', 'https://www.youtube.com/embed/')
            if '?si=' in product_video_embed:
                product_video_embed = product_video_embed.split('?si=')[0]  # Remove URL parameters

        context = {
            'product': product,
            'stoke': stoke,
            'rproduct': related_products,
            'department_description': department_description,
            'review': review,
            'review_quantity': review_quantity,
            'product_video_embed': product_video_embed if product_video_embed else None,  # Use None if empty
        }
        return render(request, 'product_details.html', context)



# @login_required(login_url='login')
# def AddToCart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         product_id = request.GET.get("prod_id")
#         product_quantity = int(request.GET.get("product_quantity", 1)) 
#         product = Product.objects.get(id=product_id)

       
#         try:
#             cart_item = Cart.objects.get(user=user, product=product, p_id = product_id)
#             cart_item.quantity = product_quantity
#             cart_item.save()
        
#         except Cart.DoesNotExist:
#             Cart.objects.create(user=user, product=product, quantity=product_quantity)

       
#         return redirect("/cart")
    
   
#     return redirect("/authentication/login/")

@login_required(login_url='login')
def AddToCart(request):
    user = request.user

    product_id = request.GET.get("prod_id")
    product_quantity = int(request.GET.get("product_quantity", 1))

    if not product_id:
        return redirect("/some_error_page")

    product = get_object_or_404(Product, id=product_id)

    product.selles += 1
    product.save()

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product,
        p_id=str(product_id),
        defaults={'quantity': product_quantity}
    )

    if not created:
        cart_item.quantity = product_quantity
        cart_item.save()

    return redirect("/cart")


# @login_required(login_url='login')
# def AddToCart(request):
#     user = request.user

#     product_id = request.GET.get("prod_id")
#     product_quantity = int(request.GET.get("product_quantity", 1))

#     if not product_id:
#         return redirect("/some_error_page")

#     product = get_object_or_404(Product, id=product_id)

#     cart_item, created = Cart.objects.get_or_create(
#         user=user,
#         product=product,
#         p_id=product_id,
#         defaults={'quantity': product_quantity}
#     )

#     if not created:
#         cart_item.quantity = product_quantity
#         cart_item.save()


#     return redirect("/cart")


@login_required(login_url='login')
def ShowCart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user).order_by('-id')
        
        subtotal = 0 
        cart_product = [p for p in cart] 

        if cart_product: 
            
            for p in cart_product:
                p.linetotal = p.quantity * p.product.selling_price  
                subtotal += p.linetotal  

            return render(request, "addtocart.html", {'cart': cart, 'subtotal': subtotal}
            )
        else:
            return render(request, 'addtocart.html', {'cart': cart, 'subtotal': subtotal})
        
    return redirect('/cart')

# @login_required(login_url='login')
# def ShowCart(request):
#     user = request.user
#     cart = Cart.objects.filter(user=user).order_by('-id')

#     subtotal = 0 
#     cart_product = [p for p in cart] 

#     # Calculate cart subtotal
#     if cart_product: 
#         for p in cart_product:
#             p.linetotal = p.quantity * p.product.selling_price  
#             subtotal += p.linetotal  
    
#     # Initialize discount-related variables
#     coupon = None
#     discount = 0
#     discount_amount = 0
#     total_after_discount = subtotal
    
#     if request.method == 'POST':
#         form = CouponForm(request.POST)
#         if form.is_valid():
#             coupon_code = form.cleaned_data.get('code')
#             print('Couupon code is: ', coupon_code)
#             try:
#                 coupon = Coupon.objects.get(code=coupon_code, active=True)
                
#                 # Check if the coupon is valid and applicable
#                 if coupon.is_valid() and subtotal > 0:
#                     discount = coupon.discount
#                     discount_amount = (subtotal * discount) / 100
#                     total_after_discount = subtotal - discount_amount
#                     print('total after discount: ', total_after_discount)
#                 else:
#                     coupon = None  
#             except Coupon.DoesNotExist:
#                 coupon = None 
#     else:
#         form = CouponForm()

#     context = {
#         'form':form,
#         'cart': cart,
#         'subtotal': subtotal,
#         'coupon': coupon,
#         'discount': discount,
#         'discount_amount': discount_amount,
#         'total_after_discount': total_after_discount
#     }

#     return render(request, 'addtocart.html', context)





@login_required(login_url='login')
def increase_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
        
        cart_item.quantity += 1
        cart_item.save()
        
        return redirect('showcart')  
    return redirect('login') 



@login_required(login_url='login')
def decrease_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
        
            cart_item.delete()
        
        return redirect('showcart')  
    return redirect('login') 



@login_required(login_url='login')
def delete_cart_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('showcart')
    
    

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    print('check the form')
    if request.method == 'POST':
        form = BillingDetailsForm(request.POST)

        if form.is_valid():
            print('form is valid')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            division = request.POST.get('division')
            district = request.POST.get('district')
            thana = request.POST.get('thana')
            street = request.POST.get('street')
            zip_code = request.POST.get('zip_code')
            phone = request.POST.get('phone')
            second_phone = request.POST.get('second_phone')
            email = request.POST.get('email')
            user = request.user

            for c in cart:
                product = c.product
                if product.stock >= c.quantity:                   
                    Billing_Details.objects.create(
                        user=user,
                        first_name=first_name,
                        last_name=last_name,
                        country=country,
                        division=division,
                        district=district,
                        thana=thana,
                        street=street,
                        zip_code=zip_code,
                        phone=phone,
                        second_phone=second_phone,
                        email=email,
                        product=product,
                        quantity=c.quantity,
                        p_id = c.p_id,
                    )
            
                    product.stock -= c.quantity

                    if product.stock < 1:
                        product.stock = 0  

                    product.save()                  
                    c.delete()
                    
                else:
                    
                    return render(request, 'checkouts.html', {
                        'form': form,
                        'cart': cart,
                        'error': f'Not enough stock for {product.name}. Only {product.stock} left.'
                    })
                
            return redirect('profile')

        else:

            context = {'form': form}
            return render(request, 'checkouts.html', context)

    else:
        form = BillingDetailsForm()

    context = {
        'form': form,
        'cart': cart
    }
    return render(request, 'checkouts.html', context)

# @login_required
# def checkout(request):
#     cart = Cart.objects.filter(user=request.user)
    
#     if request.method == 'POST':
#         form = BillingDetailsForm(request.POST)
        
#         if form.is_valid():
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             country = request.POST.get('country')
#             division = request.POST.get('division')
#             district = request.POST.get('district')
#             thana = request.POST.get('thana')
#             street = request.POST.get('street')
#             zip_code = request.POST.get('zip_code')
#             phone = request.POST.get('phone')
#             second_phone = request.POST.get('second_phone')
#             email = request.POST.get('email')
#             user = request.user

#             # Iterate through the cart and save billing details
#             for c in cart:
#                 product = c.product  # Get the product from the cart item
#                 if product.stock >= c.quantity:
#                     # Save billing details
#                     Billing_Details.objects.create(
#                         user=user,
#                         p_id = c.p_id,
#                         first_name=first_name,
#                         last_name=last_name,
#                         country=country,
#                         division=division,
#                         district=district,
#                         thana=thana,
#                         street=street,
#                         zip_code=zip_code,
#                         phone=phone,
#                         second_phone=second_phone,
#                         email=email,
#                         product=product,
#                         quantity=c.quantity,
#                     )

#                     # Decrease product stock
#                     product.stock -= c.quantity

#                     # If stock is below 1, set stock to 0 and optionally mark product as "out of stock"
#                     if product.stock < 1:
#                         product.stock = 0  # Set stock to 0 if it's less than 1

#                     product.save()  # Save the updated product stock

#                     # Remove the item from the cart after placing the order
#                     c.delete()

#                 else:
#                     # Handle insufficient stock, show an error message (optional)
#                     return render(request, 'checkout.html', {
#                         'form': form,
#                         'cart': cart,
#                         'error': f'Not enough stock for {product.name}. Only {product.stock} left.'
#                     })

#             # After processing all items, redirect to home
#             return redirect('home')

#         else:
#             # Handle form errors
#             context = {'form': form}
#             return render(request, 'checkout.html', context)

#     else:
#         form = BillingDetailsForm()

#     context = {
#         'form': form,
#         'cart': cart
#     }
#     return render(request, 'checkout.html', context)


# def OrderView(request):
#     order = Billing_Details.objects.filter(user=request.user)
#     order_product = [p for p in order]
#     total = len(order)
#     subtotal = 0  # Initialize the subtotal variable

#     for p in order_product:
#         if p.product:  # Check if product exists before calculating
#             p.linetotal = p.quantity * p.product.discount_price  # Calculate line total
#             subtotal += p.linetotal  # Add to subtotal
#     address = f"{order.first().street}, {order.first().thana}, {order.first().district}, {order.first().division}, {order.first().country}"
#     context = {
#         'order': order,
#         'subtotal': subtotal,
#         'address': address,
#         'total':total
#     }
#     return render(request, 'order.html', context)


def OrderView(request):
    orders = Billing_Details.objects.filter(user=request.user)
    total = orders.count()
    subtotal = 0 

    for order in orders:
        if order.product:
            order.linetotal = order.quantity * order.product.discount_price
            subtotal += order.linetotal  # Add to subtotal

    # Check if there are orders before attempting to access their attributes
    if orders.exists():
        address = f"{orders.first().street}, {orders.first().thana}, {orders.first().district}, {orders.first().division}, {orders.first().country}"
    else:
        address = ""

    context = {
        'order': orders,
        'subtotal': subtotal,
        'address': address,
        'total': total
    }
    return render(request, 'order.html', context)



def DeliveryView(request, order_id):

    order = get_object_or_404(Billing_Details, id=order_id, user=request.user)

    # Create a new Delivery record
    Delivery.objects.create(
        user=order.user,
        p_id = order.p_id,
        first_name=order.first_name,
        last_name=order.last_name,
        product=order.product,
        quantity=order.quantity,
        country=order.country,
        division=order.division,
        district=order.district,
        thana=order.thana,
        street=order.street,
        zip_code=order.zip_code,
        phone=order.phone,
        order_note=order.order_note,
        datetime=order.datetime,
        second_phone=order.second_phone,
        email=order.email
    )
    order.delete()

    return redirect('order')


#for history product
def Purchase(request):
    user = request.user
    purchase = Delivery.objects.filter(user=user).order_by('-id')  # Filter purchases by user

    # Initialize subtotal
    subtotal = 0

    # Iterate through purchases and calculate subtotal
    for p in purchase:
        p.linetotal = p.quantity * p.product.discount_price   # Calculate line total for each purchase
        subtotal += p.linetotal  # Add to subtotal

    # Render the template with purchases and subtotal
    return render(request, "purchase.html", {'purchase': purchase, 'subtotal': subtotal})





class ProductReviewView(View):
    def get(self, request, p_id):
        product = get_object_or_404(Product, id=p_id)

        # Check if the user has already reviewed this product
        try:
            review = Review.objects.get(product=product, user=request.user)
            form = ReviewForm(instance=review) # Pre-fill the form with existing review
        except Review.DoesNotExist:
            form = ReviewForm()  # Blank form if no review exists

        # Get all reviews for the product (optional, to display existing reviews)
        reviews = Review.objects.filter(product=product)

        context = {
            'form': form,
            'product': product,
            'reviews': reviews,
        }
        return render(request, 'product_review.html', context)

    def post(self, request, p_id):
        product = get_object_or_404(Product, id=p_id)

        # Check if the user has already reviewed this product
        try:
            review = Review.objects.get(product=product, user=request.user)
            form = ReviewForm(request.POST, instance=review)  # Update the existing review
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)  # Create a new review if none exists

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.p_id = p_id  # Add p_id to the review instance
            review.user = request.user
            review.save()

            return redirect('purchase')  # Redirect to the purchase page after review submission

        # On form error, re-render the form with existing data
        reviews = Review.objects.filter(product=product)  # Reload reviews
        return render(request, 'product_review.html', {'form': form, 'product': product, 'reviews': reviews})


def cancel_order(request, order_id):

    order = get_object_or_404(Billing_Details, id=order_id, user=request.user)

    product = order.product
    
    product.stock += order.quantity
    product.save()  

    order.delete()

    messages.success(request, "Your order has been successfully canceled.")

    return redirect('orders_page')


class DepartmentsView(View, LoginRequiredMixin):
    def get(self, request, pk=None):
        departments = Departments.objects.all()
 
        department_id = request.GET.get('department_id') or pk
        
        if department_id:
            # Get the department by 'department_id' or 'pk'
            department = get_object_or_404(Departments, pk=department_id)
            
            # Fetch related products for the selected department
            related_products = Product.objects.filter(department=department)

            context = {
                'department': department,   
                'rproduct': related_products, 
                'departments': departments,
            }
        else:

            context = {
                'departments': departments,
            }

        return render(request, 'departments.html', context)



    
def BlogView(request):
    data = BlogPost.objects.all()

    context = {
        'data':data
    }
    return render(request, 'blog.html', context)



# class BlogDetails(View):
#     def get(self, request, pk):
#         blog = get_object_or_404(BlogPost, pk=pk)
#         category = blog.category  # Assuming the BlogPost model has a 'category' field
#         suggest = BlogPost.objects.filter(category=category).exclude(pk=pk)  # Exclude the current blog from suggestions
        
#         context = {
#             'blog': blog,
#             'suggest': suggest,
#         }
#         return render(request, 'blogdetails.html', context)

class BlogDetails(View):
    def get(self, request, pk):
        blog = get_object_or_404(BlogPost, pk=pk)

        # Increment the view count on every visit
        blog.views += 1
        blog.save()

        # Increment the view for an user at a time

        # session_key = f'viewed_blog_{blog.pk}'
        # if not request.session.get(session_key):
        #     blog.views += 1
        #     blog.save()
        #     request.session[session_key] = True  # Mark this post as viewed


        # Get related blog posts by category, excluding the current blog post
        category = blog.category  # Assuming the BlogPost model has a 'category' field
        suggest = BlogPost.objects.filter(category=category).exclude(pk=pk)

        context = {
            'blog': blog,
            'suggest': suggest,
        }
        return render(request, 'blogdetails.html', context)



def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Product.objects.filter(
                Q(name__icontains=query) | Q(department__name__icontains=query)
            )
            return render(request, 'search.html', {'product': product})
        else:
            return render(request, 'search.html')
        

def add_to_wishlist(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id = product_id)
    wishlist_item, created = WishList.objects.get_or_create(user = user, product = product)
    if created:
        pass
    else:
        pass
    return redirect('wishlist')


def wishlist_view(request):
    user = request.user
    data = WishList.objects.filter(user = user)
    context = {
        'data':data
    }
    return render(request, 'wishlist.html', context)


def remove_from_wishlist(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id = product_id)
    wishlist_item = WishList.objects.filter(user = user, product = product).first()
    if wishlist_item:
        wishlist_item.delete()
    return redirect('wishlist')


def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})