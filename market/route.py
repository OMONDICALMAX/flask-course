from market import app
from flask import render_template, redirect, url_for, flash
from market.module import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/')
@app.route('/home')

def home_page():
  return render_template('index.html')


@app.route('/market')
def market_page():

  items=Item.query.all()
  return render_template ('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    user_to_create = User( username=form.username.data,
                          email_address=form.email_address.data,
                          password_hash=form.password1.data)
    db.session.add(user_to_create)
    db.session.commit()
    return redirect(url_for('market_page'))
  if form.errors != {}: # If there are no errors arising from the validations in forms.py
    for err_msg in form.errors.values():
      flash(f'There was an error with creating a user: {err_msg}')
  return render_template('register.html', form=form)

@app.route('/login')
def login_page():
  return render_template ('login.html')


if __name__ == '__main__':
  app.run(debug=True)