# app.py

from flask import Flask, request, render_template
from sf_authentication import authenticate_to_salesforce
from sf_describe_logic import get_available_objects, describe_object

app = Flask(__name__)

@app.after_request
def apply_security_headers(response):
    # Content Security Policy
    csp_policy = "default-src 'self'; script-src 'self'; object-src 'none';"
    response.headers['Content-Security-Policy'] = csp_policy

    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    return response

@app.route('/')
def index():
    return render_template('index.html')  # A web page with options and forms

@app.route('/describe', methods=['GET', 'POST'])
def describe():
    if request.method == 'POST':
        object_name = request.form.get('object_name')
        environment = request.form.get('environment')
        token_data = authenticate_to_salesforce(environment)
        
        if 'access_token' in token_data:
            result = describe_object(object_name, token_data)
            return render_template('describe_result.html', result=result)
        else:
            return render_template('describe_error.html', error="Salesforce authentication failed.")
    else:
        return render_template('describe_form.html')

# Additional routes for other functionalities

if __name__ == '__main__':
    app.run()
