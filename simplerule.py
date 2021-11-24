
import json
from typing import final
inputJson='''{
   "type":"group",
   "op":"and",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"OpenAccess",
         "mbrText":"LP.Open Access",
         "op":"contains",
         "opText":"Contains",
         "val":"PCPNotRequired/RefNotRequired",
         "valText":"PCPNotRequired/RefNotRequired",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      },
      {
         "type":"expo",
         "pln":"LP",
         "mbr":"OpenAccess",
         "mbrText":"LP.Open Access",
         "op":"contains",
         "opText":"Contains",
         "val":"PCPRequired/RefNotRequired",
         "valText":"PCPRequired/RefNotRequired",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      },
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"Platform",
         "mbrText":"LP.Platform",
         "op":"eq",
         "opText":"Is One of (=)",
         "val":"PPO,RPPO",
         "valText":"PPO,RPPO",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      }
   ]
}
'''
NextJson='''{
   "type":"group",
   "op":"and",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"OpenAccess",
         "mbrText":"LP.Open Access",
         "op":"contains",
         "opText":"Contains",
         "val":"PCPNotRequired/RefNotRequired",
         "valText":"PCPNotRequired/RefNotRequired",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      },
      {
         "type":"expo",
         "pln":"LP",
         "mbr":"OpenAccess",
         "mbrText":"LP.Open Access",
         "op":"contains",
         "opText":"Contains",
         "val":"PCPRequired/RefNotRequired",
         "valText":"PCPRequired/RefNotRequired",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      },
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"Platform",
         "mbrText":"LP.Platform",
         "op":"eq",
         "opText":"Is One of (=)",
         "val":"PPO,RPPO",
         "valText":"PPO,RPPO",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      }
   ]
}'''

def referance_rule(input_Json,input_list):
   global_list=[]
   local_input_list=input_list
   #print(local_input_list)
   lst=input_Json['exprs']
   #print(lst)
   for ndict in lst:
      local_list=[]
      for elmenet in ndict.keys():
         for k in local_input_list:
            if elmenet == k :
               if (',' in ndict[elmenet]):
                  local_split=ndict[elmenet].split(',')
                  local_list.append(local_split)
               else:
                  local_list.append(ndict[elmenet])
      global_list.append(local_list)
   #print(global_list)
   return global_list

#inputdict={"mbr":"LP.Open Access","val":"PCPNotRequired/RefNotRequired","valText":"PPO,RPPO"}
#inputdict={"mbr":"OpenAccess","valText":"PPO,RPPO","mbr":"Platform","val":"PCPNotRequired/RefNotRequired","val":"PCPRequired/RefNotRequired"}
inputdict=["mbrText","val"]
val_to_compare=["temp","PCPRequired/RefNotRequired","PPO","RPPO"]

def generateRule(referance_list,final_status):
   lst=[]
   #lst_string=["var ","_reasult = {}","if ","(lp_{}.includes","(\"{}\"))","&&"]
   init_status=False

   #varstring="var _reasult = {}  ".format(init_status)
   lst.append("var")
   lst.append("_reasult = {} ;".format(str(init_status).lower()))#lst_string[1].format(str(init_status).lower()))
   lst.append("if")#lst_string[2])
   #lst.append(lst_string[2])
   for item in range(len(referance_list)):
      #for element in range(len(referance_list[item]))
      if(item<(len(referance_list)-1)):
         referance_list[item][0]=referance_list[item][0].replace('.','_')
         referance_list[item][0]=referance_list[item][0].replace('LP','lp')
         lst.append("({}.includes ".format(referance_list[item][0]))
         lst.append("(\"{}\")".format(referance_list[item][1]))
         lst.append("&&")
      else:
         if (isinstance(referance_list[item][1],list)):
            #for list_element in referance_list[item][1]:
               referance_list[item][0]=referance_list[item][0].replace('.','_')
               referance_list[item][0]=referance_list[item][0].replace('LP','lp')

               lst.append("({} == {} || {} == {}))".format(referance_list[item][0],referance_list[item][1][0],referance_list[item][0],referance_list[item][1][1],))
               #lst.append("({} == {} ))".format(referance_list[item][0],list_element))
         else:
            lst.append("(\"{}\")".format(referance_list[item][1]))
            
   lst.append(" _reasult = {} ;".format(str(final_status).lower()))
   lst.append("return _reasult;")#lst_string[1].format(str(final_status).lower()))
   for item in lst:
      print(item, end=" ")  
   print("\n")    

def generateRule1(referance_list,final_status):
   lst=[]
   #lst_string=["var ","_reasult = {}","if ","(lp_{}.includes","(\"{}\"))","&&"]
   init_status=False

   #varstring="var _reasult = {}  ".format(init_status)
   #lst.append("var")
   lst.append("var _reasult = {} ;".format(str(init_status).lower()))#lst_string[1].format(str(init_status).lower()))
   #lst.append("if")#lst_string[2])
   #lst.append(lst_string[2])
   for item in range(len(referance_list)):
      #for element in range(len(referance_list[item]))
      #if(item<(len(referance_list)-1)):
      referance_list[item][0]=referance_list[item][0].replace('.','_')
      referance_list[item][0]=referance_list[item][0].replace('LP','lp')

   lst.append("if ({}.includes (\"{}\") && ({}.includes (\"{}\") && ({} == {} || {} == {}))".format(referance_list[0][0],referance_list[0][1],referance_list[1][0],referance_list[1][1],referance_list[item][0],referance_list[item][1][0],referance_list[item][0],referance_list[item][1][1]))
   lst.append("\n")       
   lst.append(" _reasult = {} ;".format(str(final_status).lower()))
   lst.append("\n")
   lst.append("return _reasult;")#lst_string[1].format(str(final_status).lower()))
   return (lst)
   #for item in lst:
    #  print(item, sep=" ")  
   #print("\n")    

def perform_check(referance_list,compared_list):
   for referance_item in referance_list: 
      if referance_item  in compared_list:
            return True
      else:
         return False
import  json
input_Json=json.loads(inputJson)
Next_Json=json.loads(NextJson)
referance_list=referance_rule(input_Json,inputdict)
compared_list=referance_rule(Next_Json,inputdict)
status=perform_check(referance_list,compared_list)   
lst=generateRule1(compared_list,status)
#print(lst)
convert_string="".join(lst)
#print(convert_string)

from py_mini_racer import py_mini_racer
ctx=py_mini_racer.MiniRacer()
#ctx.eval("var lst={};".format(convert_string))
ctx.eval("var lst={};".format(lst))
print(ctx.eval("var len=lst.length; var str=' ';var iter=0; while(iter<len) { str=str+lst[iter]; iter=iter+1;} str"))
#print(ctx.eval("var str=' '; var lst={};var len=lst.length; var iter=0; while (iter<len){ str=str+lst[iter] ;iter=iter+1;} str".format(lst)))
#print(ctx.eval(" {} ".format(convert_string)))
#print(convert_string)

#for item in lst:
 #  print(item)




