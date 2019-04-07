from flask import Blueprint, Response, request

from Models.Order import Order, OrderStage

marketplace = Blueprint('marketplace', __name__)


@marketplace.route('/marketplace', methods=['GET'])
def get_search_orders():
    from json import dumps

    if request.method == 'GET':
        orders = Order.get_orders_by_stage(OrderStage.SEARCH)
        resp = [i.to_marketplace_format() for i in orders]

        return Response(dumps(resp))

    return Response('marketplace.html')
