from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField

class Calculator(FlaskForm):
    expression = HiddenField('Expression') #keep track of expressions

    # number buttons
    num1 = SubmitField('1')
    num2 = SubmitField('2')
    num3 = SubmitField('3')
    num4 = SubmitField('4')
    num5 = SubmitField('5')
    num6 = SubmitField('6')
    num7 = SubmitField('7')
    num8 = SubmitField('8')
    num9 = SubmitField('9')
    num0 = SubmitField('0')

    # Operations
    button_add = SubmitField('+')
    button_subtract = SubmitField("-")
    button_divide = SubmitField("/")
    button_multiply = SubmitField("*")

    # others
    button_clear = SubmitField("C")
    button_equal = SubmitField("=")

    # cosine and sine buttons
    button_cos = SubmitField('cos')
    button_sin = SubmitField('sin')

    
   # Add the close parenthesis button here
    button_close_paren = SubmitField(')')