import datetime as dt

FORMAT = '%H:%M:%S'
WEIGHT = 79
HEIGHT = 192
K_1 = .035
K_2 = .029
STEP_M = .75
TRANSFER_COEFF = 1000


def check_time(time):
    pass


def check_steps(steps):
    ...


data = [('09:36:02', 15302), ('10:09:00', 17400), ('05:00:00', 3892), ('', 2100), ()]

storage_data = {data[i][0]: data[i][1] for i in range(len(data)) if data[i]}

for time, steps in storage_data.items():
    if not (check_time(time) and check_steps(steps)):
        print('Err')
        break
