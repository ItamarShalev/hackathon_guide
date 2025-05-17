from pathlib import Path

from flask import Flask, render_template

current_path = Path(__file__).parent
app_path = current_path / 'src' / 'app'


app = Flask(
    __name__,
    static_folder=str(app_path / 'static'),
    template_folder=str(app_path / 'templates')
)

@app.route('/')
def hello_world():
    return render_template('index.html')


def main():
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True,
        use_reloader=True
    )

if __name__ == '__main__':
    main()
