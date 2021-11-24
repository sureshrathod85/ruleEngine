
# Bulletin Rule JSON
data=(r'''{
   "varId":2,
   "blockId":2,
   "vars":[
      {
         "text":"txt1",
         "value":"",
         "symbol":"<*PrimaryCarePhysican*>",
         "fieldType":{
            "text":"Text",
            "value":"text"
         }
      },
      {
         "text":"txt2",
         "value":"",
         "symbol":"<*copays*>",
         "fieldType":{
            "text":"Text",
            "value":"text"
         }
      }
   ],
   "blocks":[
      {
         "id":"_b1",
         "name":"B1:",
         "symbol":"",
         "variable":"txt1",
         "isInvisible":false,
         "caseId":3,
         "cases":[
            {
               "id":"_b1_c1",
               "name":"C1:",
               "incrCount":false,
               "exprs":[
                  {
                     "type":"group",
                     "op":"and",
                     "opText":"",
                     "isRoot":true,
                     "exprs":[
                        {
                           "type":"expr",
                           "pls":"LP",
                           "mbr":"PrimaryCarePhysician",
                           "mbrText":"LP.Primary Care Physician",
                           "op":"contains",
                           "opText":"Contains",
                           "val":"$",
                           "valText":"$",
                           "valComp":false,
                           "editorType":4,
                           "fldComp":false
                        },
                        {
                           "type":"expr",
                           "pln":"LP",
                           "mbr":"PrimaryCarePhysician",
                           "mbrText":"LP.Primary Care Physician",
                           "op":"doesnotcontain",
                           "opText":"Does Not Contain",
                           "val":"-",
                           "valText":"-",
                           "valComp":false,
                           "editorType":4,
                           "fldComp":false
                        }
                     ]
                  }
               ],
               "actions":"<#LP.PrimaryCarePhysician#>"
            },
            {
               "id":"_b1_c3",
               "name":"C3:",
               "incrCount":false,
               "exprs":[
                  {
                     "type":"group",
                     "op":"and",
                     "opText":"",
                     "isRoot":true,
                     "exprs":[

                     ]
                  }
               ],
               "actions":"\"#ERROR\""
            }
         ],
         "actions":""
      },
      {
         "id":"_b2",
         "name":"B2:",
         "symbol":"",
         "variable":"txt2",
         "isInvisible":false,
         "caseId":2,
         "cases":[
            {
               "id":"_b2_c1",
               "name":"C1:",
               "incrCount":false,
               "exprs":[
                  {
                     "type":"group",
                     "op":"and",
                     "opText":"",
                     "isRoot":true,
                     "exprs":[
                        {
                           "type":"expr",
                           "pln":"LP",
                           "mbr":"Channel",
                           "mbrText":"LP.Channel",
                           "op":"eq",
                           "opText":"Is One of (=)",
                           "val":"Retention Direct Mail",
                           "valText":"Retention Direct Mail",
                           "valComp":false,
                           "editorType":1,
                           "fldComp":false
                        }
                     ]
                  }
               ],
               "actions":"\"copay\""
            },
            {
               "id":"_b2_c2",
               "name":"C2:",
               "incrCount":false,
               "exprs":[
                  {
                     "type":"group",
                     "op":"and",
                     "opText":"",
                     "isRoot":true,
                     "exprs":[

                     ]
                  }
               ],
               "actions":"\"copays\""
            }
         ],
         "actions":""
      }
   ]
}''')
import json
json_data=json.loads(data)#print(json_data)

def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    # Joining based on '-' delimiter
    string = ''.join(list_string)
    return string
 
def referance_rule(json_data,input_data):
   global_json=json_data
   ip_list=input_data
   global_list=[]
   lst=input_data
   case_list1=[]
   g_toekn_list=[]
   g_toekn_list = [var[var_item] for var in global_json['vars'] for var_item in var if 'symbol'==var_item]
   #print(g_toekn_list)
   for dict_element in global_json['blocks']:
       action_list=[]
       for dict_sub_element in dict_element['cases']:
           #action_list=[ case_list.append(case_elem[dict_ele]) for case_elem in dict_element['cases'] for dict_ele in case_elem if dict_ele=='actions' ]
           action_list=[ case_elem[dict_ele] for case_elem in dict_element['cases'] for dict_ele in case_elem if dict_ele=='actions' ]
           for dict_sub_elementt_item in dict_sub_element['exprs']:
               for dict_sub_element_element in dict_sub_elementt_item['exprs']:
                   local_list=[]
                   for elements in dict_sub_element_element:
                      # print(elements)
                       for list_item in ip_list:
                           #print(list_item)
                           if list_item == elements:
                               local_list.append(dict_sub_element_element[elements])
                               #print(list_item)
                   global_list.append(local_list)
       case_list1.append(action_list)
   #print(case_list1)
   return global_list,case_list1,g_toekn_list

