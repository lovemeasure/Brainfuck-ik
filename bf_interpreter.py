"""
使い方1

1.コマンドラインで、このファイルを実行する

2.1行で書かれたBrainfuckのコードを入力する

使い方2
1.コマンドライン引数として、Brainfuckコードの書かれたファイルのパスを渡し、このファイルを実行する

使い方3
1.pythonファイルでimportする。

2.BF_interpreterにBrainfuckコードの書かれた文字列を渡す。


インタプリタ仕様

30000byteの0で初期化されたのメモリ

ポインタの指す値が127のとき、インクリメントはポインタの指す値を0にする

ポインタの指す値が0のとき、デクリメントはポインタの指す値を127にする

ポインタの値が29999のとき、インクリメントはポインタの指す値を0にする

ポインタの値が0のとき、デクリメントはポインタの指す値を29999にする

「,」は読み込まれた文字のUnicodeコードポイントを128で割り、その余りの値をポインタの指す値にする
"""

import sys

pointer = 0
memory_space = [0 for _ in range(30000)]
while_point_stack = []
program = ""
order_pointer = 0
roopcount = 0

def initialization():
    global pointer
    global memory_space
    global while_point_stack
    global program
    global order_pointer
    pointer = 0
    memory_space = [0 for _ in range(30000)]
    while_point_stack = []
    program = ""
    order_pointer = 0    

def pointer_increment():
    global order_pointer
    global pointer 
    pointer += 1
    pointer %= 30000

    order_pointer +=1

def pointer_decrement():
    global order_pointer
    global pointer   
    pointer -= 1
    pointer %= 30000

    order_pointer +=1

def memory_increment():
    global order_pointer
    global pointer
    global memory_space
    memory_space[pointer] += 1
    memory_space[pointer] %= 128

    order_pointer +=1

def memory_decrement():
    global order_pointer
    global pointer
    global memory_space
    memory_space[pointer] -= 1
    memory_space[pointer] %= 128

    order_pointer +=1

def putchar():
    global order_pointer
    global pointer
    global memory_space
    char = chr(memory_space[pointer])
    print(char,end="")
    order_pointer +=1
  
def getchar():
    global order_pointer
    global pointer
    global memory_space
    inpt = input()
    if inpt == "":
        memory_space[pointer] = 10
    else:
        memory_space[pointer] = ord(inpt[0])

    order_pointer +=1

def while_start():
    global pointer
    global order_pointer
    global program
    global memory_space
    global while_point_stack


    if memory_space[pointer] == 0:
        pass_num = 0
        bracket_counter = 1
        while bracket_counter != 0:
            pass_num += 1
            if order_pointer+pass_num == len(program):
                pass #エラー発生みたいな文を出力
            if program[order_pointer+pass_num] == "[":
                bracket_counter += 1
            elif program[order_pointer+pass_num] == "]":
                bracket_counter -= 1

        order_pointer += pass_num
        order_pointer += 1
    else:
        while_point_stack.append(order_pointer)
        order_pointer += 1

def while_end():
    global order_pointer
    global while_point_stack
    global pointer
    global memory_space
    global roopcount

    if memory_space[pointer] != 0:
        order_pointer = while_point_stack.pop(-1)
    else:
        while_point_stack.pop(-1)
        order_pointer +=1

def comment():
    global order_pointer
    order_pointer +=1    



def interpretation(c:str):
    if c == ">":
        pointer_increment()
    elif c == "<":
        pointer_decrement()
    elif c == "+":
        memory_increment()
    elif c == "-":
        memory_decrement()
    elif c == ".":
        putchar()
    elif c == ",":
        getchar()
    elif c == "[":
        while_start()
    elif c == "]":
        while_end()
    else:
        comment() #プログラムを飛ばす

def main():
    global pointer
    global memory_space
    global while_point_stack
    global program 
    global order_pointer

    if len(sys.argv) == 1:
        print()
        program = input("プログラムを入力する(プログラムは一行にまとめてください)\n%")
        print()
        input("エンターキーを押し、プログラムを開始する")
        print("-------------------------------------------")

        BF_interpreter(program)

        print("-------------------------------------------")
        print("プログラムを終了します")

    if len(sys.argv) >= 2:
        with open(sys.argv[1]) as f:
            program = f.read()
        print()
        print("プログラムを開始する")
        print("-------------------------------------------")

        BF_interpreter(program)

        print("-------------------------------------------")
        print("プログラムを終了します")




def BF_interpreter(code):
    global program
    global order_pointer
    program = code
    while order_pointer < len(program):
        interpretation(program[order_pointer])
    initialization()

if __name__ == "__main__":
    main()