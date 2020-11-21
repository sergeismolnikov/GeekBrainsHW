# f= open("testhw5.txt","w+")


with open("text.txt",'w') as f_obj:
    while True:
        text = f"{input('enter some text  ')}\n"
        if text == '\n':
            break
        f_obj.write(text)