def generateRule(referance_list,case_list,g_token_list,input_text):
   lst=[]
   #lst.append("var")
   lst.append("var text= "'"{}"'";".format(input_text))
   lst.append("var txt1 = ' ', txt2=' ' ;")
   #lst.append("if")
   for item in range(len(referance_list)):
      #for element in range(len(referance_list[item]))
      referance_list[item][0]=referance_list[item][0].replace('.','_')
      referance_list[item][0]=referance_list[item][0].replace('LP','lp')
      #referance_list[item][0]=referance_list[0][0].replace('.','_')
     # referance_list[item][0]=referance_list[0][0].replace('LP','lp')
   print(referance_list)

   #print(join_string(split_string(referance_list[2][1])))
   lst.append("if (({}.includes (\"{}\") && ({}.includes (\"{}\") && ({}.includes (\"{}\") == {})){{".format(join_string(split_string(referance_list[0][0])),join_string(split_string(referance_list[0][1])),join_string(split_string(referance_list[1][0])),join_string(split_string(referance_list[1][1])),referance_list[2][0],join_string(split_string(referance_list[2][1])),str(referance_list[2][2]).lower()))
         #lst.append("(({}.includes ".format(join_string(split_string(referance_list[item][0])))) #format(referance_list[item][1])))
         #lst.append("(\"{}\")".format(join_string(split_string(referance_list[item][1]))))
         #lst.append(" && ")
         #lst.append("if (({}.includes (\"{}\") && ({}.includes (\"{}\")".format())
         #lst.append("if (({}.includes (\"{}\") && ({}.includes (\"{}\") && ({}.includes (\"{}\")  == {})){{".format(join_string(split_string(referance_list[item][0])),join_string(split_string(referance_list[item][1])),referance_list[len(referance_list)-1][0],str(referance_list[len(referance_list)-1][2]).lower()))
      #else:
          #referance_list[item][0]=referance_list[len(referance_list)-1][0].replace('.','_')
         # referance_list[item][0]=referance_list[len(referance_list)-1][0].replace('LP','lp')
          #lst.append(" ({}.includes (\"{}\") == {})){{ ".format(referance_list[len(referance_list)-1][0],format(join_string(split_string(referance_list[len(referance_list)-1][1]))),str(referance_list[len(referance_list)-1][2]).lower()))
          #lst.append(" == {})){{ ".format(str(referance_list[item][2]).lower()))       
  # lst.append("\n")
   lst.append(" txt1 = '{}'; ".format(join_string(split_string(referance_list[0][0]))))
   lst.append(" }else{ ")
   lst.append("\n")
   lst.append(" txt2 = {};".format(case_list[0][1]))#error ")
   lst.append("}}")
   lst.append("\n")
   lst.append(" if({} == "'"{}"'" ){{".format(join_string(split_string(referance_list[2][0])),join_string(split_string(str(referance_list[2][1])))))
   lst.append("  txt2 = {};".format(case_list[0][1]))#'copay' ;")
          #lst.append("(\"{}\")".format(referance_list[item][1]))
   lst.append("\n")
   lst.append("}else{")
   lst.append("\n")
   lst.append(" txt2 = {};".format(case_list[1][0]))#'copay' ;")
   lst.append("}")
   lst.append("\n")
   #lst.append("text = text.replace('{}<*PrimaryCarePhysican*>',{} txt1".format(g_token_list[0],join_string(split_string(referance_list[0][0]))));
   lst.append("text = text.replace({},{});".format(g_token_list[0],join_string(split_string(referance_list[0][0]))));

   lst.append("\n")
   #lst.append("text = text.replace('<*copays*>', txt2".format(case_list[1][0]));
   lst.append("text = text.replace({},{});".format(g_token_list[1],join_string(split_string(case_list[1][0]))));

   lst.append("\n")        
   lst.append("return text;")
   return lst
   #print(lst)
   #for item in lst:
    #   print(item,sep=" ")
  # print(str1)

          
      #lst.append("({} == {} ))".fomat(referance_list[item][0],list_element))
            
   #lst.append(" _reasult = {} ;".format(str(final_status).lower()))
   #lst.append("return _reasult;")#lst_string[1].format(str(final_status).lower()))
   #for item in lst:
    #  print(item, end=" ")  
   #print("\n")    
 
#inpput_list=['mbrText','val','valComp']      

#refernace_list,case_list,g_token_list=referance_rule(json_data,inpput_list)
#input_string="[Walk-in clinics]<*PrimaryCarePhysican*> <*copays*> for select services at nationally contracted walk-in clinics, including MinuteClinic® locations"
#generateRule(refernace_list,case_list,g_token_list,input_string)
inpput_list=['mbrText','val','valComp']      
refernace_list,case_list,g_token_list=referance_rule(json_data,inpput_list)
input_string="[Walk-in clinics]<*PrimaryCarePhysican*> <*copays*> for select services at nationally contracted walk-in clinics, including MinuteClinic® locations"
lst=generateRule(refernace_list,case_list,g_token_list,input_string)
string_repr="".join(lst)
#print(string_repr)
from py_mini_racer import py_mini_racer
ctx=py_mini_racer.MiniRacer()

print(ctx.eval("var lst={};".format(lst)))
print(ctx.eval("var len=lst.length; var str=' ';var iter=0; while(iter<len) { str=str+lst[iter]; iter=iter+1;} str"))

#for item in lst:
 #  print(item)