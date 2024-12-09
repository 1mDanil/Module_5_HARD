from multiprocessing.resource_tracker import register
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now       #Изначально 0
        self.adult_mode = adult_mode   #По умоллчанию False

class UrTube:
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def __log_in__(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register (self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users) != True:
            self.users.append(User(nickname, password, age))
        else:
            print(f'Пользователь {nickname} уже существует')
        self.__log_in__(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *others):
        for new_video in others:
            if any(video.title == new_video.title for video in self.videos) == False:
                self.videos.append(new_video)

    def get_videos(self, word):
        list = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                list.append(video.title)

        return (list)

    def watch_video(self, film_name):
        if self.current_user != None:
            for video in self.videos:
                if video.title == film_name:
                    if video.adult_mode == False or (video.adult_mode == True  and self.current_user.age >= 18):
                        for time in range(video.duration):
                            print(time + 1, end=' ')
                            sleep(1)
                        print('Конец видео')
                        video.time_now = 0
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 1, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')