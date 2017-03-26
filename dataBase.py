all_analysis = {}
#all_analysis["StopandSbottom"] = {"name_tex":"Stop and Sbottom"}
all_analysis["Gluino"] = {"name_tex":"Gluino"}
all_analysis["Squark"] = {"name_tex":"Squark"}
all_analysis["EWKGauginos"] = {"name_tex":'EWK Gauginos'}

"""
List of names corresponding to different SMS
"""
pp = 'pp #rightarrow'

T2bb 	 	  = pp+'#tilde{b}#tilde{b}, #tilde{b} #rightarrow b  #tilde{#chi}_{1}^{0}'
T2tt		  = pp+'#tilde{t}#tilde{t}, #tilde{t} #rightarrow t  #tilde{#chi}_{1}^{0}'
T6bbHH = pp+'#tilde{b}#tilde{b}, #tilde{b} #rightarrow b  #tilde{#chi}_{2}^{0}#rightarrow b H#tilde{#chi}_{1}^0'

T6bbWW 		  = pp+'#tilde{t}#tilde{t}, #tilde{t}#rightarrow #tilde{#chi}_{1}^{#pm} b #rightarrow W^{#pm} #tilde{#chi}_{1}^{0}'


TChiChipmSlepL    = pp+'#tilde{#chi}^{0}_{2} #tilde{#chi}^{#pm}_{1} #rightarrow lll #nu#tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1} '
TChiChipmSlepStau    = pp+'#tilde{#chi}^{0}_{2} #tilde{#chi}^{#pm}_{1} #rightarrow ll#tau #nu#tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1} '
TChiChipmStauStau = pp+'#tilde{#chi}^{0}_{2} #tilde{#chi}^{#pm}_{1} #rightarrow #tau#tau#tau #nu#tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1} '
TChiWZ 		  = pp+' #tilde{#chi}^{0}_{2}#tilde{#chi}^{#pm}_{1} #rightarrow W Z #tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1}'
TChiWH 		  = pp+' #tilde{#chi}^{0}_{2}#tilde{#chi}^{#pm}_{1} #rightarrow W H #tilde{#chi}^{0}_{1} #tilde{#chi}^{0}_{1}'

T1     = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow qq #tilde{#chi}^{0}_{1}'
T2     = pp+'#tilde{q}#tilde{q}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}'
T1tttt = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow tt #tilde{#chi}^{0}_{1}'
T1bbbb = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow bb #tilde{#chi}^{0}_{1}'

