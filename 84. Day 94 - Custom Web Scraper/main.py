from PIL import ImageGrab
import time

end_time = time.time() + 10

while time.time() < end_time:
    time.sleep(2)
    image = ImageGrab.grab((200, 660, 260, 750))
    x = image.getdata()
    x = list(x)
    with open('data.txt', 'w') as f:
        f.write(str(x))
    print(x)
    print(x.count((83, 83, 83)))
    print(x.count((255, 255, 255)))
    print(len(x))
    print('-------------------')
    break
