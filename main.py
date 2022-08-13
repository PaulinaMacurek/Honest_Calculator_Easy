import operator


def is_one_digit(v):
    if is_integer_num(v) and v > -10 and v < 10:
        return True
    else:
        return False


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msgs["msg_6"]
    if (v1 == 1 or v2 == 1) and v3 == ops["*"]:
        msg = msg + msgs["msg_7"]
    if (v1 == 0 or v2 == 0) and (v3 == ops["*"] or v3 == ops["+"] or v3 == ops["-"]):
        msg = msg + msgs["msg_8"]
    else:
        pass
    if msg != "":
        msg = msgs["msg_9"] + msg
        print(msg)
    else:
        pass


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
}
msgs = {"msg_0": "Enter an equation",
        "msg_1": "Do you even know what numbers are? Stay focused!",
        "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "msg_3": "Yeah... division by zero. Smart move...",
        "msg_4":  "Do you want to store the result? (y / n):",
        "msg_5":  "Do you want to continue calculations? (y / n):",
        "msg_6":  " ... lazy",
        "msg_7":  " ... very lazy",
        "msg_8":  " ... very, very lazy",
        "msg_9":  "You are",
        "msg_10": "Are you sure? It is only one digit! (y / n)",
        "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"
        }
memory = 0.0
wanna_calc = True
while wanna_calc:
    while True:
        print(msgs["msg_0"])
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            x = float(x)
            y = float(y)
            oper = ops[oper]
        except ValueError:
            print(msgs["msg_1"])
        except KeyError:
            print(msgs["msg_2"])
        else:
            check(x, y, oper)
            try:
                result = oper(x, y)
            except ZeroDivisionError:
                print(msgs["msg_3"])
            else:
                print(result)
                while True:
                    print(msgs["msg_4"]) #"Do you want to store the result? (y / n):",
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result):
                            msg_index = 10
                            while msg_index <= 12:
                                print(msgs["msg_" + str(msg_index)]) #   "Are you sure? It is only one digit! (y / n)",
                                answer = input()
                                if answer == "y":
                                    msg_index+=1
                                    if msg_index == 13:
                                        memory = result
                                    else:
                                        continue
                                else:
                                    break
                            print(msgs["msg_5"]) #"Do you want to continue calculations? (y / n):",
                            answer = input()
                            if answer == "y":
                                break
                            else:
                                wanna_calc = False
                        else:
                            memory = result
                            print(msgs["msg_5"]) #"Do you want to continue calculations? (y / n):",
                            answer = input()
                            if answer == "y":
                                break
                            else:
                                wanna_calc = False
                    else:
                        print(msgs["msg_5"]) #"Do you want to continue calculations? (y / n):",
                        answer = input()
                        if answer == "y":
                            break
                        else:
                            wanna_calc = False
                    break
                break
