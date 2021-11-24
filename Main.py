from os import stat
from combinedsimpleBulletin import *
from py_mini_racer import py_mini_racer
from time import perf_counter, perf_counter_ns
import time
import threading
ctx=py_mini_racer.MiniRacer()
#var  _reasult; if  ( ( (AP_OTCAllowance=='$' ) )|| ( (AP_ContractPBP!='' ) ) ) { _reasult = true; } else  { _reasult = false; }
start = 0.0
end_time=0.0
#ctx.eval("var selection1=function(var_AP_OTCAllowance) {var  _reasult; if  ( ( (var_AP_OTCAllowance=='$' ) )|| ( (var_AP_OTCAllowance!='' ) ) ) { _reasult = true; } else  { _reasult = false; } return _reasult}")
#perf_counter to measueare system wide time
#process_time to measure process time
#ctx.call("selection1",'$')

"""
    Time in nano seconds |requests
Total Time----2565536189 |100000
TotalTime----257088921   |10000
Total Time----27058083   |1000
Total Time----3001227    |100
Total Time----373714     |10
"""
#var_rule_call = ctx.call("selection1",'$')
#if var_rule_call==True:
 #   ctx.eval("var bulletin_board=function(lp_type,lp_care,lp_channel){var  _txt= 'inputText <PrimaryCarePhysican>';var  _txt1= '';var  _txt2= '';if  ( (lp_type=='$' )&& (lp_care!='-' ) ) { _txt1='<#LP.PrimaryCarePhysician#>';  } else   { _txt2='#ERROR';  _txt1;}if  ( (lp_channel=='Retention Direct Mail' ) ) { _txt1='copay'; } else   { _txt2='copays';  }  _txt=  _txt.replace('<PrimaryCarePhysican>', _txt1.toString());   _txt=  _txt.replace('<PrimaryCarePhysican>', _txt2.toString()); return _txt;}")
  #  var_reasult=ctx.call("bulletin_board",'$','-','Retention Direct Mail')
   # print("bulletin_board->>>>",var_reasult)
#print(ctx.eval("fun"))
#ctx.call("selection2",'d')

"""
    Time in nano seconds |requests
Total Time----2561195422|100000
Total Time----1283300800|50000
TotalTime----256078823  |10000
Total Time----27111467  |1000
Total Time----4396807   | 100
Total Time----494810    |10
"""


#print(ctx.call("selection2",'d'))

ctx.eval("var selection2=function (var_AP_OTCAllowance){var  _reasult; if  ( (var_AP_OTCAllowance!='' ) ) { _reasult = true; } else  { _reasult = false; } return _reasult;}")
#ctx.call("selection2",'e')
start, end_time
start = perf_counter_ns()
for i in range(50000):
    ctx.call("selection2",'d')
end_time=perf_counter_ns()
print("Total Time---- {}".format(end_time-start))


#print(ctx.call("selection2",'e'))
#var  _reasult; if  ( (LP_Transportation!='emergency transportation is not covered' )&& (LP_Transportation!='unlimited' )== false ) { _reasult = true; } else  { _reasult = false; }
#ctx.eval("var selection3=function(LP_Transportation,LP_Transportation_pln){ var  _reasult; if  ( (LP_Transportation!='emergency transportation is not covered' )&& (LP_Transportation_pln!='unlimited' )== false ) { _reasult = true; } else  { _reasult = false; } return _reasult;}")
#print(ctx.call("selection3",'emergency transportation is not covered','unlimited'))
"""
    Time in nano seconds |requests
Total Time----2587420011 |100000
Total Time----1269495756 |50000
TotalTime----258974466   |10000
Total Time----28159074   |1000
Total Time----2940055    |100
Total Time----540526     |10
"""
ctx.eval("var selection3=function(LP_Transportation,LP_Transportation_pln){ var  _reasult; if  ( (LP_Transportation!='emergency transportation is not covered' )&& (LP_Transportation_pln!='unlimited' )== false ) { _reasult = true; } else  { _reasult = false; } return _reasult;}")
#ctx.call("selection3",'emergency transportation is not covered','unlimited')    
#ctx.call("selection3",'','unlimited')


"""
    Time in nano seconds |requests
Total Time----2591029718 |100000
Total Time---- 1236113292|50000
TotalTime----255774097   |10000
Total Time----27742642   |1000
Total Time----2908285    |100
Total Time----439230     |10
"""

#print(ctx.call("selection3",'','unlimited'))

#var  _reasult; if  ( ( (AP_LimitedNetwork!='Yes' )&& ( (AP_VisitorTraveler=='Travel Advantage' )&& (AP_VisitorTraveler=='Explorer' ) ) )|| ( (LP_LimitedNetwork!='Yes' )|| ( (LP_VisitorTraveler=='Travel Advantage' )|| (LP_VisitorTraveler=='Explorer' ) ) ) ) { _reasult = true; } else  { _reasult = false; }
ctx.eval("var selection4=function(AP_LimitedNetwork,AP_VisitorTraveler,AP_Explorer,LP_LimitedNetwork,LP_VisitorTraveler,LP_Exporer){var  _reasult; if  ( ( (AP_LimitedNetwork!='Yes' )&& ( (AP_VisitorTraveler=='Travel Advantage' )&& (AP_Explorer=='Explorer' ) ) )|| ( (LP_LimitedNetwork !='Yes' )|| ( (LP_VisitorTraveler=='Travel Advantage' )|| (AP_Explorer=='Explorer' ) ) ) ) { _reasult = true; } else  { _reasult = false; } return _reasult;}")
ctx.call("selection4",'No','Travel Advantage','Explorer','No','Travel Advantage','Explorer')

"""
    Time in nano seconds |requests
Total Time----2687247993 |100000
Total Time---- 1315649331|50000
TotalTime----264193400   |10000
Total Time----27994615   |1000
Total Time----3020661    |100
Total Time----497700     |10
"""


#print(ctx.call("selection4",'No','Travel Advantage','Explorer','No','Travel Advantage','Explorer'))
# var  _txt= inputText;var  _txt1= '';var  _txt2= '';if  ( (LP_PrimaryCarePhysician=='$' )&& (LP_PrimaryCarePhysician!='-' ) ) { _txt1='<#LP.PrimaryCarePhysician#>'; } else   { _txt2='#ERROR';  }if  ( (LP_Channel=='Retention Direct Mail' ) ) { _txt1='copay'; } else   { _txt2='copays';  }  _txt=  _txt.replace('<PrimaryCarePhysican>', _txt1.toString());   _txt=  _txt.replace('<PrimaryCarePhysican>', _txt2.toString()); return  _txt;
ctx.eval("var bulletin_board=function(lp_type,lp_care,lp_channel){var  _txt= 'inputText <PrimaryCarePhysican>';var  _txt1= '';var  _txt2= '';if  ( (lp_type=='$' )&& (lp_care!='-' ) ) { _txt1='<#LP.PrimaryCarePhysician#>';  } else   { _txt2='#ERROR';  _txt1;}if  ( (lp_channel=='Retention Direct Mail' ) ) { _txt1='copay'; } else   { _txt2='copays';  }  _txt=  _txt.replace('<PrimaryCarePhysican>', _txt1.toString());   _txt=  _txt.replace('<PrimaryCarePhysican>', _txt2.toString()); return _txt;}")
#print(ctx.call("bulletin_board",'$','-','Retention Direct Mail'))

"""
    Time in nano seconds |requests
Total Time----2708001683 |100000
Total Time----1402656335 |50000
TotalTime----264124278   |10000
Total Time----28138809   |1000
Total Time----3073192    |100
Total Time----388443     |10
"""


