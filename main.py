from flask import Flask, render_template, request
app = Flask(__name__)

data = []


@app.route('/')
def index_story():
    return render_template('story.html')


@app.route('/list', methods=["POST", "GET"])
def index_list():
    if request.method == "GET":
        return render_template('list_page.html')
    else:
        id_ = len(data)
        title = request.form["title"]
        story = request.form["story"]
        criteria = request.form["criteria"]
        business_value = request.form["bvalue"]
        estimation = request.form["estimation"]
        status = request.form["status"]

    data.append([id_, title, story, criteria, business_value, estimation, status])
    return render_template('list_page.html', data=data)


@app.route('/delete', methods=["POST"])
def delete_row():
    id_ = list(request.form.keys())[0]
    counter = 0
    for item in data:
        if item[0] == id_:
            data.pop(counter)
        counter += 1
    return render_template("story.html")


if __name__ == '__main__':
    app.run()
