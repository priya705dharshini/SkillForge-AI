from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
from datetime import datetime
import os


DB_PATH = os.path.join(os.path.dirname(__file__), 'data.db')



def get_db_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn





def init_db():

    conn = get_db_connection()

    cur = conn.cursor()


    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        skills TEXT,
        career_goal TEXT,
        interests TEXT
    )
    ''')



    cur.execute('''
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message TEXT,
        response TEXT,
        created_at TEXT
    )
    ''')



    # Demo user

    cur.execute(
        'SELECT COUNT(*) as c FROM users WHERE id=1'
    )


    if cur.fetchone()['c'] == 0:

        cur.execute(
        '''
        INSERT INTO users
        (id,name,skills,career_goal,interests)
        VALUES(?,?,?,?,?)
        ''',
        (
            1,
            'Priyadharshini',
            'Java,Python,HTML,CSS,AI,Machine Learning',
            'Software Engineer',
            'AI,Full Stack Development,Data Science'
        )
        )


    conn.commit()

    conn.close()





app = Flask(__name__)



init_db()





@app.context_processor
def inject_year():

    return {
        "current_year": datetime.now().year
    }







@app.route('/')
def index():

    return redirect(url_for('chat'))







@app.route('/chat')
def chat():

    user_id=request.args.get('user_id',1)


    conn=get_db_connection()


    chats=conn.execute(
        '''
        SELECT *
        FROM chats
        WHERE user_id=?
        ORDER BY id ASC
        ''',
        (user_id,)
    ).fetchall()


    conn.close()


    return render_template(
        'chat.html',
        user_id=user_id,
        chats=chats
    )








def generate_ai_response(user,message):


    name=user['name'] if user else "User"

    skills=user['skills'] if user else ""

    career=user['career_goal'] if user else ""

    interests=user['interests'] if user else ""



    msg=message.lower()



    if "project" in msg:

        return f"""
{name}, based on your skills ({skills}), 
I recommend these projects:

1. AI Career Assistant using Flask
2. Machine Learning Prediction System
3. Full Stack Portfolio Application
4. Data Analysis Dashboard

These projects will improve your {career} profile.
"""




    elif "roadmap" in msg:

        return f"""
{name}, your {career} roadmap:

Step 1:
Strengthen Java, Python and DSA

Step 2:
Learn Web Development
(HTML, CSS, JavaScript, React)

Step 3:
Build AI and Full Stack projects

Step 4:
Practice coding interviews and system design.
"""




    elif "skill" in msg or "gap" in msg:

        return f"""
{name}, skill gap analysis:

Current skills:
{skills}

Recommended improvements:

- Advanced DSA
- Backend Development
- Cloud Basics
- AI/ML deployment
- Communication skills
"""




    elif "career" in msg:

        return f"""
{name}, your career goal is {career}.

Based on your interests:
{interests}

Recommended roles:

- Software Engineer
- AI Engineer
- Full Stack Developer
- Data Engineer
"""




    else:

        return f"""
{name}, I understood your query:

"{message}"

I can help you with:

• Career analysis
• Skill gap detection
• Learning roadmap
• Project recommendations
• Interview preparation
"""









@app.route('/api/chat',methods=['POST'])
def api_chat():


    data=request.get_json() or {}


    user_id=data.get('user_id',1)

    message=data.get('message','').strip()



    if not message:

        return jsonify({
            "error":"Message required"
        }),400





    conn=get_db_connection()



    user=conn.execute(
        'SELECT * FROM users WHERE id=?',
        (user_id,)
    ).fetchone()



    response=generate_ai_response(
        user,
        message
    )



    now=datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )



    conn.execute(
        '''
        INSERT INTO chats
        (user_id,message,response,created_at)
        VALUES(?,?,?,?)
        ''',
        (
            user_id,
            message,
            response,
            now
        )
    )


    conn.commit()

    conn.close()



    return jsonify({
        "response":response
    })









@app.route('/chat-history')
def chat_history():


    user_id=request.args.get(
        'user_id',
        1
    )


    conn=get_db_connection()


    chats=conn.execute(
        '''
        SELECT *
        FROM chats
        WHERE user_id=?
        ORDER BY id DESC
        ''',
        (user_id,)
    ).fetchall()


    conn.close()



    return render_template(
        'chat_history.html',
        chats=chats
    )









@app.route('/profile')
def profile():


    user_id=request.args.get(
        'user_id',
        1
    )


    conn=get_db_connection()



    user=conn.execute(
        'SELECT * FROM users WHERE id=?',
        (user_id,)
    ).fetchone()



    conn.close()



    if user:

        user_safe=dict(user)

        user_safe.setdefault(
            'education',
            'B.E Computer Science Engineering'
        )


    else:

        user_safe=None



    return render_template(
        'profile.html',
        user=user_safe
    )









@app.route('/dashboard')
def dashboard():


    user_id=request.args.get(
        'user_id',
        1
    )


    return render_template(
        'dashboard.html',
        user_id=user_id
    )








@app.errorhandler(404)
def page_not_found(e):

    return render_template(
        '404.html'
    ),404









if __name__=="__main__":

    app.run(
        debug=True
    )