# HID-PID Descriptor tool
an extendable hid descriptor tool,parses the report descriptor written by natural language.  

## Files  
- \rptDsc:  
YAML syntax definition for Sublime Text 3 to highlight the report descriptor written in natural language. In Windows copy this to "C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\User", then choose syntax "rptDsc" when editing with Sublime Text 3.  
- HID\_PID\_Descriptor\_Definitions.py:  
Human Interface Device & Physical Interface Device usage definitions.  
- HID\_PID\_DescriptorGenTool.py:  
parses the .rptDsc into bytes(report descriptor).  
- HID\_PID\_DataStructureGen.py:  
parses the .rptDsc into c language data structure definitions.  
  
## How to Use  
- Before writing report descriptor in HID\_Descriptor\_Input.rptDsc, you are recommended to copy \rptDsc to the path refered above so that syntax highlight can work. To parse the descriptor into bytes run DescriptorGenTool, to parse into c language data structure run DataStructureGen.py.   
  
## Parser Limitations  
For the purpose of freeing developers from the tedious and error prone works of writing the Report Descriptor or the data structure attached to it, i made this parser. However, the USB HID Report Descriptor itself was rather a flexible protocol. There is no perfect approach to an easy solution of all the problems we meet in developing.    
### bugs been found:  
- c doesn't support syntax like "enum XXX : _type {...}" to designate specific type to the enum.  

## Screenshots
### editing report descriptor in sublime text:  
![reportDescriptor.png](https://github.com/beantowel/HID_Descriptor_tool/raw/master/Screenshots/reportDescriptor.png)
### get parsed bytes from report descriptor:  
![outputBytes.png](https://github.com/beantowel/HID_Descriptor_tool/raw/master/Screenshots/outputBytes.png)
### get c data structure definitions from report descriptor:  
![dataStructure.png](https://github.com/beantowel/HID_Descriptor_tool/raw/master/Screenshots/dataStructure.png)
