from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')

def index():
    user={'username':'Ashutosh'}
    posts=[
        {
            'author':{'username':'John'},
            'body':'Hi, I am john cena, gonna beat brock lesnar today'
        },
        {
            'author':{'username':'anonymous'},
            'body': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ab eius pariatur at amet nesciunt mollitia, consequuntur aliquid repellat magnam?"
        },   
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)


@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    """ the form.validate ensures that the constrainnts are enforced properly over the input fields """
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form)
         