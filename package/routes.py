from package import app, request, render_template
from package.forms import Calculator
from package.models import Database  # Make sure this is your calculation model
from package import db

@app.route("/", methods=['GET', 'POST'])
def calculator():
    form = Calculator()  
    expression = form.expression.data or ""  # Retrieve expression data from form

    if request.method == "POST" and form.validate_on_submit():  # Ensure it's a POST and form was submitted
        # Append button value to the expression
        if form.num1.data:
            expression += "1"
        elif form.num2.data:
            expression += "2"
        elif form.num3.data:
            expression += "3"
        elif form.num4.data:
            expression += "4"
        elif form.num5.data:
            expression += "5"
        elif form.num6.data:
            expression += "6"
        elif form.num7.data:
            expression += "7"
        elif form.num8.data:
            expression += "8"
        elif form.num9.data:
            expression += "9"
        elif form.num0.data:
            expression += "0"
        
        # Handle operators
        elif form.button_add.data:
            expression += "+"
        elif form.button_subtract.data:
            expression += "-"
        elif form.button_divide.data:
            expression += "/"
        elif form.button_multiply.data:
            expression += "*"
        
        # Clear expression
        elif form.button_clear.data:
            expression = ""
        
        # Calculate the result when '=' is pressed
        elif form.button_equal.data:
            try:
                result = eval(expression)  
                expression = str(result)
                calculation = Database(expression=expression, result=str(result))  # Save to database
                db.session.add(calculation)
                db.session.commit()

            except Exception:
                expression = "Error"

        # Update the hidden field with the current expression
        form.expression.data = expression 

    return render_template("calculator.html", form=form, expression=expression)

@app.route("/history", methods=['GET'])
def history_page():
    calculations = Database.query.all() 
    return render_template("history.html", calculations=calculations) 
