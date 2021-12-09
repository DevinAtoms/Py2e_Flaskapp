from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spell_card/<spell_name>')
def spell_card(spell_name):
    return 'welcome %s' % spell_name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['nm']
        return redirect(url_for('spell_card', spell_name=name))
    else:
        name = request.args.get('nm')
        return redirect(url_for('spell_card', spell_spell=name))


if __name__ == '__main__':
    app.run(debug=True)
