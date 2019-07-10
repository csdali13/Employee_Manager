from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.update(
    SECRET_KEY='secret',
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:yogaforall@localhost/empManager',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

empManager_db = SQLAlchemy(app)


class Employee(empManager_db.Model):
    __tablename__ = 'employee'

    id = empManager_db.Column(empManager_db.Integer, primary_key=True)
    name = empManager_db.Column(empManager_db.String(80), nullable=False)
    designation = empManager_db.Column(empManager_db.String(80), nullable=False)
    address = empManager_db.Column(empManager_db.String(400))
    phone = empManager_db.Column(empManager_db.Integer)

    def __init__(self, name, designation, address, phone):
        self.name = name
        self.designation = designation
        self.address = address
        self.phone = phone

    def __repr__(self):
        return repr((self.name, self.id, self.designation))

    def add_employee(self, empToAdd):
        empManager_db.session.add_all([empToAdd])
        empManager_db.session.commit()


if __name__ == '__main__':
    empManager_db.create_all()
    app.run(debug=True)




