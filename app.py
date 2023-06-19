import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime,date #tempo confeir



# cria a conexao com o BD
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# query todos os posts no banco
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post
    

# cria o serviço
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY_DEV')




@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    view_posts = [dict(post) for post in posts]
    agora = datetime.now()
    for post in view_posts:
        post['vencido'] = 'green'
        try: 
            data = datetime.strptime(f"{post['data']} {post['horario']}" , '%Y-%m-%d %H:%M')
            print(data, agora)
            if data <= agora: 
                post['vencido'] = 'red'
        except: 
            post['vencido'] = 'orange'
        
        




    return render_template('index.html', posts=view_posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        return render_template('404.html')
    return render_template('post.html', post=post)



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        horario = request.form['horario']
        data = request.form['data']
        
        
        if not title or not content or not horario or not data:
            flash('Algo Não esta preencido , Verifique !')

            
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, horario, data) VALUES (?, ?, ?, ?)',
                         (title, content, horario, data))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


        


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if post is None:
        return render_template('404.html')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        horario = request.form['horario']
        data = request.form['data']
  
        if not title or not content or not horario or not data:
             flash('Algo Não esta preencido , Verifique !')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title=?, content=?, horario=?, data=? WHERE id=?',
                         (title, content, horario, data, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    if post is None:
        return render_template('404.html')
    
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" Foi Deletado com Exitô!'.format(post['title']))
    return redirect(url_for('index'))


###########################################################################################################teste




# Seu código existente ...


# Filtro personalizado para converter string em datetime.date , porque dava dandio o erro da data ta como string
@app.template_filter('letra_data')
def data(letra_data):
    return datetime.strptime(letra_data, '%Y-%m-%d').date()




@app.template_filter('letra_tempo')
def string_to_time(letra_tempo):
    return datetime.strptime(letra_tempo, '%H:%M').time()



# inicia servico
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)