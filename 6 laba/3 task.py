from datetime import datetime

class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = datetime.strptime(date_start, "%d.%m.%Y %H:%M")
        self.DateFinish = datetime.strptime(date_finish, "%d.%m.%Y %H:%M")
        self.Description = description

    def __str__(self):
        return (f"Занятие: {self.Description}\n"
                f"Начало: {self.DateStart.strftime('%d.%m.%Y %H:%M')}\n"
                f"Конец: {self.DateFinish.strftime('%d.%m.%Y %H:%M')}")

tasks = [
    Task("14.06.2025 10:50", "14.05.2024 13:10", "Пары"),
    Task("17.06.2025 13:00", "17.06.2025 15:30", "Маникюр"),
    Task("14.05.2025 20:00", "14.05.2025 20:40", "Репетитор"),
    Task("19.06.2025 8:30", "19.06.2025 10:00", "Экзамен"),
    Task("15.06.2025 18:00", "15.06.2025 20:00", "Занятие по гитаре")
]

latest_task = max(tasks, key=lambda task: task.DateFinish)

print("Занятие, которое заканчивается позже всех")
print(latest_task)