from flask import Flask, request
from waitress import serve
from escpos.printer import Usb

print("Creating Flask app...")

app = Flask(__name__)

print("Initializing USB printer...")

try:
    # USB vendor and product IDs
    usb_printer = Usb(0x04b8, 0x0e15)
    print("USB printer initialized successfully!\n")
except Exception as e:
    print(f"Failed to initialize USB printer: {e}\n")

@app.route('/print', methods=['POST'])
def print_order():
    data = request.json
    order_text = data.get('order_text', '')
    print("Printing ...")
    
    lines = order_text.split('\n')

    print("Order printed!\n")
    print("Waiting for a job ...")

    return 'Order printed successfully'

if __name__ == '__main__':
    print("Print server is running!")
    print("Press [Ctrl + C] to stop!\n")
    print("Waiting for a job ...")
    serve(app, host='0.0.0.0', port=5000)
