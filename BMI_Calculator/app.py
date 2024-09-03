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
                generated_tips = ["Consult a Healthcare Professional:-  Seek guidance from a doctor or dietitian to create a tailored plan to gain weight safely.", "Nutrient-Rich Diet:-  Prioritize foods high in both calories and nutrients, like full-fat dairy products, whole grains, lean meats, and legumes.", "Gradual Increase in Food Intake:-  Slowly increase the quantity of food consumed to avoid overwhelming the digestive system.", "Supplementation:-  Consider nutritional supplements or meal replacement shakes if recommended by a healthcare provider.", "Address Underlying Health Issues:-  Ensure there are no underlying medical conditions contributing to severe underweight status, such as hyperthyroidism or eating disorders.", "Mindful Eating:-  Practice mindful eating to improve appetite and ensure consistent meal intake."]
            elif 16.5 <= bmi <= 18.5:
                category = "Underweight"
                description = "Person falls in the Underweight Category, which suggests that the person may be undernourished or have a lower-than-recommended body weight."
                generated_tips = ["Increase Caloric Intake:-  Focus on nutrient-dense, calorie-rich foods like nuts, seeds, avocados, whole grains, and lean proteins.", "Eat More Frequently:-  Consume smaller, more frequent meals throughout the day to increase calorie intake.", "Strength Training:-  Engage in resistance exercises like weight lifting to build muscle mass, which can help increase weight.", " Choose Healthy Fats:-  Include healthy fats from sources like olive oil, fatty fish, and nuts to boost calorie intake without unhealthy fats.", "Ensure Protein Intake:-  Protein is essential for muscle growth. Include protein-rich foods like eggs, lean meats, dairy, and legumes in your diet.", "Stay Hydrated:-  Drink fluids that add calories and nutrients, such as smoothies or milk, instead of just water."]
            elif 18.5 < bmi <= 24.9:
                category = "Normal Weight"
                description = "Person falls in the Normal Weight Category, which indicates a healthy weight relative to height."
                generated_tips = ["Balanced Diet:-  Continue to eat a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats.", "Regular Exercise:-  Engage in regular physical activity, including both cardio and strength training exercises, to maintain muscle mass and cardiovascular health.", "Monitor Weight:-  Keep track of your weight regularly to catch any gradual increases or decreases early.", "Healthy Habits:-  Maintain healthy lifestyle habits such as adequate sleep, stress management, and limiting alcohol and processed foods.", "Stay Hydrated:-  Drink plenty of water throughout the day to support metabolism and overall health.", "Periodic Health Check-ups:-  Regular check-ups with a healthcare provider can help monitor and maintain overall health."]
            elif 24.9 < bmi <= 29.9:
                category = "Overweight"
                description = "Person falls in the Overweight Category, which suggests that the person has a higher-than-recommended body weight."
                generated_tips = ["Caloric Deficit:-  Create a calorie deficit by consuming fewer calories than you burn, focusing on nutrient-dense foods to avoid hunger.", "Increase Physical Activity:-  Incorporate more physical activity into your routine, such as brisk walking, cycling, swimming, or strength training.", "Portion Control:-  Be mindful of portion sizes to avoid overeating, even when consuming healthy foods.", "Reduce Sugars and Refined Carbs:-  Limit intake of sugars, sugary drinks, and refined carbohydrates, replacing them with whole grains and vegetables.", "Healthy Snacking:-  Choose healthy snacks like fruits, nuts, or yogurt instead of high-calorie, processed snacks.", "Behavioral Changes:-  Address emotional eating or stress-related eating through mindful eating practices or counseling if necessary."]
            else:
                category = "Obesity"
                description = "Person falls in the Obesity Category, which indicates a significantly higher body weight and increased risk of health issues."
                generated_tips =["Seek Professional Help:-  Consult with a healthcare provider, dietitian, or a weight-loss specialist for personalized advice and support.", "Structured Diet Plan:-  Follow a structured and sustainable diet plan that promotes weight loss while ensuring adequate nutrition.", "Increase Activity Gradually:-  Start with low-impact exercises, like walking or swimming, and gradually increase intensity as fitness improves.", "Increase Activity Gradually:-  Start with low-impact exercises, like walking or swimming, and gradually increase intensity as fitness improves.", "Focus on Whole Foods:-  Prioritize whole foods, including vegetables, lean proteins, and whole grains, while avoiding processed foods and sugary drinks.", "Monitor Progress:-  Regularly track weight, food intake, and physical activity to monitor progress and adjust as needed.", "Address Emotional Factors:-  Consider psychological support or counseling to address emotional eating habits or other underlying issues contributing to obesity.", "Long-Term Commitment:-  Focus on making long-term lifestyle changes rather than temporary diets or quick fixes."]

            return render_template('result.html', bmi=bmi, category=category, description=description, generated_tips=generated_tips)
        except ValueError:
            return "Invalid input"
    return "Error: Missing weight or height"

if __name__ == '__main__':
    app.run(debug=True)



