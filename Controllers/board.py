from flask import Blueprint, Response, request, jsonify
from flask_cors import CORS

from Models.Order import Order, OrderStage
from Models.UserCompany import UserCompany

kanban = Blueprint("board", __name__)
CORS(kanban)


def get_board():
    orders = {}
    for stage in OrderStage:
        stage_orders = []
        for order in Order.get_orders_by_stage(stage):
            stage_orders.append({"id": str(order.id),
                                 "task": order.task,
                                 "description": order.description,
                                 "email": order.customer_email})
        if len(stage_orders) != 0:
            orders.update({stage.stage_name(): stage_orders})
    return orders


@kanban.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data["action"] == "get":
            user = UserCompany(data["email"], data["password"])
            if user.verify():
                return jsonify(get_board())
        elif data["action"] == "del":
            order = Order()
            order.retrieve(data["id"])
            order.remove()
            user = UserCompany(data["email"], data["password"])
            if user.verify():
                return jsonify(get_board())
        elif data["action"] == "up":
            order = Order()
            order.retrieve(data["id"])
            order.move_stage_next()
            user = UserCompany(data["email"], data["password"])
            if user.verify():
                return jsonify(get_board())
        elif data["action"] == "down":
            order = Order()
            order.retrieve(data["id"])
            order.move_stage_back()
            user = UserCompany(data["email"], data["password"])
            if user.verify():
                return jsonify(get_board())
    return Response("board.html")
