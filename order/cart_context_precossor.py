from .models import *

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user, status='InPrograss')
        if not created:
            cart_detale = CartDetale.objects.filter(cart=cart)
            return {'cart_data': cart, 'cart_detale': cart_detale}
        return {'cart_data': cart}
    else:
        return {}

    