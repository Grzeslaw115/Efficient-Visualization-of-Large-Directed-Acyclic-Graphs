from flask import Blueprint, jsonify, request
from routes.helpers import get_db_manager

groups_bp = Blueprint("groups", __name__)

@groups_bp.route("/groups/<string:group_name>/graphs", methods=["POST"])
def list_graphs_for_group(group_name: str):
    """
    Body:
    {"password": "secret_pass"}

    Response 200:
    [
      { "id": "...", "name": "...", "num_of_vertices": 123, "last_entry_update": "..." },
      ...
    ]
    """
    db_manager = get_db_manager()

    data = request.get_json(force=True)
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password is required"}), 400

    if not db_manager.verify_group_password(group_name, password):
        return jsonify({"error": "Invalid group or password"}), 403

    graphs = db_manager.list_graphs_for_group(group_name)
    return jsonify(graphs), 200


@groups_bp.route("/groups", methods=["GET"])
def list_groups():
    db_manager = get_db_manager()
    groups = db_manager.list_groups()
    return jsonify(groups), 200


@groups_bp.route("/groups/<string:group_name>/graphs/<string:graph_id>", methods=["DELETE"])
def remove_graph_from_group(group_name: str, graph_id: str):
    db_manager = get_db_manager()
    data = request.get_json(silent=True) or {}
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password is required"}), 400

    group = db_manager.get_group(group_name)
    if group is None:
        return jsonify({"error": "Group not found"}), 404

    if not db_manager.verify_group_password(group_name, password):
        return jsonify({"error": "Invalid group password"}), 403

    graph = db_manager.fetch_data(graph_id)
    if graph is None:
        return jsonify({"error": "Graph not found"}), 404

    if graph.get("group") != group_name:
        return jsonify({"error": "Graph does not belong to this group"}), 400

    db_manager.remove_graph_from_group(graph_id)
    return jsonify({"status": "ok"}), 200
