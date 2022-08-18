from flask import Flask,  jsonify, request


app = Flask(__name__)

contact = [{
    "id":1,
    "name":"Noah",
    "number":123456789
},
{
    "id":2,
    "name":"Luna",
    "number":757456345
}]



@app.route("/get_contact")
def getcontact():
    return jsonify({
        "data":contact
    })



@app.route("/add_contact", methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the contact info"
        },400)

    contact  = {
        'id' : contact[-1]['id'] + 1,
        "name" : request.json["name"],
        "number" : request.json.get("number", "")
    }

    contact.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })









if (__name__ == "__main__"):
    app.run(debug=True)