import re
import copy
from HID_PID_Definitions import *

def ConstractStru(mainItem,value):
    global Outputs, structName, enumDef, structVars

    if mainItem=='Collection':
        try:
            sN=lcalStat['Usage'].pop()
        except:
            print('error',lcalStat)
        structName.append(sN)
        structVars.append(0)
        if len(structName)==1:
            Outputs.append('typedef struct _'+sN+'{') #meta struct begins
        else:
            Outputs.append('struct {') #inner report struct
        return
    if mainItem=='End_Collection':
        sN=structName.pop()
        structVars.pop()
        Outputs.append('} '+sN+';') #struct ends
        return

    minimum=int(glStat['Logical_Minimum'])
    maximum=int(glStat['Logical_Maximum'])
    rSize=int(glStat['Report_Size'])
    rCnt=int(glStat['Report_Count'])
    if mainItem in ['Input','Output','Feature']:
        if value=='IOF_Array':
            enumV=[] #generate enum values
            for i in range(minimum,maximum+1):
                usage=lcalStat['Usage'].pop()
                usage=usage+'='+str(minimum+maximum-i)+','
                enumV.append(usage)
            enumV.reverse() #reverse to get appropriate order

            enumT=structName[-1]+'_Enum' #enum template name
            enumtype='uint'+str(rSize)+'_t' #ARM style typedef
            enumDef.append(['enum '+enumT,copy.copy(enumV)])
            for i in range(0,rCnt):
                Outputs.append('enum '+enumT+' '+enumT.lower()+'_'+str(i)+';')
        if value == 'IOF_VariableBuffer':
            lcalStat['Usage'].pop()
            Outputs.append('//Not supported Buffer usage')
        if value == 'IOF_Variable':
            usage=[]
            for i in range(0,rCnt):
                usage.append(lcalStat['Usage'].pop())
            usage.reverse() #reverse to get appropriate order
            if rSize >= 8:
                # 1 or more bytes, assume aligned by 8-bit
                if minimum>=0:
                    uType='uint'+str(rSize)+'_t' #ARM style typedef
                else:
                    uType='int'+str(rSize)+'_t'
                for u in usage:
                    Outputs.append(uType+' '+u.lower()+';')
            else:
                #less than one byte
                #assume got proper pad behind and reportSize|8
                bitCnt = rSize * rCnt
                byteCnt = int((bitCnt+7)/8) #round byteCnt
                cnt = 0
                for i in range(0, byteCnt):
                    Outputs.append('uint8_t vars_'+str(i + structVars[-1])+';')
                    comment='//'
                    # reportSize|8
                    for j in range(0, int(8/rSize)):
                        cnt +=1
                        if cnt > rCnt:
                            break
                        u=usage[i*int(8/rSize)+j]
                        comment += u.lower() + ','
                        mask = (1 << rSize) - 1
                        mask = mask << (j * rSize)
                        bitMask.append([u,mask])
                    Outputs.append(comment)
                structVars[-1]+=byteCnt
                Outputs.append('//Check Pads')
        if value in ["IOF_ConstArry","IOF_ConstVar"]:
            pads = rCnt * rSize
            Outputs.append('//'+str(pads)+'-pads added')
        # if value=='IOF_IOF_Defalut_Items':
        #     gg

        # add some comments
        Outputs.append('//Logical_Maximum:'+str(maximum))
        if minimum!=0:
            Outputs.append('//Logical_Minimum:'+glStat['Logical_Minimum'])
        if glStat['Unit']!='Unit_None':
            Outputs.append('//Unit:'+glStat['Unit'])
        if glStat['Unit_Exponent']!='0':
            Outputs.append('//Unit_Exponent:'+glStat['Unit_Exponent'])

fileIn     = "DscInput.rptDsc"
fileOut    = open("rptStructureDef.h",'w')
lines      = open(fileIn).readlines()
glStat     = {
    'Unit':'Unit_None',
    'Unit_Exponent':'0',
} #global Status
lcalStat   = {} #local Status
mainStat   = {} #main Status
status     = [glStat,lcalStat,mainStat]
Outputs    = []
structName = []
structVars = []
enumDef   = []
rptID      = []
bitMask    = []

collectionCnt = 0
pidPageStart = False
for line in lines:
    # //Start Copy Data Structure Input
    # //The above comment was a starting flag for DataStructureGen.py, don't move
    # //End Copy Data Structure Input
    # //The above comment was an ending flag for DataStructureGen.py, don't move
    if line.find('Collection(Clc')>=0:
        collectionCnt+=1
    if line.find('End_Collection()')>=0:
        collectionCnt-=1
    if line.find('Usage_Page(Physical_Interface)')>=0:
        pidPageStart=True
    if collectionCnt<1 or not(pidPageStart):
        continue
    #escape inputs

    line=line.expandtabs(tabsize=4)
    key=line
    pos=line.find('//') #remove comments
    if pos>=0:
        key=line[:pos]
    print('------',key) #echo

    for regex in Global_Items:
        item=re.search('\\b'+regex+'\\b',key)
        value=re.search('\(.*\)',key)
        if item!=None:
            item=item.group(0)
            value=value.group(0)
            glStat[item]=value[1:-1]
            if item in ['Report_ID']:
                rptID.append(['ID_'+structName[-1],value[1:-1]])
                Outputs.append('//'+item+':'+value[1:-1])
            break

    for regex in Local_Items:
        item=re.search('\\b'+regex+'\\b',key)
        value=re.search('\(.*?[\):]',key)
        if item!=None:
            item=item.group(0)
            value=value.group(0)
            try:
                lcalStat[item].append(value[1:-1])
            except:
                lcalStat[item]=[value[1:-1]]
            break

    for regex in Main_Items:
        item=re.search('\\b'+regex+'\\b',key)
        value=re.search('\(.*\)',key)
        if item!=None:
            item=item.group(0)
            value=value.group(0)
            ConstractStru(item,value[1:-1])
            break

prefixText = '''#ifndef __USB_PID_Def
#define __USB_PID_Def

#ifdef __cplusplus
extern "C" {
#endif

#include "stdint.h"
#pragma pack(1)
#pragma pack(push)

'''
fileOut.write(prefixText)

# fileOut.write('enum Report_ID_Enum {\n') #report ID
for rpt in rptID:
    fileOut.write('#define '+rpt[0]+' '+rpt[1]+'\n')
fileOut.write('\n')

for mask in bitMask: #bit masks
    fileOut.write('#define Mask_'+mask[0]+' '+hex(mask[1])+'\n')
fileOut.write('\n')

enumVis=[] #delete repeat definition
for enum in enumDef: #enumerations
    if enum[0] in enumVis:
        continue
    enumVis.append(enum[0])
    fileOut.write(enum[0]+'{'+'\n')
    for usage in enum[1]:
        fileOut.write(usage+'\n')
    fileOut.write('};\n\n')

cnt=0 #seperate each struct
for line in Outputs: #structs
    if line.find('struct')>=0:
        cnt+=1
    if line.find('}')>=0:
        cnt-=1
    fileOut.write(line+'\n')
    if cnt==0:
        fileOut.write('\n')

sucfixText = '''
#pragma pack(pop)
#ifdef __cplusplus
}
#endif

#endif /* __USB_PID_Def */
'''
fileOut.write(sucfixText)
fileOut.close()
