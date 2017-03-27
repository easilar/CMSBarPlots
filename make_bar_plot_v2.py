#!/usr/bin/env python
import ROOT
import os, argparse, types, sys
from dataBase import *
ROOT.gStyle.Reset()

ROOT.gROOT.SetStyle("Plain")
#ROOT.gROOT.SetBatch() #canvas will not be drawn
ROOT.gStyle.SetOptStat(0000)
#ROOT.TGaxis.SetMaxDigits(4)
#ROOT.gPad.SetTicks(0,0)
#ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetPadLeftMargin(0.18)
ROOT.gStyle.SetPadRightMargin(0.05)
ROOT.gStyle.SetPadBottomMargin(0.15)
ROOT.gStyle.SetPadTopMargin(0.08)

'''
#----------------------------#Configure plot from here#----------------------#
#bar_color_13 = ROOT.kGray
bar_color_13 = ROOT.kCyan-8
#bar_color_13_Dark = ROOT.kGray+2
bar_color_13_Dark = ROOT.kCyan-1
bar_color_36 = ROOT.kAzure+5 # 36 fb bar color
#bar_color_36 = ROOT.kGray
#bar_color_13 = ROOT.kCyan-10 # 36 fb bar color

'''
bar_color_13 = ROOT.kMagenta-4

bar_color_13  = ROOT.kOrange -3
bar_color_36 = ROOT.kAzure+7 

bar_color_13  = ROOT.kOrange -3

bar_width  =  0.85 
tex_width  =  1.035 #will determine pas names spacing 
histo_xaxis_max = 2200
line_color = ROOT.kBlue
line_depence = 1.03 ## 2 blue lines spacing maybe we change this as well 
#path = "/afs/hephy.at/user/e/easilar/www/barplots/" #TODO
path = os.getcwd()+'/plots/'
filename='barplot_Moriond'
#----------------------------#------------------------#----------------------#

#for analysis_group in all_analysis.keys():
#  print "there are " , len([x for x in all_analysis[analysis_group].keys() if "-" in x]) , " analysis for " , all_analysis[analysis_group]["name_tex"]

all_analysis_list  = [x for y in all_analysis.keys() for x in all_analysis[y].keys() if not "name" in x ] #with empties
xmax = len(all_analysis_list)
#print "in total there are " , xmax ,"analysis histogram xmas will be " , xmax+1 , ".This result is calculated with 4 empty histogram" 

#---------defining histograms-----------
c = ROOT.TCanvas("c","",10000,8000)
#c = ROOT.TCanvas("c","",1000,800)
pad1 = ROOT.TPad("pad1","",0,0,1,1)
pad2 = ROOT.TPad("pad2","",0,0,1,1)
pad3 = ROOT.TPad("pad3","",0,0,1,1)
pad4 = ROOT.TPad("pad4","",0,0,1,1)
pad5 = ROOT.TPad("pad5","",0,0,1,1)
#pad6 = ROOT.TPad("pad5","",0,0,1,1)

