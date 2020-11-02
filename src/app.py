from flask import request, redirect, url_for, session, render_template
from api.util.config import app
from api.handler.users import UsersHandler
from api.handler.services import ServicesHandler

@app.route('/')
def main():
    return "hi"

@app.route('/users', methods=['GET'])
def getAllUsers():
    return UsersHandler.getAllUsers()

@app.route('/users/<int:uid>', methods=['GET'])
def getUserById(uid):
    return UsersHandler.getUserById(uid)

@app.route('/owners', methods=['GET'])
def getOwners():
    return UsersHandler.getOwners()

@app.route('/customers', methods=['GET'])
def getCustomers():
    return UsersHandler.getCustomers()

@app.route('/services', methods=['GET'])
def getAllServices():
    return ServicesHandler.getAllServices()

@app.route('/services/<int:sid>', methods=['GET'])
def getServicesById(sid):
    return ServicesHandler.getServiceById(sid)

#     msg = ''
#     # Check if "username" and "password" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']

#         #Fetch User by username and password
#         user = DL.login(username,password)

#         # If user exists in users table in out database
#         if user:
#             # Create session data, we can access this data in other routes
#             session['loggedin'] = True
#             session['id'] = user['userId']
#             session['username'] = user['username']
#             session['role'] = user['role']
            
#             # Redirect to home page depending on role
#             if user['role'] == 'customer':
#                 return redirect(url_for('home'))
#             else:
#                 return redirect(url_for('businessHome'))
#         else:
#             # user doesnt exist or username/password incorrect
#             msg = 'Incorrect username/password!'
#     return render_template('login.html', msg=msg)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     msg=''
#     # Check if "username", "password" and "email" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         #Map Form into User Model object
#         userModel = models.User(username=request.form['username'], password=request.form['password'], 
#             email=request.form['email'], first_name=request.form['first_name'], last_name=request.form['last_name'], role='customer')

#         # Check if user exists using MySQL
#         user = DL.getUserByUsername(userModel.username)

#         # If user exists show error and validation checks
#         if user:
#             msg = 'User already exists!'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', userModel.email):
#             msg = 'Invalid email address!'
#         elif not re.match(r'[A-Za-z0-9]+', userModel.username):
#             msg = 'Username must contain only characters and numbers!'
#         elif not userModel.username or not userModel.password or not userModel.email:
#             msg = 'Please fill out the form!'
#         else:
#             # User doesnt exists and the form data is valid, now insert new User into user table
#             DL.register(userModel)
#             msg = 'You have successfully registered!'
#     elif request.method == 'POST':
#         # Form is empty... (no POST data)
#         msg = 'Please fill all fields!'
#     # Show registration form with message (if any)
#     return render_template('register.html', msg=msg)

# @app.route('/logout')
# def logout():
#     # Remove session data, this will log the user out
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('username', None)
#     session.pop('role', None)
#     # Redirect to login page
#     return redirect(url_for('login'))

# #Customer Area
# @app.route('/customer/home')
# def home():
#     # Check if user is loggedin
#     if 'loggedin' in session:
#         # User is loggedin show them the home page
#         return render_template('home.html', username=session['username'])
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))

# @app.route('/customer/profile')
# def profile():
#     # Check if user is loggedin and its role
#     if 'loggedin' in session and session['role'] == 'customer':
#         # We need all the account info for the user so we can display it on the profile page
#         account = DL.getUserByUsername(session['username'])
#         # Show the profile page with account info
#         return render_template('profile.html', account=account)
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))

# @app.route('/customer/businessRegister', methods=['GET', 'POST'])
# def businessRegister():
#     if 'loggedin' in session and session['role'] == 'customer':
#         msg=''
#         # Check if "username", "password" and "email" POST requests exist (user submitted form)
#         if (request.method == 'POST' and 'business_name' in request.form 
#             and 'business_email' in request.form and 'business_phone' in request.form
#             and 'address' in request.form and 'address' in request.form
#             and 'city' in request.form and 'zip_code' in request.form
#             and 'max_capacity' in request.form):
#             #Map Form into User Model object
#             businessModel = models.Business(business_name=request.form['business_name'], business_email=request.form['business_email'], 
#             business_phone=request.form['business_phone'], address=request.form['address'], city=request.form['city'],
#             zip_code=request.form['zip_code'], max_capacity=request.form['max_capacity'], business_ownerId=session['id'])

#             # Validation checks
#             if not re.match(r'[^@]+@[^@]+\.[^@]+', businessModel.business_email):
#                 msg = 'Invalid business email address.'
#             elif not re.match(r'[A-Za-z0-9]+', businessModel.business_name):
#                 msg = 'Business name must contain only characters and numbers.'
#             elif not re.search('\w{3}-\w{3}-\w{4}', businessModel.business_phone):
#                 msg = 'The format for business phone is: ###-###-####.'
#             elif not re.match('[0-9]{5}', businessModel.zip_code):
#                 msg = 'The format for zip code is: #####'
#             elif not re.match('^[0-9 -]+$', businessModel.max_capacity):
#                 msg = 'Max Capacity must be a number.'
#             else:
#                 # The form data is valid, now insert new Business into business table
#                 DL.registerBusiness(businessModel)
                
#                 #Update user role to 'owner'
#                 DL.updateRole(businessModel.business_ownerId, 'owner')
#                 msg = 'You have successfully registered your business!'
#         elif request.method == 'POST':
#             # Form is empty... (no POST data)
#             msg = 'Please fill all fields!'
#         return render_template('businessRegister.html', msg=msg)
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))

# #Business Owner Area
# @app.route('/business/home')
# def businessHome():
#     if 'loggedin'in session and session['role'] == 'owner':
#         #TODO: fetch and show business info

#         #Show the business home page
#         return render_template('businessHome.html', username=session['username'])
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))

# @app.route('/business/profile')
# def businessProfile():
#     if 'loggedin' in session and session['role'] == 'owner':
#         # We need all the account info for the user so we can display it on the profile page
#         account = DL.getUserByUsername(session['username'])

#         #TODO: fetch and show business info

#         #Show the business profile with business info
#         return render_template('businessProfile.html', account=account)
#     # User is not loggedin redirect to login page
#     return redirect(url_for('login'))






# @app.route('/login', methods=['POST'])
# def login():
#     return UsersHandler.login(request.json)

# @app.route('/logout', methods=['GET'])
# def login():
#     return UsersHandler.logout()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')