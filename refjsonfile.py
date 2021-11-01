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
json_data=json.loads(data)


'''var text = bulletText;  //'[Walk-in clinics]<*PrimaryCarePhysican*> <*copays*> for select services at nationally contracted walk-in clinics, including MinuteClinic® locations
'
var cnt = 0, txt1 = '', txt2='';

if ((lp_PrimaryCarePhysician.includes('$')) && ( lp.PrimaryCarePhysician.includes('-') == false)) {
  txt1 = lp.PrimaryCarePhysician;
} else {
  txt1 = '#ERROR';
}

if (lp_Channel == 'Retention Direct Mail')) {
  txt2 = 'copay';
} else {
  txt2 = 'copays';
}

text = text.replace('<*PrimaryCarePhysican*>', txt1);
text = text.replace('<*copays*>', txt2);

return text;'''

