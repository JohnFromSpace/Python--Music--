from earsketch import *

init()
setTempo(120)

clip = Y25_KEY_1

pointA = 1
repeat = 5
pointB = pointA + repeat

fitMedia(clip, 1, 1, 2)

for i in range(0, repeat):
    fitMedia(clip, 2, pointA + i, pointB + i )

fitMedia(clip, 3, pointA + 4, pointB + 10)

setEffect(1, VOLUME, GAIN, -10)

finish()
