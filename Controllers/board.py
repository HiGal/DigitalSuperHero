from flask import Flask, Blueprint, Response, request, jsonify
from flask_cors import CORS
from Models.Order import Order, OrderStage
from Models.UserCompany import UserCompany

kanban = Blueprint("board", __name__)
CORS(kanban)


@kanban.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data["action"] == "get":
            user = UserCompany(data["email"], data["password"])
            if user.verify():
                orders = {}
                for stage in OrderStage:
                    stage_orders = {}
                    for order in Order.get_orders_by_stage(stage):
                        stage_orders.update({"id": order.id,
                                             "task": order.task,
                                             "description": order.description,
                                             "email": order.customer_email})
                    orders.update({stage.stage_name(): stage_orders})
                return jsonify(orders)
        elif data["action"] == "del":
            order = Order()
            order.retrieve(data["id"])
            order.remove()
            orders = {}
            for stage in OrderStage:
                stage_orders = {}
                for order in Order.get_orders_by_stage(stage):
                    stage_orders.update({"id": order.id,
                                         "task": order.task,
                                         "description": order.description,
                                         "email": order.customer_email})
                orders.update({stage.stage_name(): stage_orders})
            return jsonify(orders)
        elif data["action"] == "up":
            order = Order()
            order.retrieve(data["id"])
            order.move_stage_next()
            orders = {}
            for stage in OrderStage:
                stage_orders = {}
                for order in Order.get_orders_by_stage(stage):
                    stage_orders.update({"id": order.id,
                                         "task": order.task,
                                         "description": order.description,
                                         "email": order.customer_email})
                orders.update({stage.stage_name(): stage_orders})
            return jsonify(orders)
        elif data["action"] == "down":
            order = Order()
            order.retrieve(data["id"])
            order.move_stage_back()
            orders = {}
            for stage in OrderStage:
                stage_orders = {}
                for order in Order.get_orders_by_stage(stage):
                    stage_orders.update({"id": order.id,
                                         "task": order.task,
                                         "description": order.description,
                                         "email": order.customer_email})
                orders.update({stage.stage_name(): stage_orders})
            return jsonify(orders)
    return Response("board.html")
