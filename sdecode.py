import base64

#Input file name you wish to decode from Base64
filename = input("input file name: ")

#Process - open inputted filename and decode Base64 
file = open(filename,"r")

M = file.read()

MC = base64.b64decode(M)

MCD = MC.decode("ascii")

#Output decoded base64 in ascii
print(MCD)
