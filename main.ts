function MicOn() {
    //  設定聲音閾值，當音量超過這個值時，觸發相應事件
    input.setSoundThreshold(SoundThreshold.Loud, Mic * 16)
    //  設定音樂播放的音量，音量根據 Mic 的值調整
    music.setVolume(Mic * 16 - 8)
    //  播放一個短音符 C5 (523Hz) 來指示麥克風已開啟，音符持續一拍的八分之一
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    //  在 LED 顯示螢幕上顯示一個圖案來指示麥克風開啟狀態
    basic.showLeds(`
        . . # . .
        . # # # .
        . # # # .
        . . # . .
        . # # # .
        `)
    //  顯示當前的 Mic 數值
    basic.showNumber(Mic)
}

//  當 Micro:bit 的 logo 被長按時，執行 on_logo_long_pressed 函數
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    
    //  當長按 Micro:bit 的 logo 時
    if (Mic > 0) {
        //  如果 Mic 的值大於 0，表示麥克風已開啟
        Mic = 0
        //  將 Mic 設為 0 來關閉麥克風
        MicOff()
    } else {
        //  呼叫 MicOff 函數來處理麥克風關閉的動作
        //  如果 Mic 的值不大於 0，表示麥克風已關閉
        Mic = Sound
        //  將 Mic 設為 Sound（開啟麥克風）
        act = 0
        //  重置動作計數
        lastTime = input.runningTime()
        //  記錄當前時間作為最後一次動作的時間
        MicOn()
    }
    
    //  呼叫 MicOn 函數來處理麥克風開啟的動作
    basic.pause(200)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
//  當藍牙連接成功時
//  當藍牙連接成功時，執行 on_bluetooth_connected 函數
bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    //  顯示一個 "YES" 圖標來表示連接成功
    basic.showIcon(IconNames.Yes)
    //  暫停 5 秒以便用戶看到圖標
    basic.pause(5000)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
//  Mic關掉
function MicOff() {
    basic.showLeds(`
        # . # . .
        . # # # .
        . # # # .
        . . # # .
        . # # . #
        `)
}

//  當藍牙斷線時
//  當藍牙斷線時，執行 on_bluetooth_disconnected 函數
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    //  顯示一個 "NO" 圖標來表示斷線
    basic.showIcon(IconNames.No)
    //  暫停 5 秒以便用戶看到圖標
    basic.pause(5000)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
//  A按鈕
//  當 A 按鈕被按下時，執行 on_button_pressed_a 函數
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    //  當按下 A 按鈕時
    if (levelX < max2) {
        levelX += 1
    } else {
        //  如果 levelX 小於 max2，將 levelX 加 1
        levelX = min2
    }
    
    //  否則，將 levelX 重設為 min2
    //  顯示一個圓形邊框的 LED 圖案來指示 A 按鈕被按下
    basic.showLeds(`
        . . . . .
        . # . # .
        # . . . #
        . # . # .
        . . . . .
        `)
    //  在 LED 顯示螢幕上顯示當前的 levelX 值
    basic.showNumber(levelX)
    //  暫停 200 毫秒以便顯示數字
    basic.pause(200)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    //  麥克風按鈕
    if (Mic == 0) {
        MicOff()
    } else {
        if (Mic > 1) {
            Mic += -1
        } else {
            Mic = 9
        }
        
        MicOn()
    }
    
    basic.pause(100)
    basic.clearScreen()
})
//  設定當 P2 觸控引腳被按下時，觸發 on_pin_pressed_p2 函數
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    //  當 P2 觸控引腳被按下時，執行 Clicks 函數
    Clicks()
})
//  AB按鈕
//  當 A 和 B 按鈕同時被按下時，執行 on_button_pressed_ab 函數
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    //  當同時按下 A 和 B 按鈕時
    if (levelX == 0) {
        //  如果 levelX 為 0，則將 levelX 和 levelY 設定為 5
        levelX = 5
        levelY = 5
        //  顯示一個小鑽石圖標，然後顯示一個大鑽石圖標
        basic.showIcon(IconNames.SmallDiamond)
        basic.showIcon(IconNames.Diamond)
    } else if (levelX == 5) {
        //  如果 levelX 為 5，則將 levelX 和 levelY 設定為 0
        levelX = 0
        levelY = 0
        //  顯示一個大鑽石圖標，然後顯示一個小鑽石圖標
        basic.showIcon(IconNames.Diamond)
        basic.showIcon(IconNames.SmallDiamond)
    }
    
    //  顯示當前的 levelX 值
    basic.showNumber(levelX)
    //  暫停 200 毫秒以便顯示數字
    basic.pause(200)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
