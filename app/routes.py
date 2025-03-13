from app import app
from flask import render_template,flash,redirect,request,url_for
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
    print(request.form)
    form=LoginForm()
    """ the form.validate ensures that the constrainnts are enforced properly over the input fields """
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In',form=form)



"""  Flask-WTF Populates form Automatically
form.validate_on_submit() does two things:
Checks if the request is a POST request.
Validates and populates the form fields from request.form. """

         