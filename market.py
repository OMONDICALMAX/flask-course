from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home_page():
  return render_template('index.html')


@app.route('/market')
def market_page():
  items=[
    {'id': 1, 'item_name': 'Phone', 'barcode': '12345678', 'price': '15000 Ksh'},
    {'id': 2, 'item_name': 'Power Bank', 'barcode': '9101112', 'price': '2000 Ksh'},
    {'id': 3, 'item_name': 'Earphones', 'barcode': '13141516', 'price': '1300 Ksh'}
  ]
  return render_template('market.html', items=items)

if __name__ == '__main__':
  app.run(debug=True)