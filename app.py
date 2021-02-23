import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('Analysing_Student_Behaviour.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        raisedHands = int(request.form['raisedHands'])
        VisitedResources = int(request.form['VisitedResources'])
        AnnouncementsView = int(request.form['AnnouncementsView'])
        Discussion = int(request.form['Discussion'])

    prediction = model.predict([[raisedHands, VisitedResources, AnnouncementsView, Discussion]])
    pred = list(prediction)
    print(pred[0])
    if 0 < len(prediction):
        return render_template('index.html', prediction_text="The student will perform better in {} class".format(pred[0]))
    else:
        return render_template('index.html', prediction_text="Sorry Student is not applicable to apply for any class")
    #
    # return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
