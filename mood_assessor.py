import datetime
import os

def assess_mood():
    numberFromMood = {"happy": 2, "relaxed": 1, "apathetic": 0, "sad": -1, "angry": -2}

    def get_date_today():
        date_today = datetime.date.today()
        return str(date_today)

    if not os.path.exists('data'):
        os.makedirs('data')
    mood_diary_path = 'data/mood_diary.txt'

    date_today = get_date_today()

    lines = []
    if os.path.exists(mood_diary_path):
        with open(mood_diary_path, 'r') as file:
            lines = file.readlines()
            if any(line.startswith(date_today) for line in lines):
                return
    while True:
        mood = input("Enter your mood today (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood in numberFromMood:
            mood_value = numberFromMood[mood]
            break

    with open(mood_diary_path, 'a') as file:
        file.write(f"{date_today} {mood_value}\n")

    lines.append(f"{date_today} {mood_value}\n")
    if len(lines) >= 7:
        last_week = [int(line.split()[1]) for line in lines [-7:]]
        happy_tally = last_week.count(2)
        sad_tally = last_week.count(-1)
        apathetic_tally = last_week.count(0)
        average_mood = round(sum(last_week) / 7)
        if happy_tally >= 5:
            diagnosis = "manic"
        elif sad_tally >= 4:
            diagnosis = "depressive"
        elif apathetic_tally >= 6:
            diagnosis = "schizoid"
        else:
            diagnosis = next(key for key, value in numberFromMood.items() if value == average_mood)
        print(f"Your diagnois: {diagnosis}!")