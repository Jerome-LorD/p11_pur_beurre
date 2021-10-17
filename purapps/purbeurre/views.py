"""Purbeurre views module."""

import json
from django.http.response import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from purapps.purbeurre.models import Product, Substitutes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def index(request):
    """Index."""
    return render(request, "pages/home.html")


def mentions(request):
    """Mentions."""
    return render(request, "pages/mentions.html")


def results(request, product_name):
    """Results view from search product form."""
    try:
        result = Product.objects.filter(name__iregex=r"^%s$" % product_name)
    except Product.DoesNotExist:
        raise Http404("Cette page n'existe pas")

    page = request.GET.get("page", 1)
    if result.first():
        product = result.first()
        substitutes = product.find_substitute()
        substitute_already_saved = []
        if substitutes is not None:
            already_saved = Substitutes.objects.filter(
                product_id__in=[item.id for item in substitutes],
                user_id=request.user.id,
            )
            if already_saved:
                [
                    substitute_already_saved.append(item.product_id)
                    for item in already_saved
                ]

            paginator = Paginator(substitutes, 16)
            try:
                page_result = paginator.page(page)
            except PageNotAnInteger:
                page_result = paginator.page(1)
            except EmptyPage:
                page_result = paginator.page(paginator.num_pages)
            return render(
                request,
                "pages/results.html",
                {
                    "substit": substitutes,
                    "product": product,
                    "page_result": page_result,
                    "substitute_already_saved": substitute_already_saved,
                },
            )

        else:
            no_result = "Il n'y a pas de substitut pour ce produit."
            return render(
                request,
                "pages/results.html",
                {
                    "product": product,
                    "no_result": no_result,
                },
            )

    elif not result.first():

        general_research = Product.objects.filter(
            name__icontains="%s" % product_name
        ).order_by("nutriscore__type")

        gal_search = general_research.all()
        paginator = Paginator(gal_search, 16)

        try:
            page_no_result = paginator.page(page)
        except PageNotAnInteger:
            page_no_result = paginator.page(1)
        except EmptyPage:
            page_no_result = paginator.page(paginator.num_pages)

        return render(
            request,
            "pages/results.html",
            {
                "gal_search": gal_search,
                "search_term": product_name,
                "page_no_result": page_no_result,
            },
        )

    return render(request, "pages/results.html", {"search_term": product_name})


def error_404(request, exception):
    """Error 404 view."""
    return render(request, "pages/404.html", status=404)


def product_details(request, product_name):
    """Product details."""
    try:
        product = Product.objects.get(name=product_name)
    except Product.DoesNotExist:
        raise Http404("Cette page n'existe pas")
    return render(
        request,
        "pages/product.html",
        {
            "product": product,
        },
    )


def autocomplete(request):
    """Jquery autocomplete response."""
    if request.is_ajax() and request.method == "GET":
        product = request.GET.get("term", "")
        products = Product.objects.filter(name__icontains="%s" % product).order_by(
            "id"
        )[:10]

    return JsonResponse([{"name": item.name} for item in products], safe=False)


@login_required
def favorites(request):
    """Retrieve favorites."""
    substitutes = Substitutes.objects.filter(user=request.user)

    page = request.GET.get("page", 1)
    paginator = Paginator(substitutes, 12)

    try:
        favorite = paginator.page(page)
    except PageNotAnInteger:
        favorite = paginator.page(1)
    except EmptyPage:
        favorite = paginator.page(paginator.num_pages)

    return render(
        request,
        "pages/favorites.html",
        {"favorite": favorite},
    )


@csrf_protect
def save_substitute(request):
    """Save substitute from ajax post."""
    data = json.loads(request.body)
    product_id = data["product_id"]
    reference_id = data["reference_id"]

    created = Substitutes.objects.create(
        product_id=product_id,
        reference_id=reference_id,
        user=request.user,
    )
    if created is None:
        return JsonResponse({"is_max_in_db_reached": True})
    else:
        return JsonResponse({"is_max_in_db_reached": False})


@csrf_protect
def delete_substitute(request):
    """Delete substitute from ajax post."""
    data = json.loads(request.body)
    product_id = data["product_id"]
    reference_id = data["reference_id"]

    Substitutes.objects.get(
        product_id=product_id,
        reference_id=reference_id,
        user=request.user,
    ).delete()

    return HttpResponse(status=201)


@csrf_protect
def get_reference_id(request):
    """Get reference id."""
    data = json.loads(request.body)
    product_id = data["product_id"]
    substitute = Substitutes.objects.get(product_id=product_id, user_id=request.user.id)

    return JsonResponse({"reference_id": substitute.reference.id})
