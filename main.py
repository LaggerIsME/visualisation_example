import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def task_one():
    # Диаграмма с оценками студентов по предметам
    df = pd.DataFrame([
        ['Sadykov \n Abay', 4.0, 3.0, 2.5, 4.0, 3],
        ['Rakhym \n Rakhymzhan', 2.0, 3.0, 4.0, 3.2, 4.0],
        ['Salen \n Madina', 3, 4.0, 2.3, 4.0, 2.1],
    ],
        columns=['Full name', 'Python', 'Kazakh', 'English', 'DBMS', 'Statistics'])
    df.plot(x='Full name',
            kind='bar',
            figsize=(16, 9))
    plt.grid()
    plt.ylabel('Grades')
    plt.title('All grades of each student')
    plt.show()


def task_two():
    # График изменения погоды
    # Определенный город
    cities = ['Astana', 'Karaganda', 'Almaty']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    n = len(days)
    m = len(cities)
    temperatures = []
    # Двумерный массив m * n(3 на 7)
    print('Wait, I am parsing')
    for i in range(m):
        temperatures.append([0] * n)

    # Создание ссылки для поискового запроса
    for i in range(len(cities)):
        for j in range(len(days)):
            url = f"https://www.google.com/search?q=weather+{cities[i]}+{days[j]}"
            # Получаю сайт
            html = requests.get(url).content
            # Преобразую в понятный для Python формат
            soup = BeautifulSoup(html, 'html.parser')
            # Блок с нужной информацией преобразую в список
            info = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text.split()
            # Из всего списка данных достаю лишь температуры
            mod_info = [i for i in info if '°C' in i]
            # Удаляю знак температуры и преобразую в числа
            temperature = int([s.replace('°C', '') for s in mod_info][0])
            # Заполняю массив данных о температуре
            temperatures[i][j] = temperature
            # Задержка, чтоб не приняло за спам
            time.sleep(0.3)
        if i < 2:
            print(f'Plz wait I parsed only {i + 1} cities')
        else:
            print('I did it')
    df = pd.DataFrame([
        [days[0], temperatures[0][0], temperatures[1][0], temperatures[2][0]],
        [days[1], temperatures[0][1], temperatures[1][1], temperatures[2][1]],
        [days[2], temperatures[0][2], temperatures[1][2], temperatures[2][2]],
        [days[3], temperatures[0][3], temperatures[1][3], temperatures[2][3]],
        [days[4], temperatures[0][4], temperatures[1][4], temperatures[2][4]],
        [days[5], temperatures[0][5], temperatures[1][5], temperatures[2][5]],
        [days[6], temperatures[0][6], temperatures[1][6], temperatures[2][6]]
    ],
        columns=['Days of Week', cities[0], cities[1],
                 cities[2]])
    df.plot(x='Days of Week')
    plt.ylabel('Temperature(C)')
    plt.title('The changes of temperature in cities during a week')
    plt.grid()
    plt.show()


