import matplotlib.pyplot as plt
import Tkinter
import pandas as pd
import numpy as np

gun_control = pd.read_csv('guncontrol.csv')
shooting = pd.read_csv('shooting.csv')

#print(shooting)
#print(shooting['week'])

shooting_dates = shooting['week']
gun_dates = gun_control['week']
shooting_web = shooting['shooting']
gun_web = gun_control['gun_control']


plt.plot(shooting_dates, shooting_web, label = 'Shooting Interest')

plt.plot(gun_dates, gun_web, label = 'Gun Control Interest')

plt.title("Search interest in key words 'gun control' vs 'shooting'")
plt.ylabel("Search interest to relative popularity (peak = 100)")
plt.xlabel("Date")

plt.xticks(['2017-03-19', '2017-05-21', '2017-07-23', '2017-10-22', '2017-12-31', '2018-03-04'], ['March 17', 'May 17', 'July 17', 'October 17', 'January 18', 'March 18'])

plt.annotate('Los Vegas Shooting', xy=('2017-10-01', 100), xytext=('2017-05-21', 70), arrowprops =dict(facecolor='black', shrink = 0.05, width=2))
plt.annotate('Parkland Shooting', xy=('2018-02-18', 100), xytext=('2017-10-22', 80), arrowprops =dict(facecolor='black', shrink = 0.05, width=2))

plt.legend(loc='upper left')

plt.show()