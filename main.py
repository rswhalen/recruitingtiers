from flask import Flask, render_template, request
import pgeocode

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        zipcode = request.form['zipcode']
        dist = pgeocode.GeoDistance('us')
        distance = dist.query_postal_code(str(zipcode),"07747")
        if distance > 55:
            tier = "TIER 3"
        elif distance <30:
            tier = "TIER 1"
        else:
            tier = "TIER 2"

        return render_template('zipcode.html', zipcode = tier)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()