def task_three():
    df = pd.DataFrame([
        ['Kazakh', 1, 1, 1, 2, 1],
        ['Russian', 2, 1, 1, 1, 1],
        ['Python', 1, 1, 2, 2, 1],
        ['DBMS', 1, 1, 1, 1, 1],
        ['English', 2, 1, 1, 1, 1],
    ],
        columns=['Subjects', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday'])
    fig, axs = plt.subplots(3, 2, figsize=(16, 9))
    plt.suptitle("Comparison of disciplines in each day of week")
    ax1 = axs[0, 0]
    ax1.set_title('Monday')
    ax1.pie(df['Monday'], autopct='%1.1f%%', labels=df['Subjects'])

    ax2 = axs[0, 1]
    ax2.set_title('Tuesday')
    ax2.pie(df['Tuesday'], autopct='%1.1f%%', labels=df['Subjects'])

    ax3 = axs[1, 0]
    ax3.set_title('Wednesday')
    ax3.pie(df['Wednesday'], autopct='%1.1f%%', labels=df['Subjects'])

    ax4 = axs[1, 1]
    ax4.set_title('Thursday')
    ax4.pie(df['Thursday'], autopct='%1.1f%%', labels=df['Subjects'])

    ax5 = axs[2, 0]
    ax5.set_title('Friday')
    ax5.pie(df['Friday'], autopct='%1.1f%%', labels=df['Subjects'])

    # Удаляю ненужную ось
    fig.delaxes(axs[2, 1])
    plt.show()


def task_four():
    df = pd.DataFrame([
        ['Sleeping', 30, 30, 30, 30, 10],
        ['Working', 20, 25, 40, 25, 70],
        ['Eating', 20, 15, 10, 25, 10],
        ['Travelling', 20, 10, 15, 10, 5],
        ['Relaxing', 10, 20, 5, 10, 5],
    ],
        columns=['Day routine', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday'])
    fig, axs = plt.subplots(3, 2, figsize=(16, 9))
    plt.suptitle("Comparison of day routine in each day of week")
    ax1 = axs[0, 0]
    ax1.set_title('Monday')
    ax1.pie(df['Monday'], autopct='%1.1f%%', labels=df['Day routine'])

    ax2 = axs[0, 1]
    ax2.set_title('Tuesday')
    ax2.pie(df['Tuesday'], autopct='%1.1f%%', labels=df['Day routine'])

    ax3 = axs[1, 0]
    ax3.set_title('Wednesday')
    ax3.pie(df['Wednesday'], autopct='%1.1f%%', labels=df['Day routine'])

    ax4 = axs[1, 1]
    ax4.set_title('Thursday')
    ax4.pie(df['Thursday'], autopct='%1.1f%%', labels=df['Day routine'])

    ax5 = axs[2, 0]
    ax5.set_title('Friday')
    ax5.pie(df['Friday'], autopct='%1.1f%%', labels=df['Day routine'])

    # Удаляю ненужную ось
    fig.delaxes(axs[2, 1])
    plt.show()


def task_five():
    # График изменения погоды
    df = pd.DataFrame([
        ['00:00', 25, 20, 24, 25, 28],
        ['04:00', 24, 25, 26, 27, 29],
        ['08:00', 23, 27, 28, 29, 30],
        ['12:00', 25, 29, 30, 26, 31],
        ['16:00', 27, 30, 29, 28, 29],
        ['20:00', 25, 26, 26, 21, 27],
    ],
        columns=['Time', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday',
                 ])
    plt.grid()
    plt.title('The dependence of the weather data for the week by day ')
    plt.xlabel('Time')
    plt.ylabel('Temperature(C)')
    plt.plot(df['Time'], df['Monday'])
    plt.plot(df['Time'], df['Tuesday'], '-')
    plt.plot(df['Time'], df['Wednesday'], '--')
    plt.plot(df['Time'], df['Thursday'], '-.')
    plt.plot(df['Time'], df['Friday'], ':')

    # Исключаю Time из нужных мне колонн
    plt.legend(df.columns.drop('Time'), loc='lower right')
    plt.show()


def task_six():
    df = pd.DataFrame([
        ['Midterm', 70, 30, 50],
        ['Endterm', 80, 50, 70],
        ['Final', 50, 70, 90],
    ],
        columns=['The type of Exam', '4 Trimester', '5 Trimester', '6 Trimester'])
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    plt.suptitle("Comparison of Exam grades")

    ax1 = axs[0, 0]
    ax1.set_ylabel('Percentage(%)')
    ax1.set_title('4th Trimester')
    ax1.grid()
    for i in range(3):
        ax1.bar(df['The type of Exam'].iloc[i], df['4 Trimester'].iloc[i], 0.3)
        i = i + 1

    ax2 = axs[0, 1]
    ax2.set_ylabel('Percentage(%)')
    ax2.grid()
    ax2.set_title('5th Trimester')
    for i in range(3):
        ax2.bar(df['The type of Exam'].iloc[i], df['5 Trimester'].iloc[i], 0.3)
        i = i + 1

    ax3 = axs[1, 0]
    ax3.set_ylabel('Percentage(%)')
    ax3.grid()
    ax3.set_title('6th Trimester')
    for i in range(3):
        ax3.bar(df['The type of Exam'].iloc[i], df['6 Trimester'].iloc[i], 0.3)
        i = i + 1

    # Удаляю ненужную ось
    fig.delaxes(axs[1, 1])
    plt.show()


def main():
    task_one()
    task_two()
    task_three()
    task_four()
    task_five()
    task_six()


if __name__ == "__main__":
    main()
