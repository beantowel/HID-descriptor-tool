import sys
import fileinput
import re

from hid_definitions import *

UsagePage = None

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

def itemByHex(hexd):
  length = hexd & 0b11
  if length == 3: #0b11 represents 4-byte value
    length = 4

  for items in HID_ITEMS:
    for item in items:
      hItem = items[item]
      if (hItem == (hexd & 0xFC)):
        return [item, length]
  raise Exception('item error')

def valueByHex(item, len, hexd):
  if len == 0:
    return None

  constants = CONST_BY_ITEM[item]
  page = None
  inline_page = False
  if item in { "USAGE", "USAGE_MINIMUM", "USAGE_MAXIMUM"}:
    page = UsagePage
    if len == 4:
      page = valueByHex('USAGE_PAGE', 1, hexd >> 16)
      hexd = hexd & 0x0000FFFF
      inline_page = True
    if page in USAGE_BY_PAGE:
      constants = USAGE_BY_PAGE[page]
    else:
      eprint('Page missing: ', page)
  for key in constants:
    if constants[key] == hexd:
      val = key
      if inline_page:
        val = page + ': ' + val
      return val

  if constants != {}:
    if page != None:
      eprint('Value missing: ', page, hex(hexd))
    else:
      eprint('Value missing: ', item, hex(hexd))

  # These ones work best with a hex value
  if item in { "INPUT", "OUTPUT", "FEATURE", "COLLECTION",
               "USAGE_PAGE", "USAGE", "USAGE_MINIMUM", "USAGE_MAXIMUM"}:
    return to_hex(hexd)

  # The rest work with an integer
  if hexd > (1<<len*8-1)-1: # calculate complement
    hexd = (1<<(len*8)) - hexd
    hexd = -hexd
  return str(hexd)

def to_hex(value):
  return "0x%X" % value

fileOut = sys.stdout
tabcnt = 0
for line in fileinput.input():
  eprint('------',line.rstrip()) # echo
  line = line.expandtabs(tabsize=4)
  key = line
  pos = line.find('//') # remove comments
  if pos >= 0:
    key = line[:pos]
  hexes = re.findall('0x[0-9A-Fa-f]*',key)
  if hexes == []:
    continue

  item, length = itemByHex(int(hexes[0],16)) #got item

  hValue = 0
  for i in range(0, length):
    hValue += int(hexes[1+i],16)<<(i*8) #multi byte value
  value = valueByHex(item, length, hValue) #got value

  if item == 'USAGE_PAGE':
    UsagePage = value #update UsagePage
  if item == 'END_COLLECTION':
    tabcnt-=1
  for i in range(0,tabcnt):
    fileOut.write('  ');
  fileOut.write(item)
  if value != None:
    fileOut.write(' (' + value + ')')
  fileOut.write('\n')
  if item == 'COLLECTION':
    tabcnt += 1
fileOut.close()
