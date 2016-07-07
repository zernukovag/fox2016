from drawman import *
from time import sleep

pen_up()
drawman_scale(20)

for i in range(5):
    for j in range(5):

        to_point(0,5*(i-1))
        pen_down()
        to_point(15,5*(j-1))
        pen_up()

sleep(10)