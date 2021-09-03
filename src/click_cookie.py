import pyautogui


def find_center_on_image(path_image, confidence):
    box = pyautogui.locateOnScreen(path_image, confidence=confidence)
    if not box:
        raise Exception('could not find the image')
    
    return pyautogui.center(box)


def handle_event(timer, frequency, f):
    if timer % frequency != 0:
        return False

    try:
        f()
    except Exception as e:
        return False

    return True


def click_image(path_image, confidence):
    x, y = find_center_on_image(path_image, confidence)
    pyautogui.click(x=x, y=y)


def click_cookie():
    '''
    clicks objects repeatedly.

    golden cookie (GC):

    * run once in 10 seconds
    * try to find a GC for each time
    * click the GC

    idleverse:

    * run once in 100 seconds
    * try to find an available idleverse for each time
    * click the idleverse

    main cookie (MC):

    * run once in 0.02 seconds
    * click the MC where it was initially located
    '''

    try:
        mc_x, mc_y = find_center_on_image('./images/cookie.png', 0.9)
    except:
        raise Exception('could not found main cookie. exit')

    def handle_idleverse():
        click_image('./images/idleverse.png', 0.999)
    

    def handle_golden_cookie():
        click_image('./images/golden_cookie.png', 0.9)

    timer = 0
    while True:
        timer += 1

        pyautogui.click(x=mc_x, y=mc_y, clicks=100, interval=0.02)

        print(timer)

        # exit handler
        cur_x, cur_y = pyautogui.position()
        if cur_x < 100 and cur_y < 100:
            break

        # golden cookie
        if handle_event(timer, 5, handle_golden_cookie):
            print('click golden cookie')

        # idleverse
        if handle_event(timer, 50, handle_idleverse):
            print('buy idleverse')

        # avoid overflow of timer
        if timer > 100:
            timer %= 100


if __name__ == '__main__':
    click_cookie()
