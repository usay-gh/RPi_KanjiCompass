from sense_hat import SenseHat
import time
#import asyncio

# async def showMeasureMessage():
#     await sense.show_message("Measuring...", scroll_speed = textSpeed, text_colour = foreColor, back_colour = backColor)

def houi_hantei(houikaku):
    ret = ""

    if 360 - 45 <= houikaku < 360 or 0 <= houikaku < 90 - 45 :
        ret = "N"
    elif 90 - 45 <= houikaku < 90 or 90 <= houikaku < 180 - 45 :
        ret = "E"
    elif 180 - 45 <= houikaku < 180 or 180 <= houikaku < 270 - 45:
        ret = "S"
    elif 270 - 45 <= houikaku < 270 or 270 <= houikaku < 360 - 45:
        ret = "W"

    return ret

sense = SenseHat()
#sense.set_imu_config(compass_enabled = True, gyro_enabled = False, accel_enabled = True)
sense.set_rotation(0)
sense.clear()


initMessage = "initializing Sense Hat..."
foreColor = [0, 255, 0]
backColor = [0, 0, 0]
textSpeed = 0.05
#sense.show_message(initMessage, scroll_speed = textSpeed, text_colour = foreColor, back_colour = backColor)

# display splash
sense.load_image("kao.png")
time.sleep(2)

while True:
    # 磁気
    magnetoRaw = sense.get_compass_raw()
    # 加速度
    acceleroRaw = sense.get_accelerometer_raw()
    # 方位角
    houikaku = sense.get_compass()
    # 傾き
    katamuki = sense.get_orientation_degrees()


    print("magneto x: {x:.6g}, y: {y:.6g}, z: {z:.6g}".format(**magnetoRaw))
    print("accelero x: {x:.6g}, y: {y:.6g}, z: {z:.6g}".format(**acceleroRaw))
    print("houikaku: {:.6g}".format(houikaku))
    print("katamuki: p: {pitch}, r: {roll}, y: {yaw}".format(**katamuki))

    houi = houi_hantei(houikaku)
    sense.show_letter(houi, text_colour = foreColor, back_colour = backColor)

    houi_image = ""
    if houi == "N":
        houi_image = "kita.png"
    elif houi == "E":
        houi_image = "higashi.png"
    elif houi == "S":
        houi_image = "minami.png"
    elif houi == "W":
        houi_image = "nishi.png"
    else:
        houi_image = "kao.png"
    sense.load_image(houi_image)
    
#    time.sleep(1)



