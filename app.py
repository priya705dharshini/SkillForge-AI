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
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        skills TEXT,
        career_goal TEXT,
        interests TEXT
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message TEXT,
        response TEXT,
        created_at TEXT
    )
    ''')
    # ensure a demo user exists
    cur.execute('SELECT COUNT(*) as c FROM users WHERE id = 1')
    if cur.fetchone()['c'] == 0:
        cur.execute('INSERT INTO users (id, name, skills, career_goal, interests) VALUES (?,?,?,?,?)',
                    (1, 'Alex', 'Python,Data Analysis', 'Python Developer', 'AI,Machine Learning'))
    conn.commit()
    conn.close()

app = Flask(__name__)

# Initialize DB immediately to avoid compatibility issues with Flask versions
init_db()

@app.route('/')
def index():
    return redirect(url_for('chat'))

@app.route('/chat')
def chat():
    # For demo purposes we use user_id=1; in real app use auth
    user_id = request.args.get('user_id', 1)
    conn = get_db_connection()
    chats = conn.execute('SELECT * FROM chats WHERE user_id = ? ORDER BY created_at DESC LIMIT 50', (user_id,)).fetchall()
    conn.close()
    return render_template('chat.html', user_id=user_id, chats=chats)

def generate_ai_response(user, message):
    # Very simple response generator that includes remembered user info
    name = user['name'] if user else 'User'
    career = user['career_goal'] if user else None
    interests = user['interests'] if user else None
    skills = user['skills'] if user else None

    prefix = ''
    if career or interests or skills:
        parts = []
        if career:
            parts.append(career)
        if interests:
            parts.append(interests)
        if skills:
            parts.append(skills)
        prefix = f"Based on your {' and '.join(parts)}, "

    # Tailor short suggestion for the example "Suggest projects"
    if 'suggest project' in message.lower() or 'suggest projects' in message.lower():
        return f"{prefix}I recommend building portfolio projects that showcase practical use of {skills.split(',')[0] if skills else 'your skills'}, such as a data pipeline, a web app, or an AI prototype."

    # default echo with personalization
    return f"{prefix}{name}, I heard: '{message}'. I can help — ask for project ideas, roadmaps, or interview prep."

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json() or {}
    user_id = data.get('user_id', 1)
    message = data.get('message', '').strip()
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    ai_response = generate_ai_response(user, message)

    now = datetime.utcnow().isoformat()
    conn.execute('INSERT INTO chats (user_id, message, response, created_at) VALUES (?,?,?,?)',
                 (user_id, message, ai_response, now))
    conn.commit()
    conn.close()

    return jsonify({'response': ai_response})

@app.route('/chat-history')
def chat_history():
    user_id = request.args.get('user_id', 1)
    conn = get_db_connection()
    chats = conn.execute('SELECT * FROM chats WHERE user_id = ? ORDER BY created_at DESC', (user_id,)).fetchall()
    conn.close()
    return render_template('chat_history.html', chats=chats)

if __name__ == '__main__':
    app.run(debug=True)
