from flask import Flask, request

from controller import get_message_from_simple_chat, load_document

load_document()
app=Flask(__name__)
@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        message = request.json['message']
        return get_message_from_simple_chat(message)
    else:
        return 'Hello, World chatbot ready to battle!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)