bins = xmax
xmin = 0
#----------create TH1F with fixed bins-----------------
h_Stack = ROOT.THStack('h_Stack','h_Stack')
hmaxICHEP = ROOT.TH1F('hmaxICHEP', '', bins, xmin, xmax+1)
hmaxMoriond = ROOT.TH1F('hmaxMoriond', '', bins, xmin, xmax+1)
#--these are for axis--#
hmax05 = ROOT.TH1F('hmax05', '', bins, xmin, xmax+1)	    #SUS-XX-XX 
hmax06 = ROOT.TH1F('hmax06', '', bins, xmin, xmax+1)	    #soft , multi lepton 
hmax07 = ROOT.TH1F('hmax07', '', bins, xmin, xmax+1)	    #string mass mother or intermediate diff
hmax08 = ROOT.TH1F('hmax08', '', bins, xmin, xmax+1)	    # x= 0.5 ...
#h_Stack.Draw()
#-----------fill histograms--------------
index = 0
for analysis_group in  ['EWKGauginos','Squark','Gluino']:
#for analysis_group in all_analysis:
  #print 'THIS IS THE ANALYSIS GROUP', analysis_group

  name_tex = all_analysis[str(analysis_group)]["name_tex"] 
  #print 8*"*" , "in the analysis group : " , name_tex , 8*"*" # e.g. Stop&Sbottom
  Tot = len(all_analysis[str(analysis_group)].keys())  
  for num in reversed(range(1,Tot+1)):              # This loop respectes the ordering definined by 'pos' int he dictionary!
   for interp in all_analysis[str(analysis_group)] :
         if not "name" in interp : 
           #print 4*"-" , "interp is :" , interp
           interp_dict = all_analysis[analysis_group][interp] 
           if(interp_dict['pos']==num):
		   hmaxICHEP.SetBinContent(index+1, 0)
		   if "050" in interp_dict["max"].keys() : hmaxICHEP.SetBinContent(index+1, interp_dict["max"]["050"][0])
		   hmaxMoriond.SetBinContent(index+1, 0)
		   #if "Mor" in interp_dict["max"].keys() : hmaxMoriond.SetBinContent(index+1, interp_dict["max"]["Mor"]-interp_dict["max"]["050"][0])
		   if "Mor" in interp_dict["max"].keys() : hmaxMoriond.SetBinContent(index+1, interp_dict["max"]["Mor"])
		   hmax05.SetBinContent(index+1, interp_dict["max"]["050"][0])
		   hmax06.SetBinContent(index+1, interp_dict["max"]["050"][0])
		   hmax07.SetBinContent(index+1, interp_dict["max"]["050"][0])
		   hmax08.SetBinContent(index+1, interp_dict["max"]["050"][0])
		   list_cadi_label = interp_dict["max"]["050"][1].split(",") 
	           #print list_cadi_label
		   if len(list_cadi_label) < 2 : 
			xlabel =  list_cadi_label[0]+' ' +interp_dict['search'] 
			if "Mor" in interp_dict["max"].keys() : xlabel =  '#color[4]{'+list_cadi_label[0]+'}   '+interp_dict['search']
		   #xlabel =  '#color[4]{'+interp_dict["max"]["050"][1]+'} ' +interp_dict['search'] 
		   if len(list_cadi_label) == 2 : xlabel =  list_cadi_label[0]+',#color[4]{'+list_cadi_label[1]+'}   ' +interp_dict['search']
		   if "rightlabel" in interp_dict.keys():
		      xlabel +=100*" "+"#scale[1.4]{#font[22]{"+interp_dict['rightlabel']+"}}"
		   extra_xlabel_1 = ""
		   extra_xlabel_2 = ""
		   if "comm" in interp_dict.keys():
		      extra_xlabel_1 +=interp_dict['comm']
		   if "x" in interp_dict.keys():
		      extra_xlabel_2 +="#scale[1.2]{#font[22]{x="+str(interp_dict['x'])+"}}"
		   #h_Stack.GetXaxis().SetBinLabel(index+1, xlabel)
		   #hmaxICHEP.GetXaxis().SetBinLabel(index+1, xlabel)
		   #hmaxMoriond.GetXaxis().SetBinLabel(index+1, xlabel)
		   hmaxICHEP.GetXaxis().SetBinLabel(index+1, "")
		   hmaxMoriond.GetXaxis().SetBinLabel(index+1, "")
		   hmax05.GetXaxis().SetBinLabel(index+1, xlabel)                   #SUS-XX-XX 
		   hmax06.GetXaxis().SetBinLabel(index+1, interp_dict["decay"])     #soft , multi lepton 
		   hmax07.GetXaxis().SetBinLabel(index+1, extra_xlabel_1)	        #string mass mother or intermediate diff
		   hmax08.GetXaxis().SetBinLabel(index+1, extra_xlabel_2)	        # x= 0.5 ...
		   index +=1



#----------draw plot-----------

c.cd()
pad1.Draw()
pad1.cd()