//  B按鈕
//  當 B 按鈕被按下時，執行 on_button_pressed_b 函數
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    //  當按下 B 按鈕時
    if (levelY < max2) {
        levelY += 1
    } else {
        //  如果 levelY 小於 max2，將 levelY 加 1
        levelY = min2
    }
    
    //  否則，將 levelY 重設為 min2
    //  顯示一個十字形的 LED 圖案來指示 B 按鈕被按下
    basic.showLeds(`
        . . # . .
        . # . # .
        . . . . .
        . # . # .
        . . # . .
        `)
    //  在 LED 顯示螢幕上顯示當前的 levelY 值
    basic.showNumber(levelY)
    //  暫停 200 毫秒以便顯示數字
    basic.pause(200)
    //  清除螢幕上的顯示
    basic.clearScreen()
})
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    if (Mic > 0) {
        Clicks()
    }
    
})
function Clicks() {
    
    //  取得當前時間
    actTme = input.runningTime()
    //  如果上次動作到現在的時間差小於或等於限制時間（LimitS）或目前狀態是初始狀態（act == 0）
    if (actTme - lastTime <= LimitS || act == 0) {
        act += 1
        //  增加動作計數
        if (act == 1) {
            //  如果這是第一次動作，播放 C4 音符 (262Hz) 的短音
            music.play(music.tonePlayable(262, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
        } else if (act == 2) {
            //  如果這是第二次動作，播放 E4 音符 (330Hz) 的短音
            music.play(music.tonePlayable(330, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
        } else if (act == 3) {
            //  如果這是第三次動作，播放 G4 音符 (392Hz) 的短音
            music.play(music.tonePlayable(392, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
        } else {
            //  如果這是第四次動作或以上，播放 C5 音符 (523Hz) 的短音
            music.play(music.tonePlayable(523, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
        }
        
    }
    
    //  更新上次動作的時間為目前時間
    lastTime = actTme
}

let PressHold = false
let Y = 0
let MoveY = 0
let X = 0
let MoveX = 0
let SpeedY = 0
let SpeedX = 0
let NewY = 0
let NewX = 0
let actTme = 0
let lastTime = 0
let LimitS = 0
let act = 0
let Sound = 0
let Mic = 0
let levelY = 0
let levelX = 0
let min2 = 0
let max2 = 0
let PressLeft = false
let PressRight = false
mouse.startMouseService()
max2 = 9
min2 = 0
levelX = 5
levelY = 5
let factor = 0.004
Mic = 0
Sound = 7
act = 0
LimitS = 700
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
music.play(music.createSoundExpression(WaveShape.Sine, 5000, 1, 255, 0, 1000, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
for (let index = 0; index < 2; index++) {
    basic.showIcon(IconNames.SmallHeart)
    //  ## 顯示小愛心
    basic.showIcon(IconNames.Heart)
}
//  ## 顯示愛心
//  重複執行on_forever函數
basic.forever(function on_forever() {
    
    //  取得目前加速度感應器在X軸與Y軸的讀數
    NewX = input.acceleration(Dimension.X)
    NewY = input.acceleration(Dimension.Y) * -1
    //  根據加速度感應器的值計算滑鼠移動速度
    SpeedX = Math.map(Math.abs(input.acceleration(Dimension.X)), 0, 1023, 1, 10) * (levelX * factor)
    SpeedY = Math.map(Math.abs(input.acceleration(Dimension.Y)), 0, 1023, 1, 10) * (levelY * factor)
    //  計算滑鼠應該移動的距離
    MoveX = SpeedX * (NewX - X)
    MoveY = SpeedY * (NewY - Y)
    //  處理點擊或按住的狀態
    if (act > 0 && input.runningTime() - lastTime > LimitS) {
        if (act >= 4) {
            if (!PressHold) {
                PressHold = true
            }
            
            //  啟動按住模式
            act = 0
        } else {
            if (act == 1) {
                if (PressHold) {
                    PressHold = false
                    //  取消按住模式
                    basic.clearScreen()
                } else {
                    mouse.click()
                    //  單擊
                    basic.showString("L")
                }
                
            } else if (act == 2) {
                mouse.click()
                //  雙擊1
                basic.pause(100)
                mouse.click()
                //  雙擊2
                basic.showString("D")
            } else if (act == 3) {
                mouse.rightClick()
                //  右鍵單擊
                basic.showString("R")
            }
            
            act = 0
        }
        
        //  根據是否為按住模式，移動滑鼠
        if (PressHold) {
            basic.showString("H")
        } else {
            basic.clearScreen()
        }
        
    }
    
    if (PressHold) {
        mouse.send(MoveX, MoveY, true, false, false, 0, true)
    } else {
        mouse.movexy(MoveX, MoveY)
    }
    
    //  更新X, Y的位置，平滑移動效果
    X = SpeedX * NewX + (1 - SpeedX) * X
    Y = SpeedY * NewY + (1 - SpeedY) * Y
})
