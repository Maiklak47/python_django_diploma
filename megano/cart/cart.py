from typing import Literal, Dict

from decimal import Decimal
from rest_framework.request import Request

from megano import settings
from products.models import Product


class Cart:
    """Cart model based session"""

    def __init__(self, request: Request):
        self.session = request.session
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})

    def save(self) -> None:
        self.session.save()

    def clear(self) -> None:
        del self.session[settings.CART_SESSION_ID]

    def add(self, product_id: int, count: int) -> None:
        product = Product.objects.get(pk=product_id)
        price = product.salePrice or product.price
        product_info = self.cart.setdefault(str(product_id), {"count": 0})
        self.is_valid(
            method="POST", count=count, product_info=product_info, product=product
        )
        product_info["count"] += count
        product_info["price"] = float(price)
        self.save()

    def remove(self, product_id: int, count: int) -> None:
        product_id = str(product_id)
        product_info = self.cart.get(product_id)
        self.is_valid(method="DELETE", count=count, product_info=product_info)
        if count == product_info.get("count"):
            del self.cart[product_id]
        else:
            product_info["count"] -= count
        self.save()

    @staticmethod
    def is_valid(
        method: Literal["DELETE", "POST"],
        count: int,
        product_info: Dict,
        product: int = None,
    ) -> None:
        if method == "POST":
            new_count = product_info["count"] + count
            if product.count < new_count:
                raise ValueError("The quantity of the product is not enough")

        if method == "DELETE":
            if not product_info:
                raise ValueError("There is no such product in the cart")
            if product_info["count"] < count:
                raise ValueError("There is no such quantity of product in the basket")

    def get_total_cost(self) -> float:
        summ = sum(
            Decimal(item.get("price")) * item.get("count")
            for item in self.cart.values()
        )
        return round(float(summ), 2)
