def MicOn():
    # 設定聲音閾值，當音量超過這個值時，觸發相應事件
    input.set_sound_threshold(SoundThreshold.LOUD, Mic * 16)
    # 設定音樂播放的音量，音量根據 Mic 的值調整
    music.set_volume(Mic * 16 - 8)
    # 播放一個短音符 C5 (523Hz) 來指示麥克風已開啟，音符持續一拍的八分之一
    music.play(music.tone_playable(523, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
    # 在 LED 顯示螢幕上顯示一個圖案來指示麥克風開啟狀態
    basic.show_leds("""
        . . # . .
        . # # # .
        . # # # .
        . . # . .
        . # # # .
        """)
    # 顯示當前的 Mic 數值
    basic.show_number(Mic)
# 當 Micro:bit 的 logo 被長按時，執行 on_logo_long_pressed 函數

def on_logo_long_pressed():
    global Mic, act, lastTime
    # 當長按 Micro:bit 的 logo 時
    if Mic > 0:
        # 如果 Mic 的值大於 0，表示麥克風已開啟
        Mic = 0
        # 將 Mic 設為 0 來關閉麥克風
        MicOff()
    else:
        # 呼叫 MicOff 函數來處理麥克風關閉的動作
        # 如果 Mic 的值不大於 0，表示麥克風已關閉
        Mic = Sound
        # 將 Mic 設為 Sound（開啟麥克風）
        act = 0
        # 重置動作計數
        lastTime = input.running_time()
        # 記錄當前時間作為最後一次動作的時間
        MicOn()
    # 呼叫 MicOn 函數來處理麥克風開啟的動作
    basic.pause(200)
    # 清除螢幕上的顯示
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

# 當藍牙連接成功時
# 當藍牙連接成功時，執行 on_bluetooth_connected 函數

def on_bluetooth_connected():
    # 顯示一個 "YES" 圖標來表示連接成功
    basic.show_icon(IconNames.YES)
    # 暫停 5 秒以便用戶看到圖標
    basic.pause(5000)
    # 清除螢幕上的顯示
    basic.clear_screen()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

# Mic關掉
def MicOff():
    basic.show_leds("""
        # . # . .
        . # # # .
        . # # # .
        . . # # .
        . # # . #
        """)
# 當藍牙斷線時
# 當藍牙斷線時，執行 on_bluetooth_disconnected 函數

def on_bluetooth_disconnected():
    # 顯示一個 "NO" 圖標來表示斷線
    basic.show_icon(IconNames.NO)
    # 暫停 5 秒以便用戶看到圖標
    basic.pause(5000)
    # 清除螢幕上的顯示
    basic.clear_screen()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# A按鈕
# 當 A 按鈕被按下時，執行 on_button_pressed_a 函數

def on_button_pressed_a():
    global levelX
    # 當按下 A 按鈕時
    if levelX < max2:
        levelX += 1
    else:
        # 如果 levelX 小於 max2，將 levelX 加 1
        levelX = min2
    # 否則，將 levelX 重設為 min2
    # 顯示一個圓形邊框的 LED 圖案來指示 A 按鈕被按下
    basic.show_leds("""
        . . . . .
        . # . # .
        # . . . #
        . # . # .
        . . . . .
        """)
    # 在 LED 顯示螢幕上顯示當前的 levelX 值
    basic.show_number(levelX)
    # 暫停 200 毫秒以便顯示數字
    basic.pause(200)
    # 清除螢幕上的顯示
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    global Mic
    # 麥克風按鈕
    if Mic == 0:
        MicOff()
    else:
        if Mic > 1:
            Mic += -1
        else:
            Mic = 9
        MicOn()
    basic.pause(100)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# 設定當 P2 觸控引腳被按下時，觸發 on_pin_pressed_p2 函數

def on_pin_pressed_p2():
    # 當 P2 觸控引腳被按下時，執行 Clicks 函數
    Clicks()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

# AB按鈕
# 當 A 和 B 按鈕同時被按下時，執行 on_button_pressed_ab 函數

def on_button_pressed_ab():
    global levelX, levelY
    # 當同時按下 A 和 B 按鈕時
    if levelX == 0:
        # 如果 levelX 為 0，則將 levelX 和 levelY 設定為 5
        levelX = 5
        levelY = 5
        # 顯示一個小鑽石圖標，然後顯示一個大鑽石圖標
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_icon(IconNames.DIAMOND)
    elif levelX == 5:
        # 如果 levelX 為 5，則將 levelX 和 levelY 設定為 0
        levelX = 0
        levelY = 0
        # 顯示一個大鑽石圖標，然後顯示一個小鑽石圖標
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
    # 顯示當前的 levelX 值
    basic.show_number(levelX)
    # 暫停 200 毫秒以便顯示數字
    basic.pause(200)
    # 清除螢幕上的顯示
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# B按鈕
# 當 B 按鈕被按下時，執行 on_button_pressed_b 函數

def on_button_pressed_b():
    global levelY
    # 當按下 B 按鈕時
    if levelY < max2:
        levelY += 1
    else:
        # 如果 levelY 小於 max2，將 levelY 加 1
        levelY = min2
    # 否則，將 levelY 重設為 min2
    # 顯示一個十字形的 LED 圖案來指示 B 按鈕被按下
    basic.show_leds("""
        . . # . .
        . # . # .
        . . . . .
        . # . # .
        . . # . .
        """)
    # 在 LED 顯示螢幕上顯示當前的 levelY 值
    basic.show_number(levelY)
    # 暫停 200 毫秒以便顯示數字
    basic.pause(200)
    # 清除螢幕上的顯示
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    if Mic > 0:
        Clicks()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def Clicks():
    global actTme, act, lastTime
    # 取得當前時間
    actTme = input.running_time()
    # 如果上次動作到現在的時間差小於或等於限制時間（LimitS）或目前狀態是初始狀態（act == 0）
    if actTme - lastTime <= LimitS or act == 0:
        act += 1
        # 增加動作計數
        if act == 1:
            # 如果這是第一次動作，播放 C4 音符 (262Hz) 的短音
            music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
                music.PlaybackMode.IN_BACKGROUND)
        elif act == 2:
            # 如果這是第二次動作，播放 E4 音符 (330Hz) 的短音
            music.play(music.tone_playable(330, music.beat(BeatFraction.SIXTEENTH)),
                music.PlaybackMode.IN_BACKGROUND)
        elif act == 3:
            # 如果這是第三次動作，播放 G4 音符 (392Hz) 的短音
            music.play(music.tone_playable(392, music.beat(BeatFraction.SIXTEENTH)),
                music.PlaybackMode.IN_BACKGROUND)
        else:
            # 如果這是第四次動作或以上，播放 C5 音符 (523Hz) 的短音
            music.play(music.tone_playable(523, music.beat(BeatFraction.SIXTEENTH)),
                music.PlaybackMode.IN_BACKGROUND)
    # 更新上次動作的時間為目前時間
    lastTime = actTme
PressHold = False
Y = 0
MoveY = 0
X = 0
MoveX = 0
SpeedY = 0
SpeedX = 0
NewY = 0
NewX = 0
actTme = 0
lastTime = 0
LimitS = 0
act = 0
Sound = 0
Mic = 0
levelY = 0
levelX = 0
min2 = 0
max2 = 0
PressLeft = False
PressRight = False
mouse.start_mouse_service()
max2 = 9
min2 = 0
levelX = 5
levelY = 5
factor = 0.004
Mic = 0
Sound = 7
act = 0
LimitS = 700
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
music.play(music.create_sound_expression(WaveShape.SINE,
        5000,
        1,
        255,
        0,
        1000,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LOGARITHMIC),
    music.PlaybackMode.IN_BACKGROUND)
for index in range(2):
    basic.show_icon(IconNames.SMALL_HEART)
    # ## 顯示小愛心
    basic.show_icon(IconNames.HEART)
# ## 顯示愛心
# 重複執行on_forever函數

def on_forever():
    global NewX, NewY, SpeedX, SpeedY, MoveX, MoveY, PressHold, act, X, Y
    # 取得目前加速度感應器在X軸與Y軸的讀數
    NewX = input.acceleration(Dimension.X)
    NewY = input.acceleration(Dimension.Y) * -1
    # 根據加速度感應器的值計算滑鼠移動速度
    SpeedX = Math.map(abs(input.acceleration(Dimension.X)), 0, 1023, 1, 10) * (levelX * factor)
    SpeedY = Math.map(abs(input.acceleration(Dimension.Y)), 0, 1023, 1, 10) * (levelY * factor)
    # 計算滑鼠應該移動的距離
    MoveX = SpeedX * (NewX - X)
    MoveY = SpeedY * (NewY - Y)
    # 處理點擊或按住的狀態
    if act > 0 and input.running_time() - lastTime > LimitS:
        if act >= 4:
            if not (PressHold):
                PressHold = True
            # 啟動按住模式
            act = 0
        else:
            if act == 1:
                if PressHold:
                    PressHold = False
                    # 取消按住模式
                    basic.clear_screen()
                else:
                    mouse.click()
                    # 單擊
                    basic.show_string("L")
            elif act == 2:
                mouse.click()
                # 雙擊1
                basic.pause(100)
                mouse.click()
                # 雙擊2
                basic.show_string("D")
            elif act == 3:
                mouse.right_click()
                # 右鍵單擊
                basic.show_string("R")
            act = 0
        # 根據是否為按住模式，移動滑鼠
        if PressHold:
            basic.show_string("H")
        else:
            basic.clear_screen()
    if PressHold:
        mouse.send(MoveX, MoveY, True, False, False, 0, True)
    else:
        mouse.movexy(MoveX, MoveY)
    # 更新X, Y的位置，平滑移動效果
    X = SpeedX * NewX + (1 - SpeedX) * X
    Y = SpeedY * NewY + (1 - SpeedY) * Y
basic.forever(on_forever)
