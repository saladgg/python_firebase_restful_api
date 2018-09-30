import firebase_admin
from flask import Flask
from flask_restful import Api, Resource, reqparse
from firebase_admin import credentials, db

app = Flask(__name__)
api = Api(app)


credentials = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(credentials, {
    'databaseURL': "https://realtimedb-with-python.firebaseio.com"
})

dbStudents = db.reference("/students")
students = dbStudents.get()


class Students(Resource):
    def get(self):
        return students, 200


class Student(Resource):
    def get(self, firstName):
        for key, value in students.items():
            if firstName == value["firstName"]:
                return value, 200
        return "student not found", 404

    # def post(self, name):
    #     parser = reqparse.RequestParser
    #     parser.add_argument("name", type=str)
    #     parser.add_argument("age", type=int)
    #     parser.add_argument("college", type=str)


api.add_resource(Students, "/students/", endpoint="students")

api.add_resource(Student, "/student/<string:firstName>")


app.run(debug=True)
