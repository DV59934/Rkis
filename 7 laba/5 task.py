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
    FitnessCenter("A233", 2023, 5, 45),
    FitnessCenter("A005", 2024, 6, 60),
    FitnessCenter("E066", 2024, 6, 90),
    FitnessCenter("C344", 2025, 4, 120),
    FitnessCenter("F948", 2023, 7, 210),
    FitnessCenter("B734", 2024, 5, 55),
    FitnessCenter("A935", 2025, 6, 70),
    FitnessCenter("C826", 2025, 6, 90),
    FitnessCenter("T305", 2024, 4, 120),
    FitnessCenter("D049", 2023, 7, 100)]

sum_sessions = {}

for session in sessions:
    if session.year in sum_sessions:
        sum_sessions[session.year] += session.minutes
    else:
        sum_sessions[session.year] = session.minutes

max_session = max(sum_sessions.values())
max_year = min([year for year, session in sum_sessions.items() if session == max_session])

print(f"Год с наибольшей суммарной продолжительностью: {max_year}")
print(f"Суммарная продолжительность: {max_session} минут")