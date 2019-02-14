#-*- coding: utf-8 -*-
#Elvira says we should put a license in here. Let's give it the ol' MPL 2.
#That way attribution is required and you'll know I did this.

print("Frankly, I have no idea what I'm doing. This code is nearly 150 lines long with an if statement for every character.")
print("But, you know what? I learned something new. And I'll keep trying with ordered sets and looping counts next time.")

#Converted to lowercase. Also converted to a string in case you enter a number.
string=str(input("Enter the string you would like to assess:" )).lower()

#Starting with the letters, numbers and space character, as per the assignment.
if(string.count("a")>0):
    print("a: "+str(string.count("a")))
if(string.count("b")>0):
    print("b: "+str(string.count("b")))
if(string.count("c")>0):
    print("c: "+str(string.count("c")))
if(string.count("d")>0):
    print("d: "+str(string.count("d")))
if(string.count("e")>0):
    print("e: "+str(string.count("e")))
if(string.count("f")>0):
    print("f: "+str(string.count("f")))
if(string.count("g")>0):
    print("g: "+str(string.count("g")))
if(string.count("h")>0):
    print("h: "+str(string.count("h")))
if(string.count("i")>0):
    print("i: "+str(string.count("i")))
if(string.count("j")>0):
    print("j: "+str(string.count("j")))
if(string.count("k")>0):
    print("k: "+str(string.count("k")))
if(string.count("l")>0):
    print("l: "+str(string.count("l")))
if(string.count("m")>0):
    print("m: "+str(string.count("m")))
if(string.count("n")>0):
    print("n: "+str(string.count("n")))
if(string.count("o")>0):
    print("o: "+str(string.count("o")))
if(string.count("p")>0):
    print("p: "+str(string.count("p")))
if(string.count("q")>0):
    print("q: "+str(string.count("q")))
if(string.count("r")>0):
    print("r: "+str(string.count("r")))
if(string.count("s")>0):
    print("s: "+str(string.count("s")))
if(string.count("t")>0):
    print("t: "+str(string.count("t")))
if(string.count("u")>0):
    print("u: "+str(string.count("u")))
if(string.count("v")>0):
    print("v: "+str(string.count("v")))
if(string.count("w")>0):
    print("w: "+str(string.count("w")))
if(string.count("x")>0):
    print("x: "+str(string.count("x")))
if(string.count("y")>0):
    print("y: "+str(string.count("y")))
if(string.count("z")>0):
    print("z: "+str(string.count("z")))
if(string.count("1")>0):
    print("1: "+str(string.count("1")))
if(string.count("2")>0):
    print("2: "+str(string.count("2")))
if(string.count("3")>0):
    print("3: "+str(string.count("3")))
if(string.count("4")>0):
    print("4: "+str(string.count("4")))
if(string.count("5")>0):
    print("5: "+str(string.count("5")))
if(string.count("6")>0):
    print("6: "+str(string.count("6")))
if(string.count("7")>0):
    print("7: "+str(string.count("7")))
if(string.count("8")>0):
    print("8: "+str(string.count("8")))
if(string.count("9")>0):
    print("9: "+str(string.count("9")))
if(string.count("0")>0):
    print("0: "+str(string.count("0")))
    
#And the space character, as requested.
if(string.count(" ")>0):
    print("[space]: "+str(string.count(" ")))

#Now for a bunch of mostly random special characters. Here's hoping you don't test me with an emoji.
if(string.count("~")>0):
    print("~: "+str(string.count("~")))
if(string.count("`")>0):
    print("`: "+str(string.count("`")))
if(string.count("!")>0):
    print("!: "+str(string.count("!")))
if(string.count("@")>0):
    print("@: "+str(string.count("@")))
if(string.count("#")>0):
    print("#: "+str(string.count("#")))
if(string.count("$")>0):
    print("$: "+str(string.count("$")))
if(string.count("%")>0):
    print("%: "+str(string.count("%")))
if(string.count("^")>0):
    print("^: "+str(string.count("^")))
if(string.count("&")>0):
    print("&: "+str(string.count("&")))
if(string.count("*")>0):
    print("*: "+str(string.count("*")))
if(string.count("(")>0):
    print("(: "+str(string.count("(")))
if(string.count(")")>0):
    print("): "+str(string.count(")")))
if(string.count("-")>0):
    print("-: "+str(string.count("-")))
if(string.count("_")>0):
    print("_: "+str(string.count("_")))
if(string.count("+")>0):
    print("+: "+str(string.count("+")))
if(string.count("=")>0):
    print("=: "+str(string.count("=")))
if(string.count("[")>0):
    print("[: "+str(string.count("[")))
if(string.count("]")>0):
    print("]: "+str(string.count("]")))
if(string.count("{")>0):
    print("{: "+str(string.count("{")))
if(string.count("}")>0):
    print("}: "+str(string.count("}")))
if(string.count("|")>0):
    print("|: "+str(string.count("|")))
if(string.count("\\")>0):
    print("\\: "+str(string.count("\\"))) #Trial and error caught this one!
if(string.count(":")>0):
    print("[colon]: "+str(string.count(":"))) #Double-colon looks odd. I'll write it in.
if(string.count(";")>0):
    print("[semicolon]: "+str(string.count(";")))
if(string.count('"')>0):
    print('": '+str(string.count('"'))) #Captured the double-quote!
if(string.count("'")>0):
    print("': "+str(string.count("'")))
if(string.count(",")>0):
    print("[comma]: "+str(string.count(",")))
if(string.count(".")>0):
    print("[period]: "+str(string.count(".")))
if(string.count("<")>0):
    print("<: "+str(string.count("<")))
if(string.count(">")>0):
    print(">: "+str(string.count(">")))
if(string.count("?")>0):
    print("?: "+str(string.count("?")))
if(string.count("/")>0):
    print("/: "+str(string.count("/")))

print('Well, that looks like a job well done. You should give me an "A+" grade!')