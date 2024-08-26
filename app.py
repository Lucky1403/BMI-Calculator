from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    weight = request.form.get('weight')
    height = request.form.get('height')
    if weight and height:
        try:
            weight = float(weight)
            height = float(height)
            bmi = round(weight / (height ** 2), 2)

            # Determine the BMI category and description
            if bmi < 16.5:
                category = "Severely Underweight"
                description = "Person falls in the Severely Underweight Category, which indicates serious undernutrition and potentially severe health risks."
            elif 16.5 <= bmi <= 18.5:
                category = "Underweight"
                description = "Person falls in the Underweight Category, which suggests that the person may be undernourished or have a lower-than-recommended body weight."
            elif 18.5 < bmi <= 24.9:
                category = "Normal Weight"
                description = "Person falls in the Normal Weight Category, which indicates a healthy weight relative to height."
            elif 24.9 < bmi <= 29.9:
                category = "Overweight"
                description = "Person falls in the Overweight Category, which suggests that the person has a higher-than-recommended body weight."
            else:
                category = "Obesity"
                description = "Person falls in the Obesity Category, which indicates a significantly higher body weight and increased risk of health issues."

            return render_template('result.html', bmi=bmi, category=category, description=description)
        except ValueError:
            return "Invalid input"
    return "Error: Missing weight or height"

if __name__ == '__main__':
    app.run(debug=True)