hmaxICHEP.SetFillColor(bar_color_13)
hmaxICHEP.SetStats(0)
hmaxICHEP.SetBarWidth(bar_width)
hmaxICHEP.SetBarOffset(0.05)
hmaxICHEP.SetTickLength(0)
hmaxICHEP.GetYaxis().SetTickLength(0.01)
hmaxICHEP.GetXaxis().SetTickLength(0.0)
hmaxICHEP.SetYTitle("Mass scale [GeV]")
hmaxICHEP.GetYaxis().SetTitleFont(42)
hmaxICHEP.SetTitleSize(0.025, "Y")
hmaxICHEP.GetYaxis().SetTitleOffset(1.1)
hmaxICHEP.SetLabelSize(0.013, "X")
hmaxICHEP.SetLabelSize(0.025, "Y")
hmaxICHEP.SetLabelFont(42, "X")
hmaxICHEP.SetLabelFont(42, "Y")
hmaxICHEP.SetLabelOffset(-0.33, "X")
hmaxICHEP.SetMaximum(histo_xaxis_max)
hmaxMoriond.SetFillColor(bar_color_36)
hmaxMoriond.SetStats(0)
hmaxMoriond.SetBarWidth(bar_width)
hmaxMoriond.SetBarOffset(0.05)
hmaxMoriond.SetTickLength(0)
hmaxMoriond.GetYaxis().SetTickLength(0.01)
hmaxMoriond.GetXaxis().SetTickLength(0.0)
hmaxMoriond.SetYTitle("Mass scale [GeV]")
hmaxMoriond.GetYaxis().SetTitleFont(42)
hmaxMoriond.SetTitleSize(0.025, "Y")
hmaxMoriond.GetYaxis().SetTitleOffset(1.1)
#hmaxMoriond.SetLabelSize(0.0, "X")
#hmaxMoriond.SetLabelSize(0.0, "Y")
hmaxMoriond.SetLabelSize(0.013, "X")
hmaxMoriond.SetLabelSize(0.025, "Y")
hmaxMoriond.SetLabelFont(42, "X")
hmaxMoriond.SetLabelFont(42, "Y")
hmaxMoriond.SetLabelOffset(-0.33, "X")
hmaxMoriond.SetMaximum(histo_xaxis_max)
#h_Stack.Add(hmaxICHEP)
#h_Stack.Add(hmaxMoriond)
#h_Stack.Draw('')
#h_Stack.SetMaximum(histo_xaxis_max)
#h_Stack.SetTickLength(0)
#h_Stack.SetTitle("")
#h_Stack.Draw('HBAR0 Y+')
hmaxMoriond.Draw('HBAR0 Y+')
hmaxICHEP.Draw('HBAR0 Y+ same')
pad2.Draw()
pad2.cd()
pad2.SetFillStyle(4000)
hmax05.SetTickLength(0)
hmax05.GetYaxis().SetTickLength(0.0)
hmax05.GetXaxis().SetTickLength(0.0)
hmax05.SetLabelSize(0.013, "X")
hmax05.SetLabelSize(0.0, "Y")
hmax05.SetLabelOffset(-0.33, "X")
hmax05.SetMaximum(histo_xaxis_max)
hmax05.SetFillStyle(4000)
hmax05.Draw("HBAR0 Y+ same")
pad3.Draw()
pad3.cd()
pad3.SetFillStyle(4000)
hmax06.SetTickLength(0)
hmax06.GetYaxis().SetTickLength(0.0)
hmax06.GetXaxis().SetTickLength(0.0)
hmax06.SetLabelSize(0.013, "X")
hmax06.SetLabelSize(0.0, "Y")
hmax06.SetFillStyle(4000)
hmax06.SetMaximum(histo_xaxis_max)
hmax06.Draw("HBAR0 same")
#c.cd()
pad4.Draw()
pad4.cd()
pad4.SetFillStyle(4000)
#pad3.SetFillColor(0)
#pad3.setFrameColor(0)
hmax07.SetTickLength(0)
hmax07.GetYaxis().SetTickLength(0.0)
hmax07.GetXaxis().SetTickLength(0.0)
hmax07.SetLabelSize(0.013, "X")
hmax07.SetLabelSize(0.0, "Y")
hmax07.SetLabelOffset(-0.29, "X") # TODO position of the DeltaM labels
hmax07.SetFillStyle(4000)
hmax07.SetMaximum(histo_xaxis_max)
#hmax07.SetFillColorAlpha(ROOT.kRed, 1.0)
hmax07.Draw("HBAR0 Y+ same")
pad5.Draw()
pad5.cd()
pad5.SetFillStyle(4000)
hmax08.SetTickLength(0)
hmax08.GetYaxis().SetTickLength(0.0)
hmax08.GetXaxis().SetTickLength(0.0)
hmax08.SetLabelSize(0.013, "X")
hmax08.SetLabelSize(0.0, "Y")
hmax08.SetLabelOffset(-0.2, "X") # TODO position of the x parameter
hmax08.SetMaximum(histo_xaxis_max)
hmax08.SetFillStyle(4000)
hmax08.Draw("HBAR0 Y+ same")
#c.cd()
#pad3.RedrawAxis()
#c.cd()
#pad2.RedrawAxis()
#c.cd()
#pad1.RedrawAxis()

#------For PAS numbers / Production Types ------
latex_pas = ROOT.TLatex()
latex_pas.SetTextSize(0.013)
latex_pas.SetLineWidth(2)
latex_ana = ROOT.TLatex()
latex_ana.SetTextColor(line_color)
latex_ana.SetTextFont(70)
latex_ana.SetTextSize(0.02)
latex_ana.SetTextAngle(90)
latex_ana.SetLineWidth(2)
latex_ana.Draw()
i = 0

name_tex_xPosition = -345 # Position of the vertical label of process type, e.g. gluinos/stop and sbottom etc.

