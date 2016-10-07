from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  #---------------------------------------------
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),
  #----------------------------------------------
   #---------------------------------------------
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  #---------------------------------------------- 
   #---------------------------------------------
  ("culture_9",  "{!}culture_8", 0, 0.9, [], []),
  #----------------------------------------------   

#  ("pravar_caravans","Pravar Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("borovod_caravans","Borovod Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Kingdom of Pravar", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDC143C),
  ("kingdom_2",  "Borovod Principality",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xEE82EE),
  ("kingdom_3",  "Guhulay Khanate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xe0b25a),
  ("kingdom_4",  "Kingdom of Hadvog",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x3390dd),
  ("kingdom_5",  "Imifir Confederation",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x259b6a),
  ("kingdom_6",  "Afirid Dynastie",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x89b932),
	#---------------------------------
	("kingdom_7",  "Dirim Empire",  0, 0.9, [("outlaws",-0.05),("kingdom_1", -0.9),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xf85e11),
	#---------------------------------
	#---------------------------------
	("kingdom_8",  "West Trade Company",  0, 0.9, [("outlaws",-0.05),("kingdom_1", 1),("kingdom_2", 0.5),("kingdom_3", 1),("kingdom_4", 1),("kingdom_5", 1),("kingdom_6", 1),("kingdom_7", 1),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFFD700),
	#---------------------------------	
	
##  ("kingdom_1_rebels",  "Pravar rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Borovod rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Guhulay rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Hadvog rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Imifir rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("guhulays","{!}Guhulays", 0, 0.5,[("player_faction",0.0)], []),
  ("black_guhulays","{!}Black Guhulays", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("borovods",-0.5),("player_faction",0.0)], []),
  ("jalik_mercenaries","Jalik Mercenaries", 0, 0.5,[("deserters",-1),("player_faction",0.0),("kingdom_5",-0.1),("kingdom_7",-1)], [], 0x0045cd),
  ("knights_of_doomcall","Knights Of Doomcall", 0, 0.5,[("player_supporters_faction",-0.5),("player_faction",-0.1),("kingdom_1",0),("kingdom_7",-1),("kingdom_2",-1),("kingdom_3",-1),("kingdom_4",-1),("kingdom_5",-1),("kingdom_6",-1),("the_new_order",-1)], [], 0x000000),
   ("the_new_order","The New Order", 0, 0.5,[("player_supporters_faction",-0.01),("player_faction",0.0),("kingdom_5",1),("kingdom_7",-1),("kingdom_1",-1),("knights_of_doomcall",-1)], [], 0x6c8057), 
  ("sons_of_mekhresh","The Sons Of Mekhresh", 0, 0.5,[("player_supporters_faction",-0.5),("player_faction",-0.1),("knights_of_doomcall",-0.1),("kingdom_1",-1),("kingdom_7",-1),("kingdom_2",-1),("kingdom_3",-1),("kingdom_4",-1),("kingdom_5",-1),("kingdom_6",0),("the_new_order",-1)], [], 0x8c8859),
  ("disciplined","disciplined", 0, 0.5,[("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("player_supporters_faction",0),("player_faction",0),("knights_of_doomcall",-1),("sons_of_mekhresh",-1),("galnar_clan",-1)], [], 0xcf535f),
  ("desert_tribes","Desert Tribes", 0, 0.5,[("player_supporters_faction",-0.01),("kingdom_6",-1),("kingdom_3",0.5)], [], 0xe0b25b),  
  ("golden_horde","Golden Hordes", 0, 0.5,[("player_supporters_faction",-0.01),("kingdom_6",-1),("kingdom_5",-1),("kingdom_3",0.5)], [], 0xe0b26a),   
 
#--pretenders factions
  ("galnar_clan","Galnar Clan", 0, 0.5,[("kingdom_4",-1),("kingdom_7",-0.6),("kingdom_2",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888ffe),
#--
 
  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]
