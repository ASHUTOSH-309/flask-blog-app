from app import app
from flask import render_template

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