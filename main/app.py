from flask import Flask, render_template, request, redirect,session
from supabase import create_client
import uuid

app = Flask(__name__)
app.secret_key = 'hfh343535frfrghb56'  # Replace with your own secret key


# Supabase initialize
supabase_url = 'https://iqjbdbarlrocgcjvacfk.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlxamJkYmFybHJvY2djanZhY2ZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgxMDA3ODQsImV4cCI6MjAyMzY3Njc4NH0.lJvH2LNUtqvs_LAzmLB2fNDr19fmBWkDKqTRbbqz6Mw'
supabase = create_client(supabase_url, supabase_key)

@app.route('/register_needy', methods=['POST'])
def register_needy():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
        # Generate unique user ID
    user_id = str(uuid.uuid4())

    # Add user details to the 'needy' table in Supabase
    needy_data = {'id': user_id, 'username': username, 'email': email, 'password': password}
    response = supabase.table('needy').insert(needy_data).execute()
        # return redirect('/needy-login')  # Redirect to login page after successful registration
    return render_template('needy-login.html')



@app.route('/login-needy', methods=['GET', 'POST'])
def login_needy():
    # request=supabase.table('needy').select('username, password').execute()
    # print(request[1][1])
    return render_template('availability.html')





@app.route('/register_donor', methods=['POST'])
def register_donor():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
        # Generate unique user ID
    user_id = str(uuid.uuid4())

    # Add user details to the 'needy' table in Supabase
    needy_data = {'id': user_id, 'username': username, 'email': email, 'password': password}
    response = supabase.table('donor').insert(needy_data).execute()
        # return redirect('/needy-login')  # Redirect to login page after successful registration
    return render_template('donor-login.html')



@app.route('/login-donor', methods=['GET', 'POST'])
def login_donor():
    # username = request.form['username']
    # password = request.form['password']
    # # request=supabase.table('donor').select('username, password').execute()
    # # print(request[1][1])
    # session['username'] = username
    # session['pass'] = password
    return render_template('food-donate.html')

@app.route('/sustainability', methods=['GET', 'POST'])
def sustainability():
    return render_template('sustainability.html')


@app.route('/available_uploads', methods=['POST'])
def available_uploads():
    # Get the form data
    foodname = request.form['foodname']
    meal = request.form['meal']
    quantity = request.form['quantity']
    expiry_date_time = request.form['Expiry-Date-time']
    username=session['username']
    # Insert the food details into the 'food_donations' table in Supabase
    supabase.table('food_donations').insert({
        'username': username,  # Include the username in the insert
        'foodname': foodname,
        'meal': meal,
        'quantity': quantity,
        'expiry_daxte_time': expiry_date_time
    }).execute()

    # # Check if the insert was successful
    # if response.error:
    #     error_message = f"An error occurred: {response.error}"
    #     return render_template('donor-upload.html', error=error_message)
    # else:
    #     return redirect('/success_page')  # Redirect to a success page after successful insertion





# Routes for rendering templates
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/donor-login')
def donor_login():
    return render_template("donor-login.html")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

@app.route('/donor-reg')
def donor_reg():
    return render_template("donor-reg.html")

@app.route('/needy-login')
def needy_login():
    return render_template("needy-login.html")

@app.route('/needy-reg')
def needy_reg():
    return render_template("needy-reg.html")

if __name__ == '__main__':
    app.run(debug=True)
