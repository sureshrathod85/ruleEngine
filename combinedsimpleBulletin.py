import json
from data import *
class SimpleRule():
    def __init__(self,input_dict1):
        self.input_dict=input_dict1
        self.var_root_element=''
        self.var_local_root_element=''
        self.var_local_operator=''
        self.generated_list=[]
        self.var_init_var="var" 
        self.var_if_statement="if ";
        self.var_open_round_bracket=" ("
        self.var_open_curly_bracket=" {"
        self.var_close_round_bracket=" )"
        self.var_close_curly_bracket=" }"
        self.var_reasult_string=" _reasult"
        self.var_return_string= " return"
        self.flag=False
        self.var_txt=" _txt"
        self.var_txt1=" _txt1"
        self.var_txt2=" _txt2"
        self.var_else=" else "
    
    def getJsonData(self):
        return self.input_dict
    def getGeneratedList(self):
        return self.generated_list
    def getRootElement(self):
        return self.var_root_element
    def getLocalRootElement(self):
        return self.var_local_root_element
    def getLocalOperator(self):
        return self.var_local_operator
    def addToList(self,data):
         self.generated_list.append(data)
    def getOperatorslist(self):
        op_val={"contains":'==',"isnotempty":'!=',"neq":'!=',"eq":'==', 'and':'&&','or':'||','doesnotcontain':'!='}
        return op_val
    def getOperator(self,gl_item):
        op_val=self.getOperatorslist()
        local_operator=""
        for data in gl_item:
            if data=='op':
                if(gl_item[data] in op_val):
                    local_operator=op_val[gl_item[data]]
                break;
        #print(local_operator)
        return local_operator;
    def preConditionalPart(self):
        self.generated_list.append(self.var_init_var)
        self.generated_list.append(" {}; ".format(self.var_reasult_string))
        self.generated_list.append(self.var_if_statement)
        self.generated_list.append(self.var_open_round_bracket)
    def postConditionPart(self):
        #print(self.generated_list)
        if "'unlimited'" in self.generated_list and "'emergency transportation is not covered'" in self.generated_list:#==True:
            self.generated_list.append("== {}".format(str(False).lower()))
        else:
            self.generated_list.append("")
        self.generated_list.append(self.var_close_round_bracket)
        self.generated_list.append(self.var_open_curly_bracket)
        self.generated_list.append("{} = {};".format(self.var_reasult_string,str(True).lower()))
        self.generated_list.append(self.var_close_curly_bracket)
        self.generated_list.append(" else ")
        self.generated_list.append(self.var_open_curly_bracket)
        self.generated_list.append("{} = {};".format(self.var_reasult_string,str(False).lower()))
        self.generated_list.append(self.var_close_curly_bracket)
        self.generated_list.append("{} {};".format(self.var_return_string,self.var_reasult_string))
        self.generated_list.append("{}".format(self.var_close_curly_bracket))


        #self.generated_list.append("{} {};".format(self.var_return_string,self.var_reasult_string))
        #self.generated_list.append(self.var_close_curly_bracket)
    def getConditionalPartBulletin(self,sub_dict,var_root_element,var_action_list):
            if 'exprs' in sub_dict:
                if isinstance(sub_dict['exprs'],list):
                    if len(sub_dict['exprs'])>0:
                        self.generated_list.append(self.var_if_statement)
                        self.generated_list.append(self.var_open_round_bracket)
                        self.var_local_root_element=self.getOperator(sub_dict)
                        self.getDictionayFromList(sub_dict['exprs'],self.var_local_root_element)
                        self.generated_list.append(self.var_close_round_bracket)
                        self.generated_list.append(self.var_open_curly_bracket)
                        list_item=sub_dict['exprs']
                        self.generated_list.append("{}='{}';".format(self.var_txt1,var_action_list[0].strip('"')))
                        self.generated_list.append(self.var_close_curly_bracket)
                        self.generated_list.append("{} ".format(self.var_else))
                        self.generated_list.append(self.var_open_curly_bracket)
                        self.generated_list.append("{}='{}'; ".format(self.var_txt2,var_action_list[1].strip('"')))
                        self.generated_list.append(self.var_close_curly_bracket)

                    else:
                        pass

                else:
                    print("need to span")

            else:
               # print(var_root_element)
                var_local_str=sub_dict['val']
                #input_list,var_local_root_element,sub_dict
                self.getSplittedCondition(var_root_element,var_local_str,sub_dict) 
    def getConditionalPart(self,sub_dict,var_root_element):
            if 'exprs' in sub_dict:
                if isinstance(sub_dict['exprs'],list):
                    if len(sub_dict['exprs'])>0:
                        self.generated_list.append(self.var_open_round_bracket)
                        self.var_local_root_element=self.getOperator(sub_dict)
                        self.getDictionayFromList(sub_dict['exprs'],self.var_local_root_element)
                        self.generated_list.append(self.var_close_round_bracket)
                    else:
                        pass

                else:
                    print("need to span")

            else:
                #print(var_root_element)
                var_local_str=sub_dict['val']
                #input_list,var_local_root_element,sub_dict
                self.getSplittedCondition(var_root_element,var_local_str,sub_dict) 
   
    def getSplittedCondition(self,var_local_root_element,var_local_str,sub_dict):
        input_list=sub_dict['val'].split(',')
        if(len(input_list)>1):
            self.generated_list.append(self.var_open_round_bracket)
            for items in range(len(input_list)):
                if (items <len(input_list)-1):
                    self.generated_list.append(self.var_open_round_bracket)
                    self.generated_list.append("{}_{}".format(sub_dict['pln'],sub_dict['mbr']))
                    var_local_operator=self.getOperator(sub_dict)
                    self.generated_list.append(var_local_operator)
                    self.generated_list.append("'{}'".format(input_list[items]))
                    self.generated_list.append(self.var_close_round_bracket)
                    self.generated_list.append(var_local_root_element)
                else:
                    self.generated_list.append (self.var_open_round_bracket)
                    self.generated_list.append("{}_{}".format(sub_dict['pln'],sub_dict['mbr']))
                    var_local_operator=self.getOperator(sub_dict)
                    self.generated_list.append(var_local_operator)
                    self.generated_list.append("'{}'".format(input_list[items]))
                    self.generated_list.append(self.var_close_round_bracket)
            self.generated_list.append(self.var_close_round_bracket)
        else:
            self.generated_list.append (self.var_open_round_bracket)
            self.generated_list.append("{}_{}".format(sub_dict['pln'],sub_dict['mbr']))
            self.var_local_operator=self.getOperator(sub_dict)
            self.generated_list.append(self.var_local_operator)
            self.generated_list.append("'{}'".format(var_local_str))
            #print( var_local_str)
            self.generated_list.append(self.var_close_round_bracket)
 
    def getDictionayFromList(self,sub_list,var_root_element):
        dict_len=len(sub_list)
        if dict_len==2:
            self.flag=True
        else:
            self.flag=False
        for cnt in range(dict_len):
            if cnt<dict_len-1:
                if( isinstance(sub_list[cnt],dict)):
                    self.var_local_root_element=sub_list[cnt]['op']
                    self.getConditionalPart(sub_list[cnt],var_root_element)
                    self.generated_list.append(var_root_element)
                else:
                    self.var_local_root_element=sub_list[cnt]['op']
            else:

                self.getConditionalPart(sub_list[cnt],var_root_element)
    def startParsing(self,input_json):
        input_dict=input_json
        for item in input_dict:
            #print(input_dict[item])
            list_items=input_dict[item]
            #print("----",list_items)
            if  isinstance(item,dict):
                print("dict")
            
            elif isinstance(list_items,list):
                    self.getDictionayFromList(list_items,self.var_root_element)
            elif isinstance (list_items,dict):
                print("Dictionary-list",item)
                #dict_parser(list_items,rootKey)
            else:
                #print("Header Data ,",item)
                self.var_root_element=self.getOperator(input_dict)
            print("\n")
    def generateString(self):
        return ("".join(self.generated_list))
    def processSimpleRule(self):
        self.preConditionalPart()
        self.startParsing(self.getJsonData());
        self.postConditionPart()
        print("".join(self.getGeneratedList()))
        #return self.generateString()
    
    
    def join_string(self,list_string):
        string = ''.join(list_string)
        return string

    # def processBulletinBoard(self,input_json_file):
    #     input_json=input_json_file
    #     refernace_list,case_list,g_token_list=self.bulleting_referance_rule(input_json)
    #     input_string="[Walk-in clinics]<*PrimaryCarePhysican*> <*copays*> for select services at nationally contracted walk-in clinics, including MinuteClinic® locations"
    #     lst=self.bulletingGenerateRule(refernace_list,case_list,g_token_list,input_string)
    #     print("".join(lst))

    def split_string(self,string):
        list_string = string.split(' ')
        return list_string

    def bulletRuleReferance(self):
        input_list=['mbrText','val','valComp']      
        return input_list
    def bulleting_referance_rule(self):
        global_json=self.getJsonData()
        g_toekn_list = [var[var_item] for var in global_json['vars'] for var_item in var if 'symbol'==var_item]
        #print(g_toekn_list)
        for dict_element in global_json['blocks']:
            action_list=[]
            for dict_sub_element in dict_element['cases']:
                action_list=[ case_elem[dict_ele] for case_elem in dict_element['cases'] for dict_ele in case_elem if dict_ele=='actions' ]
                for dict_sub_elementt_item in dict_sub_element['exprs']:
                    self.var_root_element=dict_sub_elementt_item['op']
                    self.getConditionalPartBulletin(dict_sub_elementt_item,self.var_root_element,action_list)
    
    def preconditionBulletin(self):
        self.generated_list.append(" {} {}= {};".format(self.var_init_var,self.var_txt,"inputText"))
        self.generated_list.append("{} {}= {};".format(self.var_init_var,self.var_txt1,"''"))
        self.generated_list.append("{} {}= {};".format(self.var_init_var,self.var_txt2,"''"))

    def postConditionBulletin(self):
        self.generated_list.append(" {}= {}.replace('{}',{}.toString()); ".format(self.var_txt,self.var_txt,'<PrimaryCarePhysican>',self.var_txt1))
        self.generated_list.append(" {}= {}.replace('{}',{}.toString()); ".format(self.var_txt,self.var_txt,'<PrimaryCarePhysican>',self.var_txt2))
        self.generated_list.append("{} {};".format(self.var_return_string,self.var_txt))
        
    def processBullletin(self):
        self.preconditionBulletin()
        self.bulleting_referance_rule()
        self.postConditionBulletin()
        print("".join(self.generated_list))
        #self.postConditionPart()
        #print(self.getGeneratedList())
        return self.generateString()
    


#input_json=json.loads(inputJson)
#input_json=json.loads(Selection_Rule_4)
#input_json=json.loads(Selection_Rule_3)
#input_json=json.loads(Selection_Rule_4)
#rule=SimpleRule(input_json)
#rule.processSimpleRule()



input_json=json.loads(bulleting_data)
rule1=SimpleRule(input_json)
rule1.processBullletin()

