from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.converter import RatesNotAvailableError
from decimal import Decimal


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



@app.route('/')
def show_from():
    return render_template('home.html')

@app.route('/calculate-rate',methods=["POST"])
def calc_rate():
    c = CurrencyRates(force_decimal=True)
    code = CurrencyCodes()

    from_val = request.form.get("from").upper()
    to_val = request.form.get("to").upper()
    amt_val= request.form.get("amt")

    
    try:
        value = c.convert(from_val,to_val,Decimal(amt_val))
        result = round(value,2)
        symbol = code.get_symbol(to_val)
        return render_template('result.html', result = result, symbol= symbol)
    except RatesNotAvailableError:
        flash('NOT a valid Currency Code', 'err_code')
        return redirect('/')
    except:
        flash('NOT a valid amount', 'err_amt')
        return redirect('/')



    