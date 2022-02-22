import sys
import fileinput
import re

from hid_definitions import *

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

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
    x=x+2**(size * 8)
  return x

def PrefixZero(hdata,byteSize):
  '''fill PrefixZero to complete a byte'''
  #input like '0xNNN'
  lsize=len(hdata)-2
  while(lsize<byteSize*2): #0xN-->0x0N
    hdata="0x0"+hdata[2:]
    lsize=len(hdata)-2
  return hdata

def SplitToLittleEndian(hdata,byteSize):
  datalist=[]
  hdata=PrefixZero(hdata,byteSize)
  for i in range(0,byteSize*2,2): #0x1234
    datalist.insert(0,"0x"+hdata[2+i:4+i]) #[0x34,0x12]
  return datalist

def to_hex(value):
  return "0x%X" % value

def ShortItem(prefix,data,byteSize,changePage):
  '''construct short item by prefix'''
  global bytecount
  if byteSize==4:
    pre=prefix+3 #0b11 represents 4
  else:
    pre=prefix+byteSize
  hdata = to_hex(data)
  data=SplitToLittleEndian(hdata,byteSize)
  if changePage!=None:
    pre = prefix + 3
    exData = to_hex(changePage[1])
    exData = PrefixZero(exData,2)
    exData = SplitToLittleEndian(exData,2)
    data.extend(exData)
  pre = to_hex(pre)
  pre = PrefixZero(pre,1)
  bytecount += 1 + len(data)
  return pre, data

def MatchDefine(defSets,findFunc):
  '''findFunc example re.search('\\b'+regex[1]+'\\b',line)
    return defSets key when a value match
  '''
  for defDict in [t for aSet in defSets for t in aSet.items()]:
    result=findFunc(defDict[0])
    if result:
      return defDict
  return None

def swap16(x):
    return int.from_bytes(x.to_bytes(2, byteorder='little'),
      byteorder='big', signed=False)

fileOut = sys.stdout
bytecount = 0
usagePage=None
for line in fileinput.input():
  eprint('------',line.rstrip()) # echo
  line = line.expandtabs(tabsize=4)
  copyline = line
  line = line.lstrip()
  comment = line.find('//')
  if comment >= 0:
    line = line[0:comment]

  tfunc = lambda key:re.search('\\b'+key+'\\b',line) # match item
  item = MatchDefine(HID_ITEMS, tfunc)
  if item == None: # failed matching item
    continue
  # eprint('item: ', item)

  inBracket = re.search('\(.*\)',line)
  if inBracket != None:
    inBracket = inBracket.group(0)
  # eprint('inBracket: ', inBracket)

  value = None
  if inBracket != None:
    tfunc = lambda key:re.search(':'+re.escape(key)+'\)',inBracket)
    changePage = MatchDefine([USAGE_PAGES],tfunc)

    # defSet = HID_Constants
    defSet = []
    if item[0] in {"USAGE", "USAGE_MINIMUM", "USAGE_MAXIMUM"}:
      if changePage != None and changePage[0] in USAGE_BY_PAGE:
        defSet = [USAGE_BY_PAGE[changePage[0]]]
      elif usagePage in USAGE_BY_PAGE:
        defSet = [USAGE_BY_PAGE[usagePage]]
    else: # switch to corresponded item
      defSet = [CONST_BY_ITEM[item[0]]]

    tfunc = lambda key:re.search('\('+re.escape(key)+'[\):]',inBracket)
    value = MatchDefine(defSet, tfunc)
    # eprint('value: ', value)

  if value != None:
    byteSize = u_Byte_Size(value[1])
    if changePage != None:
      byteSize = 2
    out = ShortItem(item[1],value[1],byteSize,changePage)
  elif inBracket != None:
    if inBracket.startswith('(0x'):
      bracket_value = int(inBracket[1:-1], 16)
      size = u_Byte_Size(bracket_value)
    else:
      bracket_value = int(inBracket[1:-1], 10)
      size = Byte_Size(bracket_value)
      bracket_value = ToComplement(bracket_value, size)
    out = ShortItem(item[1],bracket_value,size,changePage) # signed value
  else:
    out = ShortItem(item[1],0,0,changePage) # default none value

  if item[0] == 'USAGE_PAGE' and value != None:
    usagePage = value[0]

  fileOut.write(out[0] + ', ') # prefix
  for i in out[1]: # data
    fileOut.write(i + ', ')
  for i in range(0, 4 - len(out[1])): # max 4 bytes
    fileOut.write('      ')
  fileOut.write(" // " + copyline) # copy source as comments
fileOut.write("// Total:" + str(bytecount) + " Bytes, " +
              "0x%04X" % bytecount + " (swapped: " +
              "0x%04X" % swap16(bytecount) + ")\n")
fileOut.close()