Delta_Position = 240
for analysis_group in  ['EWKGauginos','Squark','Gluino']:
  name_tex = all_analysis[str(analysis_group)]["name_tex"]
  #print name_tex
  if (name_tex =='EWK Gauginos'): latex_ana.DrawLatex(name_tex_xPosition ,0 ,name_tex)                   # Shift Position for EWkinos label 
  elif (name_tex =='Gluino'):  latex_ana.DrawLatex(name_tex_xPosition ,41 ,name_tex)                     # Shift Position for EWkinos label 
  elif (name_tex =='Squark'):  latex_ana.DrawLatex(name_tex_xPosition ,21 ,name_tex)                     # Shift Position for EWkinos label 
  Tot = len(all_analysis[str(analysis_group)].keys())  
  for num in reversed(range(1,Tot+1)):  
   for interp in all_analysis[str(analysis_group)] :
    if not "name_tex" in interp:
     interp_dict = all_analysis[analysis_group][interp]         #
     if(interp_dict['pos']==num ):              #
       #print len(all_analysis[str(analysis_group)].keys()) , num , interp_dict['pos']
       if 'line' in interp:
          exec('line_'+str(i)+' = ROOT.TLine(-320,(i*line_depence)+0.5,histo_xaxis_max,(i*line_depence)+0.5)')
          exec('line_'+str(i)+'.SetLineColor(line_color)')
          exec('line_'+str(i)+'.SetLineStyle(7)')
          exec('line_'+str(i)+'.Draw()')
       i += 1

#------------CMS Headers ------------------------#
tex = ROOT.TLatex(0,54.5,"Selected CMS SUSY Results* - SMS Interpretation")
tex.SetTextSize(0.025)
tex.SetLineWidth(2)
tex.Draw()
tex2 = ROOT.TLatex(1750,54.5,"#color[" + str(bar_color_13) + "]{ICHEP '16} - #color[" +str(bar_color_36) + "]{Moriond '17}")
tex2.SetTextSize(0.025)
tex2.SetLineWidth(2)
tex2.Draw()
tex1 = ROOT.TLatex(1500,20,"#splitline{CMS Preliminary}{#sqrt{s} = 13TeV}")
tex1.SetTextSize(0.04)
tex1.SetLineWidth(2)
tex1.Draw()
tex3 = ROOT.TLatex(1510,16,"L = 12.9 fb^{-1}")
tex3.SetTextSize(0.025)
tex3.SetTextColor(bar_color_13)
tex3.SetLineWidth(2)
tex3.Draw()
tex6 = ROOT.TLatex(1750,16.,"L = 35.9 fb^{-1}")
tex6.SetTextSize(0.025)
tex6.SetTextColor(bar_color_36)
tex6.SetLineWidth(2)
tex6.Draw()

#-------------Foot note--------------------------#
tex4 = ROOT.TLatex(1400,3.0,"#splitline{For decays with intermediate mass,}{m_{Intermediate} = x#upoint m_{Mother}+(1-x)#upoint m_{LSP}}")
tex4.SetTextFont(42)
tex4.SetTextSize(0.02)
tex4.SetLineWidth(2)
tex4.Draw()
tex5 = ROOT.TLatex(-0,-4.5,"#splitline{*Observed limits at 95% C.L. - theory uncertainties not included}{ Only a selection of available mass limits. Probe *up to* the quoted mass limit for  m_{LSP} #approx0 GeV unless stated otherwise  }")
tex5.SetTextFont(42)
tex5.SetTextSize(0.021)
tex5.SetLineWidth(2)
tex5.Draw()
#tex6 = ROOT.TLatex(-0,-6.6,"Probe *up to* the quoted mass limit for m_{LSP}= 0 GeV unless stated otherwise")
#tex6.SetTextFont(42)
#tex6.SetTextSize(0.021)
#tex6.SetLineWidth(2)
#tex6.Draw()
#tex6 = ROOT.TLatex(-0,-6.9,"** Probe up to m _{#tilde{t}} - m_{LSP}= 80 GeV probe up to m_{#tilde{#chi}^{#pm}_{1},#tilde{#chi}^{0}_{2}} - m_{LSP}= 40 GeV")
#tex6.SetTextFont(42)
#tex6.SetTextSize(0.021)
#tex6.SetLineWidth(2)
#tex6.Draw()

#------------put save directories----------------#

#if not os.path.exists(path):
#    os.makedirs(path)
pad1.cd()
pad1.Modified()
pad2.cd()
pad2.Modified()
pad3.cd()
pad3.Modified()
pad4.cd()
pad4.Modified()
pad5.cd()
pad5.Modified()
c.cd()
c.Modified()
c.cd()
c.SetSelected(c)
#c.Draw()
c.SaveAs(path+filename+".pdf")
#c.SaveAs(path+filename+".png")
c.SaveAs(path+filename+".root")
#c.SaveAs(path+filename+".C")
