from flask import Flask, request,jsonify
app = Flask(__name__)

@app.route('/params', methods=['GET'])
def get_api():
    # print(request.authorization)
    print(request.args)
    name = request.args.get('name')
    age = request.args.get('age')

    ##OR##
    
    # name = request.args['name']
    # age = request.args['age']

    return jsonify({
        'Name':name,
        'Age':age  })

if __name__ == '__main__':
    app.run(debug=True)