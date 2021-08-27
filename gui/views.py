from django.shortcuts import render, redirect
from . import models
from ml import model


def redirect_view(request):
    return redirect('/pageno=1')


def homepage(request, pageno='1'):
    page_size = 15
    start_index = page_size * pageno
    end_index = start_index + page_size

    pagination_start = pageno if pageno < 9 else pageno - 7
    pagination_end = pageno + 7;

    products = models.Product.objects.all()[start_index:end_index]
    product_count = models.Product.objects.all().count()
    return render(request, "index.html",
                  {"products": products, "currentpage": pageno, "endpage": pagination_end -1 ,
                   "startpage": pagination_start,
                   "currentpage": pageno, "pages": list(range(pagination_start, pagination_end))})


def productpage(request, id):
    product = models.Product.objects.get(pk=id)
    suggestions_ids = model.bag_of_words(product.product_id, 6)
    suggestions_bow = models.Product.objects.filter(product_id__in=suggestions_ids[1:])

    suggestions_ids = model.avg_w2v_model(product.product_id, 6)
    suggestions_w2v = models.Product.objects.filter(product_id__in=suggestions_ids[1:])
    print(suggestions_w2v)
    return render(request, "product.html", {"product": product, "suggestions_bow": suggestions_bow, "suggestions_w2v": suggestions_w2v})
