from flask import Blueprint
from flask import request, Response

from allocation import bootstrap
from allocation.domain import command
from allocation.service.handlers import InvalidSku
from src.allocation.service.unit_of_work import ProductUoW

app_route = Blueprint('route', __name__)
bus = bootstrap.bootstrap()


@app_route.post('/allocate')
def allocate():
    cmd = command.Allocate(
        request.json["orderid"], request.json["sku"], request.json["qty"],
    )
    try:
        results = bus.handle(cmd)
        batchref = results.pop(0)
    except InvalidSku as e:
        return {'error': e.message}, 500

    return {"batchref": batchref}, 201


@app_route.post('/create')
def create():
    cmd = command.CreateBatch(**request.json)
    [result] = bus.handle(cmd)
    return result.to_json()


@app_route.delete('/')
def delete_batch():
    cmd = command.Delete(request.json['ref'])
    bus.handle(cmd)
    return Response(status=201)


@app_route.get('/')
def all_batches():
    cmd = command.List()
    [results] = bus.handle(cmd)
    return {'product': [b.to_json() for b in results]}


@app_route.put('/')
def update_b():
    cmd = command.ChangeBatchSize(request.json['ref'], request.json['qty'])
    bus.handle(cmd)
    return Response(status=201)
