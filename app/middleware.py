"""Middleware module."""
from purapps.purbeurre.forms import SearchProduct
from purapps.purauth.forms import PremiumForm
from django.shortcuts import redirect


class SearchMiddleware:
    """SearchMiddleware class."""

    def __init__(self, get_response):
        """Init."""
        self.get_response = get_response

    def __call__(self, request):
        """Call."""
        search_form = SearchProduct()

        if request.method == "POST" and request.POST.get("product_name"):
            product_name = request.POST.get("product_name")
            return redirect("results", product_name=product_name)

        request.search_form = search_form
        return self.get_response(request)


class PremiumMiddleware:
    """PremiumMiddleware class."""

    def __init__(self, get_response):
        """Init."""
        self.get_response = get_response

    def __call__(self, request):
        """Call."""
        premium_form = PremiumForm()
        if request.method == "POST":
            premium_form = PremiumForm(request.POST)

            if premium_form.is_valid():
                premium_form.clean_premium()

                request.user.is_premium = True
                request.user.save()

        request.premium_form = premium_form

        return self.get_response(request)
