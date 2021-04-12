import sys
import time
import zipfile

def brute_force():

    #コマンドライン引数を使用する
    args = sys.argv 

    #コマンドライン引数[1]を指定する
    #arg[0]には、スクリプトを入れる
    dic = open(args[1], "r")

    #read():テキストを読み込む　split("\n"):区切る役割
    passwd_list = dic.read().split("\n")

    t1 = time.time()

    #コマンドライン引数[2]を指定する
    #zipfile.ZipFile(ZIPファイル):使うファイルの指定
    with zipfile.ZipFile(args[2]) as zf:
        for passwd in passwd_list:
            try:
                zf.extractall(pwd = passwd)
                print("Complete")
                print("pass : " + passwd)
                break
            except KeyboardInterrupt:
                print("Ctrl+Cで停止しました")
                break
            except:
                print(passwd)
                continue
        else:
            print("Falier...")

    t2 = time.time()

    execution_time = t2 - t1

    print("実行時間：" + execution_time + "seconds")