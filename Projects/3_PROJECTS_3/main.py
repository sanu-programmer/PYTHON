import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the dataset and train the model
iris = load_iris()
X = iris.data
y = iris.target

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict function for GUI
def predict_flower():
    try:
        sl = float(entry_sl.get())
        sw = float(entry_sw.get())
        pl = float(entry_pl.get())
        pw = float(entry_pw.get())

        input_data = [[sl, sw, pl, pw]]
        prediction = model.predict(input_data)[0]
        flower_name = iris.target_names[prediction]

        messagebox.showinfo("Prediction Result", f"🌼 The predicted flower is: {flower_name}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("🌲 Random Forest Iris Flower Predictor")

tk.Label(root, text="Enter Flower Measurements", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

tk.Label(root, text="Sepal Length (cm):").grid(row=1, column=0, sticky='e')
entry_sl = tk.Entry(root)
entry_sl.grid(row=1, column=1)

tk.Label(root, text="Sepal Width (cm):").grid(row=2, column=0, sticky='e')
entry_sw = tk.Entry(root)
entry_sw.grid(row=2, column=1)

tk.Label(root, text="Petal Length (cm):").grid(row=3, column=0, sticky='e')
entry_pl = tk.Entry(root)
entry_pl.grid(row=3, column=1)

tk.Label(root, text="Petal Width (cm):").grid(row=4, column=0, sticky='e')
entry_pw = tk.Entry(root)
entry_pw.grid(row=4, column=1)

tk.Button(root, text="Predict Flower", command=predict_flower).grid(row=5, columnspan=2, pady=10)

root.mainloop()
