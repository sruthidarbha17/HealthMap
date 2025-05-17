fitness_data = {
    "weight loss": {
        "tips": ["Do cardio like running or cycling.", "Eat a calorie-controlled diet.", "Include strength training."],
        "workout": ["30 mins HIIT 3x/week", "45 mins moderate cardio 4x/week", "Strength training 2-3x/week"],
        "nutrition": "Eat lean proteins and avoid sugary drinks."
    },
    "muscle gain": {
        "tips": ["Lift weights focusing on major muscles.", "Eat protein-rich foods.", "Rest and recover well."],
        "workout": ["Weightlifting 4-5x/week", "Compound lifts (squat, deadlift, bench)", "Increase weights progressively"],
        "nutrition": "Consume extra calories with proteins and carbs."
    },
    "flexibility": {
        "tips": ["Practice yoga or Pilates.", "Warm up before stretching.", "Hold stretches 30+ seconds."],
        "workout": ["30 mins yoga or Pilates daily", "Dynamic stretching", "Daily mobility exercises"],
        "nutrition": "Stay hydrated and eat vitamin-rich foods."
    }
}

def fitness_advice(goal):
    data = fitness_data.get(goal)
    if not data:
        return "Sorry, no advice available for that goal."
    result = f"Tips for {goal.title()}:\n"
    result += "\n".join("- " + tip for tip in data["tips"]) + "\n\n"
    result += "Workouts:\n" + "\n".join("- " + w for w in data["workout"]) + "\n\n"
    result += "Nutrition:\n- " + data["nutrition"]
    return result

goal = input("Enter fitness goal (weight loss, muscle gain, flexibility): ").lower()
print(fitness_advice(goal))
