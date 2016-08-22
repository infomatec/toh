from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_pravar_knight,1,0), (trp_pravar_peasant,10,0), (trp_pravar_crossbowman,1,0), (trp_pravar_man_at_arms, 1, 0), (trp_pravar_footman, 1, 0), (trp_pravar_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(11.05, 42.65),[(trp_player,1,0)]), #[swycartographr] prev. coords: (17, 52.5)
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("temp_party_3","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),
  ("town_1","Burfell",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.17, 79.96),[], 170),                          #[swycartographr] prev. coords: (-17.6, 79.7)
  ("town_2","Hernar",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.5, 112.88),[], 120),                          #[swycartographr] prev. coords: (-53.5, 78.4) #[swycartographr] prev. coords: (-71.1, 106.84)
  ("town_3","Taresterina",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.16, -20.72),[], 80),                          #[swycartographr] prev. coords: (-57.4, -44.5) #[swycartographr] prev. coords: (-80.48, -29.86)
  ("town_4","Kalisos",     icon_town_kalisos|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.4, -6.22),[], 290),                          #[swycartographr] prev. coords: (-70, 15.4) #[swycartographr] prev. coords: (-55.68, 18.69)
  ("town_5","Bilomadal",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.13, 56.51),[], 90),                         #[swycartographr] prev. coords: (-74.6, -79.7) #[swycartographr] prev. coords: (-118.35, -70.56) #[swycartographr] prev. coords: (-121.34, 36.56) #[swycartographr] prev. coords: (-83.56, 83.39) #[swycartographr] prev. coords: (-100.36, 51.52)
  ("town_6","Pravar",   icon_town_pravar|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.44, 16.15),[], 155),                          #[swycartographr] prev. coords: (-96, 26.4)
  ("town_7","Lankladel",   icon_town_lankladel|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.12, 15.93),[], 310),                           #[swycartographr] prev. coords: (-50, -8.5) #[swycartographr] prev. coords: (-33.38, 8.76)

  ("town_8","Nidgornia", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.64, 40.38),[], 175),                           #[swycartographr] prev. coords: (48.44, 39.3) #[swycartographr] prev. coords: (29.77, 39.64)
  ("town_9","Vodianer",   icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.56, 60.04),[], 90),                       #[swycartographr] prev. coords: (94, 65.2) #[swycartographr] prev. coords: (65.07, 77.61)
  ("town_10","Khosot",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.35, -86.76),[], 310),                  #[swycartographr] prev. coords: (135.5, -22) #[swycartographr] prev. coords: (38.21, -138.76) #[swycartographr] prev. coords: (-122.07, -101.78) #[swycartographr] prev. coords: (-106.69, -86.34) #[swycartographr] prev. coords: (-117.25, -98.12)
  ("town_11","Tarahbo",   icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.64, 23.79),[], 150),                      #[swycartographr] prev. coords: (43, 67.5)
  ("town_12","Bulcush", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.56, 100.76),[], 25),                            #[swycartographr] prev. coords: (-1.2, 108.9) #[swycartographr] prev. coords: (7.57, 111.57)
  ("town_13","Yaddala",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.24, 78.52),[], 60),                            #[swycartographr] prev. coords: (64.8, 113.7) #[swycartographr] prev. coords: (58.27, 98.99) #[swycartographr] prev. coords: (33.6, 67.13) #[swycartographr] prev. coords: (-45.57, 18.69) #[swycartographr] prev. coords: (65.33, -46.59) #[swycartographr] prev. coords: (55.61, 130.17)
  ("town_14","Gohmasda",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.49, -76.76),[], 135),                 #[swycartographr] prev. coords: (55.5, -45) #[swycartographr] prev. coords: (-90.13, -111.82) #[swycartographr] prev. coords: (-82.92, -114.75) #[swycartographr] prev. coords: (-119.88, -115.59) #[swycartographr] prev. coords: (-120.73, -118.09)

  ("town_15","Darenbay",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-134.94, 10.12),[], 45),                          #[swycartographr] prev. coords: (-132.8, -47.3) #[swycartographr] prev. coords: (-129.44, -49.48) #[swycartographr] prev. coords: (-106.81, 14.1) #[swycartographr] prev. coords: (-103.11, 7.66) #[swycartographr] prev. coords: (-142.27, 7.4)
  #--
  ("town_16","Dirim",  icon_town_capital|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.05, 19.49),[], 0),  #[swycartographr] prev. coords: (14, -2) #[swycartographr] prev. coords: (15.67, 15.89)
  #--
  
  ("town_17","Sagli",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.38, -89.66),[], 90),                   #[swycartographr] prev. coords: (121.8, 8.6) #[swycartographr] prev. coords: (62.96, -60.15) #[swycartographr] prev. coords: (-83.96, -98.71) #[swycartographr] prev. coords: (-67.63, -82.28) #[swycartographr] prev. coords: (-80.43, -99.29)
  ("town_18","Hotor",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.43, -119.95),[], 135),                    #[swycartographr] prev. coords: (88, -26.5) #[swycartographr] prev. coords: (59.63, -53.71) #[swycartographr] prev. coords: (-137.78, -112.92) #[swycartographr] prev. coords: (-141.67, -104.47)

  ("town_19","Jabba", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.11, -57.06),[], 45),                      #[swycartographr] prev. coords: (15, -107) #[swycartographr] prev. coords: (-9.9, -88.88) #[swycartographr] prev. coords: (-9.16, -77.99) #[swycartographr] prev. coords: (6.74, -59.8)
  ("town_20","Ukdud", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.89, -76.07),[], 270),                   #[swycartographr] prev. coords: (90, -95.1) #[swycartographr] prev. coords: (53.6, -134.45) #[swycartographr] prev. coords: (38.56, -95.69) #[swycartographr] prev. coords: (46.23, -82.06)
  ("town_21","Attayraq", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.09, -61.45),[], 330),                 #[swycartographr] prev. coords: (130.5, -78.5) #[swycartographr] prev. coords: (78.18, -137.32) #[swycartographr] prev. coords: (79.93, -112.17)
  ("town_22","Hilasindar", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.38, -102.65),[], 225),                  #[swycartographr] prev. coords: (165, -106.7) #[swycartographr] prev. coords: (134.45, -101.6) #[swycartographr] prev. coords: (104.52, -125.35) #[swycartographr] prev. coords: (49.85, -120.56)

	#------------free port---
	("free_port","Free Port", icon_town_with_port|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.65, 29.65),[], 130), 
	#----------------------- 
  
