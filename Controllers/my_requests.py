from flask import Blueprint, Response, request, jsonify
from flask_cors import CORS

from Models.Order import Order

requests = Blueprint("my_requests", __name__)
CORS(requests)


@requests.route("/my_requests", methods=["GET", "POST"])
def my_requests():
    if request.method == "POST":
        data = request.get_json(silent=True)
        orders = {"orders": [{
            "task": order.task,
            "description": order.description,
            "stage": order.stage.name
        } for order in Order.get_user_orders(data["email"])]}
        return jsonify(orders)
    return Response("my_requests.html")
