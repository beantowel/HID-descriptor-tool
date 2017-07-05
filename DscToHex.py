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
def ToComplement(x,size):
	x=int(x)
	if x<0:
		x=x+2**size
	return x
def PrefixZero(hdata,byteSize):
	'''fill PrefixZero to complete a byte'''
	#input like '0xNNN'
	lsize=len(hdata)-2
	while(lsize<byteSize*2): #0xN-->0x0N
		hdata="0x0"+hdata[2:]
		lsize=len(hdata)-2
	return hdata
def SplitToLittleEndien(hdata,byteSize):
	datalist=[]
	hdata=PrefixZero(hdata,byteSize)
	for i in range(0,byteSize*2,2): #0x1234
		datalist.insert(0,"0x"+hdata[2+i:4+i]) #[0x34,0x12]
	return datalist
def ShortItem(prefix,data,byteSize,changePage):
	'''construct short item by prefix'''
	global bytecount
	if byteSize==4:
		pre=prefix+3 #0b11 represents 4
	else:
		pre=prefix+byteSize
	hdata=hex(data)
	data=SplitToLittleEndien(hdata,byteSize)
	if changePage!=None:
		pre=prefix+3
		exData=hex(changePage[1])
		exData=PrefixZero(exData,2)
		exData=SplitToLittleEndien(exData,2)
		data.extend(exData)
	pre=hex(pre)
	pre=PrefixZero(pre,1)
	bytecount+=1 + len(data)
	return pre,data
def MatchDefine(defSets,findFunc):
	'''findFunc example re.search('\\b'+regex[1]+'\\b',line)
		return defSets key when a value match
	'''
	for defDict in [t for aSet in defSets for t in aSet.items()]:
		result=findFunc(defDict[0])
		if result:
			return defDict
	return None
fileIn="DscInput.rptDsc"
fileOut=open("Hex.out",'w')
lines=open(fileIn).readlines()
bytecount=0
usagePage=None
#descriptor parser
for line in lines:
	print(line) #echo
	line=line.expandtabs(tabsize=4)
	copyline=line
	line=line.lstrip()
	pos=line.find('//')
	if pos>=0:
		line=line[0:pos]

	tfunc=lambda regex:re.search('\\b'+regex+'\\b',line) #match item
	item=MatchDefine(HID_Items, tfunc)
	if item==None: #failed matching item
		continue

	inBracket=re.search('\(.*\)',line).group(0) #extract inBracket

	tfunc=lambda regex:re.search(':'+regex+'\)',inBracket)
	changePage=MatchDefine([Usage_Page_Constants],tfunc)

	defSet=HID_Constants
	if item[0]=='Usage': #switch to usagePage
		defSet=[UsageByPage[usagePage]]
		if changePage!=None:
			defSet=[UsageByPage[changePage[0]]]
	else: #switch to corresponded item
		defSet=[ConstByItem[item[0]]]

	tfunc=lambda regex:re.search('\('+regex+'[\):]',inBracket)
	value=MatchDefine(defSet, tfunc)
	if value!=None:
		byteSize=u_Byte_Size(value[1])
		if changePage!=None:
			byteSize=2
		out=ShortItem(item[1],value[1],byteSize,changePage)
		#unsigned preDefinedConstant
	else:
		if len(inBracket[1:-1])>0:
			x=int(inBracket[1:-1])
			size=Byte_Size(x)*8
			# if item[0]=='Unit_Exponent': #Unit_Exponent exception
			# 	size=4 #fucking usb.org's doc
			data=ToComplement(x,size)
			out=ShortItem(item[1],data,Byte_Size(x),changePage) #signed value
		else:
			out=ShortItem(item[1],0,0,changePage) #defalut none value

	if item[0]=='Usage_Page': #update Usage_Page
		usagePage=value[0]

	fileOut.write(out[0]+',') # prefix
	for i in out[1]: # data
		fileOut.write(i+',')
	for i in range(0,4-len(out[1])): #max 4 byte
		fileOut.write('     ')
	fileOut.write(" //"+copyline) #copy source as comments
fileOut.write("//Total:"+str(bytecount)+" Bytes")
fileOut.close()
