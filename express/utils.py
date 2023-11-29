from express.models.products import ShoppingCart


def increment_count(pk):
    try:
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        shopping_cart.count += 1
        shopping_cart.save()
    except:
        return False
    return True


def decrement_count(pk):
    try:
        shopping_cart = ShoppingCart.objects.get(pk=pk)
        shopping_cart.count -= 1
        shopping_cart.save()
    except:
        return False
    return True
