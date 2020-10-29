import csv
import os
import glob

if not os.path.isdir('csv'):
    exit()

# キャリブレーションに用いる値を導出する
# 今回は簡易的に、getThemalMap.pyで計測された表面温度のAVERAGEと体温計で測定した値の差をとり、さらにそれらの平均を補正値とする

calibrate = []

for d in glob.iglob('csv/*'):
    correct = 0
    avg = 0
    try:
        with open(os.path.join(d, 'correct.csv'), 'r') as f:
            correct = float(f.read())
        with open(os.path.join(d, 'avg.txt'), 'r') as f:
            avg = float(f.read())
    except:
        print("getThermalMapForCalibration.pyを実行してから、calibrate.pyを実行してください。")
        exit()
    calibrate.append(avg - correct)

if os.path.isdir('conf'):
    os.mkdir('conf')
if os.path.exists('conf/calibration.txt'):
    os.remove('conf/calibration.txt')
with open('conf/calibration.txt', 'a+') as f:
    f.write(str(sum(calibrate) / len(calibrate)))
