from flask import Flask, request, jsonify

try:
    from .student import Student, StudentManager
    from .routes import basic_bp
except ImportError:
    from student import Student, StudentManager
    from routes import basic_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(basic_bp)

manager = StudentManager()


@app.get("/")
@app.get("/api")
@app.get("/api/")
def home():
    return jsonify({
        "status": "online",
        "message": "Student Management API is running on Vercel",
        "endpoints": {
            "GET /": "API root documentation",
            "GET /test": "Test route to verify API health",
            "GET /basic/": "Basic Blueprint root endpoint",
            "GET /basic/greet": "Basic Blueprint greeting endpoint",
            "GET /basic/info": "Basic Blueprint info endpoint",
            "GET /students": "Get all students",
            "POST /students": "Add a new student",
            "GET /students/passed": "Get students who passed",
            "GET /students/stats": "Get statistics",
            "GET /students/<student_id>": "Get student by ID",
            "PATCH /students/<student_id>": "Update student details",
            "DELETE /students/<student_id>": "Delete student"
        }
    }), 200


# GET /test and GET /api/test
@app.get("/test")
@app.get("/api/test")
def test_route():
    return jsonify({
        "status": "success",
        "message": "Test route is working perfectly!",
        "method": request.method,
        "path": request.path
    }), 200


# POST /students and POST /api/students
@app.post("/students")
@app.post("/api/students")
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = ["student_id", "name", "age", "course", "marks"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    if manager.find_student(data["student_id"]):
        return jsonify({
            "error": "Student ID already exists"
        }), 400

    student = Student(
        data["student_id"],
        data["name"],
        data["age"],
        data["course"],
        data["marks"]
    )

    manager.add_student(student)

    return jsonify(student.get_details()), 201


# GET /students and GET /api/students
@app.get("/students")
@app.get("/api/students")
def get_students():
    students = manager.get_all_students()

    return jsonify([
        student.get_details()
        for student in students
    ]), 200


# GET /students/passed and GET /api/students/passed
@app.get("/students/passed")
@app.get("/api/students/passed")
def get_passed_students():
    students = manager.get_passed_students()

    return jsonify([
        student.get_details()
        for student in students
    ]), 200


# GET /students/<id> and GET /api/students/<id>
@app.get("/students/<student_id>")
@app.get("/api/students/<student_id>")
def get_student(student_id):
    student = manager.find_student(student_id)

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(student.get_details()), 200


# PATCH /students/<id> and PATCH /api/students/<id>
@app.patch("/students/<student_id>")
@app.patch("/api/students/<student_id>")
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    student = manager.update_student(student_id, data)

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(student.get_details()), 200


# DELETE /students/<id> and DELETE /api/students/<id>
@app.delete("/students/<student_id>")
@app.delete("/api/students/<student_id>")
def delete_student(student_id):
    deleted = manager.delete_student(student_id)

    if not deleted:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


# GET /students/stats and GET /api/students/stats
@app.get("/students/stats")
@app.get("/api/students/stats")
def student_stats():
    return jsonify(manager.get_stats()), 200


if __name__ == "__main__":
    app.run(debug=True)
