#--------------------------
#bin to dec (str to int)
#print(int('11111111', 2))
#255
#--------------------------
#dec to bin
#bin(6)
#'0b110'
#
#'{0:08b}'.format(6)
#'00000110'
#
#--------------------------
#dec to bin
#bin(2)
#'0b10'
#int('0b10',2)
#2
#--------------------------
#dec to bin
#bin(4)
#'0b100'
#int('0b100',2)
#4
#--------------------------
#
#x='0b100'
#y=int('%s'%x,2)
#print(y)
#--------------------------
#
#x='{0:08b}'.format(6)
#print(x)
#00000110
#
# ----- Just to explain the parts of the formatting string: -----
# {} places a variable into a string
# 0 takes the variable at argument position 0
# : adds formatting options for this variable (otherwise it would represent decimal 6)
# 08 formats the number to eight digits zero-padded on the left
# b converts the number to its binary representation
#
#--------------------------
#bin(6)[2:]  
#'110'
#
#