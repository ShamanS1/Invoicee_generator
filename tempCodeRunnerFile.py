from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    customer_name = request.form['name']
    customer_location = request.form['place']
    customer_email = request.form['mailid']
    items = []

    item_names = request.form.getlist('item[]')
    quantities = request.form.getlist('qty[]')
    prices = request.form.getlist('price[]')

    for item_name, quantity, price in zip(item_names, quantities, prices):
        amount = int(quantity) * float(price)
        ig=amount*0.1
        item = {
            'item': item_name,
            'price': price, 
            'igst':ig, 
            'qty': quantity,
            'amt': amount
        }
        items.append(item)

    # Calculate sub_total, tax, and total
    sub_total = sum(item['amt'] for item in items)
    tax = sub_total * 0.1  
    total = sub_total + tax

    # Generate current date
    current_date = datetime.datetime.now().strftime("%d %B %Y")

    # Generate a unique invoice number
    invoice_number = "INV-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    return render_template('invoice.html',
                           name=customer_name,
                           place=customer_location,
                           mailid=customer_email,
                           items=items,
                           sub_total=sub_total,
                           tax=tax,
                           total=total,
                           date=current_date,
                           invoice_no=invoice_number,
                           igst=ig)

if __name__ == '__main__':
    app.run()
