from django.shortcuts import render
from stock.models import Stock

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks.html', {'stocks': stocks})
