class FitnessCenter:
    def __init__(self, code_client, year, month, minutes):
        self.code_client = code_client
        self.year = year
        self.month = month
        self.minutes = minutes
    def __repr__(self):
        return (f"Код клиента: {self.code_client}\n"
                f"Год: {self.year}\n"
                f"Месяц: {self.month}\n"
                f"Продолжительность: {self.minutes} мин")
sessions = [
    FitnessCenter("A233", 2025, 5, 45),
    FitnessCenter("A005", 2025, 6, 60),
    FitnessCenter("E066", 2025, 6, 90),
    FitnessCenter("C344", 2025, 4, 120),
    FitnessCenter("F948", 2025, 7, 210)
]
longest_session = max(sessions, key=lambda session: session.minutes)
shortest_session = min(sessions, key=lambda session: session.minutes)
print(f"Самое продолжительное занятие: \n {longest_session}")
print(f"Самое короткое занятие: \n {shortest_session}")