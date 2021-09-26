from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myuser.models import myuser_model, amount_model, warehouse, ware, order_model, order_table_model, buyer_model
from myuser.serializers import myuser_model_Serializer, amount_model_Serializer, ware_Serializer, warehouse_Serializer, \
    order_Serializer, order_table_Serializer, buyer_mode_Serializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = myuser_model.objects.all()
        serializer = myuser_model_Serializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = myuser_model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = myuser_model.objects.get(pk=pk)
    except myuser_model.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = myuser_model_Serializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = myuser_model_Serializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def warehouse_list(request):
    if request.method == 'GET':
        warehouses = warehouse.objects.all()
        serializer = warehouse_Serializer(warehouses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = warehouse_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def warehouse_detail(request, pk):
    try:
        ware_house = warehouse.objects.get(pk=pk)
    except warehouse.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        ware_house_json = warehouse_Serializer(ware_house).data
        if ware_house.amount_model_set.exists():
            serializer = amount_model_Serializer(ware_house.amount_model_set, many=True).data
            ware_info = {}
            for a_amount in serializer:
                a_ware = ware.objects.get(id=a_amount['ware'])
                if a_ware.name in ware_info.keys():
                    ware_info[a_ware.name] += a_amount['amount']
                else:
                    ware_info[a_ware.name] = a_amount['amount']
            ware_info_list = []
            for key in ware_info.keys():
                a_dict = {"name": key, "amount": ware_info[key]}
                ware_info_list.append(a_dict)
            ware_house_json['ware'] = ware_info_list
        else:
            ware_house_json['ware'] = []
        return JsonResponse(ware_house_json)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = warehouse_Serializer(ware_house, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ware_house.delete()
        return HttpResponse(status=204)


@csrf_exempt
def ware_list(request):
    if request.method == 'GET':
        serializers = []
        for a_ware in ware.objects.all():
            serializer = ware_Serializer(a_ware)
            s = serializer.data
            if a_ware.amount_model_set.exists():
                amounts = amount_model_Serializer(a_ware.amount_model_set, many=True)
                sum_number = 0
                for a_amount in amounts.data:
                    sum_number += a_amount['amount']
                s['amounts'] = amounts.data
                s['sum'] = sum_number
            else:
                s['amounts'] = []
                s['sum'] = 0
            serializers.append(s)
        return JsonResponse(serializers, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ware_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ware_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ware.objects.get(pk=pk)
    except ware.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ware_Serializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ware_Serializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def amount_list(request):
    if request.method == 'GET':
        snippets = amount_model.objects.all()
        serializer = amount_model_Serializer(snippets, many=True).data
        ret_table = []
        for amount in serializer:
            a_warehouse = warehouse.objects.get(id=amount['warehouse'])
            a_ware = ware.objects.get(id=amount['ware'])
            amount['location'] = a_warehouse.location
            amount['name'] = a_ware.name
            ret_table.append(amount)
        return JsonResponse(ret_table, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = amount_model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order_table_list(request):
    if request.method == 'GET':
        snippets = order_table_model.objects.all()
        serializer = order_table_Serializer(snippets, many=True).data
        ret_table = []
        for snippet in serializer:
            serializer = order_table_Serializer(snippet)
            orders = order_Serializer(order_model.objects.filter(order_table=snippet['id']), many=True).data
            orders_sum = 0
            for order in orders:
                the_order = ware.objects.get(id=order['ware'])
                orders_sum += the_order.price * order['number']
            order_table = serializer.data
            order_table['orders_sum'] = orders_sum
            ret_table.append(order_table)
        return JsonResponse(ret_table, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = order_table_Serializer(data=data)
        orders = data['orders']

        buyer = buyer_model(buyer_name=data['buyer_name'], buyer_phone_number=data['buyer_phone_number'],
                            buyer_email=data['buyer_email'], buyer_sex=data['buyer_sex'])
        if serializer.is_valid():
            order_table = serializer.save()
            for order in orders:
                order['order_table'] = order_table.id
                the_order = order_Serializer(data=order)
                if the_order.is_valid():
                    the_order.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order_table_detial(request, pk):
    try:
        snippet = order_table_model.objects.get(pk=pk)
    except ware.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = order_table_Serializer(snippet)
        orders = order_Serializer(order_model.objects.filter(order_table=snippet.id), many=True).data
        new_orders = []
        orders_sum = 0
        for order in orders:
            the_order = ware.objects.get(id=order['ware'])
            order['price'] = the_order.price
            order['name'] = the_order.name
            order['sum_price'] = the_order.price * order['number']
            orders_sum += order['sum_price']
            new_orders.append(order)
        order_table = serializer.data
        order_table['orders'] = new_orders
        order_table['orders_sum'] = orders_sum
        return JsonResponse(order_table)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['order_table'] = pk
        serializer = order_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        snippet.status = data['status']
        snippet.save()
        return JsonResponse(order_table_Serializer(snippet).data)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def ware_order_statistic(request):
    if request.method == 'GET':
        wares = ware_Serializer(ware.objects.all(), many=True).data
        ret_table = []
        for a_ware in wares:
            orders = order_Serializer(order_model.objects.filter(ware=a_ware['id']), many=True).data
            a_ware['sum_out'] = 0
            for order in orders:
                a_ware['sum_out'] += order['number']
            a_ware['sum_price'] = a_ware['sum_out'] * a_ware['price']
            ret_table.append(a_ware)
        return JsonResponse(ret_table, safe=False)
    return HttpResponse(status=400)
