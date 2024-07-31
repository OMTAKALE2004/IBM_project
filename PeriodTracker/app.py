from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    cycle_length = db.Column(db.Integer, nullable=False)
    period_length = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cycle_length = request.form['cycle_length']
        period_length = request.form['period_length']
        start_date = request.form['start_date']
        new_user = User(username=username, password=password, cycle_length=cycle_length,
                        period_length=period_length, start_date=datetime.strptime(start_date, '%Y-%m-%d'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    user = User.query.filter_by(username=session['username']).first()
    return render_template('dashboard.html', user=user)

@app.route('/calender')
def calendar_view():
    user = User.query.filter_by(username=session['username']).first()
    events = []

    current_date = datetime.combine(user.start_date, datetime.min.time())
    end_date = datetime.today() + timedelta(days=365)

    while current_date < end_date:
        if (current_date - datetime.combine(user.start_date, datetime.min.time())).days % user.cycle_length == 0:
            events.append({
                'start': current_date,
                'end': current_date + timedelta(days=user.period_length - 1),
                'type': 'period'
            })
        if (current_date - datetime.combine(user.start_date, datetime.min.time())).days % user.cycle_length == user.cycle_length // 2:
            events.append({
                'start': current_date,
                'end': current_date,
                'type': 'ovulation'
            })
        current_date += timedelta(days=1)

    return render_template('calender1.html', events=events)

@app.route('/log')
def log_view():
    user = User.query.filter_by(username=session['username']).first()
    return render_template('log.html', user=user, timedelta=timedelta)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
