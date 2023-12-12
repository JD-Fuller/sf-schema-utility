from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from sf_authentication import authenticate_to_salesforce
from sf_describe_logic import get_available_objects, describe_object

# Initialize Flask app and CSRF protection
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YourSecretKeyHere'  # Replace with a real secret key
csrf = CSRFProtect(app)

@app.after_request
def apply_security_headers(response):
    # Content Security Policy
    csp_policy = "default-src 'self'; script-src 'self'; object-src 'none';"
    response.headers['Content-Security-Policy'] = csp_policy

    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'

    # X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'

    # X-XSS-Protection
    response.headers['X-XSS-Protection'] = '1; mode=block'

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
            # Ensure input validation
            if not object_name.isalnum():
                return render_template('describe_error.html', error="Invalid object name.")

            result = describe_object(object_name, token_data)
            return render_template('describe_result.html', result=result)
        else:
            # Log detailed error for internal review and display a generic error message
            app.logger.error("Salesforce authentication failed for environment: " + environment)
            return render_template('describe_error.html', error="Authentication failed.")
    else:
        return render_template('describe_form.html')

# Additional routes for other functionalities

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug mode is off in production
