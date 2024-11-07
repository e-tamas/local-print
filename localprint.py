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
    # for line in lines: 
    #     if "Order ID" in line: 
    #         usb_printer.set(align='center', bold=True) 
    #         usb_printer.text(f"{line}\n\n") 
    #     elif "Phone" in line or "Date" in line or "Total" in line: 
    #         usb_printer.set(align='left', bold=False) 
    #         usb_printer.text(f"{line}\n") 
    #     elif "Items:" in line: 
    #         usb_printer.set(align='left', bold=True, underline=True) 
    #         usb_printer.text(f"{line}\n") 
    #     else: 
    #         usb_printer.set(align='left') 
    #         usb_printer.text(f"{line}\n") 

    # usb_printer.cut()

    print("Order printed!\n")
    print("Waiting for a job ...")

    return 'Order printed successfully'

if __name__ == '__main__':
    print("Print server is running!")
    print("Press [Ctrl + C] to stop!\n")
    print("Waiting for a job ...")
    serve(app, host='0.0.0.0', port=5000)