T5VV   = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow qq(#tilde{#chi}^{#pm}_{1}/#tilde{#chi}^{0}_{2})#rightarrow qq (W/Z)#tilde{#chi}^{0}_{1}'
T5WW   = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow qq#tilde{#chi}^{#pm}_{1} #rightarrow qq W#tilde{#chi}^{0}_{1}'


T5tctc = pp+'#tilde{g}#tilde{g}, #tilde{g} #rightarrow t #tilde{t} #rightarrow t c #tilde{#chi}_{1}^{0} '

T2bbWWoff = pp+'#tilde{t}#tilde{t}, #tilde{t} #rightarrow b f f  #tilde{#chi}_{1}^{0}(4-body)'

T5ZZGMSB = '#tilde{g} #rightarrow qq#tilde{#chi}^{0} _1, #tilde{#chi}^{0} _1 #rightarrow Z #tilde{G}'


squarks = '#tilde{q}_{R}+#tilde{q}_{L}(#tilde{u},#tilde{d},#tilde{c},#tilde{s})'  # Label to be put for degenerate squarks

D_M = 'M_{Mother}- M_{LSP}#approx'
D_I = 'M_{Interm.}- M_{LSP}#approx'
# NEW


lumi = 12.9
sqrt =  13

# Gluino production
#all_analysis["Gluino"]['']                 = {'pos':1, 'search':'', 		 'max'  : {'050': [0.0, '' , 0 , 0   ]}, 'min': {}, 'decay': ''  ,  'delta': {'050': [0.0,''         , 0 , 0]}} # Useless?
all_analysis["Gluino"]['']                 = {'pos':1, 'search':'', 		 'max'  : {'050': [0.0, '' , 0 , 0   ]}, 'min': {}, 'decay': ''  , }
all_analysis["Gluino"]['16-014-16-033-T1'] = {'pos':2,'search':'0l(MHT)', 	 'max'  : {'050': [1675, 'SUS-16-014 , SUS-16-033',   sqrt, lumi],'Mor':1840},  'decay': T1, }
all_analysis["Gluino"]['16-015-16-036-T1'] = {'pos':3,'search':'0l(MT2)', 	 'max'  : {'050': [1650, 'SUS-16-015 , SUS-16-036',   sqrt, lumi],'Mor':1860},  'decay': T1, }
all_analysis["Gluino"]['16-014-16-033-T1bbbb']    = {'pos':4,'search':'0l(MHT)', 'max'  : {'050': [1750, 'SUS-16-014 , SUS-16-033',   sqrt, lumi],'Mor':1925},  'decay': T1bbbb, }
all_analysis["Gluino"]['16-015-16-036-T1bbbb']    = {'pos':5,'search':'0l(MT2)',	 'max'  : {'050': [1750, 'SUS-16-015 , SUS-16-033',   sqrt, lumi],'Mor':2025},  'decay': T1bbbb, }
all_analysis["Gluino"]['16-016-T1bbbb']    = {'pos':6,'search':'0l(#alpha_{T})', 'max'  : {'050': [1720, 'SUS-16-016',   sqrt, lumi]},  'decay': T1bbbb,}

all_analysis["Gluino"]['16-014-16-033-T1tttt'] = {'pos':7,'search':'0l(MHT)',       'max'  : {'050': [1620, 'SUS-16-014 , SUS-16-033',   sqrt, lumi],'Mor':1945},  'decay': T1tttt, }
all_analysis["Gluino"]['16-015-16-036-T1tttt'] = {'pos':8,'search':'0l(MT2)',       'max'  : {'050': [1700, 'SUS-16-015 , SUS-16-033',   sqrt, lumi],'Mor':1900},  'decay': T1tttt, }
all_analysis["Gluino"]['16-016-T1tttt'] = {'pos':9,'search':'0l(#alpha_{T})',    'max'  : {'050': [1440, 'SUS-16-016',  sqrt, lumi]},  'decay': T1tttt, }
all_analysis["Gluino"]['16-019-16-042-T1tttt'] = {'pos':10,'search':'1l(#Delta#phi)','max': {'050': [1630, 'SUS-16-019 , SUS-16-042',   sqrt, lumi] , 'Mor':1900},  'decay': T1tttt, }
all_analysis["Gluino"]['16-020-16-035-T1tttt'] = {'pos':11,'search':'2l same-sign','max': {'050': [1370, 'SUS-16-020', sqrt, lumi], 'Mor':1530},  'decay': T1tttt, }
all_analysis["Gluino"]['16-022-16-041-T1tttt'] = {'pos':12,'search':'multilepton', 'max': {'050': [1200, 'SUS-16-022',  sqrt, lumi], 'Mor':1630},  'decay': T1tttt, }
all_analysis["Gluino"]['16-030-T1tttt']    = {'pos':13,'search':'0l', 		 'max'  : {'050': [1760, 'SUS-16-030',   sqrt, lumi]},  'decay': T1tttt,  }
all_analysis["Gluino"]['16-037-T1tttt']    = {'pos':14,'search':'1l(MJ)', 	 'max'  : {'050': [0 , 'SUS-16-037',   sqrt, lumi], 'Mor':1900 },  'decay': T1tttt,  }

all_analysis["Gluino"]['16-030-T5tctc']    = {'pos':15,'search':'0l', 	   	 'max'  : {'050': [1500, 'SUS-16-030',   sqrt, lumi]},  'decay': T5tctc, 'x':0.5}
all_analysis["Gluino"]['16-019-16-042-T5WW']  = {'pos':16,'search':'1l(#Delta#phi)','max'  : {'050': [1600, 'SUS-16-019 , SUS-16-042',   sqrt, lumi] , 'Mor':1900},  'decay': T5WW, 'x':0.5  }


all_analysis["Gluino"]['16-020-T5WW']        = {'pos':17,'search':'2l same-sign',  'max'  : {'050': [1100, 'SUS-16-020',   sqrt, lumi]},  'decay': T5WW, 'x':0.5 }
all_analysis["Gluino"]['16-020-T5WWDelta20'] = {'pos':18,'search':'2l same-sign',  'max'  : {'050': [1100, 'SUS-16-020',   sqrt, lumi]},  'decay': T5WW, 'x':0.5, 'comm':'('+D_I +'20 GeV)'  }
all_analysis["Gluino"]['16-014-T5VV']        = {'pos':19,'search':'0l(MHT)', 	 'max'  : {'050': [1625, 'SUS-16-014',   sqrt, lumi]},  'decay': T5VV, 'x':0.5}
all_analysis["Gluino"]['16-022-T5VV']        = {'pos':20,'search':'multilepton',   'max'  : {'050': [1010, 'SUS-16-022',   sqrt, lumi]},  'decay': T5VV, 'x':0.5}
all_analysis["Gluino"]['line']               = {'pos':21, 'search':'', 		   'max'  : {'050': [0.0, '' , 0 , 0   ]}, 'min': {}, 'decay': ''  ,     'delta': {'050': [0.0,''         , 0 , 0]}}



'''
Stop
'''
all_analysis["Squark"]['16-014-16-033-T2tt']= {'pos':1,'search':'0l(MHT)', 	'max'  : {'050': [840, 'SUS-16-014 , SUS-16-033',  sqrt, lumi],'Mor':970},  	'decay': T2tt,   }
all_analysis["Squark"]['16-015-16-036-T2tt']= {'pos':2,'search':'0l(MT2)', 	'max'  : {'050': [900, 'SUS-16-015 , SUS-16-036',  sqrt, lumi],'Mor':1070},  	'decay': T2tt,  }
all_analysis["Squark"]['16-016-T2tt']    = {'pos':3,'search':'0l(#alpha_{T})', 	'max'  : {'050': [860, 'SUS-16-016',  sqrt, lumi]},     'decay': T2tt,   }
all_analysis["Squark"]['16-027-17-001-T2tt']= {'pos':4,'search':'2l','max':{'050': [650, 'SUS-16-027 , 17-001',  sqrt, lumi] ,'Mor':820 },'decay': T2tt,  }
all_analysis["Squark"]['16-028-16-051-T2tt']= {'pos':5,'search':'1l', 	        'max'  : {'050': [860, 'SUS-16-028 , SUS-16-051',  sqrt, lumi],'Mor':1115 },     'decay': T2tt,  }
all_analysis["Squark"]['16-029-T2tt']    = {'pos':6,'search':'0l', 	        'max'  : {'050': [860, 'SUS-16-029',  sqrt, lumi]},     'decay': T2tt,}
all_analysis["Squark"]['16-030-T2tt']    = {'pos':7,'search':'0l', 		'max'  : {'050': [900, 'SUS-16-030',  sqrt, lumi]},     'decay': T2tt,}
all_analysis["Squark"]['16-049-T2tt']    = {'pos':8,'search':'0l', 		'max'  : {'050': [0, 'SUS-16-049',  sqrt, lumi], 'Mor':1030},     'decay': T2tt,}

all_analysis["Squark"]['16-025-T2bbWWoff'] = {'pos':9,'search':'2l' , 'max'  : {'050': [365, 'SUS-16-025',  sqrt, lumi]},    'decay': T2bbWWoff, 'comm':'('+D_M +'30 GeV)'    ,}
all_analysis["Squark"]['16-029-T2bbWWoff'] = {'pos':10,'search':'0l', 'max'  : {'050': [450, 'SUS-16-029',  sqrt, lumi]},    'decay': T2bbWWoff,  'comm':'('+D_M +'25 GeV)'     , }
all_analysis["Squark"]['16-031-T2bbWWoff'] = {'pos':11,'search':'1l soft','max'  : {'050': [330, 'SUS-16-031',  sqrt, lumi]},'decay': T2bbWWoff, 'comm':'('+D_M +'30 GeV)',}

all_analysis["Squark"]['16-028-T6bbWW']  = {'pos':12,'search':'1l', 	'max'  : {'050': [760, 'SUS-16-028',  sqrt, lumi]},  'decay': T6bbWW, 'x':0.5}
all_analysis["Squark"]['16-029-T6bbWW']  = {'pos':13,'search':'0l', 	'max'  : {'050': [710, 'SUS-16-029',  sqrt, lumi]},  'decay': T6bbWW, 'x':0.5}



'''
Sbottom
'''
all_analysis["Squark"]['16-014-16-033-T2bb']= {'pos':14,'search':'0l(MHT)', 	'max'  : {'050': [790,  'SUS-16-014 , SUS-16-033',  sqrt, lumi],'Mor':1040},'decay': T2bb,}
all_analysis["Squark"]['16-015-16-036-T2bb']= {'pos':15,'search':'0l(MT2)', 	'max'  : {'050': [1030, 'SUS-16-015 , SUS-16-036',  sqrt, lumi],'Mor':1170},'decay': T2bb,    }
all_analysis["Squark"]['16-016-T2bb']  = {'pos':16,'search':'0l(#alpha_{T})',	'max'  : {'050': [1020, 'SUS-16-016',  sqrt, lumi]},	'decay': T2bb, }
all_analysis["Squark"]['16-032-T2bb']  = {'pos':17,'search':'0l', 		'max'  : {'050': [0,    'SUS-16-032',  sqrt, lumi],'Mor':1235},	'decay': T2bb,    }
#all_analysis["Squark"]['line']         = {'pos':17,'search':'', 	        'max'  : {'050': [0.0, ''           , 0 , 0   ]},	'decay': ''  ,}

'''
Squark
'''
#all_analysis["Squark"]['line']           	 = {'pos':18,'search':'', 		'max'  : {'050': [0.0, ''           , 0 , 0   ]}, 	'decay': ''  ,    }
all_analysis["Squark"]['16-014-16-033-T2-squark']       = {'pos':18,'search':'0l(MHT)','max'  : {'050': [1160, 'SUS-16-014 , SUS-16-033',sqrt, lumi],'Mor':1450},   'decay': T2, 'rightlabel': squarks }
all_analysis["Squark"]['16-015-16-036-T2-squark']       = {'pos':19,'search':'0l(MT2)','max'  : {'050': [1400, 'SUS-16-015 , SUS-16-036',sqrt, lumi],'Mor':1550},   'decay': T2, 'rightlabel': squarks }
#all_analysis["Squark"]['']           	 = {'pos':18,'search':'', 		'max'  : {'050': [0.0, ''           , 0 , 0   ]}, 	'decay': ''  ,    }



'''
EW Gauginos
'''
all_analysis["EWKGauginos"]['line']                  	 = {'pos':1,'search':'', 'max'  : {'050': [0.0, ''           , 0 , 0   ]}, 'decay': ''}

all_analysis["EWKGauginos"]['16-024-16-039-TChiChipmSlepL05']   = {'pos':2,'search':'multilepton (flavour democratic)', 'max'  : {'050': [1000, 'SUS-16-024 , SUS-16-039',  sqrt, lumi],'Mor':1150}, 
'decay': TChiChipmSlepL, 'x':0.5}
all_analysis["EWKGauginos"]['16-024-16-039-TChiChipmSlepL005']  = {'pos':3,'search':'multilepton + 2l same-sign (flavour democratic)', 'max'  : {'050': [990, 'SUS-16-024 , SUS-16-039',  sqrt, lumi],'Mor':1145},
'decay': TChiChipmSlepL, 'x':0.05}
all_analysis["EWKGauginos"]['16-039-TChiChipmSlepL095']  = {'pos':4,'search':'multilepton + 2l same-sign (flavour democratic)', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':1050},
'decay': TChiChipmSlepL, 'x':0.95}

all_analysis["EWKGauginos"]['16-024-16-039-TChiChipmSlepStau005']   = {'pos':5,'search':'multilepton (tau enriched)', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':1030}, 
'decay': TChiChipmSlepStau, 'x':0.5}
all_analysis["EWKGauginos"]['16-024-16-039-TChiChipmSlepStau050']  = {'pos':6,'search':'multilepton (tau enriched)', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':1080},
'decay': TChiChipmSlepStau, 'x':0.05}
all_analysis["EWKGauginos"]['16-039-TChiChipmSlepStau095']  = {'pos':7,'search':'multilepton (tau enriched)', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':1050},
'decay': TChiChipmSlepStau, 'x':0.95}

all_analysis["EWKGauginos"]['16-039-TChiChipmStauStau'] = {'pos':8,'search':'Multilepton (tau dominated)', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':625}, 'decay': TChiChipmStauStau, 'x':0.5}

#all_analysis["EWKGauginos"]['16-024-TChiChipmStauStau'] = {'search':'Multilepton (tau enriched)', 'max'  : {'050': [460, 'SUS-16-024',  sqrt, lumi]}, 'decay': TChiChipmStauStau, }

all_analysis["EWKGauginos"]['16-024-16-039-TChiWZ'] = {'pos':9,'search':'multilepton', 'max'  : {'050': [375, 'SUS-16-024 , SUS-16-039',  sqrt, lumi],'Mor':450}, 'decay': TChiWZ,}
all_analysis["EWKGauginos"]['16-024-TChiWH']       = {'pos':10,'search':'Multilepton', 'max'  : {'050': [0, 'SUS-16-039',  sqrt, lumi],'Mor':185},  'decay': TChiWH, }
#all_analysis["EWKGauginos"]['16-024-TChiWH']       = {'search':'Multilepton', 'max'  : {'050': [150, 'SUS-16-024',  sqrt, lumi]},  'decay': TChiWH, }
all_analysis["EWKGauginos"]['16-025-16-048-TChiWZ'] = {'pos':11,'search':'2l soft', 'max'  : {'050': [195, 'SUS-16-025',  sqrt, lumi],'Mor':230},  'decay': TChiWZ, 'comm':'('+D_M +'20 GeV)'}
all_analysis["EWKGauginos"]['']           	    = {'pos':12,'search':'', 'max'  : {'050': [0.0, '', 0 , 0   ]}, 'decay': ''  ,    }







# GMSB
#all_analysis["GMSB"]['empty']                   = {'search':'2L(OS)', 'max'  : {'050': [0.0, ''           , 0 , 0   ]}, 'min': {}, 'decay': ''  ,     'delta': {'050': [0.0,''         , 0 , 0]}}
#all_analysis["GMSB"]['16-021-T5ZZGMSB']                   = {'search':'2L(OS) , m_{#tilde{G}}=1 GeV', 'max'  : {'050': [0.0, 'SUS-16-021'           , sqrt , lumi   ]}, 'min': {}, 'decay': T5ZZGMSB  ,     'delta': {'050': [0.0,''         , 0 , 0]}}
#all_analysis["GMSB"]['16-024-TChiZZGMSB']                   = {'search':'Multilepton', 'max'  : {'050': [0.0, 'SUS-16-024'           , sqrt , lumi   ]}, 'min': {}, 'decay': TChiZZGMSB  ,     'delta': {'050': [0.0,''         , 0 , 0]}}




