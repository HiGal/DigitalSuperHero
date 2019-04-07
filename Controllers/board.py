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
        user = UserCompany(data["email"], data["password"])
        if user.verify():
            orders = {}
            for stage in OrderStage:
                stage_orders = {}
                for order in Order.get_orders_by_stage(stage):
                    stage_orders.update({"id": order.id,
                                         "task": order.task,
                                         "description": order.description,
                                         "email": order.customer_email,
                                         "stage": order.stage_name()})
                orders.update({stage.stage_name(): stage_orders})
            return jsonify(orders)
    return Response("board.html")
