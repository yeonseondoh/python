def rep_char(nstr) :
    print("-" * nstr)

def draw_line_string():
    name = str(input("Input his/her name: "))
    msg1 = "Hello " + name + ","
    msg2 = "Welcome to Seoul."
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char(nstr)
    print(msg1 + "\n" + msg2)
    rep_char(nstr)
    

draw_line_string()