#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Famir_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.93, -19.53),[],50),              #[swycartographr] prev. coords: (-101.3, -21) #[swycartographr] prev. coords: (-64.88, -18.75)
  ("castle_2","Saniag_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44, -75.2),[],75),              #[swycartographr] prev. coords: (97.5, -2.2) #[swycartographr] prev. coords: (36.74, -50.24) #[swycartographr] prev. coords: (-74.68, -94.75) #[swycartographr] prev. coords: (-54.3, -73.27) #[swycartographr] prev. coords: (-42.86, -79.66)
  ("castle_3","Badras_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.62, 29.88),[],100),               #[swycartographr] prev. coords: (47.5, 111.3) #[swycartographr] prev. coords: (46.86, 105.5)
  ("castle_4","Gahman_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.85, 67.78),[],180),              #[swycartographr] prev. coords: (32.5, 47.8)
  ("castle_5","Dabaran_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.17, 64.15),[],90),                #[swycartographr] prev. coords: (-4.8, 63.7)
  ("castle_6","Tilbaut_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.82, 34.28),[],55),                #[swycartographr] prev. coords: (37.6, 17.1) #[swycartographr] prev. coords: (19.72, 31.62) #[swycartographr] prev. coords: (15.07, 21.99) #[swycartographr] prev. coords: (13.47, 29.85)
  ("castle_7","Ezanab_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.7, -116.45),[],45),      #[swycartographr] prev. coords: (109.5, 41.5) #[swycartographr] prev. coords: (-87.39, -126.14)
  ("castle_8","Jakaris_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.59, 80.77),[],30),                 #[swycartographr] prev. coords: (35.2, 89)
  ("castle_9","Afdarin_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.93, -43.57),[],100),            #[swycartographr] prev. coords: (-7.5, -82.6) #[swycartographr] prev. coords: (-109.72, -44.56) #[swycartographr] prev. coords: (-113.12, -45.98) #[swycartographr] prev. coords: (-113.21, -44.05)
  ("castle_10","Casbiran_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.13, 89.65),[],110),               #[swycartographr] prev. coords: (24.2, 96.85)
  ("castle_11","Tarbarich_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.50, 97.32),[],75),                #[swycartographr] prev. coords: (-27.5, 83.46)
  ("castle_12","Kasmaral_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.63, 107.71),[],95),            #[swycartographr] prev. coords: (-84.75, 105.5) #[swycartographr] prev. coords: (-103.87, 135.47)
  ("castle_13","Nahramis_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.43, -0.72),[],115),                #[swycartographr] prev. coords: (-10.6, 17.6) #[swycartographr] prev. coords: (-10, 3.26)
  ("castle_14","Kamdisdah_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.95, 34.01),[],90),                 #[swycartographr] prev. coords: (-122.4, -18.1) #[swycartographr] prev. coords: (-85.28, 41.6) #[swycartographr] prev. coords: (-78.22, 33.54)
  ("castle_15","Erlasdim_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.17, 23.74),[],235),            #[swycartographr] prev. coords: (-52.5, -28) #[swycartographr] prev. coords: (-93.99, 18.41)
  ("castle_16","Samawik_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.3, 82.47),[],45),             #[swycartographr] prev. coords: (-10.6, -65.6) #[swycartographr] prev. coords: (-129.92, -73.8) #[swycartographr] prev. coords: (-78.08, 57.16) #[swycartographr] prev. coords: (-95.6, 85.06) #[swycartographr] prev. coords: (-87.41, 80.44)
  ("castle_17","Jibald_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.01, -54.58),[],15),              #[swycartographr] prev. coords: (140.3, -10.8) #[swycartographr] prev. coords: (37.04, -120.98) #[swycartographr] prev. coords: (-135, -102.87) #[swycartographr] prev. coords: (-56.18, -60.17) #[swycartographr] prev. coords: (-50.71, -57.83) #[swycartographr] prev. coords: (-54.25, -54.44)
  #("castle_18","Ismirala_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.58, 56.4),[],300),         #[swycartographr] prev. coords: (14.4, 70.1)
   ("castle_18","Isdarij_Castle",icon_castle_borovod_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.58, 56.4),[],300),         #[swycartographr] prev. coords: (14.4, 70.1)
  ("castle_19","Yasridal_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.73, 55.91),[],280),           #[swycartographr] prev. coords: (69.5, 55.6)
  ("castle_20","Ganisfall_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.86, 7.19),[],260),              #[swycartographr] prev. coords: (16, 11.5)
  ("castle_21","Bolfas_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.11, -43.6),[],260),            #[swycartographr] prev. coords: (-73, -89.5) #[swycartographr] prev. coords: (-110.2, -66.45) #[swycartographr] prev. coords: (-114.22, -25.12) #[swycartographr] prev. coords: (-130.38, -35.47)
  ("castle_22","Naharar_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.14, -52.08),[],260),            #[swycartographr] prev. coords: (33, -64) #[swycartographr] prev. coords: (-77.92, -92.33) #[swycartographr] prev. coords: (-70.56, -74.12) #[swycartographr] prev. coords: (-83.33, -70.71) #[swycartographr] prev. coords: (-75.87, -63.69)
  ("castle_23","Lobania_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.2, 35.1),[],80),              #[swycartographr] prev. coords: (-124.8, 44.3) #[swycartographr] prev. coords: (-19.63, 23.93) #[swycartographr] prev. coords: (-13.59, 27.22)
  ("castle_24","Djibla_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.17, -31.49),[],260),              #[swycartographr] prev. coords: (24.9, -35.6) #[swycartographr] prev. coords: (21.23, -26.85) #[swycartographr] prev. coords: (10.01, -12.47)
  ("castle_25","Frigil_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.37, 27.57),[],260),             #[swycartographr] prev. coords: (-57, 30.6) #[swycartographr] prev. coords: (-47.9, 28.61)
  ("castle_26","Timawil_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.91, -24.63),[],260),             #[swycartographr] prev. coords: (-2.5, -9.5)
  ("castle_27","Carbasidal_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.69, -9.64),[],260),             #[swycartographr] prev. coords: (63.3, -2) #[swycartographr] prev. coords: (26.12, -22.86) #[swycartographr] prev. coords: (10.79, -0.75) #[swycartographr] prev. coords: (2.48, -8.43)
  ("castle_28","Ritus_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.45, -17.63),[],260),         #[swycartographr] prev. coords: (-36.4, -39.3) #[swycartographr] prev. coords: (-35.06, -34.72) #[swycartographr] prev. coords: (-102.11, 3.51) #[swycartographr] prev. coords: (-92.13, -14.4)

  ("castle_29","Galinar_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.97, 80),[],280),          #[swycartographr] prev. coords: (147.7, 50.4) #[swycartographr] prev. coords: (123.78, 64.55) #[swycartographr] prev. coords: (123.82, 64.59)
  ("castle_30","Nasrug_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.52, -74.15),[],260),             #[swycartographr] prev. coords: (176, -47) #[swycartographr] prev. coords: (151.66, -42.14) #[swycartographr] prev. coords: (45.02, -144.58) #[swycartographr] prev. coords: (-130.27, -86.54) #[swycartographr] prev. coords: (-127.69, -84.59)
  ("castle_31","Ndrougda_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.69, -17.05),[],260),          #[swycartographr] prev. coords: (-65.7, -12.5)
  ("castle_32","Randuc_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.47, 82.45),[],260),             #[swycartographr] prev. coords: (2, 30.1) #[swycartographr] prev. coords: (-40.32, 92.26)
  ("castle_33","Korastd_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.81, -31.67),[],80),              #[swycartographr] prev. coords: (-101.4, -32.1) #[swycartographr] prev. coords: (-97.86, -23.85)
  ("castle_34","Shus_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.61, 93.27),[],260),                 #[swycartographr] prev. coords: (-72.5, 78.6) #[swycartographr] prev. coords: (-71.16, 91.7)
  ("castle_35","Hermangild_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.99, 4.74),[],260),            #[swycartographr] prev. coords: (-110, 0)
  ("castle_36","Beligi_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.6, 60.77),[],260),              #[swycartographr] prev. coords: (-47.3, 53.2)
  ("castle_37","Gumrad_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.81, 38.62),[],260),                #[swycartographr] prev. coords: (55.3, 23) #[swycartographr] prev. coords: (71.6, 36.58)
  ("castle_38","Kutublay_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99.36, -63.87),[],260),              #[swycartographr] prev. coords: (141.7, 33.3) #[swycartographr] prev. coords: (63.26, -65.28) #[swycartographr] prev. coords: (-81.78, -106.14) #[swycartographr] prev. coords: (-57.93, -89.69) #[swycartographr] prev. coords: (-109.11, -72.04) #[swycartographr] prev. coords: (-103.04, -67.56)
  ("castle_39","Khiraz_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.8, 74.5),[],280),
  ("castle_40","Hunro_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.94, -110.92),[],260),               #[swycartographr] prev. coords: (62.9, -26) #[swycartographr] prev. coords: (42.45, -33.49)

  ("castle_41","Demiaj_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.59, -38.64),[],260),               #[swycartographr] prev. coords: (71.3, -71.1) #[swycartographr] prev. coords: (64, -54.85)
  ("castle_42","Matran_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.55, -93.98),[],80),              #[swycartographr] prev. coords: (70, -96)
  ("castle_43","Awasher_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.69, -58.32),[],260),             #[swycartographr] prev. coords: (172, -65) #[swycartographr] prev. coords: (147.75, -52.98) #[swycartographr] prev. coords: (61.49, -143.09) #[swycartographr] prev. coords: (65.18, -83.23) #[swycartographr] prev. coords: (28.44, -72.81) #[swycartographr] prev. coords: (10.87, -64.51)
  ("castle_44","Rinda_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.39, -72.83),[],260),             #[swycartographr] prev. coords: (128, -87) #[swycartographr] prev. coords: (82.87, -128.52) #[swycartographr] prev. coords: (69.52, -122.72)
  ("castle_45","Facris_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.49, -45.45),[],260),               #[swycartographr] prev. coords: (30.6, -110.6) #[swycartographr] prev. coords: (19.67, -91.71) #[swycartographr] prev. coords: (-20.8, -57.26) #[swycartographr] prev. coords: (-43.78, -48.97)
  ("castle_46","Hayad_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.29, -87.54),[],260),              #[swycartographr] prev. coords: (13.3, -84.4) #[swycartographr] prev. coords: (16.15, -70.52) #[swycartographr] prev. coords: (-5.58, -95.01)
  ("castle_47","Rasmun_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.55, -37.31),[],260),            #[swycartographr] prev. coords: (116, -74) #[swycartographr] prev. coords: (71.65, -136.24) #[swycartographr] prev. coords: (62.97, -69.63) #[swycartographr] prev. coords: (24.76, -47.08)
  ("castle_48","Qarir_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.32, -34.13),[],260),            #[swycartographr] prev. coords: (157, -80) #[swycartographr] prev. coords: (119.21, -147.67) #[swycartographr] prev. coords: (37.84, -111.41) #[swycartographr] prev. coords: (1.33, -38.2)
	#-----------out post----------------
  #("outpost","Out-Post",icon_village_a|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22, -22),[]),
	("outpost","Alankaa",icon_castle_a|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24, -24),[],260),  
	#-------------------------------

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1", "Rageag",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.94, -8.41),[], 100),              #[swycartographr] prev. coords: (-60, -9.5)
  ("village_2", "Nelbur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.79, -1.12),[], 110),              #[swycartographr] prev. coords: (-13.5, 3.5)
  ("village_3", "Daza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.63, 19.87),[], 120),                #[swycartographr] prev. coords: (-97.4, 36) #[swycartographr] prev. coords: (-64.13, 23.85)
  ("village_4", "Ramin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.85, 8.45),[], 130),                #[swycartographr] prev. coords: (-36.6, -13.2) #[swycartographr] prev. coords: (-27.59, 10.28)
  ("village_5", "Muka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.12, 105.51),[], 170),              #[swycartographr] prev. coords: (-122.7, 106.3) #[swycartographr] prev. coords: (-121.69, 116.02)
  ("village_6", "Niris",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.31, -8.21),[], 100),                #[swycartographr] prev. coords: (5.5, -2.5)
  ("village_7", "Remay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.16, -24.07),[], 110),                #[swycartographr] prev. coords: (39.3, -5.25) #[swycartographr] prev. coords: (20.47, -18.47) #[swycartographr] prev. coords: (19.7, -12.98)
  ("village_8", "Niehra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.45, 90.68),[], 120),                 #[swycartographr] prev. coords: (-49.7, 74) #[swycartographr] prev. coords: (-60.99, 86.04)
  ("village_9", "Nabuy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.74, -1.28),[], 130),              #[swycartographr] prev. coords: (-85, -75.35) #[swycartographr] prev. coords: (-120.02, -58.3) #[swycartographr] prev. coords: (-118.11, -50.83)
  ("village_10","Nimcha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.82, 98.13),[], 170),               #[swycartographr] prev. coords: (8.8, 34.75) #[swycartographr] prev. coords: (-45.23, 95.39)

  ("village_11","Lidusil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.5, -97.42),[], 100),            #[swycartographr] prev. coords: (137.2, -36.5) #[swycartographr] prev. coords: (45.15, -130.81) #[swycartographr] prev. coords: (-110.93, -109.22) #[swycartographr] prev. coords: (-111.81, -99.87) #[swycartographr] prev. coords: (-87.57, -100.84)
  ("village_12","Reman",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.79, -11.47),[], 110),                #[swycartographr] prev. coords: (-45.8, -58.5) #[swycartographr] prev. coords: (-100.92, -7.39) #[swycartographr] prev. coords: (-97.85, -12.06)
  ("village_13","Jaribafi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.6, 0.73),[], 120),                 #[swycartographr] prev. coords: (-119, 3)
  ("village_14","Lumbus",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.26,48.52),[], 130),                #[swycartographr] prev. coords: (40, 52)
  ("village_15","Tielbari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.2, 24.83),[], 170),             #[swycartographr] prev. coords: (-49.3, 26.25) #[swycartographr] prev. coords: (-47.01, 18.53)
  ("village_16","Tispar",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.89, 20.46),[], 170),           #[swycartographr] prev. coords: (74, 86.8) #[swycartographr] prev. coords: (65.99, 85)
  ("village_17","Nozra",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.06, 94.05),[], 35),             #[swycartographr] prev. coords: (44.7, 91.4)
  ("village_18","Nalbiqar",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.29, 25.03),[], 170),         #[swycartographr] prev. coords: (73.7, 30.1)
  ("village_19","Nuhur",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.04, 79.12),[], 170),           #[swycartographr] prev. coords: (152.3, 53.5) #[swycartographr] prev. coords: (127.18, 74.17)
  ("village_20","Mieliss",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.14, 60.06),[], 170),           #[swycartographr] prev. coords: (116, 80.3) #[swycartographr] prev. coords: (107.87, 88.33)

  ("village_21","Kzibaar",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.04, 81.27),[], 100),           #[swycartographr] prev. coords: (60.4, 85)
  ("village_22","Sulshim",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.04, 71.56),[], 110),          #[swycartographr] prev. coords: (125.4, 64) #[swycartographr] prev. coords: (108.04, 74.79)
  ("village_23","Aliya",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.68, 64.53),[], 120),              #[swycartographr] prev. coords: (-133.3, -37.6) #[swycartographr] prev. coords: (-131.28, -38.59) #[swycartographr] prev. coords: (-127.14, -5.63) #[swycartographr] prev. coords: (-133.67, -7.22) #[swycartographr] prev. coords: (-133, -12.92) #[swycartographr] prev. coords: (-73.11, 57)
  ("village_24","Iblud",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.49, 71.66),[], 130),               #[swycartographr] prev. coords: (-57.6, -73) #[swycartographr] prev. coords: (-97.29, -71.06) #[swycartographr] prev. coords: (-102.29, -67.73) #[swycartographr] prev. coords: (-110.79, -53.7) #[swycartographr] prev. coords: (-82.22, 74.14) #[swycartographr] prev. coords: (-83.36, 68.97)
  ("village_25","Ghabachin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.27, -68.99),[], 170),           #[swycartographr] prev. coords: (125.2, -8) #[swycartographr] prev. coords: (20.54, -118.38) #[swycartographr] prev. coords: (8.39, -105.86) #[swycartographr] prev. coords: (6.28, -68.48)
  ("village_26","Ropdur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.99, -11.39),[], 170),            #[swycartographr] prev. coords: (-58.5, -30.8) #[swycartographr] prev. coords: (-79.83, -13.93)
  ("village_27","Ragrita",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.48, -17.73),[], 170),            #[swycartographr] prev. coords: (-146.3, -16.6) #[swycartographr] prev. coords: (-132.68, -20.35)
  ("village_28","Kultash",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.19, -72.8),[], 170),              #[swycartographr] prev. coords: (95, -11.4) #[swycartographr] prev. coords: (47, -48.22) #[swycartographr] prev. coords: (-99.47, -90.66) #[swycartographr] prev. coords: (-106.95, -79.21)
  ("village_29","Nilubina",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.68, 99.82),[], 170),            #[swycartographr] prev. coords: (-90.6, 110.9) #[swycartographr] prev. coords: (-104.28, 125.14)

  ("village_30","Rabri",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.96, 107.02),[], 170),                #[swycartographr] prev. coords: (29.2, 114.3)
  ("village_31","Benami",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.28, 57.49),[], 100),               #[swycartographr] prev. coords: (-24, 53)
  ("village_32","Radsir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.3 , 14.5 ),[], 110),
  ("village_33","Ralismar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59, 10.6),[], 120),
  ("village_34","Halka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.85, 8.77),[], 130),                #[swycartographr] prev. coords: (34.15, -30) #[swycartographr] prev. coords: (7.32, 3.68)
  ("village_35","Nechraf",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.43, 95.57),[], 170),              #[swycartographr] prev. coords: (2.14, 86.9) #[swycartographr] prev. coords: (-2.96, 96.3)
  ("village_36","Kayjak",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.4, 100.7),[], 170),
  ("village_37","Nulakdir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.04, -127.01),[], 170),             #[swycartographr] prev. coords: (164.4, 26) #[swycartographr] prev. coords: (145.2, 18.53) #[swycartographr] prev. coords: (23.32, -134.06) #[swycartographr] prev. coords: (-128.51, -112.69) #[swycartographr] prev. coords: (-124.61, -115.82) #[swycartographr] prev. coords: (-128.5, -120.16)
  ("village_38","Nabiraq",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.8, 11.25),[], 170),
  ("village_39","Narich",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.35, 19.95),[], 170),            #[swycartographr] prev. coords: (-124.3, -29.5) #[swycartographr] prev. coords: (-131.38, -22.59) #[swycartographr] prev. coords: (-129.86, -47.27)
  ("village_40","Nisrab",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.63, 30.48),[], 170),              #[swycartographr] prev. coords: (-12, -53) #[swycartographr] prev. coords: (-132.13, -76.87) #[swycartographr] prev. coords: (-127.85, 24.16) #[swycartographr] prev. coords: (-142.39, 20.3)

  ("village_41","Nagd",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.58, -61.87),[], 100),               #[swycartographr] prev. coords: (175, -39.5) #[swycartographr] prev. coords: (154.42, -30.03) #[swycartographr] prev. coords: (33.66, -131.94) #[swycartographr] prev. coords: (-119.61, -91.38) #[swycartographr] prev. coords: (-129.26, -80.79) #[swycartographr] prev. coords: (-124.21, -81.12)
  ("village_42","Charapan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.7, -92.99),[], 110),       #[swycartographr] prev. coords: (115.4, 21.6) #[swycartographr] prev. coords: (-113.93, -118.59) #[swycartographr] prev. coords: (-95.14, -105.37)
  ("village_43","shuksa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.21, -82.09),[], 120),               #[swycartographr] prev. coords: (99.4, -21.3) #[swycartographr] prev. coords: (51.11, -57.65) #[swycartographr] prev. coords: (-90.84, -101.34) #[swycartographr] prev. coords: (-97.4, -108.26) #[swycartographr] prev. coords: (-117.78, -104.9) #[swycartographr] prev. coords: (-111.7, -106.4)
  ("village_44","Imeb",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.04, -61.29),[], 130),             #[swycartographr] prev. coords: (51.8, -50) #[swycartographr] prev. coords: (-77.86, -100.73) #[swycartographr] prev. coords: (-75.49, -97.33) #[swycartographr] prev. coords: (-59.54, -66.73) #[swycartographr] prev. coords: (-60.08, -61.23) #[swycartographr] prev. coords: (-63.11, -58.87)
  ("village_45","Rulber",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.63, -95.97),[], 170),              #[swycartographr] prev. coords: (151.5, -3) #[swycartographr] prev. coords: (26.2, -125.65) #[swycartographr] prev. coords: (-138.09, -93.92) #[swycartographr] prev. coords: (-139.93, -97.57) #[swycartographr] prev. coords: (-138.19, -94.12)
  ("village_46","Nerfad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.41, -29.65),[], 170),               #[swycartographr] prev. coords: (-82.4, -48.8) #[swycartographr] prev. coords: (-91.22, -37.2)
  ("village_47","Pshish",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.24, 81.4),[], 170),              #[swycartographr] prev. coords: (-101.2, -53.7) #[swycartographr] prev. coords: (-106.06, 24.89) #[swycartographr] prev. coords: (-118.99, 6.12)
  ("village_48","Raviwir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.09, -0.22),[], 170),               #[swycartographr] prev. coords: (-103, 15.3)
  ("village_49","Riraf",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.15, 58.18),[], 10),           #[swycartographr] prev. coords: (90.8, 60.5) #[swycartographr] prev. coords: (63.97, 69.44)
  ("village_50","Indikar",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.89, 47.86),[], 170),          #[swycartographr] prev. coords: (64.1, 55.9)

  ("village_51","Ilbej",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.01, 79.65),[], 100),               #[swycartographr] prev. coords: (-40, 62) #[swycartographr] prev. coords: (-53.13, 79.1)
  ("village_52","Kermash",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.28, -83.36),[], 110),             #[swycartographr] prev. coords: (38.2, -67.7) #[swycartographr] prev. coords: (-66.1, -108.14) #[swycartographr] prev. coords: (-60.43, -105.1) #[swycartographr] prev. coords: (-43.76, -86.56)
  ("village_53","Ilbanil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.45, 13.24),[], 120),             #[swycartographr] prev. coords: (-130.3, 42) #[swycartographr] prev. coords: (-130.03, 39.77) #[swycartographr] prev. coords: (-25.01, 21.57)
  ("village_54","Disha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.6, 4.8),[], 130),                   #[swycartographr] prev. coords: (-19, 15.5)
  ("village_55","Hemadki",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.96, 22.9),[], 170),              #[swycartographr] prev. coords: (37.3, 23.7) #[swycartographr] prev. coords: (22.75, 34.6) #[swycartographr] prev. coords: (16.08, 27.96)
  ("village_56","Andif",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.87, 95.44),[], 170),               #[swycartographr] prev. coords: (-5.55, 75.5)
  ("village_57","Rugarfis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.39, -5.9),[], 170),              #[swycartographr] prev. coords: (24.75, -7.7) #[swycartographr] prev. coords: (17.38, -12.02) #[swycartographr] prev. coords: (16.03, -0.84)
  ("village_58","Zinev",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.50, 71.62),[], 170),                 #[swycartographr] prev. coords: (78.5, 118.3)
  ("village_59","Rumd",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.97, -47.02),[], 170),               #[swycartographr] prev. coords: (-101, -45) #[swycartographr] prev. coords: (-94.44, -30.88) #[swycartographr] prev. coords: (-93.17, -36.06)
  ("village_60","Lahirji",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.35, 25.65),[], 170),               #[swycartographr] prev. coords: (-26.6, 30)

  ("village_61","Nelfaras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.49, 100.89),[], 100),             #[swycartographr] prev. coords: (-99.8, 85.65) #[swycartographr] prev. coords: (-103.32, 96.02)
  ("village_62","cherba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.74, 53.95),[], 100),               #[swycartographr] prev. coords: (36.7, 59.5) #[swycartographr] prev. coords: (21.76, 53.69)
  ("village_63","Nurd",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.57, -17.4),[], 100),                #[swycartographr] prev. coords: (70.75, 1.6) #[swycartographr] prev. coords: (13.93, -14.36) #[swycartographr] prev. coords: (13.21, -7.78)
  ("village_64","Darsihdar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.77, 46.27),[], 100),            #[swycartographr] prev. coords: (-41.5, -35.8) #[swycartographr] prev. coords: (-91.02, 10.01) #[swycartographr] prev. coords: (-85.03, 22.71)
  ("village_65","Halin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.21, 3.67),[], 100),               #[swycartographr] prev. coords: (-86.3, 12.4)
  ("village_66","Rafsind",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.33, 80.39),[], 100),              #[swycartographr] prev. coords: (109, 127.5) #[swycartographr] prev. coords: (87.92, 104.85)
  ("village_67","Jahbara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.78, 36.77),[], 100),               #[swycartographr] prev. coords: (65, 23) #[swycartographr] prev. coords: (80.24, 35.9)
  ("village_68","Silabqir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.75, 51.88),[], 100),            #[swycartographr] prev. coords: (-72.6, -97.5) #[swycartographr] prev. coords: (-123.79, -64.99) #[swycartographr] prev. coords: (-92.75, 41.52) #[swycartographr] prev. coords: (-89.21, 61.19) #[swycartographr] prev. coords: (-92.81, 59.61) #[swycartographr] prev. coords: (-101.65, 49.37)
  ("village_69","Winkar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.48, 77.52),[], 100),                #[swycartographr] prev. coords: (-26.5, 77.6)
  ("village_70","Gensal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.38, -25.91),[], 100),           #[swycartographr] prev. coords: (-94, -27) #[swycartographr] prev. coords: (-74.14, -25.88)

  ("village_71","Nitbat",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.06, -20.85),[], 20),              #[swycartographr] prev. coords: (-9, -20)
  ("village_72","Berl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.18, 7.09),[], 60),               #[swycartographr] prev. coords: (-144, 16.15) #[swycartographr] prev. coords: (-138.48, 14.93) #[swycartographr] prev. coords: (-134.93, 12.45)
  ("village_73","Zachis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.05, -25.7),[], 55),                #[swycartographr] prev. coords: (-63.2, -51.4) #[swycartographr] prev. coords: (-83.9, -43.75) #[swycartographr] prev. coords: (-60.77, -23.48)
  ("village_74","Yakka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.13, 47.57),[], 15),                 #[swycartographr] prev. coords: (49, 31) #[swycartographr] prev. coords: (70.31, 43.19)
  ("village_75","Nalbuh",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.36, 49.47),[], 10),         #[swycartographr] prev. coords: (110.2, 48.8)
  ("village_76","Kedelk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.67, -74.17),[], 35),               #[swycartographr] prev. coords: (91.5, -34.8) #[swycartographr] prev. coords: (67.31, -52.18) #[swycartographr] prev. coords: (-89.62, -85.56) #[swycartographr] prev. coords: (-85.95, -84.01) #[swycartographr] prev. coords: (-85.3, -76.76) #[swycartographr] prev. coords: (-75.88, -78.91) #[swycartographr] prev. coords: (-76.93, -76.66)
  ("village_77","Izir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.2, 116.95),[], 160),                #[swycartographr] prev. coords: (-64.8, 81.5) #[swycartographr] prev. coords: (-64.76, 119.85)
  ("village_78","Misra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.65, 10.96),[], 180),               #[swycartographr] prev. coords: (-30.2, -53.3) #[swycartographr] prev. coords: (-39.88, -30) #[swycartographr] prev. coords: (-100.09, 9.64) #[swycartographr] prev. coords: (-103.55, 9.48) #[swycartographr] prev. coords: (-103.4, 12.79)
  ("village_79","Nastir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-133.34, 1.7),[], 0),                #[swycartographr] prev. coords: (-134.1, -5.5) #[swycartographr] prev. coords: (-129.5, 3.76)
  ("village_80","Daryid",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.25, 54.86),[], 40),                #[swycartographr] prev. coords: (-1.5, 56)

  ("village_81","Nadso",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.66, 77.94),[], 20),                #[swycartographr] prev. coords: (-17.2, 123.6) #[swycartographr] prev. coords: (18.96, 110.44)
  ("village_82","baliy",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.17, -38.97),[], 60),                 #[swycartographr] prev. coords: (12, -26)
  ("village_83","Migsa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.89, 25.41),[], 55),                 #[swycartographr] prev. coords: (-79.9, 55.2) #[swycartographr] prev. coords: (-36.27, 22.65) #[swycartographr] prev. coords: (-32.49, 26.66)
  ("village_84","Zilcha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.29, -29.89),[], 15),               #[swycartographr] prev. coords: (-45.6, -83) #[swycartographr] prev. coords: (-96.68, -77.54) #[swycartographr] prev. coords: (-90.37, -72.09) #[swycartographr] prev. coords: (-92.17, -46.86)
  ("village_85","Malisra",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.84, 72.7),[], 10),           #[swycartographr] prev. coords: (22.8, 71.7)
  ("village_86","Khesal",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.54, 35.98),[], 35),            #[swycartographr] prev. coords: (60.5, 68.2)
  ("village_87","Daniod",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.24, 102.22),[], 160),              #[swycartographr] prev. coords: (52.3, 111.8)
  ("village_88","Kublut",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.81, -117.16),[], 180),                #[swycartographr] prev. coords: (135.8, 24.7) #[swycartographr] prev. coords: (57.99, -61.6) #[swycartographr] prev. coords: (-85.55, -105) #[swycartographr] prev. coords: (-143.34, -110.59) #[swycartographr] prev. coords: (-136.28, -113.63)
  ("village_89","Nuha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.06, -112.05),[], 0),                   #[swycartographr] prev. coords: (70.1, -27.9) #[swycartographr] prev. coords: (45.95, -37.4) #[swycartographr] prev. coords: (-71.73, -113.75)
  ("village_90","Michios",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.86, -45.88),[], 40),             #[swycartographr] prev. coords: (-12.7, -85.5) #[swycartographr] prev. coords: (-110.97, -41.33) #[swycartographr] prev. coords: (-112.8, -35.08) #[swycartographr] prev. coords: (-111.15, -33.01)

  ("village_91","Saria",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.53, -41.28),[], 20),             #[swycartographr] prev. coords: (21.6, -95.3) #[swycartographr] prev. coords: (3.24, -82.1) #[swycartographr] prev. coords: (-25.36, -45.61)
  ("village_92","Nwala",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.84, -68.91),[], 60),              #[swycartographr] prev. coords: (42.5, -111.6) #[swycartographr] prev. coords: (41.86, -76.82) #[swycartographr] prev. coords: (39.96, -68.63)
  ("village_93","Gueton",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.98, -108.23),[], 55),              #[swycartographr] prev. coords: (50, -94.8) #[swycartographr] prev. coords: (-97.56, -122.63) #[swycartographr] prev. coords: (-92.95, -124.72) #[swycartographr] prev. coords: (-92.06, -119.04)
  ("village_94","Kima",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.38, -44.82),[], 15),                #[swycartographr] prev. coords: (75.4, -61.65) #[swycartographr] prev. coords: (73.22, -66.43) #[swycartographr] prev. coords: (65.55, -49.44)
  ("village_95","Ribaz",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.75, -40.32),[], 10),               #[swycartographr] prev. coords: (99, -90.5) #[swycartographr] prev. coords: (73.57, -124.51) #[swycartographr] prev. coords: (27.75, -103.68)
  ("village_96","Chadmar",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.05, -100.59),[], 35),                #[swycartographr] prev. coords: (107, -75) #[swycartographr] prev. coords: (60.18, -133.47) #[swycartographr] prev. coords: (53.51, -100.59)
  ("village_97","Arobia",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.97, -88.53),[], 160),              #[swycartographr] prev. coords: (82.3, -76.8) #[swycartographr] prev. coords: (79.18, -79.43) #[swycartographr] prev. coords: (-99.45, -103.48) #[swycartographr] prev. coords: (-116.31, -91.57) #[swycartographr] prev. coords: (-121.42, -90.26)
  ("village_98","Koh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.97, -75.97),[], 180),               #[swycartographr] prev. coords: (117.7, -62.2) #[swycartographr] prev. coords: (69.12, -120.7) #[swycartographr] prev. coords: (40.02, -100.43) #[swycartographr] prev. coords: (27.74, -78.93)
  ("village_99","Zarda",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.39, -80.18),[], 0),              #[swycartographr] prev. coords: (158.35, -98) #[swycartographr] prev. coords: (107.68, -130.66) #[swycartographr] prev. coords: (87.18, -116.5)
  ("village_100","Boziq",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.91, -87.99),[], 40),             #[swycartographr] prev. coords: (150, -106.5) #[swycartographr] prev. coords: (108.76, -136.48) #[swycartographr] prev. coords: (32.61, -75.84) #[swycartographr] prev. coords: (0.46, -97.8)

  ("village_101","Ghaz",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.04, -60.54),[], 20),               #[swycartographr] prev. coords: (154, -69.5) #[swycartographr] prev. coords: (84.49, -137.24)
  ("village_102","Tmanayun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.7, -62.95),[], 60),           #[swycartographr] prev. coords: (77.2, -91)
  ("village_103","Shidra",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.68, -82.07),[], 55),             #[swycartographr] prev. coords: (121, -95.6) #[swycartographr] prev. coords: (89.49, -126.96) #[swycartographr] prev. coords: (73.53, -108.54)
  ("village_104","Junzatar",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.09, -109.14),[], 15),            #[swycartographr] prev. coords: (159, -58.5) #[swycartographr] prev. coords: (148.11, -69.49) #[swycartographr] prev. coords: (89.85, -139.91) #[swycartographr] prev. coords: (63.69, -106.94)
  ("village_105","Barat",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.57, -50.66),[], 10),                 #[swycartographr] prev. coords: (135, -88.5) #[swycartographr] prev. coords: (97.54, -136.32)
  ("village_106","Waidiha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.72, -91.0),[], 35),                 #[swycartographr] prev. coords: (10.3, -58.78) #[swycartographr] prev. coords: (-3.2, -91)
  ("village_107","Yanrif",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.13, -108.4),[], 160),             #[swycartographr] prev. coords: (156.6, -84) #[swycartographr] prev. coords: (112.19, -143.4) #[swycartographr] prev. coords: (96.17, -120.07)
  ("village_108","Nitmun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.78, -70.11),[], 180),             #[swycartographr] prev. coords: (28.8, -107.3) #[swycartographr] prev. coords: (13.23, -85.07) #[swycartographr] prev. coords: (-7.15, -76.4)
  ("village_109","Badir",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.03, -79.24),[], 0),              #[swycartographr] prev. coords: (53, -114.5)
  ("village_110","Digra",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.41, -49.99),[], 40),              #[swycartographr] prev. coords: (38, -104) #[swycartographr] prev. coords: (29.79, -65.3) #[swycartographr] prev. coords: (22.1, -50.96)
	#-----------refugee camp-------------
  ("village_111","Workers Camp", icon_village_a|pf_village|pf_disabled, no_menu, pt_none,fac_neutral,0,ai_bhvr_hold,0,(-21, -21),[]),              #[swycartographr] prev. coords: (38, -104) #[swycartographr] prev. coords: (29.79, -65.3) #[swycartographr] prev. coords: (22.1, -50.96)
	#-------------------------------------
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
	#-------------------------------
  ("ruins","Ancient Ruins",icon_village_deserted_a|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22, -22),[]),
	#------------------------------
  ("new_order_camp","White Order Camp",icon_castle_c|pf_is_static|pf_hide_defenders|pf_disabled, no_menu, pt_none, fac_the_new_order,0,ai_bhvr_hold,0,(-52.58, 53.74),[]),
	#-------------------------------
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.96, 101.51),[], 100), #[swycartographr] prev. coords: (37.4, 102.8)
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.62, 33.43),[], 100), #[swycartographr] prev. coords: (-12.8, 33) #[swycartographr] prev. coords: (3.84, 34.02)
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.24, 72.0),[], 100), #[swycartographr] prev. coords: (70.5, 66.79) #[swycartographr] prev. coords: (65.18, 72)
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.96, -13),[], 100), #[swycartographr] prev. coords: (11.5, -75.2) #[swycartographr] prev. coords: (-2.14, -63.73) #[swycartographr] prev. coords: (-15.75, -10.6) #[swycartographr] prev. coords: (-14.65, -10.4)
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.77, -7.67),[], 100), #[swycartographr] prev. coords: (-125.8, 12.5)


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.23, 79.70),[], 107), #[swycartographr] prev. coords: (39.37, 51.46) #[swycartographr] prev. coords: (31.37, 54.4) rot: -44.8 #[swycartographr] prev. coords: (31.82, 89.65) #[swycartographr] prev. coords: (32.49, 89.66) rot: 72 #[swycartographr] prev. coords: (37.13, 89.64) #[swycartographr] prev. coords: (37.16, 79.87) #[swycartographr] prev. coords: (37.16, 88.89) rot: 100 #[swycartographr] prev. coords: (42.28, 65.1)
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.63, 98.79),[], 262), #[swycartographr] prev. coords: (56.44, 77.88) rot: 4.28 #[swycartographr] prev. coords: (-52.79, 14.81) rot: 356
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.46, -19.04),[], 335), #[swycartographr] prev. coords: (70.87, 87.95) #[swycartographr] prev. coords: (65.53, 90.49) rot: 64.5 #[swycartographr] prev. coords: (-81.54, -26.79) rot: 24
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.2, 89.64),[], 278), #[swycartographr] prev. coords: (93.71, 62.13) #[swycartographr] prev. coords: (60.58, 78.75) rot: -2.13 #[swycartographr] prev. coords: (37.42, 69.67) #[swycartographr] prev. coords: (-9.71, 26.12) rot: 251
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.05, 18.3),[], 352), #[swycartographr] prev. coords: (11.02, 72.61) rot: 21.5 #[swycartographr] prev. coords: (11.3, 18.21) rot: 3
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.16, 17.06),[], 169), #[swycartographr] prev. coords: (-8.83, 52.24) #[swycartographr] prev. coords: (-28.28, 18.13) rot: -73.5 #[swycartographr] prev. coords: (-29.06, 18.38) rot: 154 #[swycartographr] prev. coords: (-29.03, 18.3) rot: 157
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.15, 64.64),[], -64), #[swycartographr] prev. coords: (-29.79, 76.84) #[swycartographr] prev. coords: (49.56, 61.86)
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.19, 11.76),[], 40), #[swycartographr] prev. coords: (-64.05, -6) #[swycartographr] prev. coords: (-68.33, 10.95) #[swycartographr] prev. coords: (-69.35, 10.2) rot: 1.72 #[swycartographr] prev. coords: (-71.49, 8.37)
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.94, 14.65),[], 8), #[swycartographr] prev. coords: (-64.95, 14.69) #[swycartographr] prev. coords: (-72.22, -9.6) rot: -33.76
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.19, -26.94),[], 144), #[swycartographr] prev. coords: (-75.32, -75.27) #[swycartographr] prev. coords: (-102.27, -60.33) #[swycartographr] prev. coords: (-101.29, -52.26) #[swycartographr] prev. coords: (-99.76, -92.09) #[swycartographr] prev. coords: (-93.25, -29.46) rot: -44.07 #[swycartographr] prev. coords: (-79.67, 0.9) rot: 233 #[swycartographr] prev. coords: (-85.19, -26.94) rot: 229
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.95, 17.31),[], 348), #[swycartographr] prev. coords: (-24.39, 67.82) rot: 81.3 #[swycartographr] prev. coords: (-8.65, 18.18) rot: 351
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.92, -28.59),[], 359), #[swycartographr] prev. coords: (-114.33, -1.94) #[swycartographr] prev. coords: (-82.26, 7.41) rot: -35.5 #[swycartographr] prev. coords: (-60.7, -25.75) rot: 331
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.84, 18.24),[], 329), #[swycartographr] prev. coords: (-84.02, -7) #[swycartographr] prev. coords: (-81.85, -0.93) #[swycartographr] prev. coords: (-71.56, 21.62) #[swycartographr] prev. coords: (-71.66, 21.33) rot: -17.7
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.77, 51.4),[], 71), #[swycartographr] prev. coords: (-23.36, 75.8) rot: 66.6 #[swycartographr] prev. coords: (37.97, 87.36) rot: 105

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-98, -98),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(65, 83),[(trp_looter,15,0)]),
##  ("black_guhulay_spawn_point"  ,"black_guhulay_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-52, 44),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(104, -24.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_galnar_clan,0,ai_bhvr_hold,0,(-36.5, 108),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_galnar_clan,0,ai_bhvr_hold,0,(-96, 91.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(61, -93),[(trp_looter,15,0)]),
	#--free companies
  ("north_free_company_spawn_point"  ,"the north",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(7.18, 62.41),[(trp_looter,15,0)]),
  ("west_free_company_spawn_point"  ,"the west",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-65.94, 30.77),[(trp_looter,15,0)]),
  ("south_free_company_spawn_point"  ,"the south",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42.72, -55.23),[(trp_looter,15,0)]),
	#--
 #--doomcall 
   ("doomcall_spawn_point"  ,"the lac",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-24, -24),[(trp_looter,15,0)]),
  ("new_order_spawn_point"  ,"the mountain",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-52.58, 53.74),[(trp_looter,15,0)]),

 
 #--
 
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
