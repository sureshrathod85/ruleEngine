inputJson="""{
   "type":"group",
   "op":"or",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"group",
         "op":"and",
         "opText":"",
         "isRoot":false,
         "exprs":[
            {
               "type":"expr",
               "pln":"AP",
               "mbr":"OTCAllowance",
               "mbrText":"AP.OTC Allowance",
               "op":"contains",
               "opText":"Contains",
               "val":"$",
               "valText":"$",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            }
           
         ],
         "actions":[

         ]
      },
      {
         "type":"group",
         "op":"and",
         "opText":"",
         "isRoot":false,
         "exprs":[
            {
               "type":"expr",
               "pln":"AP",
               "mbr":"ContractPBP",
               "mbrText":"AP.Contract PBP",
               "op":"isnotempty",
               "opText":"Is Not Empty",
               "val":"",
               "valText":"",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            }
         ],
         "actions":[

         ]
      }
   ]
}
"""


Selection_Rule_2="""
{
   "type":"group",
   "op":"and",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"DiagProceduresTests",
         "mbrText":"LP.Diag Procedures Tests",
         "op":"isnotempty",
         "opText":"Is Not Empty",
         "val":"",
         "valText":"",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      }
   ]
}
"""
Selection_Rule_4 ="""{
   "type":"group",
   "op":"or",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"group",
         "op":"and",
         "opText":"",
         "isRoot":false,
         "exprs":[
            {
               "type":"expr",
               "pln":"AP",
               "mbr":"LimitedNetwork",
               "mbrText":"AP.Limited Network",
               "op":"neq",
               "opText":"Not One of (!=)",
               "val":"Yes",
               "valText":"Yes",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            },
            {
               "type":"expr",
               "pln":"AP",
               "mbr":"VisitorTraveler",
               "mbrText":"AP.Visitor Traveler",
               "op":"eq",
               "opText":"Is One of (=)",
               "val":"Travel Advantage,Explorer",
               "valText":"Travel Advantage,Explorer",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            }
         ],
         "actions":[

         ]
      },
      {
         "type":"group",
         "op":"or",
         "opText":"",
         "isRoot":false,
         "exprs":[
            {
               "type":"expr",
               "pln":"LP",
               "mbr":"LimitedNetwork",
               "mbrText":"LP.Limited Network",
               "op":"neq",
               "opText":"Not One of (!=)",
               "val":"Yes",
               "valText":"Yes",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            },
            {
               "type":"expr",
               "pln":"LP",
               "mbr":"VisitorTraveler",
               "mbrText":"LP.Visitor Traveler",
               "op":"eq",
               "opText":"Is One of (=)",
               "val":"Travel Advantage,Explorer",
               "valText":"Travel Advantage,Explorer",
               "valComp":false,
               "editorType":1,
               "fldComp":false
            }
         ],
         "actions":[

         ]
      }
   ]
}
"""

Selection_Rule_3="""
{
   "type":"group",
   "op":"and",
   "opText":"",
   "isRoot":true,
   "exprs":[
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"Transportation",
         "mbrText":"LP.Transportation",
         "op":"neq",
         "opText":"Not One of (!=)",
         "val":"emergency transportation is not covered",
         "valText":"Non-emergency transportation is not covered",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      },
      {
         "type":"expr",
         "pln":"LP",
         "mbr":"Transportation",
         "mbrText":"LP.Transportation",
         "op":"doesnotcontain",
         "opText":"Does not Contain",
         "val":"unlimited",
         "valText":"unlimited",
         "valComp":false,
         "editorType":1,
         "fldComp":false
      }

   ]
}
"""

bulleting_data=(r'''{
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
                           "pln":"LP",
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
