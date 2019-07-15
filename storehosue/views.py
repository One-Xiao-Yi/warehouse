from django.shortcuts import render
from storehosue.models import *
from django.http import JsonResponse
import json,uuid


def ini_store_house(request):
    stock = Stock.objects.all()
    return render(request,'store_house.html',{"stock":stock})


def update_good(request):
    stock = json.loads(request.body)
    stock_id = stock['stock_id']
    stock_id = stock_id.replace("#","")
    stock_save = Stock.objects.get(stock_id=stock_id)
    stock_save.surplus = int(stock['surplus'])
    stock_save.retail_price = int(stock['retail_price'])
    stock_save.good.purchase_price = int(stock['purchase_price'])
    stock_save.save()
    return JsonResponse({'msg':'更新成功'})


def add_good(request):
    data_json = json.loads(request.body)
    good_json = data_json['good']
    supplier_json = good_json['supplier']
    del good_json['supplier']
    good = Goods(**good_json)
    supplier = Suppliers(**supplier_json)
    del data_json['good']
    stock = Stock(**data_json)
    stock.stock_id = str(uuid.uuid1()).replace("-","")
    good.good_id = str(uuid.uuid1()).replace("-","")
    supplier.supplier_id = str(uuid.uuid1()).replace("-","")
    stock.good_id = good.good_id
    good.supplier_id = supplier.supplier_id
    print(supplier.phone_number)
    print(len(supplier.phone_number))
    good.save()
    supplier.save()
    stock.save()
    return JsonResponse({"msg":"添加成功"})
