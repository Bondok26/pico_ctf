'''
* input this command (nc mercury.picoctf.net 22902) to the terminal will output some numbers, I changed these numbers to
its corresponding characters (I guessed these numbers are ascii, and it worked)

* nc command will print to the terminal directly so i redirected the output to a text file called pico
so the final command --> nc mercury.picoctf.net 22902 | pico

* now extract the data from the text file pico, the data looks like this
10
20
30
so i spilt the file to a list at each new line "\n", I also noticed that the file ended with an empty line
so the list contains an empty string at the last item so i removed it

* note the flag is repeated twice when you print
'''
file = open("/home/bondok/pico", "r")
data = list(map(int, file.read().split("\n")[:-1]))
flag = "".join([chr(x) for x in data])
print(flag)


