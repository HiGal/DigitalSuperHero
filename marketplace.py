from flask import Blueprint, Response, request

from Models.Order import Order

marketplace = Blueprint('marketplace', __name__)


@marketplace.route('/marketplace', methods=['GET'])
def get_search_orders():
    from json import dumps

    if request.method == 'GET':
        orders = Order.get_search_orders()
        resp = [i.to_front_format() for i in orders]

        return Response(dumps(resp))

    return Response('marketplace.html')
