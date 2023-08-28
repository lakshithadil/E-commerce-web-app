from django.urls import path
from . import views
from rest_framework_nested import routers

# URLConf
router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("customer", views.CustomerViewSet)
router.register("orders", views.OrderViewSet, basename="orders")

product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemVeiwSet, basename="cart-items")

urlpatterns = router.urls + product_router.urls + cart_router.urls

# urlpatterns = [
#     path("products/", views.ProductList.as_view()),
#     path("products/<int:pk>", views.ProductDetail.as_view()),
#     path("collections/", views.CollectionList.as_view()),
#     path(
#         "collections/<int:pk>",
#         views.CollectionDetail.as_view(),
#         name="collection-detail",
#     ),
# ]
