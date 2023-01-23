import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {"students": []}
json_string = json.dumps(data)
with open("students.json", "w") as json_file:
    json_file.write(json_string)

{
  "students": [
    {"sName": "Elad", "Email": "eladrotfus@gmail.com", "mGrade": 87, "eGrade": 97, "cGrade": 76 },
    {"sName": "Bar", "Email": "bardavid2000@gmail.com", "mGrade": 96, "eGrade": 72, "cGrade": 0 },
    ...
  ]
}
@app.route('/', methods=['GET'])
def getStudents():
    with open('students.json') as json_file:
        data = json.load(json_file)
    return data["students"]

@app.route('/add', methods=['POST'])
def addStudent():
    student = request.get_json()
    students = getStudents()
    new_student = {"sName": student["sName"], "Email": student["Email"], "mGrade": student["mGrade"],
     "eGrade":student["eGrade"], "cGrade":student["cGrade"]}
    students.append(new_student)
    save_students(students)
    return jsonify({"success": True})
    

@app.route('/')
def save_students(students):
    with open('students.json', 'w') as json_file:
        json.dump({"students": students}, json_file)


if __name__ == '__main__':
    app.run(debug=True)