from django.contrib import admin
from . models import Product, Departments, Category, Size, Cart, BlogPost, Tag, Billing_Details, Delivery, Brand, HomeCarousel, Review, WishList, Coupon, About, Social, PaymentMethod, FAQ, SpecialOffer, BlogPage

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        # 'description', 
        'selling_price', 
        'discount_percentage',
        'discount_price', 
        'SpecialOffer_price',
        'stock',
        'image',
        # 'image1',
        # 'image2',
        # 'image3',
        # 'image4',
        'created_at', 
        'updated_at', 
        'shipping_time',
        'selles',
        'product_video',
        'status',
        'department', 
        'category', 
        'size'
    )
    actions = ['Enable', 'Disable']

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")
    
    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Product, ProductAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'link',
        'image',
        'status'
    )
    actions = ['Enable', 'Disable']

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")
    
    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Category, CategoryAdmin)


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'link',
        'image',
        'status'
    )
    actions = ['Enable', 'Disable']

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status="False")

admin.site.register(Departments, DepartmentsAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'link'
    )
admin.site.register(Size, SizeAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'p_id', 'product','quantity', 'created_at'
    )

admin.site.register(Cart, CartAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'author',
        # 'content',
        'featured_image',
        # 'tags',
        'category',
        'excerpt',
        'publish_date',
        'updated_at',
        'status',
        'views',
        'meta_title',
        'meta_description',
        'comments_enabled'
    )
    actions = ['Draft', 'Published']

    @admin.action(description="Draft")
    def Draft(self, request, status):
        status.update(status = "False")

    @admin.action(description="Published")
    def Published(self, request, status):
        status.update(status = "True")

admin.site.register(BlogPost, BlogPostAdmin)


class BlogPageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'head',
        'description',
        'banner',
        'banner_head',
        'banner_description',
        'status'
    )
    actions = ['Disable', 'Enable']

    def Disable(self, request, status):
        status.update(status= "False")

    def Enable(self, request, status):
        status.update(status="True")

admin.site.register(BlogPage, BlogPageAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
admin.site.register(Tag, TagAdmin)


class Billing_DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'p_id',
        'first_name',
        'last_name',
        'product',
        'quantity',
        'country',
        'division',
        'district',
        'thana',
        'street',
        'zip_code',
        'phone',
        'second_phone',
        'order_note',
        'datetime',
        'email'
    )

admin.site.register(Billing_Details, Billing_DetailsAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'p_id',
        'order_id',
        'first_name',
        'last_name',
        'product',
        'quantity',
        'country',
        'division',
        'district',
        'thana',
        'street',
        'zip_code',
        'phone',
        'second_phone',
        'order_note',
        'datetime',
        'email',
        'delivery_charge'
    )

admin.site.register(Delivery, DeliveryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'link',
        'logo',
        'banner'
    )
admin.site.register(Brand, BrandAdmin)


class HomeCarouselAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'title',
        'description',
        'link',
        'banner'
    )
admin.site.register(HomeCarousel, HomeCarouselAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'p_id',
        'user',
        'rating',
        'comment',
        'created_at',
        'updated_at'
    )
admin.site.register(Review, ReviewAdmin)



class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
    )
admin.site.register(WishList, WishListAdmin)



# class CouponAdmin(admin.ModelAdmin):
#     list_display = (
#         'code',
#         'discount',
#         'valid_from',
#         'valid_to',
#         'active'
#     )
# admin.site.register(Coupon, CouponAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'about',
        # 'description',
        'contact',
        'email',
        'mission_statement',
        'vision',
        'address',
        'logo',
        'banner',
        'year_established',
        'support_contact',
        'operating_hours',
        'map_location',
        'testimonials',
        'team_info'
    )
admin.site.register(About, AboutAdmin)


class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
        'logo'
    )
admin.site.register(Social, SocialAdmin)


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
        'logo'
    )
admin.site.register(PaymentMethod, PaymentMethodAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question',
        'answer',
        'status',
        'created_at'
    )
    search_fields = ('question',)
    actions = ['ShowFAQ', 'HideFAQ']

    admin.action(description="Show FAQ")
    def ShowFAQ(self, request, status):
        status.update(status = "True")

    admin.action(description="Hide FAQ")
    def HideFAQ(self, request, status):
        status.update(status = "False")

admin.site.register(FAQ, FAQAdmin)



class SpecialOfferModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'discount_percentage',
        'start_date',
        'end_date',
        'active',
        'banner',
        'products_list',
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "products":
            # Filter products with stock greater than zero
            kwargs["queryset"] = Product.objects.filter(stock__gt=0)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    # Method to display selected products in a readable format
    def products_list(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    products_list.short_description = "Products"

    # Optional: Add filter_horizontal for a more user-friendly selection widget
    filter_horizontal = ('products',)

admin.site.register(SpecialOffer, SpecialOfferModelAdmin)
