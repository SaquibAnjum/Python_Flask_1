from flask import Blueprint, jsonify, request

# Create a basic Blueprint instance
# 'basic_bp' is the blueprint name, and url_prefix defines the base path for all its routes
basic_bp = Blueprint("basic_bp", __name__, url_prefix="/basic")


@basic_bp.get("/")
def basic_home():
    """Basic root route for the blueprint."""
    return jsonify({
        "status": "success",
        "message": "Hello from the Basic Blueprint!",
        "path": request.path
    }), 200


@basic_bp.get("/greet")
def basic_greet():
    """A route accepting optional query parameter 'name'."""
    name = request.args.get("name", "World")
    return jsonify({
        "status": "success",
        "message": f"Hello, {name}!"
    }), 200


@basic_bp.get("/info")
def basic_info():
    """Information route describing the blueprint."""
    return jsonify({
        "blueprint": "basic_bp",
        "description": "Sample Flask Blueprint demonstrating modular routing",
        "available_routes": [
            "GET /basic/",
            "GET /basic/greet?name=<your_name>",
            "GET /basic/info"
        ]
    }), 200
