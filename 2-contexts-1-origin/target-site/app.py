from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'sup3r_r4nd0m_k3y'

users = {
    'user1': 'password1',
    'admin': 'sup3r-s3cr3t-4dm1n-p4s5w0rd'
}

api_keys = {
    'user1': 'flag{not_the_apikey_youre_looking_for}',
    'admin': 'flag{gg_you_got_the_correct_apikey}'
}

user_mail = {
    'user1': 'user1@example.com',
    'admin': 'admin@example.com'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        flash('You need to log in first', 'warning')
        return redirect(url_for('login'))
    
    current_user = session['username']
    
    if request.method == 'POST':
        mail = request.form['mail']
        user_mail[current_user] = mail
    
    return render_template('dashboard.html', username=current_user,
                           mail=user_mail[current_user], apikey=api_keys[current_user])

@app.route('/logout')
def logout():
    session.clear()
    
    session.modified = True
    session.permanent = False

    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
