from flask import Flask, render_template, url_for
import dataManager as D
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    awards = D.get_awards()
    title = D.get_title()
    subtitle = D.get_subtitle()
    image = D.get_image()
    read_more = D.get_read_more()
    css = url_for("static", filename="css/base.css")
    return render_template("base.html", 
        title=title, subtitle=subtitle, 
        image=image, awards=awards, read_more=read_more,
        css=css)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')