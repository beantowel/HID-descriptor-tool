import re
from HID_PID_Definitions import *
def Byte_Size(x):
	'''ByteSize for Short Items
	return 0,1,2,or4'''
	x=int(x)
	if x>=-0x7F-1 and x<=0x7F:
		return 1
	if x>=-0x7FFF-1 and x<=0x7FFF:
		return 2
	if x>=-0x7FFFFFFF-1 and x<=0x7FFFFFFF:
		return 4 #0b11 represents 4
def u_Byte_Size(x):
	'''ByteSize for Short Items
	return 0,1,2,or4'''
	x=int(x)
	if x<=0xFF:
		return 1
	if x<=0xFFFF:
		return 2
	if x<=0xFFFFFFFF:
		return 4 #0b11 represents 4
def toComplementBytes(x,size):
	x=int(x)
	if x<0:
		x=x+2**size
	return hex(x)
def prefixZero(hdata,byteSize):
	'''fill prefixZero to complete a byte'''
	#input like '0xNNN'
	lsize=len(hdata)-2
	while(lsize!=byteSize*2): #0xN-->0x0N
		hdata="0x0"+hdata[2:]
		lsize=len(hdata)-2
	return hdata
def SplitToLittleEndien(hdata,byteSize):
	datalist=[]
	hdata=prefixZero(hdata,byteSize)
	for i in range(0,byteSize*2,2): #0x1234
		datalist.insert(0,"0x"+hdata[2+i:4+i]) #[0x34,0x12]
	return datalist
def ShortItem(prefix,x,isSign):
	'''construct short item by prefix'''
	global bytecount
	if isSign:
		byteSize=Byte_Size(x)
	else:
		byteSize=u_Byte_Size(x)
	if byteSize==4:
		prefix=prefix+3 #0b11 represents 4
	else:
		prefix=prefix+byteSize
	pre=hex(prefix)
	pre=prefixZero(pre,1)

	size=byteSize*8
	if prefix==0x54: #Unit_Exponent exception
		size=4 #one nibble
	hdata=toComplementBytes(x,size)
	data=SplitToLittleEndien(hdata,byteSize)
	if prefix==0xc0: #End_Collection exception
		bytecount+=1
		return "0xc0",[]
	bytecount=bytecount+1+len(data)
	return pre,data
fileIn="HID_Descriptor_Input.rptDsc"
fileOut=open("HID_Descriptor.out",'w')
lines=open(fileIn).readlines()
bytecount=0
#descriptor parser
for line in lines:
	line=line.expandtabs(tabsize=4)
	copyline=line
	line=line.lstrip()
	pos=line.find('//')
	if pos>=0:
		line=line[0:pos]

	b=False
	for items in HID_Items:
		for regex in items:
			item=re.findall('\\b'+regex+'\\b',line)
			for i in item:
				prefix=items[regex]
				value=re.findall('\(.*\)',line)
				for consts in HID_Constants:
					for regex1 in consts:
						const=re.findall('\('+regex1+'\)',value[0])
						for j in const:
							x=consts[regex1]
							out=ShortItem(prefix,x,False)
							b=True
				if not(b) and len(value[0])>2:
					x=int(value[0][1:-1])
					out=ShortItem(prefix,x,True)
					b=True
				if not(b):
					out=ShortItem(prefix,0,True) #defalut x=0
					b=True
	if not(b):
		continue
	#print(out)
	fileOut.write(out[0]+',') # prefix
	for i in out[1]: # data
		fileOut.write(i+',')
	for i in range(0,4-len(out[1])): #max 4 byte
		fileOut.write('     ')
	fileOut.write(" //"+copyline) #copy source as comments
fileOut.write("//Total:"+str(bytecount)+" Bytes")
fileOut.close()
