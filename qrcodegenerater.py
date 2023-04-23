import qrcode

input1 = input('ENTER TEXT:')
input2 = input('ENTER NAME OF FILE:')

qrc = qrcode.make(input1)
qrc.save(input2)