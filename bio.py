from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# PINDAHKAN KE SINI (Di luar blok if __name__)
@app.route('/story')
def story_page():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)