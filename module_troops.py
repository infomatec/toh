import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_nidgornia_castle|entry(1) puts troop in nidgornia castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Burfell
#  town_2   Hernar
#  town_3   Taresterina
#  town_4   Kalisos
#  town_5   Bilomadal
#  town_6   Pravar
#  town_7   Lankladel
#  town_8   Nidgornia
#  town_9   Vodianer
#  town_10  Khosot
#  town_11  Tarahbo
#  town_12  Bulcush
#  town_13  Yaddala
#  town_14  Gohmasda
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2| knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_4|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_4|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9
#--
#knight_weapons = itm_knights_winged_mace_1h,itm_war_hammer_no4,itm_horsemans_axe_no3,itm_ball_mace_no2,itm_war_hammer_no4,itm_morningstar_no1,itm_arming_winged_mace,itm_byzantine_mace_3,itm_morningstar_2,itm_morningstar_3,itm_light_knightly_axe,itm_knights_winged_mace_1h,itm_warhammer_ita,itm_gothic_hammer,itm_gothic_puncture_mace
#mercenary_melee_armors=itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail
#mercenary_ranger_armors=itm_nord_breastplate_over_gambeson,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail
#mercenary_nord_armors=itm_nord_breastplate_over_gambeson,itm_nord_cuirass_over_gambeson,itm_nord_breastplate_over_mail,itm_nord_cuirass_over_mail,itm_nord_heavy_cuirass_over_mail,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c
#mercenary_heavy_armors=itm_nord_cuirass_over_mail,itm_nord_heavy_cuirass_over_mail,,itm_short_coat_of_plates_a,itm_common_cuirass_orange
#--
#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.

reserved = 0

no_scene = 0

dirim_face_young_1 		= 0x000000073301101038e36db6e36db6e300000000001db8db0000000000000000
dirim_face_middle_1		= 0x0000000c480cc0104adceac574d564ab00000000001e44990000000000000000

pravar_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
pravar_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
pravar_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
pravar_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
pravar_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

pravar_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
pravar_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
pravar_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
pravar_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
pravar_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

borovod_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
borovod_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
borovod_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
borovod_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
borovod_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

borovod_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
borovod_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
borovod_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
borovod_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
borovod_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

guhulay_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
guhulay_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
guhulay_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
guhulay_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
guhulay_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

guhulay_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
guhulay_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
guhulay_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
guhulay_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
guhulay_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

hadvog_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
hadvog_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
hadvog_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
hadvog_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
hadvog_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

hadvog_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
hadvog_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
hadvog_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
hadvog_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
hadvog_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

imifir_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
imifir_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
imifir_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
imifir_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
imifir_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

imifir_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
imifir_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
imifir_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
imifir_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
imifir_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

#--------------------afirids faces--------------------------------------------------------------
afirid_face_younger_1 = 0x000000003f10a00436db6db6db6db6db00000000001db6db0000000000000000
afirid_face_young_1   = 0x000000013100b4c646dc6db4e369b6db00000000001e38e30000000000000000
afirid_face_middle_1  = 0x000000023100a18646dc6db6db6db6db00000000001e38e30000000000000000
afirid_face_old_1     = 0x0000000d3100a29246dd6dd4e369b6d300000000001e38a10000000000000000
afirid_face_older_1   = 0x0000000f9600a35346dd6dd4e369b6d300000000001e38a10000000000000000

afirid_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
afirid_face_young_2   = 0x000000003f10d00436db6db6db6db6db00000000001db6db0000000000000000
afirid_face_middle_2  = 0x00000004f600d00046dd6dd4e369b6d300000000001e38a10000000000000000
afirid_face_old_2     = 0x0000000d6b00b58646dd6dd4e369b6d300000000001e38a10000000000000000
afirid_face_older_2   = 0x0000000fff00a19446dd6dd4e369b6d300000000001e38a10000000000000000
#-------------------------------------------------------------------------------------------

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

pravar_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
pravar_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

guhulay_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
guhulay_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

#--nizh
# nizh_face_1 = 0x000000018000000236db6db6db6db6db00000000001db6db0000000000000000
# nizh_face_2 = 0x000000018000000236db6db6db6db6db00000000001db6db0000000000000000
#--

borovod_face1  = borovod_face_young_1
borovod_face2  = borovod_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1 ,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2 ,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3 ,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
	#-------------RANDOM MERCENARIES---------------------

  ["temp_troop_manual_loot","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],

["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(9),wp(75),knows_common,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet,no_scene,0,fac_commoners,
   [itm_lobarian_spear_b,itm_lobarian_spear_a,itm_tab_shield_round_b,itm_tab_shield_round_c,
   itm_aketon,itm_padded_jack,itm_long_gambeson,itm_hide_boots,itm_footman_helmet,itm_leather_boots],
   def_attrib|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1 ,mercenary_face_1, mercenary_face_2],
  # ["caravan_heavy_guard","Caravan Mounted Guard","Caravan heavy Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet,no_scene,0,fac_commoners,
   # [itm_sword_medieval_c_small,itm_tab_shield_heater_b,itm_tab_shield_round_c,itm_brigandine_grey_mail,itm_mail_boots,itm_footman_helmet,itm_sumpter1],
   # def_attrib|level(18),wp(110),knows_common|knows_riding_1|knows_ironflesh_3 ,mercenary_face_1, mercenary_face_2],
   #--test nizh troops
   # ["nizh_guard","Nizh Guard","Nizh Guards",tf_nizh|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_helmet,no_scene,0,fac_commoners,
   # [itm_nizh_outfit,itm_nizh_mask,itm_nizh_greaves,itm_iron_staff],
   # def_attrib|level(60),wp(400),knows_common|knows_ironflesh_9|knows_power_strike_10|knows_athletics_10 ,nizh_face_1, nizh_face_2],
   #--

  # ["knight_errant","Knight Errant","Knights Errant",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   # [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_dirim_cav_sword, itm_tab_shield_heater_c,itm_tab_shield_heater_c,
   # itm_early_transitional_blue,itm_early_transitional_orange,itm_early_transitional_white,itm_coat_of_plates_steel,
   # itm_splinted_leather_greaves,itm_mail_chausses,itm_splinted_greaves,itm_mail_boots,itm_iron_greaves,
   # itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_lamellar_gauntlets,
   # itm_visored_sallet_coif,itm_great_helm_1,itm_mail_coif,itm_great_bascinet_1,itm_madeln_bucket_1,itm_norman_helm_full_coif,itm_barbuta1,itm_bascinet_3,
   # itm_warhorse,itm_hunter,itm_destrier,itm_rouncy],
   # def_attrib|level(35),wp(180),knows_common|knows_riding_6|knows_ironflesh_4| knows_power_strike_2,mercenary_face_1, mercenary_face_2],
   #-----------------------------------------------------
	#-------------FACTIONS MERCENARIES---------------------
  ["mercenary_halberdier","Mercenary Halberdier","Mercenary Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_commoners,
   #[itm_imifir_halberd_1,itm_imifir_halberd_2,itm_imifir_halberd_3,itm_imifir_halberd_4,itm_imifir_halberd_5,itm_imifir_halberd_6,
   [itm_poleaxe_no3,itm_pravar_poleaxe,
   itm_tares_helmet_1,itm_tares_helmet_2,
    itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_blue,
   itm_shynbaulds, itm_mail_chausses,itm_mail_boots,itm_steel_greaves,itm_leather_boots_black,itm_iron_greaves,itm_mail_mittens,itm_splinted_leather_greaves,itm_leather_gloves,itm_gauntlets],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (20) | wp_polearm (120) ,knows_common|knows_ironflesh_5|knows_power_strike_1|knows_athletics_5,imifir_face_middle_1, imifir_face_older_2],

  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_tab_shield_pavise_d,itm_sniper_crossbow,itm_steel_bolts,
    itm_lobarian_helmet_4,itm_open_sallet,itm_tares_helmet_0,itm_chapel_de_fer_cloth1,itm_chapel_de_fer_cloth2,itm_chapel_de_fer_cloth3,
	itm_nord_breastplate_over_gambeson,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_blue,
	itm_leather_boots_black,itm_mail_mittens,itm_leather_gloves],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (110) | wp_two_handed (10) | wp_polearm (110) | wp_archery (0) | wp_crossbow (100) | wp_throwing (0),knows_common|knows_ironflesh_3| knows_power_strike_1|knows_athletics_4,imifir_face_middle_1, imifir_face_older_2],

   ["nord_mercenary","Nord Mercenary","Nord Mercenaries",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_shortened_spear,itm_one_handed_battle_axe_c,itm_tab_shield_round_d,
    itm_leather_gloves,itm_norman_helm_1,itm_norman_helm_coif,itm_norman_helm_full_coif,
    itm_nord_breastplate_over_gambeson,itm_nord_cuirass_over_gambeson,itm_short_coat_of_plates_c,
    itm_splinted_greaves,itm_leather_boots,itm_mail_mittens,itm_gauntlets],
   def_attrib|level(25),wp_one_handed (150) | wp_two_handed (50) | wp_polearm (140),knows_athletics_4|knows_ironflesh_4|knows_power_strike_2,hadvog_face_middle_1, hadvog_face_older_2],

 ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_tab_shield_heater_cav_a,
    itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,
	itm_iron_greaves,itm_leather_gloves,itm_mail_mittens,itm_mail_chausses,itm_shynbaulds,
     itm_lobarian_helmet_4,itm_visored_sallet_coif,itm_open_sallet,itm_tares_helmet_0,itm_tares_helmet_1,itm_tares_helmet_2,itm_lobarian_bascinet_visor,itm_lobarian_bascinet_visor_open,
	 itm_rouncy,itm_saddle_horse],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (50) | wp_polearm (150) ,knows_common|knows_riding_3| knows_ironflesh_5,pravar_face_middle_1, pravar_face_old_1],

   ["sellsword","Lobarian Mercenary","Lobarian Mercenaries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_afirid_medium_spear,itm_italian_warhammer,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_lobarian_falchion,itm_sword_medieval_c,itm_tab_shield_heater_c,
   itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_short_coat_of_plates_c,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_blue,
   itm_lobarian_helmet_4,itm_open_sallet,itm_tares_helmet_0,itm_tares_helmet_1,itm_tares_helmet_2,itm_leather_boots,
   itm_gauntlets,itm_mail_boots],
   def_attrib|level(25),wp_one_handed (140) | wp_two_handed (10) | wp_polearm (140),knows_common|knows_riding_1|knows_ironflesh_2|knows_power_strike_1,pravar_face_young_1, pravar_face_old_2],

  ["mercenary_archer","Mercenary archer","Mercenary Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_barbed_arrows,itm_bodkin_arrows,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_long_bow,itm_strong_bow,
    itm_nord_breastplate_over_gambeson,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_blue,
	itm_leather_boots,itm_open_sallet,itm_tares_helmet_0,itm_chapel_de_fer_cloth1,itm_chapel_de_fer_cloth2,itm_chapel_de_fer_cloth3],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (80) | wp_two_handed (10) | wp_polearm (80) | wp_archery (100) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_4|knows_athletics_3,borovod_face_young_1, borovod_face_older_2],

 ["south_cavalry","South Cavalry","South Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_light_lance,itm_tab_shield_small_round_b,itm_javelin,itm_light_crossbow,itm_bolts,
    itm_southern_light_armor,itm_south_long_armor_a,itm_south_long_armor_b,itm_south_long_armor_c,itm_arabian_mail_shirt_b,itm_afirid_boots_d,itm_afirid_boots_c,itm_leather_gloves,
     itm_saracen_helmet_f,itm_turban_helmet,itm_arabian_horse_a],
   def_attrib|level(25),wp_one_handed (150) | wp_two_handed (10) | wp_polearm (130) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_5| knows_ironflesh_5|knows_horse_archery_3,afirid_face_middle_1, afirid_face_old_1],

   ["south_spearman","South Spearman","South Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_tab_shield_kite_c,itm_lobarian_spear_a,itm_lobarian_spear_b,itm_lobarian_spear_c,itm_afirid_medium_spear,itm_afirid_light_lamellar_1,itm_south_armor_a,itm_south_long_armor_a,itm_leather_boots_black,itm_afirid_conical_helmet_1],
   def_attrib|level(25),wp_one_handed (100) | wp_polearm (160) | wp_crossbow (0) | wp_throwing (0),knows_common|knows_ironflesh_2|knows_power_strike_4|knows_athletics_6,afirid_face_young_1, afirid_face_old_2],

["mounted_archer","Mounted Archer","Mounted Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_tab_shield_small_round_b,itm_nomad_bow,itm_arrows,
    itm_steppe_armor_a,itm_guhulay_cav_boots,itm_leather_gloves,
     itm_nomad_cap,itm_nomad_cap_b,itm_steppe_horse_1,itm_steppe_horse, itm_guhulay_cav_boots],
   def_attrib|level(25),wp_one_handed (150) | wp_two_handed (0) | wp_polearm (130) | wp_archery (100),knows_common|knows_riding_5| knows_ironflesh_5|knows_power_draw_3|knows_horse_archery_5,guhulay_face_middle_2, guhulay_face_old_2],

   ["double_sold","Double Solde","Double Solde",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_lobarian_polehammer_1,itm_italian_warhammer,itm_great_bardiche,itm_sword_two_handed_a,itm_tab_shield_heater_c,itm_claymore,
   itm_nord_cuirass_over_mail,itm_nord_heavy_cuirass_over_mail,itm_short_coat_of_plates_a,itm_common_cuirass_orange,itm_darenbay_armor,itm_darenbay_armor_1,
   itm_visored_sallet_coif,itm_lobarian_bascinet_visor,itm_lobarian_bascinet_visor_open,
   itm_gauntlets,itm_shynbaulds],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200),knows_common|knows_riding_1|knows_ironflesh_2|knows_power_strike_2,pravar_face_young_1, pravar_face_old_2],

	##-----------------------FACTIONS MERCENARIES END--------------------------

    ["matchlock_man","Matchlock Man","Matchlock men",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_atian_short_sword,itm_matchlock_2,itm_cartridges,
    itm_atian_padded_vest,itm_bear_paw_shoes,itm_combed_morion,itm_leather_gloves],
   def_attrib|level(25),wp(90)| wp_firearm (100),knows_common|knows_ironflesh_2,imifir_face_middle_1, imifir_face_older_2],

  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,   [],   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

##HEAVY MERCENARIES
  ["heavy_mercenary_halberdier","Mercenary Heavy Halberdier","Mercenary Heavy Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_commoners,
   #[itm_imifir_halberd_1,itm_imifir_halberd_2,itm_imifir_halberd_3,itm_imifir_halberd_4,itm_imifir_halberd_5,itm_imifir_halberd_6,
   [itm_luc_partisan,itm_italian_scorpion_guisarme,itm_halberd_no1,itm_poleaxe_no3,itm_pravar_poleaxe,
   itm_tares_helmet_1,itm_tares_helmet_2,
   itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,
   itm_shynbaulds, itm_mail_chausses,itm_mail_boots,itm_steel_greaves,itm_leather_boots_black,itm_iron_greaves,itm_mail_mittens,itm_splinted_leather_greaves,itm_leather_gloves,itm_gauntlets],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (40) | wp_polearm (150) ,knows_common|knows_ironflesh_5|knows_power_strike_1|knows_athletics_5,imifir_face_middle_1, imifir_face_older_2],

  ["heavy_mercenary_crossbowman","Mercenary Heavy Crossbowman","Mercenary heavy Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_tab_shield_pavise_d,itm_sniper_crossbow,itm_steel_bolts,
    itm_lobarian_helmet_4,itm_open_sallet,itm_tares_helmet_0,itm_tares_helmet_1,itm_tares_helmet_2,
	itm_nord_breastplate_over_gambeson,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,
	itm_leather_boots_black,itm_mail_mittens,itm_leather_gloves],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (120) | wp_two_handed (10) | wp_polearm (110) | wp_archery (0) | wp_crossbow (130) | wp_throwing (0),knows_common|knows_ironflesh_3| knows_power_strike_1|knows_athletics_4,imifir_face_middle_1, imifir_face_older_2],

   ["heavy_nord_mercenary","Nord Heavy Mercenary","Nord Heavy Mercenaries",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_one_handed_battle_axe_c,itm_tab_shield_round_d,
    itm_leather_gloves,itm_norman_helm_1,itm_norman_helm_coif,itm_norman_helm_full_coif,
    itm_nord_breastplate_over_gambeson,itm_nord_cuirass_over_gambeson,itm_nord_breastplate_over_mail,itm_nord_cuirass_over_mail,itm_nord_heavy_cuirass_over_mail,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,
    itm_splinted_greaves,itm_leather_boots,itm_mail_mittens,itm_gauntlets],
   def_attrib|level(25),wp_one_handed (150) | wp_two_handed (50) | wp_polearm (140),knows_athletics_4|knows_ironflesh_4|knows_power_strike_2,hadvog_face_middle_1, hadvog_face_older_2],

 ["heavy_mercenary_cavalry","Mercenary Heavy Cavalry","Mercenary Heavy Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_tab_shield_heater_cav_a,
    itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,itm_nord_breastplate_over_gambeson,itm_nord_cuirass_over_gambeson,itm_nord_breastplate_over_mail,itm_nord_cuirass_over_mail,itm_nord_heavy_cuirass_over_mail,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,
	itm_iron_greaves,itm_leather_gloves,itm_mail_mittens,itm_mail_chausses,itm_shynbaulds,
     itm_lobarian_helmet_4,itm_visored_sallet_coif,itm_open_sallet,itm_tares_helmet_0,itm_tares_helmet_1,itm_tares_helmet_2,itm_lobarian_bascinet_visor,itm_lobarian_bascinet_visor_open,
	 itm_hunter,itm_destrier,itm_rouncy,itm_saddle_horse],
   def_attrib|level(28),wp_one_handed (160) | wp_two_handed (70) | wp_polearm (170) ,knows_common|knows_riding_4| knows_ironflesh_5,pravar_face_middle_1, pravar_face_old_1],

   ["heavy_sellsword","Lobarian Heavy Mercenary","Lobarian Heavy Mercenaries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_lobarian_polehammer_1,itm_italian_warhammer,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_lobarian_falchion,itm_sword_medieval_c,itm_tab_shield_heater_c,
   itm_common_cuirass,itm_common_cuirass_orange,itm_common_cuirass_green,itm_common_cuirass_red,itm_common_cuirass_blue,itm_common_cuirass_brown,itm_breastplate_over_gambeson,itm_common_breastplate,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_short_coat_of_plates_a,itm_short_coat_of_plates_b,itm_short_coat_of_plates_c,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,
   itm_lobarian_helmet_4,itm_open_sallet,itm_tares_helmet_0,itm_tares_helmet_1,itm_tares_helmet_2,itm_shynbaulds,
   itm_gauntlets,itm_mail_boots],
   def_attrib|level(25),wp_one_handed (160) | wp_two_handed (30) | wp_polearm (160),knows_common|knows_riding_1|knows_ironflesh_2|knows_power_strike_1,pravar_face_young_1, pravar_face_old_2],

  ["heavy_mercenary_archer","Mercenary Heavy Archer","Mercenary Heavy Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_barbed_arrows,itm_bodkin_arrows,itm_common_sword_a,itm_common_sword_b,itm_common_sword_c,itm_common_sword_d,itm_common_sword_e,itm_war_bow,itm_long_bow,itm_strong_bow,
    itm_nord_breastplate_over_gambeson,itm_common_breastplate_orange,itm_common_breastplate_blue,itm_common_breastplate_red,itm_brigandine_grey_mail,itm_brigandine_grey,itm_merc_padded_armor,itm_brigandine_leg,itm_brigandine_blue,itm_brigandine_blue_mail,
	itm_leather_boots,
	itm_chapel_de_fer_mail1,itm_chapel_de_fer_mail2,itm_chapel_de_fer_mail3,itm_open_sallet,itm_tares_helmet_0,itm_chapel_de_fer_cloth1,itm_chapel_de_fer_cloth2,itm_chapel_de_fer_cloth3],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (80) | wp_two_handed (10) | wp_polearm (80) | wp_archery (100) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_4|knows_athletics_3,borovod_face_young_1, borovod_face_older_2],

   ["heavy_south_spearman","South Heavy Spearman","South Heavy Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_tab_shield_kite_c,itm_afirid_spears_b,itm_afirid_spears_a,itm_afirid_long_spear,itm_afirid_medium_spear,itm_afirid_light_lamellar_1,itm_south_armor_a,itm_south_long_armor_c,itm_south_armor_b,itm_leather_boots_black,itm_afirid_conical_helmet_1],
   def_attrib|level(25),wp_one_handed (120) | wp_polearm (180) | wp_crossbow (0) | wp_throwing (0),knows_common|knows_ironflesh_3|knows_power_strike_4|knows_athletics_6,afirid_face_young_1, afirid_face_old_2],

 ["heavy_south_cavalry","South Heavy Cavalry","South Heavy Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_tab_shield_small_round_b,itm_javelin,itm_light_crossbow,itm_bolts,
    itm_south_long_armor_d,itm_south_long_armor_a,itm_south_long_armor_b,itm_south_long_armor_c,itm_arabian_mail_shirt_b,itm_afirid_boots_d,itm_afirid_boots_c,itm_leather_gloves,
     itm_saracen_helmet_f,itm_turban_helmet,itm_arabian_horse_a,itm_arabian_horse_b, itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(25),wp_one_handed (170) | wp_two_handed (10) | wp_polearm (150) | wp_crossbow (85) | wp_throwing (130),knows_common|knows_riding_5| knows_ironflesh_5|knows_horse_archery_4,afirid_face_middle_1, afirid_face_old_1],

["heavy_mounted_archer","Heavy Mounted Archer","Heavy Mounted Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_heavy_lance,itm_tab_shield_small_round_c,itm_nomad_bow,itm_arrows,
    itm_steppe_armor_a,itm_steppe_armor_b,itm_south_armor_c,itm_south_armor_d,itm_guhulay_mail_c,
     itm_nomad_cap,itm_nomad_cap_b,itm_steppe_horse_1,itm_steppe_horse, itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(25),wp_one_handed (170) | wp_two_handed (0) | wp_polearm (150) | wp_archery (130),knows_common|knows_riding_6| knows_ironflesh_5|knows_power_draw_3|knows_horse_archery_6,guhulay_face_middle_2, guhulay_face_old_2],

   ##HEAVY MERCENARIES END

   ##-----------------------jalik's mercenaries--------------------------
   ["jalik_mercenary","Jalik's mercenary","Jalik's Mercenaries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_jalik_mercenaries,
   [itm_atian_longsword,itm_bw_kite_shield,itm_corrazina_grey,itm_splinted_greaves_spurs, itm_mail_mittens,itm_open_sallet],
   def_attrib|level(25),wp(130),knows_common|knows_athletics_4|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ##---------------------------------------------------------------------
#--(toh 0.51) bodysliding
["bodysliding_temp", "BODYSLIDING TEMP", "BODYSLIDING TEMP", 0,0,0, tf_hero|fac_kingdom_6,[],str_30|agi_14|int_8|cha_16|level(1),wp(1),knows_inventory_management_10, 0x000000000000710004820c24204c000200000000001d16100000000000000000, 0x000000003f00714049fefe393fffc7ff00000000001ef96f0000000000000000],
#--


#########################################################################################
#########################################################################################
#########################################################################################

  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_spiked_club,itm_dagger,
   itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
 ["paysan","Paysan","Paysan",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_butchering_knife,itm_hand_axe,
    itm_tunic_with_green_cape,itm_pelt_coat,itm_leather_apron,itm_coarse_tunic,itm_wrapping_boots],
   def_attrib|level(6),wp(65),knows_common,pravar_face_younger_1, pravar_face_middle_2],
  ["militia","Militia","Militia",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_shortened_spear,itm_tab_shield_round_b,itm_tab_shield_kite_b,itm_tab_shield_heater_b,
    itm_leather_cap,itm_padded_jack,itm_gambeson,itm_green_tourney_armor,itm_gold_tourney_armor,itm_mail_coif,itm_nomad_boots],
   def_attrib|level(8),wp(75),knows_common,pravar_face_young_1, pravar_face_old_2],
   ["footman","footman","Footmen",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_c,itm_lobarian_spear_c,itm_tab_shield_round_c,itm_tab_shield_kite_c,itm_tab_shield_heater_c,
    itm_toh_padded,itm_leather_boots,itm_toh_open_sallet],
   def_attrib|level(10),wp_melee(95),knows_common|knows_ironflesh_2|knows_athletics_2,pravar_face_young_1, pravar_face_old_2],

	["bowman","Bowman","Bowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_arrows,itm_short_bow,itm_sword_medieval_a,
    itm_lobarian_bowman_aketon,itm_ankle_boots,itm_simple_chapel],
   def_attrib|level(6),wp_one_handed (60) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (70) | wp_throwing (90),knows_common|knows_power_draw_1|knows_ironflesh_1|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],
   	# ["archer","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   # [itm_arrows,itm_short_bow,itm_sword_medieval_a,
    # itm_padded_jack,itm_narf_hose,itm_skullcap],
   # def_attrib|level(10),wp_one_handed (80) | wp_two_handed (90) | wp_polearm (90) | wp_archery (110) | wp_crossbow (70) | wp_throwing (90),knows_common|knows_power_draw_2|knows_ironflesh_1|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],

   ["cavalryman","Cavalryman","Cavalrymen",tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_c,itm_tab_shield_round_d,itm_tab_shield_kite_d,itm_tab_shield_heater_d,itm_light_lance,
    itm_toh_cav_breastplate_a,itm_splinted_leather_greaves,itm_toh_sallet_mail,itm_leather_gloves,itm_sumpter1,itm_sumpter2],
   def_attrib|level(20),wp_melee(150),knows_common|knows_riding_1|knows_ironflesh_2|knows_power_strike_2| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   ["trained_cavalryman","Trained Cavalryman","Trained Cavalrymen",tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_c_long,itm_tab_shield_round_d,itm_tab_shield_kite_d,itm_tab_shield_heater_d,itm_lance,
    itm_toh_cav_breastplate_b,itm_splinted_leather_greaves,itm_toh_sallet_mail,itm_mail_mittens,itm_sumpter1,itm_sumpter2],
   def_attrib|level(24),wp_melee(160),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   ["veteran_cavalryman","Veteran Cavalryman","Veteran Cavalrymen",tf_guarantee_horse|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_d_long,itm_tab_shield_round_d,itm_tab_shield_kite_d,itm_tab_shield_heater_d,itm_heavy_lance,
    itm_toh_cav_breastplate_c,itm_iron_greaves,itm_toh_sallet_mail_mask,itm_gauntlets,itm_hunter],
   def_attrib|level(30),wp_melee(180),knows_common|knows_riding_4|knows_ironflesh_3|knows_power_strike_2| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],

   # ["heavy_infantry","Heavy Infantry","Heavy Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   # [itm_sword_medieval_c,itm_mace_3,itm_tab_shield_kite_d,itm_tab_shield_heater_d,itm_awlpike_long,itm_winged_mace_1,
	# itm_toh_mail_plates,itm_splinted_greaves_spurs,itm_toh_sallet_mail,itm_mail_mittens],
   # def_attrib|level(20),wp_melee(150),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
	 ["heavy_archer","Heavy Archer","Heavy Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_bodkin_arrows,itm_war_bow,itm_sword_medieval_c,
    itm_lobarian_archer_brigandine,itm_splinted_greaves,itm_chapel_de_fer_mail1],
   def_attrib|level(18),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (130) | wp_crossbow (70) | wp_throwing (90),knows_common|knows_power_draw_4|knows_ironflesh_1|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],
   # ["armoured_sergeant","Armoured Sergeant","Armoured Sergeants",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   # [itm_sword_medieval_d_long,itm_winged_mace_2,itm_tab_shield_kite_d,
    # itm_brigandine_c_heraldic,itm_splinted_greaves_spurs,itm_pigface_klappvisor_open,itm_wisby_gauntlets_black],
   # def_attrib|level(24),wp_melee(160),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],

  #>>>>>see  module_constant(Tohlobaria  armoured troops)<<<<<
   ["light_infantry","Infantry","Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_c,itm_war_hammer_no3,itm_war_hammer_no3,itm_tab_shield_round_d,itm_tab_shield_kite_d,itm_tab_shield_heater_d,
    itm_light_mail_over_padded,itm_leather_boots,itm_toh_sallet_cloth,itm_leather_gloves],
   def_attrib|level(20),wp_melee(150),knows_common|knows_riding_1|knows_ironflesh_2|knows_power_strike_2| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
	["archer","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_arrows,itm_long_bow,itm_sword_medieval_a,
    itm_lobarian_archer_aketon,itm_leather_boots,itm_chapel_de_fer_cloth1],
	def_attrib|level(18),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (130) | wp_crossbow (70) | wp_throwing (90),knows_common|knows_power_draw_4|knows_ironflesh_1|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],
   ["elite_foot_soldier","Elite Foot Soldier","Elite Foot Soldier",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_great_sword,itm_winged_mace_2,itm_war_hammer_no2,itm_war_hammer_no2,itm_tab_shield_kite_d,
    itm_toh_breastplate,itm_splinted_leather_greaves,itm_pigface_klappvisor,itm_wisby_gauntlets_black],
   def_attrib|level(30),wp_melee(190),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2| knows_athletics_4,pravar_face_middle_1, pravar_face_old_2],



  # ["elite_cavalry","Elite Cavalry","Elite Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
   # [itm_heavy_lance,itm_bastard_sword_b,itm_sword_medieval_b,itm_tab_shield_heater_cav_a,
    # itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_great_helmet,itm_munitions_helm_1,itm_helmet_with_neckguard,itm_leather_charger],
   # def_attrib|level(30),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) ,knows_common|knows_riding_4| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
  ["bachelor","Bachelor","Bachelors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_heavy_lance,
    itm_bachelor_platemail,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets],
   def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knows_common|knows_riding_4| knows_ironflesh_5|knows_power_strike_4,pravar_face_middle_1, pravar_face_older_2],


   ##-----------------------prisoners--------------------------
   ["common_prisoner","Common Prisoner","Common Prisoners",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(6),wp(50),knows_common,mercenary_face_1, mercenary_face_2],

   ["war_prisoner","War Prisoner","War Prisoners",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(10),wp(70),knows_common,mercenary_face_1, mercenary_face_2],

   ["imprisoned_archer","Imprisoned Archer","Imprisoned Archers",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(20),wp(60),knows_common|knows_athletics_2,mercenary_face_1, mercenary_face_2],

   ["imprisoned_crossbowman","Imprisoned Crossbowman","Imprisoned Crossbowmen",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(20),wp(60),knows_common|knows_athletics_2,mercenary_face_1, mercenary_face_2],

   ["imprisoned_horseman","Imprisoned Horseman","Imprisoned Horsemen",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(20),wp(100),knows_common|knows_athletics_2,mercenary_face_1, mercenary_face_2],

   ["imprisoned_veteran","Imprisoned Veteran","Imprisoned Veterans",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_shirt,itm_knife],
   def_attrib|level(24),wp(100),knows_common|knows_athletics_2,mercenary_face_1|knows_power_strike_1, mercenary_face_2],

   ["imprisoned_nobleman","Imprisoned Nobleman","Imprisoned Noblemen",tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_knife],
   def_attrib|level(26),wp_one_handed (130) | wp_two_handed (120) | wp_polearm (120),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,pravar_face_young_1],
  ##---------------------------------------------------------------------

  #========speciality troops upgrade========
    # ["light_cavalry","Light Cavalry","Light Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	# [itm_lance,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_a,itm_double_sided_lance,
	# itm_mail_mittens,itm_horseman_brigandine,itm_mail_boots,itm_lobarian_helmet_mail_coif,itm_hunter,itm_sumpter1,itm_sumpter2],
	# def_attrib|level(20),wp_one_handed (130) | wp_polearm (130) ,knows_common|knows_riding_4| knows_ironflesh_4,afirid_face_middle_1, afirid_face_older_2],
	["veteran_pikeman","Veteran Pikeman","Veteran Pickmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	[itm_pike_long,
	itm_pikeman_brigandine,itm_iberian_helmet,itm_leather_boots,itm_mail_mittens],
	def_attrib|level(20), wp_polearm (180) ,knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_6,imifir_face_young_1, imifir_face_older_2],
	["veteran_crossbowman","Veteran Crossbowman","Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
	[itm_sword_medieval_c,itm_sniper_crossbow,itm_steel_bolts,
	itm_crossbowman_brigandine,itm_leather_boots,itm_crossbowman_kettle_hat_c],
	def_attrib|level(20),wp_crossbow (100) ,knows_common|knows_ironflesh_4|knows_athletics_4,imifir_face_middle_1, imifir_face_older_2],
  #=========================================

#>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  #----------------noble--------------------------
  ["knight","Knight","Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    itm_knight_armor,itm_toh_shynbaulds,itm_armet1_open,itm_plated_bw_knight_horse,itm_wisby_gauntlets_black],
   def_attrib|level(30),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) ,knows_common|knows_riding_4| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
  ["banneret","Banneret","Banneret",tf_unmoveable_in_party_window|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,
    itm_baron_plate1,itm_toh_shynbaulds,itm_armet2,itm_long_barded_horse_black,itm_mail_mittens],
   def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knows_common|knows_riding_4| knows_ironflesh_5|knows_power_strike_4,pravar_face_middle_1, pravar_face_older_2],

  #-----------------------------------------------
  ["messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,pravar_face_young_1, pravar_face_old_2],
  ["deserter","Deserter","Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,pravar_face_young_1, pravar_face_old_2],
  ["prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  ["castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
   #-----------town guard---------------
   ["guard","Guard","Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_haubergeon,itm_mail_chausses,itm_flat_topped_helmet,itm_mail_mittens],
   def_attrib|level(20),wp_melee(100),knows_common|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   #--------------------------------
 #-----------castle troops---------------
	["novice_pikeman","Novice Pikeman","Novice Pickmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	[itm_ashwood_pike,
	itm_simple_iberian_helmet,itm_pikeman_gambeson,itm_ankle_boots],
	def_attrib|level(10), wp_polearm (120) ,knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3,imifir_face_young_1, imifir_face_older_2],
	["trained_pikeman","Trained Pikeman","Trained Pickmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	[itm_pike,
	itm_pikeman_mail,itm_pikeman_helmet,itm_leather_boots,itm_leather_gloves],
	def_attrib|level(16), wp_polearm (150) ,knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_5,imifir_face_young_1, imifir_face_older_2],


	["novice_crossbowman","Novice Crossbowman","Novice Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
	[itm_sword_medieval_b_small,itm_crossbow,itm_bolts,itm_bolts,
	itm_crossbowman_gambeson,itm_ankle_boots,itm_crossbowman_kettle_hat_a],
	def_attrib|level(10),wp_crossbow (60) ,knows_common|knows_ironflesh_2|knows_athletics_2,imifir_face_middle_1, imifir_face_older_2],
	["trained_crossbowman","Trained Crossbowman","Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
	[itm_sword_medieval_b_small,itm_heavy_crossbow,itm_bolts,itm_steel_bolts,
	itm_crossbowman_mail,itm_leather_boots,itm_crossbowman_kettle_hat_b],
	def_attrib|level(16),wp_crossbow (80) ,knows_common|knows_ironflesh_3|knows_athletics_3,imifir_face_middle_1, imifir_face_older_2],

	# ["novice_cavalryman","Novice Cavalryman","Novice Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	# [itm_light_lance,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_a,
	# itm_horseman_gambeson,itm_lobarian_simple_helmet,itm_leather_boots,itm_sumpter_horse],
	# def_attrib|level(10),wp_one_handed (60)|wp_polearm (60) ,knows_common|knows_riding_1|knows_ironflesh_3,afirid_face_middle_1, afirid_face_older_2],
	# ["trained_cavalryman","Trained Cavalryman","Trained Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	# [itm_lance,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_a,
	# itm_leather_gloves,itm_horseman_mail,itm_splinted_greaves,itm_lobarian_helmet_coif,itm_sumpter_horse],
	# def_attrib|level(16),wp_one_handed (100) | wp_polearm (100) ,knows_common|knows_riding_3| knows_ironflesh_3,afirid_face_middle_1, afirid_face_older_2],
	#=============
	# ["heavy_cavalry","Heavy Cavalry","Heavy Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_player_supporters_faction,
	# [itm_heavy_lance,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_a,
	# itm_mail_mittens,itm_cavalry_brigandine,itm_mail_boots,itm_lobarian_faceplate,itm_leather_warhorse],
	# def_attrib|level(20),wp_one_handed (130) | wp_polearm (130) ,knows_common|knows_riding_4| knows_ironflesh_4,afirid_face_middle_1, afirid_face_older_2],
	#==============
	["halberdier","Halberdier","Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_heavy_halberd,
    itm_halberdier_helmet,itm_halberdier_brigandine,itm_mail_chausses,itm_gauntlets],
  	def_attrib|level(20), wp_polearm (150) ,knows_common|knows_ironflesh_6|knows_power_strike_2|knows_athletics_6,imifir_face_young_1, imifir_face_older_2],
	["sapper","Sapper","sapper",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
	[itm_sapper_warhammer,itm_sniper_crossbow,itm_steel_bolts,itm_lobarian_pavise,
	itm_sapper_plate,itm_splinted_greaves_spurs,itm_sallet_rondel,itm_leather_gloves],
	def_attrib|level(20),wp_one_handed (160) |wp_crossbow (140) ,knows_common|knows_ironflesh_4|knows_athletics_4,imifir_face_middle_1, imifir_face_older_2],
  #--------------------------
["sergeant","Sergeant","Sergeants",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_c,itm_winged_mace_2,itm_war_hammer_no2,itm_war_hammer_no2,itm_tab_shield_kite_d,itm_tab_shield_heater_d,itm_awlpike_long,
    itm_toh_mail_plates,itm_rus_splint_greaves,itm_toh_sallet_mail,itm_mail_mittens],
   def_attrib|level(24),wp_melee(160),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   #########################################################################################
    #########################################################################################

#peasant - retainer - footman - man-at-arms -  knight
  ["pravar_recruit","Pravar Recruit","Pravar Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_padded_cloth,itm_arming_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,pravar_face_younger_1, pravar_face_middle_2],
  ["pravar_militia","Pravar Militia","Pravar Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [#itm_spiked_club,itm_fighting_pick,itm_lobarian_spear_a,itm_tab_shield_heater_a,
   itm_lobarian_spear_a,itm_tab_shield_heater_a,
    itm_pravar_gambeson,itm_pravar_simple_helmet,itm_ankle_boots,itm_wrapping_boots],
   def_attrib|level(9),wp(75),knows_common,pravar_face_young_1, pravar_face_old_2],
  ["pravar_footman","Pravar Footman","Pravar Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [#itm_lobarian_spear_a,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_spiked_war_club_no1,
   itm_lobarian_spear_a,itm_tab_shield_heater_b,
    itm_light_brigandine_red,itm_leather_boots,itm_pravar_helmet_coif],
   def_attrib|level(14),wp_melee(85),knows_common|knows_ironflesh_2|knows_athletics_2,pravar_face_young_1, pravar_face_old_2],
  ["pravar_infantry","Pravar Infantry","Pravar Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_tab_shield_heater_c,itm_mace_4,itm_italian_warhammer,itm_awlpike,
    itm_pravar_light_brigandine,itm_mail_chausses,itm_pravar_helmet_mail_coif],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
    ["pravar_crossbowman","Pravar Crossbowman","Pravar Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,
    itm_medium_brigandine_red,itm_leather_boots,itm_ankle_boots,itm_pravar_kettlehat],
   def_attrib|level(20),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (60) | wp_throwing (90),knows_common|knows_ironflesh_1|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],
  # ["pravar_sharpshooter","Pravar Sharpshooter","Pravar Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   # [itm_bolts,itm_arrows,itm_crossbow,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_c,
    # itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_helmet_with_neckguard,itm_leather_gloves],
   # str_14 | agi_10 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_athletics_2,pravar_face_middle_1, pravar_face_older_2],
  ["pravar_man_at_arms","Pravar Man at Arms","Pravar Men at Arms",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_pravar_poleaxe,
   itm_red_cuirass,itm_shynbaulds,itm_pravar_faceplate,itm_pravar_faceplate_b,itm_mail_mittens,itm_gauntlets],
   def_attrib|level(25),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140),knows_common|knows_riding_1|knows_ironflesh_2| knows_power_strike_1,pravar_face_young_1, pravar_face_old_2],
  ["pravar_mounted_sergeant","Pravar Mounted Sergeant","Pravar Mounted Sergeants",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_sword_medieval_b,itm_luc_hache_d_armes_b,itm_one_handed_war_axe_spiked,itm_tab_lobarian_knight_shield,
   itm_brigandine_red_mail,itm_splinted_greaves_spurs,itm_pravar_faceplate,itm_pravar_faceplate_b,itm_sumpter1,itm_sumpter2,itm_mail_mittens],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (130) | wp_polearm (130),knows_common|knows_riding_1|knows_ironflesh_2| knows_power_strike_1,pravar_face_young_1, pravar_face_old_2],
  #----------------noble--------------------------
  ["pravar_squire","Pravar Squire","Pravar Squires",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_great_lance,itm_sword_medieval_b,itm_tab_shield_heater_cav_a,itm_bastard_mace,
    itm_pravar_noble_armor,itm_mail_chausses,itm_oniontop_bascinet_red,itm_hounskull_red,itm_pravar_warhorse],
   def_attrib|level(21),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,pravar_face_young_1,pravar_face_middle_2],
  ["pravar_knight","Pravar Knight","Pravar Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_knights_winged_mace_1h,
   itm_colored_lance_e,itm_luc_knights_warhammer,itm_sword_of_war,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    itm_pravar_knight_armor,itm_plate_boots,itm_pigface_klappvisor_red,itm_pigface_klappvisor_open_red,itm_pravar_barded_horse,itm_pravar_plated_warhorse,itm_pravar_plated_knight_warhorse,itm_gauntlets,itm_mail_mittens],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knows_common|knows_riding_5| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
  #-----------------------------------------------
  ["pravar_messenger","Pravar Messenger","Pravar Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,pravar_face_young_1, pravar_face_old_2],
  ["pravar_deserter","Pravar Deserter","Pravar Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,pravar_face_young_1, pravar_face_old_2],
  ["pravar_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates_red,itm_plate_boots,itm_pravar_simple_helmet,itm_pravar_helmet_coif,itm_pravar_helmet_mail_coif,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  ["pravar_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pravar_poleaxe,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_pravar_cuirasse,itm_plate_boots,itm_oniontop_bascinet_red,itm_pigface_klappvisor_open_red,itm_pravar_helmet_mail_coif,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
   #-----------town guard---------------
   ["pravar_guard","Pravar Guard","Pravar Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_pravar_haubergeon,itm_mail_chausses,itm_pravar_helmet_mail_coif,itm_mail_mittens],
   def_attrib|level(20),wp_melee(100),knows_common|knows_ironflesh_2|knows_power_strike_1| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   #-----------town guard---------------
   #--pravar household
 ["red_knight","Red Knight","Red Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_colored_lance_g,itm_morningstar,itm_sword_medieval_d_long,
    itm_red_armour,itm_plate_boots,itm_hounskull_plume,itm_pravar_knight_warhorse,itm_wisby_gauntlets_black],
   def_attrib|level(36),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) ,knows_common|knows_riding_6| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
   #--

# Borovod watchman?
  ["borovod_recruit","Borovod Recruit","Borovod Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_stones,itm_tab_shield_kite_a, itm_tab_shield_kite_a,
    itm_linen_tunic, itm_rawhide_coat,itm_nomad_boots],
   def_attrib|level(4),wp(60),knows_common, borovod_face_younger_1, borovod_face_middle_2],
  ["borovod_footman","Borovod Footman","Borovod Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [#itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,
   itm_tab_shield_kite_b,itm_spear,
   itm_borovod_fur_cap,itm_rich_padded,itm_nomad_boots],
   #itm_borovod_lamellar_helmet,itm_borovod_spiked_helmet,itm_borovod_fur_helmet,
   def_attrib|level(9),wp(75),knows_common, borovod_face_young_1, borovod_face_middle_2],
  ["borovod_archer","Borovod Archer","Borovod Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_2,itm_short_bow,itm_short_bow,
   itm_borovod_fur_cap,itm_rus_padded_cloth,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(40),knows_ironflesh_1|knows_power_draw_1,borovod_face_young_1, borovod_face_old_2],
  ["borovod_trained_archer","Borovod Trained Archer","Borovod Trained Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_3,itm_nomad_bow,itm_nomad_bow,itm_short_bow,
    itm_padded_cloth_mails,itm_nomad_boots,itm_borovod_fur_helmet,itm_nomad_cap],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (50) | wp_two_handed (40) | wp_polearm (30) | wp_archery (120) | wp_crossbow (70) | wp_throwing (70),knows_ironflesh_1|knows_power_draw_4|knows_power_strike_2|knows_athletics_2,borovod_face_young_1, borovod_face_older_2],
  ["borovod_marksman","Borovod Marksman","Borovod Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_mace_4,itm_war_bow,itm_luc_kriegshammer,
    itm_archer_heavy_armor,itm_leather_boots,itm_spiked_helmet],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_one_handed (60) | wp_two_handed (50) | wp_polearm (40) | wp_archery (160) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_5|knows_power_strike_3|knows_athletics_3,borovod_face_young_1, borovod_face_older_2],
  ["borovod_axeman","Borovod Axeman","Borovod Axemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_borov_axe,itm_bastard_axe,itm_tab_shield_kite_cav_a,
    itm_rus_helm,itm_borovod_spiked_helmet,itm_rus_mails,itm_nomad_boots],
   def_attrib|level(14),wp_melee(90),knows_athletics_2|knows_ironflesh_1,borovod_face_young_1, borovod_face_old_2],
  ["borovod_veteran","Borovod Veterans","Borovod Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bardiche,
    itm_heavy_leather_kuyak,itm_leather_boots,itm_tagancha_helm_a],
   def_attrib|level(19),wp_one_handed (100) | wp_two_handed (20) | wp_polearm (80),knows_athletics_1|knows_ironflesh_2|knows_power_strike_1,borovod_face_young_1, borovod_face_older_2],
  ["borovod_bardiche_master","Borovod Bardiche Master","Borovod Bardiche Masters",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_great_bardiche,
    itm_bardiche_master_armor,itm_mail_chausses,itm_tagancha_helm_b,itm_wisby_gauntlets_black],
   def_attrib|level(24),wp_one_handed (100) | wp_two_handed (80) | wp_polearm (100),knows_riding_2|knows_athletics_1|knows_ironflesh_3|knows_power_strike_1,borovod_face_middle_1, borovod_face_older_2],
  #---------------------borovod noble--------------------------
  ["borovod_horseman","Borovod Horseman","Borovod Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_luc_knightly_axe_v2,itm_barbed_arrows,itm_war_bow,itm_lance,itm_sword_medieval_c_long,
    itm_borovod_lamellar_armor,itm_rus_lamellar_a,itm_leather_boots,itm_rus_horse,itm_borovod_light_charger,itm_borovod_noble_helmet],
   def_attrib|level(21),wp(150),knows_riding_3|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_4,borovod_face_young_1, borovod_face_older_2],
  ["borovod_knight","Borovod Knight","Borovod Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_luc_hammer_spike,itm_barbed_arrows,itm_war_bow,
   itm_gothic_puncture_mace,
    itm_knyaz_armor,itm_rus_splint_greaves,itm_novogrod_helm,itm_mail_armor_horse,itm_lamellar_armor_horse,itm_hourglass_gauntlets_ornate],
   def_attrib|level(26),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (160) | wp_crossbow (10) | wp_throwing (10),knows_riding_4| knows_ironflesh_4|knows_power_strike_3|knows_power_draw_5,borovod_face_middle_1, borovod_face_older_2],
  #---------------------------------------------------------
 ["borovod_messenger","Borovod Messenger","Borovod Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,borovod_face_young_1, borovod_face_older_2],
  ["borovod_deserter","Borovod Deserter","Borovod Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,borovod_face_young_1, borovod_face_older_2],
  ["borovod_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ball_mace_no2,
   itm_rus_lamellar_a,itm_rus_splint_greaves,itm_tagancha_helm_a,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,borovod_face_middle_1, borovod_face_older_2],
  ["borovod_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_borovod_glaive,itm_kuyak_b,itm_kuyak_a,itm_mail_chausses,itm_iron_greaves,itm_facecover_kettlehat,itm_mail_mittens],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,borovod_face_middle_1, borovod_face_older_2],
	#-----------town guard-----------------
	["borovod_guard","Borovod Guard","Borovod Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
	   [itm_sword_medieval_c_small,itm_tab_shield_kite_cav_b,
		itm_borovod_guard_armor,itm_leather_boots,itm_borovod_guard_helmet,itm_leather_gloves],
	   def_attrib|level(20),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_1,borovod_face_young_1, borovod_face_older_2],
	#--------------------------------------
   #--borovod's household
 ["prince_hussar","Prince's Hussar","Prince's Hussars",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_colored_lance_d,itm_hussar_sword,itm_tab_shield_kite_cav_b,
    itm_hussar_armor,itm_plate_boots,itm_kapalin,itm_hussar_horse,itm_mail_mittens],
   def_attrib|level(36),wp_one_handed (220) | wp_two_handed (80) | wp_polearm (260) ,knows_common|knows_riding_8| knows_ironflesh_5|knows_power_strike_3,borovod_face_middle_1, borovod_face_older_2],
   #--


  ["guhulay_tribesman","Guhulay Tribesman","Guhulay Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows,itm_club,itm_spear,itm_hunting_bow,
    itm_steppe_cap,itm_nomad_cap_b,itm_guhulay_vest_c,itm_guhulay_vest_a,itm_nomad_boots,itm_guhulay_leather_boots],
   def_attrib|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_1|knows_horse_archery_2,guhulay_face_younger_1, guhulay_face_old_2],
  ["guhulay_skirmisher","Guhulay Skirmisher","Guhulay Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_guhulay_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_tab_shield_small_round_a,
    itm_guhulay_helmet_e,itm_hide_boots,itm_g_padded,itm_steppe_horse],
   def_attrib|level(10),wp_one_handed (80) | wp_two_handed (60) | wp_polearm (60) | wp_archery (80) | wp_crossbow (60) | wp_throwing (80),knows_common|knows_riding_4|knows_power_draw_3|knows_horse_archery_3,guhulay_face_younger_1, guhulay_face_old_2],
  ["guhulay_horseman","Guhulay Horseman","Guhulay Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [itm_arrows,itm_nomad_bow,itm_sword_guhulay_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
   itm_guhulay_helmet_f,itm_g_padded_mail,itm_guhulay_leather_boots,itm_steppe_horse,itm_steppe_horse_1],
   def_attrib|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_horse_archery_3,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_horse_archer","Guhulay Horse Archer","Guhulay Horse Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_guhulay_bow,itm_lance,itm_bodkin_arrows,itm_sword_guhulay_3,itm_guhulay_mace,
    itm_guhulay_helmet_g,itm_g_coat_of_plates_a,itm_guhulay_cav_boots,itm_steppe_horse,itm_steppe_horse_1],
   def_attrib|level(19),wp_one_handed (110) | wp_two_handed (80) | wp_polearm (80) | wp_archery (110) | wp_crossbow (80) | wp_throwing (110),knows_riding_6|knows_power_draw_2|knows_ironflesh_1|knows_horse_archery_7|knows_power_throw_3|knows_power_strike_1|knows_athletics_3,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_veteran_horse_archer","Guhulay Veteran Horse Archer","Guhulay Veteran Horse Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_guhulay_4,itm_guhulay_bow,itm_luc_horsemans_axe,itm_wyu_sword,
   itm_guhulay_poisoned_arrows,itm_tab_shield_small_round_c,
    itm_guhulay_helmet_h,itm_g_coat_of_plates_b,itm_rus_splint_greaves,itm_leather_gloves,itm_steppe_horse,itm_courser],
   def_attrib|level(21),wp_one_handed (120) | wp_two_handed (90) | wp_polearm (90) | wp_archery (130) ,knows_riding_7|knows_power_draw_3|knows_ironflesh_3|knows_horse_archery_9|knows_power_strike_2|knows_athletics_4,guhulay_face_middle_1, guhulay_face_older_2],

 ["guhulay_native_militia","Guhulay Native Militia","Guhulay Native Milicia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_spear,itm_tab_shield_small_round_a,
    itm_guhulay_helmet_a,itm_hide_boots,itm_guhulay_padded],
   def_attrib|level(10),wp(80),knows_common,guhulay_face_younger_1, guhulay_face_old_2],
  ["guhulay_native_footman","Guhulay Native Footman","Guhulay Native Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
  [itm_tab_shield_small_round_b,itm_spear,itm_tab_shield_small_round_b,
   itm_guhulay_helmet_b,itm_guhulay_padded_mail,itm_guhulay_leather_boots],
   def_attrib|level(14),wp(100),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_horse_archery_3,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_native_infantry","Guhulay Native Infantry","Guhulay Native Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_tab_shield_small_round_c,itm_lobarian_spear_a,
    itm_guhulay_helmet_c,itm_guhulay_padded_mail_lamellar,itm_rus_splint_greaves,itm_lamellar_gauntlets],
   def_attrib|level(19),wp(110) ,knows_ironflesh_1|knows_power_strike_1|knows_athletics_3,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_foot_soldier","Guhulay Heavy Infantry","Guhulay Heavy Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_guhulay_hafted_blad,itm_hafted_blade_1,itm_hafted_blade_2,itm_hafted_blade_3,itm_hafted_blade_4,itm_hafted_blade_5,itm_hafted_blade_6,
    itm_guhulay_helmet_d,itm_guhulay_lamellar_armor,itm_rus_splint_greaves,itm_lamellar_gauntlets],
   def_attrib|level(24),wp(140) ,knows_ironflesh_1|knows_power_strike_1|knows_athletics_3,guhulay_face_young_1, guhulay_face_older_2],
 #---------------nobles---------------------
  ["guhulay_lancer","Guhulay Lancer","Guhulay Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_lance,itm_guhulay_bow,itm_guhulay_poisoned_arrows,itm_tab_shield_small_round_c,
   itm_guhulay_helmet_i,itm_guhulay_coat_of_plates_a,itm_splinted_leather_greaves,itm_scale_gauntlets,itm_courser],
   def_attrib|level(23),wp_one_handed (150) | wp_two_handed (90) | wp_polearm (250) | wp_archery (150),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_ironflesh_4|knows_horse_archery_9| knows_athletics_4,guhulay_face_middle_1, guhulay_face_older_2],
  ["guhulay_mirza","Guhulay Mirza","Guhulay Mirzas",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_guhulay_4,itm_luc_horseman_pick,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,itm_wyu_sword,itm_guhulay_bow,itm_guhulay_poisoned_arrows,
    itm_guhulay_helmet_j,itm_guhulay_mirza_armor,itm_guhulay_noble_armor,itm_splinted_leather_greaves,itm_scale_gauntlets,
	itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_warhorse_steppe,itm_steppe_char_iron],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (300) | wp_archery (200) ,knows_riding_9|knows_power_strike_3|knows_power_draw_4|knows_ironflesh_4|knows_horse_archery_10| knows_athletics_5,guhulay_face_middle_1, guhulay_face_older_2],
  #------------------------------------------
  #---------------special troops---------------------
 ["wyu_golden_warrior","Wyu Golden Warrior","Wyu Golden Warriors",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_wyu_axe,itm_wyu_sword,itm_horn_bow,itm_guhulay_poisoned_arrows,itm_light_lance,
    itm_guhulay_elite_helm,itm_guhulay_horseman_armor,itm_guhulay_horseman_scale,itm_warhorse_steppe_golden,itm_guhulay_cav_boots,itm_lamellar_gauntlets],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (90) | wp_polearm (90) | wp_archery (160) ,knows_riding_9|knows_power_draw_4|knows_ironflesh_3|knows_horse_archery_9|knows_power_strike_2|knows_athletics_4,0x0000000a2e08900c20db6db6db6db1c300000000001fc7300000000000000000, 0x0000000a2e08710b36db6db6db6db6db00000000001db6db0000000000000000],
  ["desert_camel_rider","Desert Camel Rider","Desert Camel Riders",tf_mounted|tf_guarantee_all,0,0,fac_desert_tribes,
   [itm_desert_scimitar,itm_tab_shield_round_b,
    itm_desert_turban_blue,itm_desert_armor_b,itm_desert_armor_a,itm_guhulay_leather_boots,itm_leather_gloves,itm_camel],
   def_attrib|level(21),wp_one_handed (120) | wp_two_handed (90) | wp_polearm (90)  ,knows_riding_7|knows_ironflesh_3|knows_power_strike_1|knows_athletics_4,0x000000097f00a5c036db6dbfffb2eedc00000000001c3bf90000000000000000, 0x000000097008d14036db6db6db6db6db00000000001db6db0000000000000000],
  ["desert_warrior","Desert Warrior","Desert Warriors",tf_guarantee_all,0,0,fac_desert_tribes,
   [itm_desert_scimitar,itm_tab_shield_round_c,itm_bamboo_spear,
    itm_desert_turban_blue,itm_desert_armor_a,itm_guhulay_leather_boots],
   def_attrib|level(16),wp_one_handed (100) | wp_two_handed (90) | wp_polearm (90)  ,knows_riding_7|knows_ironflesh_3|knows_power_strike_1|knows_athletics_4,0x000000097008d14036db6db6db6db6db00000000001db6db0000000000000000, 0x000000097f00a5c036db6dbfffb2eedc00000000001c3bf90000000000000000],

  #-------------------------------------------------
  ["guhulay_messenger","Guhulay Messenger","Guhulay Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_guhulay_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_deserter","Guhulay Deserter","Guhulay Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_guhulay_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_guhulay_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,guhulay_face_young_1, guhulay_face_older_2],
  ["guhulay_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_guhulay_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_guhulay,itm_guhulay_padded_mail_lamellar,itm_guhulay_padded_mail,itm_guhulay_leather_boots,itm_iron_greaves,itm_guhulay_helmet_b,itm_guhulay_helmet_c],
   def_attrib|level(24),wp(130),knows_athletics_5| knows_ironflesh_5,guhulay_face_middle_1, guhulay_face_older_2],
  ["guhulay_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_guhulay_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_guhulay,itm_g_coat_of_plates_a,itm_g_coat_of_plates_b,itm_guhulay_leather_boots,itm_iron_greaves,itm_guhulay_helmet_f,itm_guhulay_helmet_g,itm_guhulay_helmet_b,itm_guhulay_helmet_c],
   def_attrib|level(24),wp(130),knows_athletics_5| knows_ironflesh_5,guhulay_face_middle_1, guhulay_face_older_2],
#-----------town guard-------------
   ["guhulay_guard","Guhulay Guard","Guhulay Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_sword_guhulay_2,itm_fighting_pick,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
    itm_gi_watchman_padded_mail,itm_guhulay_helmet_c,itm_guhulay_leather_boots],
   def_attrib|level(20),wp_melee(100),knows_ironflesh_1|knows_power_strike_1|knows_athletics_3,guhulay_face_young_1, guhulay_face_older_2],
#----------------------------------

  ["hadvog_recruit","Hadvog Recruit","Hadvog Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_hatchet,itm_sml_rshield,itm_sml_lshield,
    itm_blue_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
   def_attrib|level(6),wp(50),knows_power_throw_1|knows_athletics_1,hadvog_face_younger_1, hadvog_face_old_2],
  ["hadvog_footman","Hadvog Footman","Hadvog Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [#itm_one_handed_war_axe_a,itm_spear,itm_tab_shield_round_a,itm_mid_lshield,
    itm_spear,itm_tab_shield_round_a,itm_mid_lshield,
	itm_hadvog_helmet_1,itm_hadvog_gambeson,itm_leather_boots,itm_nomad_boots],
   def_attrib|level(10),wp(70),knows_ironflesh_2|knows_power_strike_1|knows_power_throw_2|knows_athletics_2 ,hadvog_face_young_1, hadvog_face_old_2],
  ["hadvog_trained_footman","Hadvog Trained Footman","Hadvog Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [#itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_mid_rwshield,itm_war_spear,itm_javelin,
    itm_mid_rwshield,itm_war_spear,
	itm_nasal_helmet_cloth_blue,itm_hadvog_gambeson_mail,itm_splinted_leather_greaves],
   def_attrib|level(14),wp(100),knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_3 ,hadvog_face_young_1, hadvog_face_old_2],
  ["hadvog_warrior","Hadvog Warrior","Hadvog Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_large_lshield,itm_javelin,itm_javelin,
    itm_big_nasal_helmet,itm_nasal_helmet_mail_blue,itm_hadvog_coat_of_plates_a,itm_splinted_greaves,itm_wisby_gauntlets_black],
   def_attrib|level(19),wp(120),knows_ironflesh_4|knows_power_strike_2|knows_power_throw_3|knows_athletics_4 ,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_veteran","Hadvog Veteran","Hadvog Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_warhammer_ita,itm_huskarl_axe_a,itm_sword_viking_2,itm_large_rwshield,itm_colored_hadvog_shield,itm_javelin,itm_javelin,
    #itm_hadvog_warlord_helmet ,itm_banded_armor,itm_hadvog_cuir_bouilli,itm_splinted_leather_greaves,itm_splinted_greaves_spurs,itm_leather_gloves],
	itm_hadvog_faceplate_a,itm_hadvog_coat_of_plates_b,itm_splinted_leather_greaves,itm_splinted_greaves_spurs,itm_gauntlets,itm_wisby_gauntlets_black],

   def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_3|knows_power_throw_3|knows_athletics_1 ,hadvog_face_young_1, hadvog_face_older_2],
   #---------special troops-------------
   ["hadvog_berserker","Hadvog Berserker","Hadvog Berserkers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_long_axe_c_alt,
    itm_royal_huskarl_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens,itm_full_helm],
   def_attrib|level(25),wp(190),knows_ironflesh_10|knows_power_strike_3|knows_athletics_10,hadvog_face_middle_1, hadvog_face_older_2],
  #------------------------------------
	#------------noble--------------
   ["hadvog_huskarl","Hadvog Huskarl","Hadvog Huskarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
 [itm_long_axe_c,itm_huskarl_axe_a,itm_tab_shield_round_e,itm_javelin,itm_knights_winged_mace_1h,itm_war_hammer_no4,itm_horsemans_axe_no3,itm_ball_mace_no2,
    itm_norman_faceplate_a,itm_norman_pepperpot,itm_nord_coat_of_plates,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(26),wp(150),knows_ironflesh_5|knows_power_strike_3|knows_power_throw_4|knows_athletics_7 ,hadvog_face_middle_1, hadvog_face_older_2],
  ["hadvog_chieftain","Hadvog Chieftain","Hadvog Chieftains",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_tab_shield_round_e,itm_knights_winged_mace_1h,itm_war_hammer_no4,itm_horsemans_axe_no3,itm_ball_mace_no2,
    itm_chieftain_armour,itm_nord_splinted_greaves,itm_nord_ornate_visored_helmet,itm_gauntlets,itm_mail_mittens],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_throwing (75),knows_common| knows_ironflesh_8|knows_power_strike_3,hadvog_face_middle_1, hadvog_face_older_2],
	#-----------------------------
  ["hadvog_messenger","Hadvog Messenger","Hadvog Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_rus_horse,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_deserter","Hadvog Deserter","Hadvog Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_battle_axe,itm_tab_shield_round_d,itm_hadvog_coat_of_plates_a,itm_hadvog_coat_of_plates_b,itm_nord_coat_of_plates,itm_mail_chausses,itm_iron_greaves,itm_hadvog_helmet_2,itm_hadvog_helmet_3,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,hadvog_face_middle_1, hadvog_face_older_2],
  ["hadvog_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_battle_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_hadvog_coat_of_plates_a,itm_hadvog_coat_of_plates_b,itm_nord_coat_of_plates,itm_mail_chausses,itm_iron_greaves,itm_norman_helm_1,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,hadvog_face_middle_1, hadvog_face_older_2],
#----------town guard------------
 ["hadvog_guard","Hadvog Guard","Hadvog Guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2_small,itm_tab_shield_round_d,
    itm_hadvog_helmet_3,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(20),wp(100),knows_ironflesh_3|knows_power_strike_1|knows_power_throw_3|knows_athletics_5 ,hadvog_face_young_1, hadvog_face_older_2],
#--------------------------------
   #--hadvog household
 ["king_huskarl","King's Huskarl","King's HusKarls",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_huskarl_axe,itm_tab_shield_round_d,
    itm_hadvog_coat_of_plates,itm_iron_greaves,itm_hadvog_champion_helm,itm_nord_warhorse,itm_mail_mittens],
   def_attrib|level(36),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) ,knows_common|knows_riding_4| knows_ironflesh_7|knows_power_strike_3,hadvog_face_middle_1, hadvog_face_older_2],
   #--


  ["imifir_recruit","Imifir Recruit","Imifir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_pitch_fork,itm_tab_shield_pavise_a,
    itm_arena_tunic_green,itm_wrapping_boots,itm_nomad_boots,itm_head_wrappings,itm_straw_hat],
   def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,imifir_face_younger_1, imifir_face_old_2],
  ["imifir_spearman","Imifir Paviser","Imifir Pavisers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [#itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,itm_tab_shield_pavise_c,itm_falchion,
   itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,itm_tab_shield_pavise_c,
    itm_chapel_de_fer_cloth2,itm_green_gambeson_a,itm_wrapping_boots,itm_nomad_boots],
   def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_athletics_1,imifir_face_young_1, imifir_face_old_2],
  ["imifir_trained_spearman","Imifir Trained Paviser","Imifir Trained Paviserq",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [#itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,itm_imifir_fauchard_fork,itm_war_spear,itm_tab_shield_pavise_d,itm_military_cleaver_b,
   itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,itm_war_spear,itm_tab_shield_pavise_d,
    itm_chapel_de_fer_mail1,itm_brigandine_green_mail,itm_nomad_boots,itm_leather_boots],
   def_attrib|level(14),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (170) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_3|knows_power_strike_1|knows_athletics_2,imifir_face_young_1, imifir_face_older_2],
  ["imifir_pikeman","Imifir Pikeman","Imifir Pickmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_pike_long,
    itm_zitta_bascinet_novisor,itm_brigandine_plackart,itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(19),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (200) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_1,imifir_face_young_1, imifir_face_older_2],
  ["imifir_halberdier","Imifir Halberdier","Imifir Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_halberd,itm_halberd,itm_halberd,itm_halberd,itm_halberd,itm_imifir_fauchard_fork,#itm_atian_longsword,itm_steel_buckler1,
	itm_heavy_brigandine_plackart,itm_iron_greaves,itm_zitta_bascinet,itm_gauntlets],
   def_attrib|level(22),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (160) | wp_throwing (115),knows_common|knows_ironflesh_6| knows_power_strike_1|knows_athletics_1,imifir_face_middle_1, imifir_face_older_2],


 # ["imifir_crossbowman","Imifir Crossbowman","Imifir Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   # [itm_sword_medieval_a,itm_falchion,itm_tab_shield_pavise_c,itm_crossbow,itm_bolts,
    # itm_green_gambeson_a,itm_imifir_padded_coif,itm_nomad_boots,itm_wrapping_boots],
   # def_attrib|level(10),wp(85),knows_common|knows_ironflesh_2| knows_athletics_2,imifir_face_young_1, imifir_face_older_2],
  ["imifir_crossbowman","Imifir Crossbowman","Imifir Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_pavise_d,itm_crossbow,itm_bolts,
    itm_chapel_de_fer_cloth1,itm_brigandine_green,itm_leather_boots_black,itm_leather_gloves],
   def_attrib|level(15),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (105) | wp_throwing (90),knows_common|knows_ironflesh_1|knows_athletics_3,imifir_face_young_1, imifir_face_older_2],
  ["imifir_pavise_crossbowman","Imifir Pavise Crossbowman","Imifir Pavise Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_military_cleaver_c,itm_pavise,itm_sniper_crossbow,itm_steel_bolts,
     itm_chapel_de_fer_mail3,itm_brigandine_green_mail,itm_mail_boots,itm_mail_mittens],
   def_attrib|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (115) | wp_throwing (100),knows_common|knows_ironflesh_2| knows_athletics_1,imifir_face_middle_1, imifir_face_older_2],
   #------------mod--------------
   ["imifir_bodyguard","Imifir Trabant","Imifir Trabants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_luc_bill_guisarme_long,
    itm_brigandine_plackart_gorget,itm_plate_boots,itm_sallet_mask,itm_gauntlets],
   def_attrib|level(24),wp_melee(150),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,imifir_face_young_1],
  ["imifir_richman","Imifir Field Captain","Imifir Field Captains",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_luc_english_bill,
   itm_milanese_armour,itm_pigface_klappvisor,itm_plate_boots,itm_gauntlets,itm_mail_mittens],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common| knows_ironflesh_6|knows_power_strike_2,imifir_face_middle_1, imifir_face_older_2],
	#------------mod--------------
  ["imifir_messenger","Imifir Messenger","Imifir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_deserter","Imifir Deserter","Imifir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_military_hammer,itm_chapel_de_fer_cloth2,itm_imifir_breastplate,itm_mail_chausses,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_luc_english_bill,itm_bascinet_2,itm_brigandine_plackart_gorget,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3| knows_ironflesh_3,imifir_face_middle_1, imifir_face_older_2],
#------town guard--------------
 ["imifir_guard","Imifir Guard","Imifir Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_military_cleaver_c,itm_steel_buckler1,
    itm_chapel_de_fer_mail2,itm_imifir_breastplate,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   def_attrib|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) ,knows_common|knows_ironflesh_3|knows_power_strike_1|knows_athletics_3,imifir_face_young_1, imifir_face_older_2],
#------------------------------
#--imifir household troops
 ["bilomadal_arquebuser","Bilomadal Arquebuser","bilomadal_arquebuser",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_leather_gloves,itm_bilomadal_armor,itm_bilomadal_helmet_1,itm_imifir_axe,itm_shynbaulds,itm_early_arquebuse,itm_cartridges],
   def_attrib|level(36),wp(220)| wp_firearm (260),knows_ironflesh_3,imifir_face_middle_1, imifir_face_older_2],
#--

   #peasant - retainer - footman - man-at-arms -  knight


 ["afirid_recruit","Afirid Recruit","Afirid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_scythe,itm_hatchet,itm_club,itm_tab_shield_heater_a,itm_afirid_felt_hat,itm_turban,itm_afirid_boots_a,
    itm_sar_pants,],
   def_attrib|level(4),wp(60),knows_common|knows_athletics_1,afirid_face_younger_1, afirid_face_middle_2],
 ["afirid_footman","Afirid Footman","Afirid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_tab_shield_kite_a,
    itm_afirid_inf_armor,itm_turban_mail_a,itm_afirid_boots_a,itm_afirid_boots_b],
   def_attrib|level(9),wp(75),knows_common|knows_athletics_2,afirid_face_young_1, afirid_face_old_2],
 ["afirid_light_infantry","Afirid Light Infantry ","Afirid Light Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_afirid_medium_spear,itm_tab_shield_kite_b,
    itm_afirid_boots_b,itm_afirid_helmet_inf_1,itm_afirid_inf_armor_a],
   def_attrib|level(14),wp_one_handed (85) | wp_two_handed (85) | wp_polearm (160) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_athletics_5|knows_power_throw_2|knows_ironflesh_1,afirid_face_young_1, afirid_face_old_2],
 ["afirid_infantry","Afirid Infantry","Afirid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_afirid_inf_armor_b,itm_afirid_helmet_inf_2,itm_afirid_boots_c,itm_afirid_boots_b,
   itm_afirid_axe_a,itm_afirid_axe_b,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (170) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_3|knows_ironflesh_2  | knows_power_throw_3|knows_athletics_4,afirid_face_middle_1, afirid_face_old_2],
 ["afirid_heavy_infantry","Afirid Heavy infantry","Afirid Heavy Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_military_pick,itm_afirid_two_handed_mace_1,itm_afirid_two_handed_axe_a,itm_mace_4,
   itm_afirid_boots_d, itm_afirid_boots_c,itm_afirid_inf_armor_c,itm_afirid_helmet_inf_3,itm_mail_mittens,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_one_handed (150) | wp_two_handed (135) | wp_polearm (180) | wp_archery (75) | wp_crossbow (75) | wp_throwing (140),knows_common| knows_ironflesh_3|knows_power_strike_1|knows_athletics_3,afirid_face_middle_1, afirid_face_older_2],

 ["afirid_skirmisher","Afirid Skirmisher","Afirid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_afirid_ran_armor_a,itm_shortened_spear,itm_javelin,itm_afirid_conical_helmet_1,itm_leather_boots_black,itm_tab_shield_kite_b],
   def_attrib|level(14),wp_one_handed (60) | wp_two_handed (0) | wp_polearm (200) | wp_archery (10) | wp_crossbow (10) | wp_throwing (100),knows_common|knows_power_strike_3|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,afirid_face_young_1, afirid_face_middle_2],

 # ["afirid_mounted_skirmisher","Afirid Mounted Skirmisher","Afirid Mounted Skirmishers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_6,
   # [itm_afirid_light_lamellar,itm_shortened_spear,itm_javelin,itm_afirid_conical_helmet_1,itm_leather_boots_black,itm_tab_shield_kite_b],
   # def_attrib|level(20),wp_one_handed (100) | wp_two_handed (0) | wp_polearm (200) | wp_archery (10) | wp_crossbow (10) | wp_throwing (100),knows_common|knows_power_strike_3|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,afirid_face_young_1, afirid_face_middle_2],

  ["afirid_horseman","Afirid Horseman","Afirid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_scimitar,itm_tab_shield_kite_cav_a,
    itm_afirid_cav_armor_a,itm_afirid_boots_b, itm_afirid_helmet_cav_1,itm_leather_gloves,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2,afirid_face_young_1, afirid_face_old_2],
 ["afirid_heavy_horseman","Afirid Veteran Horseman","Afirid Veteran Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_afirid_cavalry_sword,itm_tab_shield_kite_cav_b,
	itm_afirid_cav_armor_b,itm_afirid_boots_d,itm_afirid_boots_c,itm_afirid_helmet_cav_2,itm_mail_mittens,itm_arabian_horse_b],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (110) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_6|knows_ironflesh_5|knows_power_strike_1,afirid_face_middle_1, afirid_face_older_2],
	#--------------mod-----------------
	 ["afirid_charif","Afirid Charif","Afirid Charifs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
	   [itm_scimitar_b,itm_afirid_shield_p,itm_afirid_shield_q,itm_afirid_lance,
		itm_afirid_nob_armor_a,itm_afirid_boots_c,itm_afirid_boots_d,itm_afirid_charif_helmet_1,itm_afirid_charif_helmet_2,itm_leather_gloves,itm_afirid_warhorse,itm_afirid_warhorse_lamellar,itm_afirid_warhorse_deco,itm_afirid_warhorse_lamellar_deco],
	   def_attrib|level(20),wp_melee(150),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,afirid_face_young_1, afirid_face_old_2],
	 ["afirid_caid","Afirid Caid","Afirid Caids",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
	   [itm_scimitar_b,itm_afirid_shield_l,itm_jarid,
	    itm_byzantine_mace_3,itm_afirid_lance,
		itm_afirid_nob_armor_b,itm_mail_boots,itm_afirid_caid_helmet_1,itm_afirid_caid_helmet_2,itm_afirid_noble_warhorse,itm_afirid_noble_warhorse_deco,itm_mail_mittens],
	   def_attrib|level(27),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (75) | wp_crossbow (75) | wp_throwing (200),knows_common|knows_riding_6|knows_horse_archery_3| knows_ironflesh_5|knows_power_strike_3|knows_power_throw_4,afirid_face_middle_1, afirid_face_older_2],
	#---------------------------------

   ["afirid_messenger","Afirid Messenger","Afirid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_afirid_cav_armor_b,itm_mail_chausses,itm_afirid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_3,afirid_face_young_1, afirid_face_old_2],
  ["afirid_deserter","Afirid Deserter","Afirid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_afirid_cav_armor_b,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_3,afirid_face_young_1, afirid_face_old_2],
  ["afirid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_mace_4,itm_tab_shield_kite_d,
   itm_afirid_boots_c,itm_afirid_inf_armor_b,itm_afirid_cav_armor_a,itm_afirid_ran_armor_a,itm_afirid_mail_coif,
   itm_afirid_helmet_inf_1,itm_afirid_conical_helmet_1,itm_turban_helmet,itm_afirid_sallet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common| knows_ironflesh_3|knows_power_strike_3,afirid_face_middle_1, afirid_face_older_2],
  ["afirid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_arabian_sword_b,itm_tab_shield_kite_d,
   itm_afirid_inf_armor_c,itm_afirid_cav_armor_b,itm_afirid_ran_armor_b,
   itm_afirid_helmet_inf_1,itm_afirid_conical_helmet_1,itm_turban_helmet,itm_afirid_sallet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_afirid_boots_c, itm_afirid_boots_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common| knows_ironflesh_3|knows_power_strike_3,afirid_face_middle_1, afirid_face_older_2],
	#-----------town guard-------------
	["afirid_guard","Afirid Guard","Afirid Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_6,
	   [itm_afirid_light_lamellar,itm_shahi,itm_afirid_boots_c,itm_afirid_boots_b,itm_afirid_axe_b,itm_afirid_crossbow,itm_bolts],
	   def_attrib|level(20),wp_one_handed (100) | wp_two_handed (105) | wp_polearm (105)|wp_crossbow(40) ,knows_common|knows_ironflesh_3|knows_power_strike_1  | knows_power_throw_3|knows_athletics_3,afirid_face_middle_1, afirid_face_old_2],
	#---------------------------------
   #--afirid household
 ["sultan_guard","Sultan's Guard","Sultan's Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_scimitar_b,itm_tab_shield_small_round_c,itm_heavy_lance,
    itm_sultan_guard_armor,itm_afirid_boots_c,itm_sultan_guard_helm,itm_sultan_charger,itm_mail_mittens],
   def_attrib|level(36),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) ,knows_common|knows_riding_8| knows_ironflesh_5|knows_power_strike_3,afirid_face_middle_1, afirid_face_older_2],
   #--

#----------------------------
#peasant - retainer - footman - man-at-arms -  knight
  ["dirim_recruit","Dirim Recruit","Dirim Recruits",tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_linen_tunic,itm_arming_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,pravar_face_younger_1, pravar_face_middle_2],
  ["dirim_militia","Dirim Militia","Dirim Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_tab_shield_sarranid_a,itm_shortened_spear,itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,
    itm_dirim_jerkin,itm_dirim_helmet,itm_dirim_half_greaves],
   def_attrib|level(9),wp(75),knows_common,pravar_face_young_1, pravar_face_old_2],
  ["dirim_footman","Dirim Footman","Dirim Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [#itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a,itm_dirim_gladius,itm_tab_shield_sarranid_a,
   itm_lobarian_spear_c,itm_lobarian_spear_b,itm_tab_shield_sarranid_a,
	itm_dirim_footman_armor,itm_dirim_pilum,itm_dirim_greaves,itm_dirim_footman_helmet],
   def_attrib|level(14),wp_melee(85),knows_common|knows_ironflesh_2|knows_athletics_2,pravar_face_young_1, pravar_face_old_2],
  ["dirim_regular","Dirim Regular","Dirim Regulars",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_common_sword_d,itm_dirim_pilum,itm_tab_shield_sarranid_b,itm_luc_german_winged_mace,
    #itm_swa_surcoat_over_mail,itm_mail_chausses,itm_barbuta2],
	itm_dirim_regular_armor,itm_dirim_regular_helm,itm_dirim_mail_greaves,itm_mail_mittens],
   def_attrib|level(20),wp_melee(105)| wp_throwing (100),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_1| knows_athletics_1|knows_power_throw_2,pravar_face_young_1, pravar_face_old_2],
  ["dirim_veteran","Dirim Veteran","Dirim Veterans",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_poleaxe_no3,
    #itm_swa_mail_and_platee,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_gauntlets,itm_barbuta1],
    itm_dirim_veteran_armor,itm_shynbaulds,itm_wisby_gauntlets_black,itm_dirim_veteran_helm],
   def_attrib|level(25),wp_melee(135)| wp_throwing (110),knows_common| knows_power_throw_3|knows_ironflesh_5|knows_power_strike_2|knows_athletics_4,0x0000000e7f0c200436e1b22b11914cdc00000000001f2b1a0000000000000000, 0x0000000a3f0d100436e1b22b1192c8fc00000000001f2b1a0000000000000000],
  ["dirim_forest_hunter","Dirim Forest Hunter","Dirim Forest Hunters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
  [itm_arrows,itm_short_bow,itm_archers_hatchet,itm_archer_armor,itm_ankle_boots, itm_dirim_archer_helmet],
   def_attrib|level(14),wp(80)| wp_archery(110),knows_common|knows_riding_2|knows_ironflesh_1|knows_power_draw_3,pravar_face_young_1, pravar_face_middle_2],
  ["dirim_long_bowman","Dirim Longbownam","Dirim Longbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_bodkin_arrows,itm_long_bow,itm_bowman_hatchet,itm_bowman_armor,itm_leather_boots_black,itm_dirim_bowman_helmet],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (150),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1|knows_power_draw_4,pravar_face_young_1, pravar_face_old_2],
  #----------------noble--------------------------
  ["dirim_cavalryman","Dirim Cavalryman","Dirim Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_lance,itm_dirim_cav_sword,itm_tab_shield_heater_cav_a,
    #itm_swa_mail_long_surcoat,itm_swa_cuir_bouilli_a,itm_mail_chausses,itm_swa_bascinet_new_a,itm_hunter],
	 itm_dirim_breastplate,itm_gauntlets,itm_mail_chausses,itm_cataphract_helm,itm_rouncy],
   def_attrib|level(21),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,dirim_face_young_1, dirim_face_middle_1],
  ["dirim_pronoiar","Dirim Pronoiar","Dirim Pronoiars",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_heavy_lance,itm_sword_medieval_d_long,itm_bronze_spiked_mace_5p,itm_dirim_cav_sword,itm_tab_shield_heater_cav_b,
	itm_dirim_plate_armor,itm_shynbaulds,itm_pronoiar_helm,itm_romanhalfcata,itm_gauntlets],
   def_attrib|level(28),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knows_common|knows_riding_5| knows_ironflesh_5|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  #-----------------------------------------------
    #----------------special troop--------------------------
  # ["dirim_centuri","Dirim Centuri","Dirim Centuri",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_7,
   # [itm_dirim_cav_sword,itm_lion_round_shield,
	 # itm_dirim_mail,itm_gauntlets,itm_mail_chausses,itm_h_tribune2],
   # def_attrib|level(24),wp_one_handed (150) | wp_two_handed (140) | wp_polearm (140),knows_common|knows_ironflesh_2| knows_power_strike_2,pravar_face_middle_1, pravar_face_older_2],
  #-----------------------------------------------

  ["dirim_messenger","Dirim Messenger","Dirim Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_7,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,pravar_face_young_1, pravar_face_old_2],
  ["dirim_deserter","Dirim Deserter","Dirim Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,pravar_face_young_1, pravar_face_old_2],
  ["dirim_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_sword_medieval_c_small,itm_tab_shield_heater_c,itm_dirim_breastplate,itm_plate_boots,itm_dirim_bowman_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  ["dirim_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_luc_celtic_sword_3,itm_luc_partisan,
    itm_dirim_veteran_armor,itm_iron_greaves,itm_gauntlets,itm_dirim_regular_helm],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
   #-----------town guard---------------
   ["dirim_pretorian_guard","Dirim Pretorian Guard","Dirim pretorian Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_tab_shield_sarranid_c,itm_luc_burgundian_axe,itm_bronze_mace,
	itm_pretorian_armor,itm_iron_greaves,itm_pretorian_helm,itm_mail_mittens],
   def_attrib|level(26),wp_melee(160),knows_common|knows_ironflesh_2|knows_power_strike_2| knows_athletics_3,pravar_face_middle_1, pravar_face_old_2],
   #-----------town guard---------------
#-------------------------------------------

#------------THE TRADE COMPANY------------
  ["company_colonial_militia","Company Colonial Militia","Company Colobial Milicia",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_sword_medieval_c_small,itm_glaive,itm_steel_buckler2,
   itm_atian_colonial_tunic,itm_black_boots,itm_chapel_de_fer],
   def_attrib|level(14),wp(100),knows_common,pravar_face_young_1, pravar_face_old_2],
  #----------------noble--------------------------
  ["company_ranger","Company Ranger","Company Rangers",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_atian_longsword,itm_flintlock_rifle,itm_cartridges,itm_fragmentation_grenade,
    itm_colonial_ranger_tunic,itm_black_boots,itm_combed_morion,itm_leather_gloves],
   def_attrib|level(21),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140)| wp_firearm (100),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["company_dragon","Company Dragon","Company Dragon",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_atian_longsword,itm_cartridges, itm_flintlock_pistol_1,itm_cartridges,
    itm_company_helm,itm_plate_boots,itm_company_armor,itm_hunter],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) ,knows_common|knows_riding_5| knows_ironflesh_5|knows_power_strike_2,pravar_face_middle_1, pravar_face_older_2],
  #-----------------------------------------------
  ["company_messenger","Dirim Messenger","Dirim Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,pravar_face_young_1, pravar_face_old_2],
  ["company_deserter","Dirim Deserter","Dirim Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,pravar_face_young_1, pravar_face_old_2],
  ["company_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_arming_winged_mace,itm_black_boots,itm_colonial_pikeman_armor,itm_combed_morion,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  ["company_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_atian_guisarme,itm_colonial_torso,itm_black_boots,itm_combed_morion_blued,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common| knows_ironflesh_3|knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
#-------------------------------------------


  ["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_hadvog_shield,itm_rawhide_coat,itm_leather_cap,itm_leather_jerkin,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots,itm_saddle_horse],
   def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_pike_long,itm_spear,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_hadvog_shield],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_1,imifir_face_young_1, imifir_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_short_bow,itm_hunting_bow,
    itm_common_hood,itm_simple_iberian_helmet,itm_shirt,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots,itm_leather_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,pravar_face_young_1, pravar_face_old_2],

  # ["sea_raider","Nordic Raider","Nordic Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   # [itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_hadvog_shield,itm_hadvog_shield,itm_hadvog_shield,itm_wooden_shield,itm_javelin,itm_throwing_axes,
    # itm_hadvog_helmet,itm_hadvog_helmet,itm_nasal_helmet,itm_nomad_vest,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_nomad_boots],
   # def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_1|knows_power_draw_2|knows_power_throw_2|knows_riding_1|knows_athletics_2,hadvog_face_young_1, hadvog_face_old_2],
["sea_raider","Galnar Raider","Galnar Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_wooden_shield,itm_spear,itm_throwing_axes,
    itm_hadvog_helmet,itm_tribal_warrior_outfit,itm_hunter_boots,itm_splinted_greaves],
   def_attrib|level(16),wp(100),knows_ironflesh_4|knows_power_strike_1|knows_power_throw_2|knows_athletics_4 ,hadvog_face_young_1, hadvog_face_older_2],

  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_guhulay_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_guhulay_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_4|knows_power_draw_3,guhulay_face_young_1, guhulay_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_guhulay_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_borovod_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_3,borovod_face_young_1, borovod_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_jarid,itm_jarid,itm_afirid_cloth_robe, itm_afirid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_throw_3,guhulay_face_young_1, guhulay_face_old_2],
  #-----------The Order--------------
["order_priest","Doomcall Priest","Doomcall priests",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_knights_of_doomcall,
   [itm_black_greaves,itm_doomcall_coat_of_plates,itm_order_winged_helmet,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b],
   #[],
   def_attrib|level(30),wp(200),knows_ironflesh_3|knows_power_strike_3,bandit_face1, bandit_face2],
["order_knight","Doomcall Faith Guard","Doomcall Faith Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_knights_of_doomcall,
  # [itm_black_greaves,itm_coat_of_plates,itm_castillan_helm,itm_order_sword_1,itm_steel_shield_heater,itm_courser_black,itm_light_lance],
    [itm_black_greaves,itm_order_surcoat_over_mail,itm_castillan_helm,itm_sword_medieval_d_long,itm_bw_horseman_shield,itm_courser_black,itm_light_lance],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) ,knows_common|knows_riding_5| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
 ["order_follower","Doomcall Follower","Doomcall Followers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_knights_of_doomcall,
   [itm_leather_gloves,itm_black_tabard,itm_leather_boots,itm_doomcall_cap,
   itm_tab_shield_kite_cav_b,itm_lobarian_spear_c,itm_lobarian_spear_b,itm_lobarian_spear_a],
   def_attrib|level(16),wp(100),knows_ironflesh_3,bandit_face1, bandit_face2],
	#---------------------------------
  #-----------The white Order--------------
["order_billman","Order Billman","Order Billmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_the_new_order,
    [itm_splinted_leather_greaves,itm_new_order_plate,itm_hounskull,itm_gauntlets,itm_luc_english_bill],
   def_attrib|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) ,knows_common|knows_riding_5| knows_ironflesh_5|knows_power_strike_3,pravar_face_middle_1, pravar_face_older_2],
 ["order_gunner","Order canoner","Order Canoners",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_the_new_order,
   [itm_new_order_brigandine,itm_conic_helm,itm_military_cleaver_b,itm_leather_boots_black,itm_hand_canon,itm_cartridges],
   def_attrib|level(22),wp(120)| wp_firearm (100),knows_ironflesh_2,bandit_face1, bandit_face2],
	#---------------------------------



  ["black_guhulay_horseman","Black Guhulay Horseman","Black Guhulay Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_guhulays,
   [itm_arrows,itm_sword_guhulay_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_guhulay_bow,itm_guhulay_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_guhulay_war_helmet,itm_guhulay_war_helmet,itm_mail_hauberk,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,guhulay_face_young_1, guhulay_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_pravar_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_hadvog_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#--pretenders troops
  ["galnar_warrior","Galnar Warrior","Galnar Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_wooden_shield_1,itm_shortened_spear,
    itm_hadvog_helmet,itm_norman_short_hauberk_blue,itm_hunter_boots],
   def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_2|knows_power_throw_3|knows_athletics_4 ,hadvog_face_young_1, hadvog_face_older_2],
 ["galnar_ship_captain","Galnar Ship Captain","Galnar Ship Captain",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_wooden_shield_2,itm_throwing_axes,
    itm_hadvog_warlord_helmet,itm_norman_hauberk_a,itm_splinted_leather_greaves,itm_splinted_greaves_spurs,itm_leather_gloves],
   def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_2|knows_power_throw_3|knows_athletics_5 ,hadvog_face_young_1, hadvog_face_older_2],
#--

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_hadvog_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_hadvog_shield,itm_leather_boots,itm_leather_gloves,itm_guhulay_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_chapel_de_fer_mail2,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_1,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_2,bandit_face1, bandit_face2],

#Imifir tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [],
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [],
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_guhulays,
#   [],
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,guhulay_face1, guhulay_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [],
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [],
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_hadvog_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_hadvog_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_1|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_guhulay_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_crossbow,itm_plate_armor,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_1|knows_riding_5|knows_athletics_3|knows_ironflesh_2 ,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],


  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["guhulay_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_afirid_felt_hat,itm_turban,itm_wrapping_boots,itm_guhulay_leather_boots,itm_afirid_cloth_robe, itm_afirid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,pravar_face_younger_1, pravar_face_middle_2],
 ["guhulay_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["afirid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_afirid_felt_hat,itm_turban,itm_wrapping_boots,itm_afirid_boots_a,itm_sar_pants,itm_afirid_cloth_robe, itm_afirid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,afirid_face_younger_1, afirid_face_middle_2],
 ["afirid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_afirid_common_dress, itm_afirid_common_dress_b,itm_woolen_hose,itm_afirid_boots_a, itm_afirid_felt_head_cloth, itm_afirid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Jana","Jana","Jana",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_short_coat_of_plates_b,itm_splinted_leather_greaves,itm_mail_mittens,itm_bascinet,itm_spiked_mace,itm_steel_buckler2,itm_courser],def_attrib|str_15|agi_15|level(39),wp(300),knows_power_strike_4|knows_ironflesh_5|knows_riding_8|knows_power_draw_4|knows_athletics_5 ,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Notnad","Notnad","Notnad",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_banded_armor,itm_leather_boots,itm_leather_gloves,itm_gnezdovo_helm_b,itm_afirid_medium_spear,itm_tab_shield_kite_d,itm_bronze_mace],def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Sudarka","Sudarka","Sudarka",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_plate_harness_02,itm_plate_boots,itm_plate_mittens,itm_great_bascinet_1,itm_bastard_sword_b,itm_tab_shield_kite_cav_b,itm_charger,itm_colored_lance_e],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],

  ["Norha","Norha","Norha",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_lobarian_bascinet_visor,itm_scale_armor,itm_splinted_leather_greaves,itm_leather_boots,itm_iron_staff],def_attrib|str_15|agi_15|level(39),wp(350),knows_power_strike_6|knows_ironflesh_4|knows_riding_6|knows_power_draw_4|knows_athletics_10 ,0x00000008740c2007492a84bbadb0fdfc00000000001ca54b0000000000000000],

  ["Zarkuch","Zarkuch","Zarkuch",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_sar_haubergeon,itm_rus_cav_boots,itm_afirid_face_helm_n_2,itm_warhorse_afirid,itm_scimitar_b,itm_tab_shield_kite_b,itm_heavy_lance],def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_4|knows_ironflesh_4|knows_riding_7|knows_power_draw_4|knows_athletics_8 ,0x0000000aae08e0007d2491b6dbf1effb00000000001db5a80000000000000000],

  ["Majrim","Majrim","Majrim",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_full_helm,itm_plate_armor,itm_plate_boots,itm_plate_mittens,itm_great_long_bardiche,itm_throwing_axes],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_2 ,0x0000000c8a0812927d2491b6dbd1effb00000000001db5a80000000000000000],

  ["Felina","Felina","Felina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_darenbay_armor,itm_mail_boots,itm_mail_mittens,itm_barbuta1,itm_rouncy,itm_lance,itm_sword_medieval_d_long,itm_steel_shield],def_attrib|str_15|agi_15|level(39),wp(250),knows_power_strike_4|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8 ,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],

  ["Pipo","Pipo","Pipo",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_luc_ball_mace_one_handed,itm_stones,itm_leather_gloves,itm_haubergeon,itm_mail_boots,itm_bascinet,itm_plate_covered_round_shield],def_attrib|str_15|agi_14|level(42),wp(320),knows_power_strike_3|knows_ironflesh_5|knows_riding_4|knows_power_draw_4|knows_power_throw_10|knows_athletics_9 ,0x000000024b0d25d148d1d9951489c25b00000000001eeb620000000000000000],

  ["Dinma","Dinma","Dinma",tf_hero|tf_female, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_borovod_noble_helmet,itm_rus_lamellar_a,itm_rus_cav_boots,itm_wisby_gauntlets_black,itm_sword_guhulay_4,itm_bardiche,itm_tab_shield_heater_cav_b,itm_winged_mace_2,itm_hunter],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x0000000cb304000328a38aa51b6e451b00000000001d990a0000000000000000],

  ["Prince_Figar","Prince Figar","Prince Figar",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_gothic_armour,itm_steel_greaves,itm_visored_sallet_coif,itm_wisby_gauntlets_black,itm_sword_two_handed_a],def_attrib|str_15|agi_8|level(42),wp(280),knows_power_strike_4|knows_ironflesh_6|knows_riding_4|knows_power_draw_4|knows_athletics_1 ,0x0000000793043502481d3d96dbb6549b00000000001d64d40000000000000000],
  ["Halof","Halof","Halof",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_norman_faceplate_a,itm_nord_coat_of_plates,itm_plate_boots,itm_warhammer],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000005200c23007e3b75b6dbfe0ff800000000001db9180000000000000000],
  ["Musdur","Musdur","Musdur",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_corrazina_red,itm_open_sallet_coif,itm_mail_chausses,itm_atian_longsword,itm_bw_knight_shield,itm_mail_mittens,itm_destrier],def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x0000000a350d21842d6fa9f6a779c6b200000000001dd71c0000000000000000],
  ["Ydir_Red_Eye","Ydir_Red_Eye","Ydir_Red_Eye",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_guhulay_noyan_armor,itm_afirid_boots_c,itm_guhulay_helmet_g,itm_guhulay_sword_two_handed_b,itm_jarid],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_throw_4|knows_athletics_4 ,0x0000000a2e00b14359aca9e25965b75200000000001c39a90000000000000000],
  ["Turaq","Turaq","Turaq",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_arabian_mail_shirt_b,itm_afirid_helmet_inf_3,itm_leather_boots,itm_lamellar_gauntlets,itm_sword_guhulay_4,itm_tab_shield_kite_c,itm_light_lance,itm_arabian_horse_b],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000006a71135803f236db6dbf2df7c00000000001db6f30000000000000000],
  ["Sebutai","Sebutai","Sebutai",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_guhulay_elite_helm,itm_guhulay_mirza_armor,itm_guhulay_cav_boots,itm_leather_gloves,itm_steppe_char_iron,itm_horn_bow,itm_guhulay_poisoned_arrows,itm_desert_scimitar],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_3|knows_ironflesh_5|knows_riding_8|knows_power_draw_6|knows_athletics_8 |knows_horse_archery_7,0x00000006a710910d36db6db6db6db6db00000000001db6db0000000000000000],
  ["Acheron","Acheron","Acheron",tf_hero, scn_the_happy_boar|entry(5),reserved,  fac_commoners,  [itm_brigandine_grey_mail,itm_splinted_leather_greaves,itm_mail_mittens,itm_bascinet,itm_dirim_cav_sword,itm_steel_shield,itm_courser],
  def_attrib|str_15|agi_15|level(39),wp(300),knows_power_strike_4|knows_ironflesh_5|knows_riding_8|knows_power_draw_4|knows_athletics_5 ,0x00000001840824c368544b58e275c56400000000001238db0000000000000000],
  ["Andraz","Andraz","Andraz",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,
  [itm_guhulay_mail_c,itm_leather_boots,itm_leather_gloves,itm_gnezdovo_helm_b,itm_heavy_halberd,itm_tab_shield_kite_d,itm_luc_scramasax],
  def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000001b205429952e5ae976368cc5700000000001d36e20000000000000000],
  ["Selcur","Selcur","Selcur",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_milanese_armour,itm_plate_boots,itm_plate_mittens,itm_great_bascinet_1,itm_tab_shield_kite_cav_b,itm_charger,itm_luc_hammer_spike],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000001940402ce54b9cd68c271cb1900000000001cb5190000000000000000],
  ["Rector","Rector","Rector",tf_hero, scn_the_happy_boar|entry(5),reserved,  fac_commoners,
  [itm_zitta_bascinet,itm_plate_harness_02,itm_splinted_leather_greaves,itm_leather_boots,itm_flamberge],
  def_attrib|str_15|agi_15|level(39),wp(350),knows_power_strike_6|knows_ironflesh_4|knows_riding_6|knows_power_draw_4|knows_athletics_10 ,0x00000001b91115425d1cb5c75d5bb71d00000000000edb180000000000000000],

  ["Och","Och","Och",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,
  [itm_guhulay_lamellar_armor_b,itm_rus_cav_boots,itm_oniontop_bascinet,itm_warhorse_afirid,itm_scimitar_b,itm_tab_shield_kite_b,itm_heavy_lance],
  def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_4|knows_ironflesh_4|knows_riding_7|knows_power_draw_4|knows_athletics_8 ,0x000000018100c2403b2671e4a0a94d6100000000001e3adb0000000000000000],

  ["Sonaf","Sonaf","Sonaf",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_full_helm,itm_heraldic_jarl_armor,itm_plate_boots,itm_plate_mittens,itm_shortened_voulge,itm_throwing_axes],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_2 ,0x00000001b3005251332bcd58a28e293400000000001de4d30000000000000000],

  ["Leto","Leto","Leto",tf_hero, scn_the_happy_boar|entry(5),reserved,  fac_commoners,
  [itm_dirim_breastplate,itm_iron_greaves,itm_mail_mittens,itm_barbuta1,itm_charger,itm_lance,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b],
  def_attrib|str_15|agi_15|level(39),wp(250),knows_power_strike_4|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8 ,0x000000018611358d1b1e75389cb9252600000000001e1ad40000000000000000],

  ["Sotan","Sotan","Sotan",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,
  [itm_winged_mace_1,itm_jarid,itm_leather_gloves,itm_coat_of_plates_blue,itm_mail_boots,itm_bascinet,itm_plate_covered_round_shield],
  def_attrib|str_15|agi_14|level(42),wp(320),knows_power_strike_3|knows_ironflesh_5|knows_riding_4|knows_power_draw_4|knows_power_throw_10|knows_athletics_9 ,0x00000001840015805984a7269b3ba44600000000001e16520000000000000000],

  ["Asudem","Asudem","Asudem",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_borovod_noble_helmet,itm_churburg_13_mail,itm_rus_cav_boots,itm_wisby_gauntlets_black,itm_sword_guhulay_4,itm_tab_shield_heater_cav_b,itm_winged_mace_2,itm_hunter],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x000000018d10154a5922b4355b8e2b1100000000001ed6610000000000000000],

  ["Noroc","Noric","Noric",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,
  [itm_chieftain_armour,itm_steel_greaves,itm_visored_sallet_coif,itm_wisby_gauntlets_black,itm_great_sword],
  def_attrib|str_15|agi_8|level(42),wp(280),knows_power_strike_4|knows_ironflesh_6|knows_riding_4|knows_power_draw_4|knows_athletics_1 ,0x000000018a00a501347568a9296a5d0b000000000018c2ab0000000000000000],

  ["Cronus","Cronus","Cronus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_dirim_bowman_helmet,itm_pretorian_armor,itm_plate_boots,itm_dirim_pilum,itm_steel_shield,itm_bronze_spiked_mace_5p],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000001a50c90100b1cab591baadb2d00000000000e3a9c0000000000000000],

  ["Darko","Darko","Darko",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,
  [itm_coat_of_plates,itm_open_sallet_coif,itm_mail_chausses,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_mail_mittens,itm_destrier],
  def_attrib|str_15|agi_14|level(42),wp(280),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x00000001b3004310389a9195296acb5100000000001f19290000000000000000],

  ["Goran","Goran","Goran",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_early_transitional_white,itm_guhulay_helmet_i,itm_afirid_boots_c,itm_luc_knightly_axe_v2],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_throw_4|knows_athletics_4 ,0x000000018f087151325c54d4b539d8fe00000000001b26a30000000000000000],

  ["Casimir","Casomir","Casomir",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_unicorne_armor,itm_nikolskoe_helm,itm_leather_boots,itm_lamellar_gauntlets,itm_sword_guhulay_4,itm_tab_shield_heater_c,itm_light_lance,itm_arabian_horse_b],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_4|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4 ,0x000000018500d1d04915b53b1db257ca00000000001136710000000000000000],

  ["Borvuk","Borvuk","Borvuk",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,
  [itm_milanese_sallet,itm_milanese_armour,itm_guhulay_cav_boots,itm_leather_gloves,itm_mail_armor_horse,itm_luc_horseman_pick,itm_tab_shield_kite_c],
  def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_3|knows_ironflesh_5|knows_riding_8|knows_power_draw_6|knows_athletics_8 |knows_horse_archery_7,0x000000019b0ce5d4479492c71ad22524000000000016355c0000000000000000],

#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, pravar_face_young_1, pravar_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, pravar_face_young_1, pravar_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, pravar_face_young_1, pravar_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, pravar_face_young_1, pravar_face_old_2],

#Burfell
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_11","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, scn_free_port_center|entry(7), reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face,0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership,
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade,
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra

#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Charob","Charob",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_shirt],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,
   0x000000019808314438caf6629a8ceb2c00000000001dd2a30000000000000000],
  ["npc2","Rijat","Rijat", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Tofara","Tofara",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x00000001e10c10060000a2a566e3fff300000000001f84000000000000000000],
  ["npc4","Ymir","Ymir",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],

  #--Comrade Crimson
  ["npc5","Azhar","Azhar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_steppe_horse_1,itm_south_armor_c,itm_nomad_boots, itm_sword_guhulay_1,itm_guhulay_bow,itm_bodkin_arrows],
   str_12|agi_10|int_12|cha_7|level(20),wp(150),knows_warrior_npc|
   knows_riding_4|knows_horse_archery_4|knows_power_draw_3|knows_leadership_3|knows_weapon_master_3,
   0x0000000eff0071cd56e5a2dde455470900000000001c26f00000000000000000],
   ["npc6","Stavik","Stavik",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_padded,itm_nomad_boots, itm_sword_guhulay_3],
   str_10|agi_8|int_7|cha_8|level(2),wp(100),knows_merchant_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000018808144428a58f46d38ec70500000000001ec6a60000000000000000],
   ["npc7","Marina","Marina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_brigandine_leg,itm_leather_boots,itm_awlpike,itm_falchion],
   str_8|agi_11|int_10|cha_10|level(8),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x00000008790c000d552bb6eb2569c52c00000000001d386d0000000000000000],
  ["npc8","Vultuire","Vultuire",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_wrapping_boots, itm_long_war_club],
   str_12|agi_10|int_12|cha_7|level(20),wp(150),knows_warrior_npc|
   knows_riding_4|knows_horse_archery_4|knows_power_draw_3|knows_leadership_3|knows_weapon_master_3,
   0x0000000b9c091000499ad0a732ba0fb800000000001ea5640000000000000000],

  ["npc9","Olaf","Olaf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_galnar_hauberk,itm_large_hadvog_shield,itm_galnar_chief_axe,itm_splinted_leather_greaves],
   str_12|agi_8|int_12|cha_7|level(20),wp(140),knows_warrior_npc|
   knows_riding_1|knows_leadership_2|knows_weapon_master_4,
   0x00000009b00913477f9fbfed2fb1aeb800000000001fb4600000000000000000],
  ["npc10","Ignatius","Ignatius",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_unicorne_armor,itm_sword_medieval_c_long, itm_tab_shield_heater_cav_b,itm_toh_shynbaulds],
   str_12|agi_10|int_12|cha_7|level(20),wp(140),knows_warrior_npc|
   knows_riding_4|knows_leadership_4|knows_weapon_master_4,
   0x0000000ddc0104462f2392389bcd1fea00000000001d56fa0000000000000000],
  ["npc11","Makkara","Makkara",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_afirid_pants,itm_southern_axe,itm_afirid_boots_a,itm_arabian_horse_a],
   str_6|agi_10|int_10|cha_8|level(4),wp(80),knows_tracker_npc|
   knows_riding_3|knows_leadership_1|knows_weapon_master_2,
   0x000000039a00d143346676ab9c6db29700000000001fb7240000000000000000],
   ["npc12","Sayyid","Sayyid",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_southern_lamellar,itm_saracen_helmet_f,itm_afirid_boots_b,itm_guhulay_sword_two_handed_a,itm_javelin], str_10|agi_10|int_9|cha_8|level(12),wp(100),knows_warrior_npc| knows_riding_1|knows_leadership_1|knows_weapon_master_4,
   0x00000007a90ca34473e48b4ff2cedeb800000000001f83210000000000000000],

   ["npc13","Yuewei","Yuewei",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tunic_lamellar,itm_guhulay_cav_boots,itm_wyu_ring_sword,itm_wyu_light_crossbow,itm_bolts],
   str_10|agi_10|int_9|cha_8|level(12),wp(100),knows_warrior_npc|
   knows_leadership_1|knows_weapon_master_4,
   0x000000077b0c838a492991d64db1d96400000000001d35ae0000000000000000],

   ["npc14","Zhurina","Zhurina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_fur_vest,itm_nomad_boots,itm_hunting_bow,itm_arrows,itm_knife],
   str_9|agi_10|int_10|cha_3|level(8),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000f270020032e846275e552292400000000001edb1d0000000000000000],
  #--



#  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a],
#   str_10|agi_12|int_10|cha_5|level(6),wp(105),knows_warrior_npc|
#   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
#  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
#  #["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows],
   #str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   #knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   #0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
#  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
#   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
#   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
#   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
#  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small],
#   str_11|agi_8|int_7|cha_8|level(2),wp(100),knows_warrior_npc|
#   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
#   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
#  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe],
#   str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|
#   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
#   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
#  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots],
#   str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
#   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
#   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
#  #---------------armurier(jeremus)--------------
#  ["npc12","Fuhlanirus","Fuhlanirus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[ itm_leather_apron,itm_nomad_boots],
#   str_10|agi_7|int_12|cha_3|level(7),wp(100),   knows_merchant_npc|
#   knows_ironflesh_4|knows_power_strike_2,
#   0x00000009f00911802add2e4aca22372100000000001d67490000000000000000],
  #------------------------------------------------
#  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
#   str_7|agi_7|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
#   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
#   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
#  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
#   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
#   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
#   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  #---------------ingenieur (artim)--------------
  ["npc15","Moktarus","Moktarus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_merchant_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x00000004400922812add2e4aca22372100000000001d67490000000000000000],
  #-------------------------------------
 ["npc16","Antonius","Antonius",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Wigberht",  "Wigberht",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_pravar_plated_barded_horse,   itm_noble_doublet_cloack,        itm_blue_hose,                  itm_plate_boots,               itm_red_lion_armor, itm_gauntlets,    itm_morningstar_2,      itm_tab_shield_heater_cav_b,       itm_pravar_crown],
  knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5, 0x0000000cd400358f572475b6e4dffdb600000000001f355b0000000000000000,pravar_face_older_2],
  ["kingdom_2_lord",  "Prince Burelek",  "Burelek",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_mail_armor_horse,    itm_borov_noble_outfit_cloak,      itm_leather_boots,              itm_plate_boots,              itm_platemail_harness_05, itm_gauntlets,      itm_bardiche,      itm_tab_shield_kite_cav_b,      itm_litchina_helm],
  knight_attrib_5,wp(320),knight_skills_5|knows_trainer_4, 0x0000000c280112863edb95b6db6dbcdb00000000001f85bb0000000000000000, borovod_face_old_2],
  ["kingdom_3_lord",  "Janakir Khan",  "Janakir",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_steppe_char_iron,   itm_guhulay_vest_c,             itm_leather_boots,              itm_splinted_greaves,           itm_khan_armor,  itm_lamellar_gauntlets,       itm_sword_guhulay_3,              itm_tab_shield_small_round_c,       itm_guhulay_khan_mask],
  knight_attrib_5,wp(350),knight_skills_5|knows_trainer_6, 0x0000000d640091ca46dc8db1dbadb6a800000000001db6e40000000000000000,guhulay_face_old_2],
  ["kingdom_4_lord",  "King Viskhard",  "Viskhard",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_nord_plated_warhorse,    itm_nobleman_outfit,    itm_leather_boots,              itm_mail_boots,                 itm_plate_armor,  itm_gauntlets,    itm_great_axe,           itm_tab_shield_round_e,    itm_hadvog_king_helm],
  knight_attrib_5,wp(350),knight_skills_5|knows_trainer_4, 0x0000000c170003075dfdb64925b32e3a00000000001f37a20000000000000000, hadvog_face_older_2],
  ["kingdom_5_lord",  "Duke Montagu",  "Montagu",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_plated_charger_6,  itm_imifir_rich_jacket_2,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_imifir_ducal_armor,  itm_gauntlets,         itm_sword_of_war,         itm_steel_shield,        itm_duc_sallet],
  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_5, 0x0000000d3f0903c653246cb89bb0aa2300000000001f325b0000000000000000, imifir_face_old_2],
  ["kingdom_6_lord",  "Sultan Ayzar",  "Ayzar",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_afirid_noble_caftan_cloak, itm_warhorse_afirid,     itm_sultan_armor,          itm_afirid_boots_c,   itm_sultan_helm,  itm_mail_mittens,      itm_luc_zulfiqar,    itm_tab_shield_small_round_c],
  knight_attrib_4,wp(280),knight_skills_5|knows_trainer_5, 0x0000000d9c00a2c034dba2385c7d515100000000001db71b0000000000000000, afirid_face_old_2],
	#--------------------
  ["kingdom_7_lord",  "Empress Birinda",  "Birinda",  tf_hero|tf_female, 0,reserved,  fac_kingdom_7,[itm_hunter,   itm_empress_dress,        itm_leather_boots,                  itm_iron_greaves,               itm_empress_plate, itm_wisby_gauntlets_black,    itm_dirim_infantry_mace, itm_tab_shield_heater_cav_b, itm_lioness_helm],
  knight_attrib_5,wp(300),knight_skills_5|knows_trainer_5, 0x00000001c50c3002411c6c4924f3773700000000001fff1c0000000000000000,pravar_face_young_2],
  #------------------------
	#--------------------
  ["kingdom_8_lord",  "Governor Jame Bodlos",  "Jame Bodlos",  tf_hero, 0,reserved,  fac_kingdom_8,
  [itm_plated_charger_6,   itm_baretunic_blue,        itm_black_boots,                  itm_plate_boots,               itm_company_armor, itm_gauntlets,    itm_atian_longsword,      itm_steel_buckler1,       itm_company_helm,itm_flintlock_pistol_1, itm_cartridges],
  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_5, 0x00000005bd082508059aa9bd176da51400000000001d4b510000000000000000,pravar_face_young_2],
  #------------------------

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina
# Dunga        Agatha     Dibus Crahask

#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Pravar civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Charibert", "Charibert", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_warhorse,      itm_noble_doublet,      itm_gothic_armour,   itm_nomad_boots, itm_splinted_greaves,       itm_visored_sallet,           itm_sword_medieval_c,  itm_scale_gauntlets,         itm_tab_shield_heater_cav_a],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000cb80814813d1a6ce4a595551100000000001ce2dc0000000000000000, pravar_face_older_2],
  ["knight_1_2", "Count Dagaric", "Dagaric", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_barded_horse,           itm_red_gambeson,      itm_gothic_armour,               itm_nomad_boots,            itm_iron_greaves,                    itm_hounskull,  itm_gauntlets,        itm_bastard_sword_a,    itm_tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x000000047f010194372585b70ea9a50c00000000001e52ea0000000000000000, pravar_face_young_2],
  ["knight_1_3", "Count Hermangild", "Hermangild", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,          itm_noble_doublet,     itm_plate_harness_02,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_b,   itm_tab_shield_heater_d],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x00000007770802c6375d8de7562b671c00000000001dc2a90000000000000000, pravar_face_young_2],
  ["knight_1_4", "Count Carloman", "Carloman", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_barded_horse,      itm_pravar_doublet,       itm_gothic_armour,           itm_leather_boots,          itm_mail_chausses,                   itm_visored_sallet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000d820113946ca564d2a251ed6c00000000001f4ae40000000000000000, pravar_face_older_2],
  ["knight_1_5", "Count Burdan", "Burdan", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_barded_horse,            itm_rich_outfit,        itm_gothic_armour,itm_woolen_hose, itm_mail_chausses, itm_visored_sallet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000d5d0c60d2339b4d9d9db13aac00000000000ed5280000000000000000, pravar_face_older_2],
  ["knight_1_6", "Count Theuderic", "Theuderic", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_warhorse,            itm_pravar_doublet_cloack,      itm_gothic_armour,               itm_leather_boots,          itm_mail_boots,                      itm_visored_sallet, itm_gauntlets, itm_morningstar_no1, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000d5d10c0c2592a8aa94b4a64ea00000000001c61db0000000000000000, pravar_face_older_2],
  ["knight_1_7", "Count Gundobad", "Grainwad", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_warhorse,            itm_noble_doublet,      itm_plate_harness_02,               itm_leather_boots,          itm_mail_boots,                      itm_great_helm_1, itm_gauntlets, itm_bastard_sword_b,   itm_sword_two_handed_b, itm_tab_shield_heater_cav_b], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x000000010b10c14f165b70c58b73956b00000000001dc65a0000000000000000, pravar_face_young_2],
  ["knight_1_8", "Count Rathar", "Rathar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,          itm_nobleman_outfit,     itm_plate_harness_02,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_winged_great_helmet,  itm_gauntlets,itm_morningstar_no1,  itm_sword_two_handed_a, itm_tab_shield_heater_d],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000d400835024b5372330c95d6db00000000001f245c0000000000000000, pravar_face_older_2],


#Pravar younger knights
  ["knight_1_9", "Count Brantley", "Brantley", tf_hero, 0, reserved,  fac_kingdom_1, [itm_pravar_plated_warhorse,      itm_gambeson,     itm_heraldic_gothic_armor,                 itm_blue_hose,              itm_mail_boots,                      itm_visored_sallet_coif,  itm_scale_gauntlets,     itm_knights_war_axe_1h,   itm_tab_shield_heater_c],    knight_attrib_3,wp(160),knight_skills_3, 0x00000002a90422c858ab2a3763b62ab400000000001d3b1a0000000000000000, pravar_face_old_2],
  ["knight_1_10", "Count Magneric", "Magneric", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,           itm_blue_gambeson,        itm_heraldic_gothic_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_visored_sallet,    itm_gauntlets,    itm_knights_winged_mace_1h,        itm_tab_shield_heater_cav_b],   knight_attrib_3,wp(190),knight_skills_3, 0x00000003d110201462d368b6e4c9d91e00000000001f5b0b0000000000000000, pravar_face_older_2],
  ["knight_1_11", "Count Sichar", "Sichar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_red_gambeson,      itm_heraldic_gothic_armor,               itm_nomad_boots,            itm_iron_greaves,                    itm_visored_sallet,   itm_gauntlets,       itm_morningstar_2,    itm_tab_shield_heater_cav_b],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000d3211008238e9b5a2698ec6e400000000001e192a0000000000000000, pravar_face_older_2],
  ["knight_1_12", "Count Meginhard", "Meginhard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_rich_outfit,        itm_heraldic_gothic_armor,                    itm_nomad_boots,            itm_mail_boots,                      itm_visored_sallet,   itm_gauntlets,         itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000a94004052673c51a7162e693600000000001ea6960000000000000000, pravar_face_older_2],
  ["knight_1_13", "Count Burchard", "Burchard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_pravar_doublet_cloack,      itm_heraldic_gothic_armor,           itm_nomad_boots,            itm_splinted_greaves,                itm_visored_sallet,   itm_gauntlets,         itm_horsemans_axe_no3,  itm_sword_two_handed_a,     itm_tab_shield_heater_c],   knight_attrib_2,wp(160),knight_skills_2, 0x000000074204c241396a97488db2397500000000001e12e40000000000000000, pravar_face_older_2],
  ["knight_1_14", "Count Bradburn", "Bradburn", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_noble_doublet,       itm_heraldic_gothic_armor,           itm_leather_boots,          itm_mail_chausses,                   itm_visored_sallet,  itm_scale_gauntlets,     itm_morningstar_2,    itm_tab_shield_heater_cav_a],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x000000075d0425cf2461c924dbadc66a00000000001d52760000000000000000, pravar_face_older_2],
  ["knight_1_15", "Count Averey", "Averey", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_pravar_doublet,        itm_gothic_armour,                   itm_woolen_hose,            itm_mail_chausses,                   itm_visored_sallet,   itm_gauntlets,       itm_sword_viking_3, itm_sword_two_handed_a,  itm_tab_shield_heater_d],      knight_attrib_4,wp(140),knight_skills_2, 0x000000076608200645a476056a52491c00000000001da6ad0000000000000000, pravar_face_young_2],
  ["knight_1_16", "Count Eberulf", "Eberulf", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_courtly_outfit,      itm_heraldic_gothic_armor,                     itm_nomad_boots,            itm_splinted_greaves,                itm_visored_sallet,   itm_gauntlets,         itm_sword_medieval_c,           itm_tab_shield_heater_c],   knight_attrib_1,wp(130),knight_skills_2, 0x000000076c0113c36afcad35a4523b5c00000000001d666b0000000000000000, pravar_face_young_2],
  ["knight_1_17", "Count Ranulf", "Ranulf", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_gambeson,     itm_heraldic_gothic_armor,                 itm_blue_hose,              itm_mail_boots,                      itm_visored_sallet,   itm_scale_gauntlets,    itm_fighting_pick,   itm_tab_shield_heater_cav_b],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x00000002f20400c658b249289e352d2000000000001e43630000000000000000, pravar_face_young_2],
  ["knight_1_18", "Count Terric", "Terric", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_blue_gambeson,        itm_heraldic_gothic_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_visored_sallet,   itm_gauntlets,     itm_arming_winged_mace,        itm_tab_shield_heater_cav_a],   knight_attrib_3,wp(210),knight_skills_1, 0x00000002f101108f26d0b08ab5aa589900000000001ed6ab0000000000000000, pravar_face_young_2],
  ["knight_1_19", "Count Blakely", "Blakely", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_rich_outfit,        itm_heraldic_gothic_armor,                    itm_nomad_boots,            itm_mail_boots,                      itm_visored_sallet, itm_gauntlets,           itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_heater_cav_a],    knight_attrib_1,wp(120),knight_skills_1, 0x00000002e8111143531467555ee9d51500000000001656d90000000000000000, pravar_face_young_2],
  ["knight_1_20", "Count Munderic", "Munderic", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,      itm_noble_doublet,      itm_heraldic_gothic_armor,           itm_nomad_boots,            itm_splinted_greaves,                itm_visored_sallet, itm_gauntlets,           itm_arming_winged_mace,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_1, 0x00000002f611101458da92d09a8ea8d400000000001d3d0b0000000000000000, pravar_face_young_2],




#  ["knight_1_21", "Lord Pravar 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, pravar_face_young_2],
 # ["knight_1_22", "Lord Pravar 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, pravar_face_older_2],
#  ["knight_1_23", "Lord Pravar 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, pravar_face_older_2],
#  ["knight_1_24", "Lord Pravar 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, pravar_face_older_2],



  ["knight_2_1", "Boyar Demomir", "Dedomir", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,      itm_borov_noble_outfit,     itm_borovod_lamellar_armor,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_nikolskoe_helm,    itm_mail_mittens,       itm_sword_viking_3,           itm_tab_shield_kite_c],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000b481001504aa3a9cc6350dca600000000001f16a30000000000000000, borovod_face_middle_2],
  ["knight_2_2", "Boyar Boric", "Noric", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_rich_outfit,        itm_knyaz_armor,               itm_woolen_hose,            itm_mail_chausses,                   itm_nikolskoe_helm,  itm_mail_mittens,      itm_shortened_military_scythe,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000b410832823b2592c51b88b89b000000000015db240000000000000000, borovod_face_old_2],
  ["knight_2_3", "Boyar Domagoj", "Domagoj", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,            itm_borov_noble_outfit,        itm_rus_scale,                   itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_lamellar_helmet, itm_lamellar_gauntlets,           itm_great_bardiche,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x00000005090d01443a5d6d2499cea92c00000000001ea91b0000000000000000, borovod_face_older_2],
  ["knight_2_4", "Boyar Kulin", "Kulin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_courtly_outfit,     itm_knyaz_armor,               itm_leather_boots,          itm_mail_boots,                      itm_borovod_noble_helmet, itm_lamellar_gauntlets,         itm_bastard_sword_b,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4, 0x00000005040c35505ca2d4073691cb2300000000001daa5d0000000000000000, borovod_face_older_2],
  ["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,            itm_rich_outfit,        itm_knyaz_kuyak_2,                     itm_leather_boots,          itm_mail_chausses,                   itm_nikolskoe_helm, itm_scale_gauntlets,   itm_bastard_sword_b,   itm_tab_shield_kite_d],       knight_attrib_5,wp(250),knight_skills_5, 0x00000005200910924cf26ee79c72ad2500000000001db2e40000000000000000, borovod_face_older_2],
  ["knight_2_6", "Boyar Lovro", "Lovro", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_borov_noble_outfit,      itm_knyaz_kuyak_1,                   itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_lamellar_helmet,  itm_mail_mittens,          itm_sword_viking_3,           itm_tab_shield_kite_c],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000500080507465a99e49a11bb6400000000001db8a10000000000000000, borovod_face_middle_2],
  ["knight_2_7", "Boyar Rucha", "Rucha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_borov_noble_outfit_cloak,     itm_knyaz_kuyak,                   itm_leather_boots,          itm_mail_boots,                      itm_nikolskoe_helm,  itm_lamellar_gauntlets,          itm_great_bardiche,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000005200c319046a191ab216a5b950000000000051a1b0000000000000000, borovod_face_old_2],
  ["knight_2_8", "Boyar Stepan", "Stepan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,            itm_borov_noble_outfit,             itm_rus_scale,                     itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_noble_helmet, itm_lamellar_gauntlets,       itm_shortened_military_scythe,    itm_tab_shield_kite_d],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x00000009ff0103815b1a49a4b3693f1b00000000001d47510000000000000000, borovod_face_older_2],
  ["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rus_horse,      itm_rich_outfit,        itm_boyar_armor,                     itm_leather_boots,          itm_mail_chausses,                   itm_borovod_lamellar_helmet,  itm_lamellar_gauntlets,        itm_great_bardiche,   itm_tab_shield_kite_d],    knight_attrib_4,wp(230),knight_skills_4, 0x00000009c005125918d994c33231c4cb00000000001ed71c0000000000000000, borovod_face_older_2],
  ["knight_2_10", "Boyar Mladen", "Mladen", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,          itm_borov_noble_outfit_cloak,        itm_boyar_armor,               itm_woolen_hose,            itm_mail_boots,                      itm_borovod_noble_helmet,  itm_scale_gauntlets,      itm_military_pick,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x00000005ce11100a551185d89a51dc8a00000000001c32d30000000000000000, borovod_face_older_2],
  ["knight_2_11", "Boyar Frankopan", "Frankopan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_borov_noble_outfit_cloak,     itm_rus_scale,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_nikolskoe_helm, itm_scale_gauntlets,           itm_sword_viking_3,           itm_tab_shield_kite_cav_a],    knight_attrib_1,wp(130),knight_skills_1, 0x00000005e410144526b24566ec5ae6cb00000000001c48a50000000000000000, borovod_face_middle_2],
  ["knight_2_12", "Boyar Petar", "Petar", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rus_horse,      itm_rich_outfit,        itm_knyaz_kuyak,               itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_noble_helmet,  itm_mail_mittens,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(170),knight_skills_2, 0x00000005c10005c61ae46ec54b96386200000000001e39ab0000000000000000, borovod_face_old_2],
  ["knight_2_13", "Boyar Ivanus", "Ivanus", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,            itm_borov_noble_outfit,        itm_boyar_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_lamellar_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x00000005fc0c0489689a897b146a391000000000001c171c0000000000000000, borovod_face_older_2],
  ["knight_2_14", "Boyar Vinomir", "Vinomir", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_courtly_outfit,     itm_rus_lamellar_a,               itm_leather_boots,          itm_mail_boots,                      itm_nikolskoe_helm,  itm_lamellar_gauntlets,        itm_shortened_military_scythe,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000005c40003c6371c7a32ce4dca65000000000005b2da0000000000000000, borovod_face_older_2],
  ["knight_2_15", "Boyar Tipimir", "Tipimir", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,            itm_rich_outfit,        itm_knyaz_kuyak_2,                     itm_leather_boots,          itm_mail_chausses,                   itm_borovod_lamellar_helmet, itm_lamellar_gauntlets,   itm_bastard_sword_b,  itm_shortened_military_scythe, itm_tab_shield_kite_cav_b],       knight_attrib_5,wp(250),knight_skills_5, 0x00000005e20910c248f59ed8e33158cc00000000001d18910000000000000000, borovod_face_older_2],
  ["knight_2_16", "Boyar Pavir", "Pavir", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rus_horse,      itm_borov_noble_outfit_cloak,      itm_rus_scale,                   itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_noble_helmet,  itm_mail_mittens,          itm_great_bardiche,           itm_tab_shield_kite_c],   knight_attrib_1,wp(120),knight_skills_1, 0x00000005db0433424eac6db4dd4dd59200000000001e34f50000000000000000, borovod_face_middle_2],
  ["knight_2_17", "Boyar Bernadin", "berna", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,      itm_borov_noble_outfit,     itm_rus_scale,                   itm_leather_boots,          itm_mail_boots,                      itm_nikolskoe_helm,   itm_scale_gauntlets,         itm_great_bardiche,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(150),knight_skills_2, 0x00000005f1101346072d4218a289a29c00000000001d468d0000000000000000, borovod_face_old_2],
  ["knight_2_18", "Boyar Blazius", "Blazius", tf_hero, 0, reserved,  fac_kingdom_2, [itm_mail_armor_horse,            itm_borov_noble_outfit_cloak,             itm_boyar_armor,                     itm_woolen_hose,            itm_mail_chausses,                   itm_borovod_lamellar_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_3,wp(180),knight_skills_3, 0x00000005f000220548971a6adccd975500000000001db9320000000000000000, borovod_face_older_2],
  ["knight_2_19", "Boyar Ljutmir", "Ljutmir", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rus_horse,      itm_rich_outfit,        itm_knyaz_kuyak_1,                     itm_leather_boots,          itm_mail_chausses,                   itm_nikolskoe_helm, itm_scale_gauntlets,         itm_fighting_pick,  itm_shortened_military_scythe, itm_tab_shield_kite_d],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x00000005e000121459a44b26a31239e200000000001d58920000000000000000, borovod_face_older_2],
  ["knight_2_20", "Boyar Miuda", "Miuda", tf_hero, 0, reserved,  fac_kingdom_2, [itm_lamellar_armor_horse,          itm_borov_noble_outfit,        itm_knyaz_kuyak,               itm_woolen_hose,            itm_mail_boots,                      itm_borovod_lamellar_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x00000008c0003090570d4e3a95b3338b00000000001dd95d0000000000000000, borovod_face_older_2],



#guhulay civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Gonbayar Noyan", "Gonbayar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest,  itm_guhulay_noyan_armor,itm_nomad_boots,  itm_mail_boots, itm_guhulay_noble_helm_2, itm_lamellar_gauntlets, itm_leather_gloves,  itm_sword_guhulay_3, itm_tab_shield_small_round_c, itm_guhulay_bow, itm_arrows],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x0000000cac0471cd128a2ecce44db6e500000000001d47130000000000000000, guhulay_face_middle_2],
  ["knight_3_2", "Ganzorig Noyan",  "Ganzorig", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_vest,   itm_g_coat_of_plates_a, itm_hide_boots,  itm_mail_boots, itm_guhulay_noble_helmet, itm_lamellar_gauntlets, itm_leather_gloves, itm_guhulay_sword_two_handed_b,  itm_tab_shield_small_round_b, itm_guhulay_bow, itm_arrows], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000ca800914538d46ef4f395aadb00000000001d409b0000000000000000, guhulay_face_old_2],
  ["knight_3_3", "Baterd Noyan",  "Baterd", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_robe, itm_guhulay_mirza_armor,itm_nomad_boots,  itm_splinted_leather_greaves,  itm_guhulay_noble_helm_2, itm_lamellar_gauntlets, itm_fighting_pick,  itm_tab_shield_small_round_c, itm_guhulay_bow, itm_arrows],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x00000007be00700c372a96caa14cca9900000000001ecd260000000000000000, guhulay_face_older_2],
  ["knight_3_4", "Batbayar Noyan", "Batbayar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_lamellar_vest_guhulay,  itm_guhulay_lamellar_armor_b, itm_hide_boots,  itm_splinted_greaves,   itm_guhulay_noble_helmet, itm_lamellar_gauntlets, itm_guhulay_sword_two_handed_b, itm_lance,  itm_tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000098300838d1ad3388ae74958a400000000001e655a0000000000000000, guhulay_face_older_2],
  ["knight_3_5", "Farukh Noyan",  "Farukh", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_ragged_outfit,  itm_lamellar_vest_guhulay, itm_hide_boots,  itm_mail_boots, itm_guhulay_noble_helm_2, itm_lamellar_gauntlets, itm_sword_guhulay_3, itm_lance, itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x00000009990c94d216dcb1475555bad100000000001e36590000000000000000, guhulay_face_older_2],
  ["knight_3_6", "Rustom Noyan", "Rustom", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_guhulay_lamellar_armor_b,itm_hide_boots, itm_splinted_leather_greaves,  itm_guhulay_noble_helmet,  itm_lamellar_gauntlets, itm_sword_guhulay_4,itm_lance,  itm_tab_shield_small_round_b], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x00000009891073d756d361d6ab894d0c00000000001dc4d50000000000000000, guhulay_face_middle_2],
  ["knight_3_7", "Azat Noyan","Azat", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_guhulay_lamellar_armor_b,itm_leather_boots, itm_hide_boots, itm_skullcap, itm_guhulay_noble_helm_2, itm_lamellar_gauntlets,  itm_sword_guhulay_3, itm_tab_shield_small_round_b], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x00000009b600810738d568a94b4c94e200000000001e289c0000000000000000, guhulay_face_old_2],
  ["knight_3_8", "Timur Noyan", "Timur", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_nomad_vest, itm_guhulay_lamellar_armor_b, itm_woolen_hose, itm_splinted_greaves, itm_guhulay_noble_helmet, itm_lamellar_gauntlets,   itm_great_bardiche,  itm_tab_shield_small_round_c],  knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x0000000deb0c82461b748d26d42d9ac200000000001e5ccb0000000000000000, guhulay_face_older_2],
  ["knight_3_9", "Aybek Noyan","Aybek", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,  itm_nomad_robe, itm_guhulay_noyan_armor,  itm_leather_boots, itm_splinted_leather_greaves,  itm_guhulay_noble_helm_2, itm_lamellar_gauntlets,  itm_guhulay_sword_two_handed_b,  itm_tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000080c1081d268dbca9b1b6eaa9300000000001e3ad20000000000000000, guhulay_face_older_2],
  ["knight_3_10", "Sukhrab Noyan","Sukhrab", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,  itm_lamellar_vest_guhulay, itm_g_coat_of_plates_a, itm_hide_boots, itm_mail_chausses,  itm_guhulay_noble_helm_2, itm_lamellar_gauntlets,  itm_sword_guhulay_4, itm_guhulay_sword_two_handed_b,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x000000097000801644a4c71a5169b9a900000000001cb94a0000000000000000, guhulay_face_older_2],
  ["knight_3_11", "Lalay Noyan", "Lalay", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest, itm_guhulay_lamellar_armor_b, itm_nomad_boots, itm_mail_boots,  itm_guhulay_noble_helmet,  itm_leather_gloves, itm_sword_guhulay_4,  itm_tab_shield_small_round_b, itm_guhulay_bow, itm_arrows],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x00000009780c80cb0b59acc4a3ae5cf400000000001d92e60000000000000000, guhulay_face_middle_2],
  ["knight_3_12", "Jirgal Noyan", "Jirgal", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_vest, itm_guhulay_mirza_armor, itm_hide_boots, itm_mail_boots,  itm_guhulay_noble_helm_2,  itm_leather_gloves, itm_sword_guhulay_3,  itm_tab_shield_small_round_b], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x000000094008400c37bdd88776965d6b00000000001d18e60000000000000000, guhulay_face_old_2],
  ["knight_3_13", "Norasyl Noyan","Norasyl", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_robe,  itm_lamellar_vest_guhulay, itm_nomad_boots, itm_splinted_leather_greaves,  itm_guhulay_noble_helmet, itm_lamellar_gauntlets, itm_fighting_pick,  itm_tab_shield_small_round_c, itm_guhulay_bow, itm_arrows],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x000000095900711068eb7348db8ad72c00000000001da9670000000000000000, guhulay_face_older_2],
  ["knight_3_14", "Serik Noyan",  "Serik", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_robe,  itm_guhulay_lamellar_armor_b, itm_hide_boots, itm_splinted_greaves, itm_guhulay_noble_helm_2, itm_lamellar_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_small_round_c, itm_guhulay_bow, itm_arrows],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x000000096e1075cc546592da55b6b49900000000001e3b3b0000000000000000, guhulay_face_older_2],
  ["knight_3_15", "Bolat Noyan", "Bolat", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,   itm_ragged_outfit, itm_guhulay_noyan_armor, itm_hide_boots, itm_mail_boots,  itm_guhulay_noble_helmet, itm_sword_guhulay_4, itm_guhulay_sword_two_handed_b, itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x000000097d0084cd3cd56d88649a26a300000000001d3cde0000000000000000, guhulay_face_older_2],
  ["knight_3_16", "Talat Noyan","Talat", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_tribal_warrior_outfit,  itm_guhulay_lamellar_armor_b,  itm_hide_boots,  itm_splinted_leather_greaves,  itm_guhulay_noble_helm_2, itm_leather_gloves,   itm_guhulay_sword_two_handed_a,  itm_lance, itm_tab_shield_small_round_b, itm_guhulay_bow, itm_arrows],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x00000009720c810326e15246bd69b8a300000000001d46e30000000000000000, guhulay_face_middle_2],
  ["knight_3_17", "Arman Noyan", "Arman", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_leather_vest, itm_guhulay_noyan_armor, itm_leather_boots, itm_mail_boots, itm_guhulay_noble_helm_2, itm_leather_gloves,   itm_great_bardiche, itm_tab_shield_small_round_c, itm_guhulay_bow, itm_arrows],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x000000097100838018e45254eec826a400000000001d26950000000000000000, guhulay_face_old_2],
  ["knight_3_18", "Aiman Noyan", "Aiman", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,   itm_nomad_vest, itm_guhulay_mirza_armor, itm_hide_boots, itm_splinted_greaves,  itm_guhulay_noble_helm_2, itm_scale_gauntlets,   itm_war_axe, itm_tab_shield_small_round_c, itm_lance,  itm_guhulay_bow, itm_arrows],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x000000096b0883d72729663b9586a25c00000000001e18530000000000000000, guhulay_face_older_2],
  ["knight_3_19", "Rasim Noyan","Rasim", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,   itm_nomad_robe, itm_lamellar_vest_guhulay, itm_leather_boots, itm_splinted_leather_greaves,  itm_guhulay_noble_helmet, itm_lamellar_gauntlets, itm_sword_guhulay_4, itm_shortened_military_scythe, itm_tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000955089249435b2ca36e4ebadd00000000001e34d10000000000000000, guhulay_face_older_2],
  ["knight_3_20", "Ilkin Noyan","Ilkin", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_lamellar_vest, itm_guhulay_mirza_armor, itm_hide_boots, itm_mail_chausses, itm_guhulay_noble_helm_2, itm_scale_gauntlets, itm_guhulay_sword_two_handed_a, itm_tab_shield_small_round_c, itm_lance, itm_guhulay_bow, itm_arrows],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x000000095600700d191cb2475c32369b00000000001d66ab0000000000000000, guhulay_face_older_2],

  ["knight_4_1", "Jarl Thormodr", "Thormodr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,  itm_nord_coat_of_plates_pelt,   itm_woolen_hose,  itm_mail_boots,  itm_nord_ornate_visored_helmet, itm_mail_mittens, itm_great_axe, itm_tab_shield_round_d, itm_throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x000000089a11144149abc54adbb138e400000000001e58f30000000000000000, hadvog_face_middle_2],
  ["knight_4_2", "Jarl Thorgil", "Thorgil", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_chieftain_armour, itm_blue_hose,  itm_splinted_greaves,  itm_norman_faceplate_a, itm_scale_gauntlets, itm_one_handed_battle_axe_c,  itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000c2711030f5a9c54a36459956c00000000001e349a0000000000000000, hadvog_face_old_2],
  ["knight_4_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_heraldic_jarl_armor,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_norman_faceplate_a,   itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000c0709204734daca40a510c49a00000000001d3b150000000000000000, hadvog_face_older_2],
  ["knight_4_4", "Jarl Jormundur", "Jormundur", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_leather_vest,   itm_chieftain_armour,   itm_woolen_hose,  itm_mail_boots, itm_scale_gauntlets,  itm_hadvog_huscarl_helmet, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000b670823135a1679b9149518cd00000000001eb2db0000000000000000, hadvog_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_nord_coat_of_plates_pelt,   itm_leather_boots,  itm_splinted_leather_greaves,  itm_scale_gauntlets, itm_nord_ornate_visored_helmet, itm_bastard_sword_b, itm_tab_shield_round_e, itm_throwing_axes, itm_throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000b530923505cf46e3b4c52d73300000000001cda9b0000000000000000, hadvog_face_older_2],
  ["knight_4_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_norman_faceplate_a, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x000000036e01121446e4bb532b89c8de00000000001e27210000000000000000, hadvog_face_middle_2],
  ["knight_4_7", "Jarl Arngeirr", "Arngeirr", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_scale_armor,   itm_nomad_boots,  itm_mail_boots,  itm_norman_faceplate_a, itm_mail_mittens,   itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000a320802902a9372bcc3b244f900000000001e98b30000000000000000, hadvog_face_old_2],
  ["knight_4_8", "Jarl Nikholai", "Nikholai", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_chieftain_armour,   itm_woolen_hose,  itm_mail_chausses,   itm_nord_ornate_visored_helmet, itm_scale_gauntlets, itm_war_axe,  itm_tab_shield_round_e, itm_throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000a090d1144496d6eec94a9172500000000001f73ae0000000000000000, hadvog_face_older_2],
  ["knight_4_9", "Jarl Ingvarr", "Ingvarr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,   itm_chieftain_armour, itm_blue_hose,  itm_mail_boots,   itm_hadvog_huscarl_helmet, itm_scale_gauntlets, itm_arrows, itm_long_bow,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, hadvog_face_older_2],
  ["knight_4_10", "Jarl Hrothgar", "Hrothgar", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_courtly_outfit,   itm_heraldic_jarl_armor,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x0000000a2c0d15ca266db1b4a390c8df00000000001d49330000000000000000, hadvog_face_older_2],
  ["knight_4_11", "Jarl Hergeir", "Hergeir", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_hadvog_helmet,  itm_mail_mittens,  itm_great_bardiche, itm_tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x0000000a361114854adc4ec96d8d992100000000001f55590000000000000000, hadvog_face_middle_2],
  ["knight_4_12", "Jarl Ornolf", "Ornolf", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor, itm_blue_hose,  itm_splinted_greaves,  itm_hadvog_huscarl_helmet,  itm_mail_mittens,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x0000000a3f00128a6a8cc5c8eb51691300000000001f494b0000000000000000, hadvog_face_old_2],
  ["knight_4_13", "Jarl Alfer", "Alfer", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_chieftain_armour,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_norman_faceplate_a,   itm_war_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x0000000a170522524732d9d92569e6cc00000000001dc5210000000000000000, hadvog_face_older_2],
  ["knight_4_14", "Jarl Arvid", "Arvid", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_leather_vest,   itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_hadvog_helmet, itm_scale_gauntlets, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x0000000a330910065585b346ee35b6d300000000001da7750000000000000000, hadvog_face_older_2],
  ["knight_4_15", "Jarl Asjborn", "Asjborn", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_leather_jacket,   itm_plate_armor,   itm_plate_boots, itm_scale_gauntlets,  itm_splinted_leather_greaves,  itm_hadvog_huscarl_helmet, itm_shortened_military_scythe, itm_tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x0000000a290515813f9d7635915738b400000000001d42490000000000000000, hadvog_face_older_2],
  ["knight_4_16", "Jarl Ejill", "Ejill", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_hadvog_huscarl_helmet, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x0000000a0910028a085c31552d7228d400000000001de6da0000000000000000, hadvog_face_middle_2],
  ["knight_4_17", "Jarl Einar", "Einar", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor,   itm_nomad_boots,  itm_mail_boots,  itm_norman_faceplate_a, itm_mail_mittens,   itm_sword_viking_3,  itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x0000000a0910028a085c31552d7228d400000000001de6da0000000000000000, hadvog_face_old_2],
  ["knight_4_18", "Jarl Erlendur", "Erlendur", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_chieftain_armour,   itm_woolen_hose,  itm_mail_chausses,  itm_nord_ornate_visored_helmet, itm_scale_gauntlets, itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_3,wp(180),knight_skills_3, 0x00000006630023055362954313a5af3400000000001e29240000000000000000, hadvog_face_older_2],
  ["knight_4_19", "Jarl Haldor", "Haldor", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,   itm_heraldic_jarl_armor, itm_blue_hose,  itm_mail_boots,   itm_hadvog_huscarl_helmet, itm_scale_gauntlets,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x00000009ff1000017a99725f9d89d71a00000000001ea6a90000000000000000, hadvog_face_older_2],
  ["knight_4_20", "Jarl Vidar", "Vidar", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courtly_outfit,   itm_hadvog_cuir_bouilli,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_nord_ornate_visored_helmet,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x00000004bf0c02c145646ec86d50b8b700000000001ec4bd0000000000000000, hadvog_face_older_2],

  ["knight_5_1", "Patrician Adeodat", "Adeodat", tf_hero, 0, reserved,  fac_kingdom_5, [   itm_imifir_rich_jacket_1,   itm_milanese_armor_outfit,       itm_leather_boots,    itm_mail_boots,    itm_milanese_sallet, itm_leather_gloves,     itm_claymore],     knight_attrib_2,wp(130),knight_skills_1|knows_trainer_3, 0x0000000bc20c358542db2db753995a6b00000000000d4adc0000000000000000, imifir_face_middle_2],
  ["knight_5_2", "Patrician Viator", "Viator", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_imifir_rich_jacket_2,       itm_milanese_armor_outfit,    itm_leather_boots,    itm_mail_boots,    itm_flemish_armet, itm_leather_gloves,      itm_claymore,  itm_sword_two_handed_a],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000a38010581532252a8b3d5c8a500000000001e36a40000000000000000, imifir_face_old_2],
  ["knight_5_3", "Patrician Verissim", "Verissim", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,  itm_rich_plate_armor,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_chapel_de_fer, itm_gauntlets, itm_shortened_military_scythe],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000a270c2186592b7294e2a0b6a600000000001d4b690000000000000000, imifir_face_older_2],
  ["knight_5_4", "Patrician Sirus", "Sirus", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_2,     itm_rich_plate_armor,       itm_woolen_hose,      itm_splinted_greaves,    itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_a],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000a0b103584383386352b30c90e00000000001da2750000000000000000, imifir_face_older_2],
  ["knight_5_5", "Patrician Ursus", "Ursus", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_1,  itm_milanese_armor_outfit,     itm_leather_boots,    itm_mail_boots,    itm_visored_sallet_coif, itm_gauntlets, itm_shortened_military_scythe], knight_attrib_5,wp(250),knight_skills_5, 0x0000000a3e0c14d0289a6abcab991cdc00000000000f26610000000000000000, imifir_face_older_2],
  ["knight_5_6", "Patrician Urban", "Urban", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_imifir_rich_jacket_2,      itm_rich_plate_armor,       itm_woolen_hose,      itm_splinted_greaves, itm_gauntlets,   itm_pigface_klappvisor_open,     itm_sword_two_handed_b],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000a2404508f14cb5543e276a48c00000000001daa910000000000000000, imifir_face_middle_2],
  ["knight_5_7", "Patrician Servat", "Servat", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,       itm_heraldic_plate_01,   itm_leather_boots,    itm_mail_chausses,  itm_gauntlets,      itm_nasal_helmet,       itm_bastard_sword_a],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000a310815d63323aed96dc5d94d00000000001766d90000000000000000, imifir_face_old_2],
  ["knight_5_8", "Patrician Sebatian", "Sebatian", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_imifir_rich_jacket_1,     itm_milanese_armor_outfit,    itm_woolen_hose,      itm_mail_boots,    itm_visored_sallet_coif,  itm_gauntlets,      itm_claymore, itm_sword_two_handed_b],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000a2205409257238dc2548a555e00000000001dc6d20000000000000000, imifir_face_older_2],
  ["knight_5_9", "Patrician Sanctos", "Sanctos", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_2,     itm_rich_plate_armor,   itm_leather_boots,    itm_splinted_leather_greaves,       itm_visored_sallet, itm_gauntlets,   itm_corseque],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000a370832104b7db71915aeeca000000000001c9a2c0000000000000000, imifir_face_older_2],
  ["knight_5_10", "Patrician Quirun", "Quirun", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,  itm_milanese_armor_outfit,     itm_blue_hose,  itm_mail_chausses,       itm_barbuta1, itm_gauntlets,       itm_bastard_sword_a],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x0000000cc0050011169981caf165b8f500000000001cea9d0000000000000000, imifir_face_older_2],
  ["knight_5_11", "Patrician Etrosq", "Etrosq", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,       itm_milanese_armor_outfit,       itm_leather_boots,    itm_mail_boots,    itm_barbuta1,  itm_leather_gloves,    itm_corseque],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000cff10020012dcad94eb2854e300000000001e31120000000000000000, imifir_face_middle_2],
  ["knight_5_12", "Patrician Primus", "Primus", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_imifir_rich_jacket_1,       itm_rich_plate_armor,    itm_leather_boots,    itm_mail_boots,    itm_barbuta1,  itm_leather_gloves,      itm_claymore],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x00000008bf0503c234e46a371ddb4ad100000000001d37720000000000000000, imifir_face_old_2],
  ["knight_5_13", "Patrician Pastor", "pastor", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_2,  itm_milanese_armor_outfit,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_barbuta1, itm_gauntlets,       itm_sword_two_handed_a],    knight_attrib_3,wp(190),knight_skills_3, 0x00000008b40915d0472686d6cbb136e300000000001dc6d90000000000000000, imifir_face_older_2],
  ["knight_5_14", "Patrician Leo", "Leo", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_1,     itm_rich_plate_armor,       itm_woolen_hose,      itm_splinted_greaves,    itm_barbuta1, itm_gauntlets, itm_bastard_sword_a],    knight_attrib_4,wp(220),knight_skills_4, 0x00000008a90c359324cc9156d675a76400000000001e38eb0000000000000000, imifir_face_older_2],
  ["knight_5_15", "Patrician Justor", "Justor", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,  itm_milanese_armor_outfit,     itm_leather_boots,    itm_mail_boots,    itm_pigface_klappvisor_open, itm_gauntlets,       itm_sword_two_handed_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000008bc105004556c57752629c71900000000001d50e10000000000000000, imifir_face_older_2],
  ["knight_5_16", "Patrician Gerontus", "Gerontus", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_imifir_rich_jacket_2,      itm_rich_plate_armor,       itm_woolen_hose,      itm_splinted_greaves,    itm_barbuta1, itm_leather_gloves,     itm_corseque],    knight_attrib_1,wp(120),knight_skills_1, 0x00000005aa011485359a335d235138d100000000001c1d230000000000000000, imifir_face_middle_2],
  ["knight_5_17", "Patrician Duran", "Duran", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket_1,       itm_milanese_armor_outfit,   itm_leather_boots,    itm_mail_chausses,       itm_barbuta1,  itm_leather_gloves,      itm_bastard_sword_a],     knight_attrib_2,wp(150),knight_skills_2, 0x00000005930432c137599ab51d62e91d00000000001d291d0000000000000000, imifir_face_old_2],
  ["knight_5_18", "Patrician Kyriac", "Kyriac", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_imifir_rich_jacket_1,     itm_milanese_armor_outfit,    itm_woolen_hose,      itm_mail_boots,    itm_barbuta1, itm_gauntlets,       itm_claymore],    knight_attrib_3,wp(180),knight_skills_3, 0x000000087f0d054716ab9129248d566a00000000001e449d0000000000000000, imifir_face_older_2],
  ["knight_5_19", "Patrician Mitur", "Mitur", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_imifir_rich_jacket_2,     itm_rich_plate_armor,   itm_leather_boots,    itm_splinted_leather_greaves,       itm_chapel_de_fer_mail2, itm_gauntlets,   itm_fighting_pick,  itm_sword_two_handed_a],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000085b10c2067ad214db3c6daa8900000000001e439b0000000000000000, imifir_face_older_2],
  ["knight_5_20", "Patrician Chinar", "Chunar", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_imifir_rich_jacket,  itm_rich_plate_armor,     itm_blue_hose,  itm_mail_chausses,       itm_barbuta1, itm_gauntlets,       itm_bastard_sword_b],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x000000087401458e24e3c19493694ae300000000001e369b0000000000000000, imifir_face_older_2],


  ["knight_6_1", "Emir Hodaif", "Hodaif", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_arabian_horse_a,   itm_afirid_emir_armor,          itm_afirid_boots_c,    itm_mail_boots,    itm_afirid_face_helm_n_1, itm_leather_gloves,    itm_heavy_lance, itm_afirid_cavalry_sword,   itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000bf20114c85ab3d6484c94a7a300000000001d4ab30000000000000000],
  ["knight_6_2", "Emir Banidar", "Banidar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_a, itm_afirid_noble_warhorse_deco,    itm_afirid_emir_lamellar,       itm_afirid_boots_c,    itm_mail_boots,    itm_afirid_face_helm_n_1, itm_leather_gloves,   itm_lance,   itm_military_pick,  itm_sword_two_handed_a,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000d3610a5c0676342454a6b451c00000000001e69150000000000000000],
  ["knight_6_3", "Emir Malik", "Malik", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_noble_caftan, itm_arabian_horse_a,     itm_afirid_emir_armor,       itm_nomad_boots,      itm_afirid_face_helm_n_1,  itm_shortened_military_scythe, itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000efa0513462b5cb6379e49b88900000000001dca640000000000000000],
  ["knight_6_4", "Emir Fayd", "Fayd", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_hunter,     itm_afirid_emir_armor_b,            itm_afirid_boots_c,          itm_afirid_face_helm_n_2,  itm_afirid_cavalry_sword, itm_lamellar_gauntlets, itm_lance,   itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000ec810a4546d0b51b85a73249e00000000001e1b4d0000000000000000],
  ["knight_6_5", "Emir Molhim", "Molhim", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_arabian_horse_b,     itm_afirid_emir_lamellar,       itm_afirid_boots_c,    itm_afirid_emir_helmet_1,  itm_shortened_military_scythe,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000eef08a546211c5298e5aec91b00000000001c1ae20000000000000000],
  ["knight_6_6", "Emir Harmid", "Harmid", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_a, itm_afirid_noble_warhorse,    itm_afirid_nob_armor_b,            itm_afirid_boots_c,      itm_splinted_greaves,    itm_afirid_emir_helmet_2, itm_lance,      itm_afirid_cavalry_sword,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000bfb0d1586688e65a6d574975d00000000001dd7dc0000000000000000],
  ["knight_6_7", "Emir Nosman", "Nosman", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_arabian_horse_b,     itm_afirid_emir_armor_b,          itm_afirid_boots_c,          itm_afirid_face_helm_n_1,       itm_afirid_cavalry_sword,  itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000ff60cc145592cb6468df1b6dc00000000001eed160000000000000000],
  ["knight_6_8", "Emir Darwij", "Darwij", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_noble_caftan, itm_afirid_noble_warhorse_deco, itm_afirid_emir_armor,         itm_afirid_boots_c,      itm_mail_boots,    itm_afirid_emir_helmet_2,        itm_military_pick, itm_lance,  itm_afirid_cavalry_sword,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000],
  ["knight_6_9", "Emir Lamrif", "Lamrif", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_afirid_emir_warhorse,     itm_afirid_emir_armor_b,        itm_afirid_boots_c,    itm_afirid_emir_helmet_2, itm_lamellar_gauntlets,   itm_lance, itm_tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000f07113506665d69cb114d54f100000000001eecc90000000000000000],
  ["knight_6_10", "Emir salafdar", "Salafdar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_a, itm_afirid_emir_warhorse,     itm_afirid_nob_armor_b,       itm_afirid_boots_c,  itm_afirid_boots_c,       itm_afirid_emir_helmet_2, itm_lamellar_gauntlets,   itm_lance,     itm_afirid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x0000000f3a08b39445b4a8d85c50b71c00000000001d273c0000000000000000],
  ["knight_6_11", "Emir Dunji", "Dunji", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_afirid_noble_warhorse_deco,     itm_afirid_emir_armor_b,              itm_afirid_boots_c,    itm_afirid_boots_c,    itm_afirid_face_helm_n_2,  itm_leather_gloves,    itm_fighting_pick,   itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000a3600c20f399156aaa22b291900000000001eccd30000000000000000],
  ["knight_6_12", "Emir Saryaq", "Saryaq", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_noble_caftan, itm_courser,    itm_afirid_emir_armor,           itm_afirid_boots_c,    itm_mail_boots,    itm_afirid_emir_helmet_2, itm_lance,    itm_military_pick,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000da70c42953a69934b5d86b94b00000000001e22320000000000000000],
  ["knight_6_13", "Emir Tumar", "Tumar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_arabian_horse_b,     itm_afirid_emir_armor_b,       itm_afirid_boots_c,      itm_afirid_boots_c,  itm_afirid_emir_helmet_2,   itm_lamellar_gauntlets,     itm_sword_two_handed_a,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000],
  ["knight_6_14", "Emir Bordif", "Bordif", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_noble_caftan, itm_arabian_horse_b,     itm_afirid_emir_lamellar,       itm_afirid_boots_c,      itm_afirid_boots_c,    itm_afirid_face_helm_n_1, itm_lance,  itm_afirid_cavalry_sword,    itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000dc80ca00545d392c95358b71a00000000001eb8740000000000000000],
  ["knight_6_15", "Emir Samruch", "Samruch", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_hunter,     itm_afirid_emir_armor_b,       itm_afirid_boots_c,    itm_mail_boots,    itm_afirid_emir_helmet_2,  itm_sword_two_handed_a,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ded1143431af269395b8e191200000000001d392b0000000000000000],

  ["knight_6_16", "Emir Walifdar", "Walifdar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_afirid_noble_warhorse,    itm_afirid_emir_armor,             itm_afirid_boots_c,      itm_afirid_boots_c,    itm_afirid_face_helm_n_2, itm_leather_gloves,  itm_lance,    itm_fighting_pick,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000ae910b2504b14ce450cb3469100000000001e7acd0000000000000000],
  ["knight_6_17", "Emir Mahronar", "Mahronar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_a, itm_arabian_horse_b,     itm_afirid_emir_armor_b,          itm_afirid_boots_c,    itm_afirid_boots_c,       itm_afirid_face_helm_n_2,  itm_leather_gloves,      itm_afirid_cavalry_sword,    itm_tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000de30cd2c53554863b4d891b1c00000000001f2ad50000000000000000],
  ["knight_6_18", "Emir Sanjir", "Sanjir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_afirid_noble_warhorse,  itm_afirid_elite_armor,     itm_afirid_boots_c,      itm_mail_boots,    itm_afirid_emir_helmet_2,  itm_lance,       itm_military_pick,   itm_tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000a9d0c458f5422a9b10bccb76d00000000001d9cd30000000000000000],
  ["knight_6_19", "Emir Jalosir", "Jalosar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_a, itm_afirid_emir_warhorse_deco,     itm_afirid_emir_armor_b,        itm_afirid_boots_c,    itm_afirid_boots_c,       itm_afirid_face_helm_n_2, itm_lamellar_gauntlets,   itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_small_round_c],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000096a10334755938916e361141200000000001d67a10000000000000000],
  ["knight_6_20", "Emir Almadkuk", "Almadkuk", tf_hero, 0, reserved,  fac_kingdom_6, [itm_afirid_rich_caftan_b, itm_afirid_emir_warhorse,     itm_afirid_cavalry_robe,       itm_afirid_boots_c,  itm_afirid_boots_c,       itm_afirid_emir_helmet_1,   itm_lance,      itm_afirid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x0000000aed00a20532e58f56cd72c39200000000001e25610000000000000000],

	#--------------------------
  ["knight_7_1", "Duc Kaladus", "Kaladus", tf_hero, 0, reserved,  fac_kingdom_7, [itm_romanhalfcata,      itm_courtly_outfit,      itm_dirim_general_armor,   itm_nomad_boots, itm_splinted_greaves,       itm_dirim_general_helm,           itm_sword_medieval_c,  itm_scale_gauntlets,         itm_tab_shield_heater_cav_a],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_3|knows_trainer_4, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, pravar_face_older_2],
	#------------------------

  ["kingdom_1_pretender",  "Strat Filos",       "Filos",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Queen Burka", "Burka",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_guhulay_lamellar_armor_b,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, borovod_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Nubud Khan",               "Nubud",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_guhulay_lamellar_armor_b,         itm_sword_guhulay_2,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, guhulay_face_middle_2],
#of the family

 ["kingdom_4_pretender",  "High Jarl Ijarmof",   "Ijarmof",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_galnar_clan,[itm_courtly_outfit,   itm_hadvog_cuir_bouilli,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_nord_ornate_visored_helmet,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000],
 #dispossessed and wronged

	["kingdom_5_pretender",  "Doge Jolus",  "Jolus",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, imifir_face_old_2],
#republican

  ["kingdom_6_pretender",  "Wali Dahmad",       "Dahmad",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_afirid_cav_armor_b, itm_afirid_boots_c, itm_afirid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Wigberht",  "King Wigberht",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_pravars,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_pravars,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_pravars,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_pravars,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_pravars,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_pravars,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_pravars,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],

#  ["town_8_ruler_b", "King Burelek", "King_Burelek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_borovods,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Pravar ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_2],

  #Borovod ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, guhulay_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, guhulay_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, guhulay_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, guhulay_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],



  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

#Afirid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,  itm_afirid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_afirid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_afirid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1, pravar_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_afirid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, pravar_woman_face_2],

#--Dirim ladies
  ["kingdom_7_lady_1","Lady Julia","Julia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_7_lady_2","Lady Hinda","Hinda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  #["kingdom_7_lady_3","Lady Yaniss","Yaniss",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],




#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_hadvog_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_hadvog_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_hadvog_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_hadvog_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],


#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
#---------------
  ["free_port_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
#---------------


  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["outpost_seneschal", "{!}outpost Seneschal", "{!}outpost Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
#---------------
#["free_port_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_free_port_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
#---------------


# Underground

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_afirid_common_dress,         itm_afirid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
#---------------
  ["free_port_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_afirid_common_dress,         itm_afirid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
#---------------
# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_afirid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_afirid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_afirid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_afirid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
#---------------
  ["free_port_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_afirid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
#---------------
#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_afirid_dress_a,        itm_afirid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_afirid_cloth_robe,       itm_afirid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_afirid_common_dress,        itm_afirid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_afirid_cloth_robe_b,               itm_afirid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
#---------------
  ["free_port_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_free_port_tavern|entry(9),0,  fac_commoners,[itm_afirid_cloth_robe_b,               itm_afirid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
#---------------
#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_afirid_common_dress_b,  itm_afirid_boots_a, itm_afirid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_afirid_dress_a,         itm_afirid_boots_a,  itm_afirid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],
#---------------
 ["free_town_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_free_port_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
#---------------
# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_afirid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_afirid_cloth_robe,      itm_afirid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_afirid_cloth_robe_b,        itm_afirid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_afirid_common_dress_b,       itm_blue_hose,      itm_afirid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
#---------------
   ["free_port_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_afirid_common_dress_b,       itm_blue_hose,      itm_afirid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
#---------------

#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat_green,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,     itm_afirid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,       itm_afirid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,    itm_afirid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,      itm_afirid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
#---------------
  ["free_port_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,      itm_afirid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
#---------------

#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_afirid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_111_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],

# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
#---------------
   ["free_port_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_afirid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
#---------------


# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_guhulay_guard","Black Guhulay Guard","Black Guhulay Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_guhulays,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_guhulay_bow,itm_guhulay_guard_helmet,itm_guhulay_cavalry_helmet,itm_guhulay_guard_boots,itm_guhulay_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,guhulay_face1, guhulay_face2],


# Add Extra Quest NPCs below this point

#~----------tohlobaria troops/npc------------
  ["npc17","Genaral Linkadas","Linkadas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_kingdom_7,[itm_dirim_general_armor,itm_mail_boots,itm_dirim_general_helm,itm_luc_celtic_sword_3,itm_tab_shield_heater_cav_b,itm_romanhalfcata],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_3,
   0x0000000da00835c454ed4a7a4293397400000000001ec2b10000000000000000],
  ["npc18","Magnate Liktan","Magnate Liktan",tf_hero|tf_unmoveable_in_party_window,0, reserved,  fac_kingdom_8,[itm_rich_outfit, itm_wrapping_boots],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_3,
   0x0000000d790d10005addb6570cb1656400000000001da2e40000000000000000],
     ["jalik","Jalik","Jalik",tf_hero|tf_unmoveable_in_party_window,scn_free_port_center|entry(15), reserved,  fac_jalik_mercenaries,[itm_atian_longsword,itm_corrazina_grey,itm_splinted_greaves_spurs, itm_wisby_gauntlets_black],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_3,
   0x0000000ab704100046915736d5ab36fe00000000001e54f10000000000000000],
   #---------------ingenieur (artim)--------------
  ["npc19","Moktar","Moktar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_merchant_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x00000004400922812add2e4aca22372100000000001d67490000000000000000],
  #-------------------------------------
  #---------------armurier(jeremus)--------------
  ["npc20","Fuhlanir","Fuhlanir",tf_hero|tf_unmoveable_in_party_window, scn_my_castle_exterior|entry(23), reserved,  fac_commoners,
  [ itm_leather_apron,itm_nomad_boots],
   str_10|agi_7|int_12|cha_3|level(7),wp(100),   knows_merchant_npc|
   knows_ironflesh_4|knows_power_strike_2,
   0x00000009f00911802add2e4aca22372100000000001d67490000000000000000],
  #------------------------------------------------
  #----------ancient empereur (pour le fort abandonne)---------------
  ["dead_emperor","{!}Oclatan Emperator","{!}Oclatan Emperator",tf_hero|tf_inactive, 0, reserved,  fac_neutral,
  [itm_corrazina_red,itm_mail_boots,itm_barbuta2,itm_luc_celtic_sword_3],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_3,
   0x00000009f00911802add2e4aca22372100000000001d67490000000000000000],
  #--------------------------------------------
  #-----------------order leader-------------------------
  ["sorobodol","Sorbodol","Sorbodol",tf_hero|tf_unmoveable_in_party_window,0, reserved,  fac_knights_of_doomcall,[itm_morningstar,itm_black_armor,itm_black_greaves, itm_plate_boots,itm_high_priest_helmet,itm_courser_black],
   str_24|agi_16|int_20|cha_20|level(36),wp(280),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_3,
   0x0000000ab704100046915736d5ab36fe00000000001e54f10000000000000000],
   #-----------------------------------------------------
      ["finjir","Finjir","Finjir",tf_hero|tf_unmoveable_in_party_window,0, reserved,  fac_kingdom_7, [itm_blue_hose,itm_short_tunic,itm_one_handed_battle_axe_c,
    itm_vardian_guard_armor,itm_fluted_helmet_mail,itm_nord_splinted_greaves,itm_gauntlets],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_4,
   0x0000000dc00402522a5aaee5a5972dfd00000000001e4a530000000000000000],
#------------------------------------------------------------
   #-----------------------------------------------------
      ["pedran","Pedran","Pedran",tf_hero|tf_unmoveable_in_party_window,0, reserved,  fac_jalik_mercenaries, [itm_blue_hose,itm_short_tunic,itm_military_cleaver_c,itm_steel_shield,
    itm_new_order_plate,itm_splinted_greaves_spurs,itm_gauntlets,itm_open_sallet],
   str_20|agi_16|int_20|cha_20|level(30),wp(200),knows_warrior_npc|
   knows_trainer_6|knows_weapon_master_5|knows_leadership_7|knows_power_strike_4,
   0x00000001b7091404136e4e26d696292500000000001f572f0000000000000000],
#------------------------------------------------------------
  ["charob","Charob","Charob",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_shirt],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x000000019808314438caf6629a8ceb2c00000000001dd2a30000000000000000],
  #------------------------------------------------------------
	#-----------player knights------------
  ["knight_9_1", "Vladir", "Vladir", tf_hero, 0, reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000018f04020552a2c536d4a9235a000000000009266d0000000000000000],
 ["knight_9_2", "Solbalin",  "Solbalin",  tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000019d0d04063b6c6945db7594aa00000000000541520000000000000000],
 ["knight_9_3", "Taugard",  "Taugard",  tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001b110e5924725862cdc724915000000000012ab220000000000000000],
 ["knight_9_4", "Grimar",  "Grimar",  tf_hero, 0,reserved, fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001a304b182149b8618dc0d94e6000000000019cb9b0000000000000000],
 ["knight_9_5", "Haxalye", "Haxalye", tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001a610d4c4535390a7114da6e300000000001e48e30000000000000000],
 ["knight_9_6", "Belicha", "Belicha", tf_hero, 0,reserved, fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001b901141436ee46a8cb91370b00000000001f28b20000000000000000],
 ["knight_9_7", "Nourbis", "Nourbis", tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001b100208746ee71996929cb13000000000006472c0000000000000000],
 ["knight_9_8", "Rhudolg", "Rhudolg", tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000019710a1016894b22b134a3a55000000000015d69c0000000000000000],

 ["knight_9_9", "Bulak", "Bulak", tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001830523474d72b84a94b1c464000000000012470b0000000000000000],
 ["knight_9_10", "Aolbrug", "Aolbrug", tf_hero,0 ,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001be08c08128cf89c95c929b3500000000000dd66b0000000000000000],
 ["knight_9_11","Rasevas", "Rasevas", tf_hero, 0,reserved, fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001bc0cc58348a58a4b4b79169200000000001f3aed0000000000000000],
 ["knight_9_12","Leomir",  "Leomir",  tf_hero,0 ,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x00000001a60c720d599cae3515971a93000000000009c4e20000000000000000],
 ["knight_9_13","Haelbrad","Haelbrad",tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000019605204128e391125346e72c00000000000e18970000000000000000],
 ["knight_9_14","Mira",    "Mira",    tf_hero,0 ,reserved, fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000019510c094639cb4c8d4765ce3000000000016446b0000000000000000],
 ["knight_9_15","Camechaw","Camechaw",tf_hero, 0,reserved,  fac_commoners,   [itm_luc_flanged_mace_iron,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_great_lance,itm_baron_plate1,itm_plate_boots,itm_armet2_open,itm_long_barded_horse_black,itm_gauntlets,itm_wisby_gauntlets_black],def_attrib|level(40),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) ,knight_skills_4|knows_trainer_3, 0x000000019c0c14c5190bdaab2266486100000000000935510000000000000000],
	#------------------------

	#--extra merchants
	["fire_arm_merchant", "Fire Arms Merchant", "Fire Arms Merchant", tf_hero|tf_is_merchant, scn_free_port_center|entry(14), reserved, fac_commoners,
	 [itm_flintlock_pistol_1,itm_atian_short_sword,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_flintlock_pistol_1,itm_flintlock_pistol_1,itm_matchlock_2,itm_matchlock_2,itm_matchlock_2,itm_matchlock_2,itm_musketeer_tunic_1,itm_musketeer_tunic_2,itm_musketeer_tunic_1,itm_musketeer_tunic_2,itm_musketeer_tunic_1,itm_musketeer_tunic_2],
	 def_attrib|level(10)|str_16, wp(20), knows_common|knows_inventory_management_10, 0x00000001e200514239db6db6db61b6db00000000001db8db0000000000000000 ],

	 ["pravar_quartermaster", "Quartermaster", "Quartermasters", tf_hero|tf_is_merchant, scn_town_6_center|entry(14), reserved, fac_kingdom_1,
	 [itm_pravar_gambeson,itm_woolen_hose,itm_sword_medieval_b],
	 def_attrib|level(10)|str_16, wp(20), knows_common|knows_inventory_management_10, 0x0000000be200514238db6d56db61b6db00000000001db6db0000000000000000 ],
	 ["dirim_quartermaster", "Quartermaster", "Quartermasters", tf_hero|tf_is_merchant, scn_town_16_center|entry(14), reserved, fac_kingdom_7,
	 [itm_dirim_jerkin,itm_leather_boots_black,itm_dirim_sword],
	 def_attrib|level(10)|str_16, wp(20), knows_common|knows_inventory_management_10, 0x00000001e200514238db6db6db6136db00000000001db6db0000000000000000 ],
	#--

	["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,borovod_face1, borovod_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,borovod_face1, borovod_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],

  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],



  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],

  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,borovod_face1, borovod_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],


##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,borovod_face1, borovod_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,borovod_face1, borovod_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,borovod_face1, borovod_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,pravar_face1, pravar_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["pravar_crossbowman_multiplayer_ai","Pravar Crossbowman","Pravar Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6 |knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],
  ["pravar_infantry_multiplayer_ai","Pravar Infantry","Pravar Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5 |knows_power_strike_5|knows_athletics_4,pravar_face_middle_1, pravar_face_old_2],
  ["pravar_man_at_arms_multiplayer_ai","Pravar Man at Arms","Pravar Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4 |knows_power_strike_4|knows_athletics_1,pravar_face_young_1, pravar_face_old_2],
  ["borovod_archer_multiplayer_ai","Borovod Archer","Borovod Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6 ,borovod_face_young_1, borovod_face_older_2],
  ["borovod_spearman_multiplayer_ai","Borovod Spearman","Borovod Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3 ,borovod_face_young_1, borovod_face_older_2],
  ["borovod_horseman_multiplayer_ai","Borovod Horseman","Borovod Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4 ,borovod_face_young_1, borovod_face_older_2],
  # ["guhulay_dismounted_lancer_multiplayer_ai","Guhulay Dismounted Lancer","Guhulay Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   # [itm_sword_guhulay_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    # itm_guhulay_cavalry_helmet,itm_guhulay_war_helmet,itm_lamellar_vest_guhulay,itm_tribal_warrior_outfit,itm_guhulay_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   # def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,guhulay_face_middle_1, guhulay_face_older_2],
  # ["guhulay_veteran_horse_archer_multiplayer_ai","Guhulay Horse Archer","Guhulay Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   # [itm_sword_guhulay_3,itm_guhulay_bow,itm_guhulay_arrows,itm_tab_shield_small_round_b,
    # itm_guhulay_cavalry_helmet,itm_tribal_warrior_outfit,itm_guhulay_leather_boots,itm_steppe_horse],
   # def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5| knows_horse_archery_5,guhulay_face_middle_1, guhulay_face_older_2],
  # ["guhulay_lancer_multiplayer_ai","Guhulay Lancer","Guhulay Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   # [itm_sword_guhulay_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    # itm_guhulay_guard_helmet,itm_guhulay_cavalry_helmet,itm_guhulay_war_helmet,itm_lamellar_vest_guhulay,itm_lamellar_armor,itm_guhulay_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   # def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,guhulay_face_middle_1, guhulay_face_older_2],
  ["hadvog_veteran_multiplayer_ai","Hadvog Footman","Hadvog Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_hadvog_helmet,itm_hadvog_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5 ,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_scout_multiplayer_ai","Hadvog Scout","Hadvog Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_hadvog_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2| knows_horse_archery_2|knows_power_throw_3,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_archer_multiplayer_ai","Hadvog Archer","Hadvog Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2| knows_power_draw_5|knows_athletics_6,hadvog_face_young_1, hadvog_face_old_2],
  ["imifir_pavise_crossbowman_multiplayer_ai","Imifir Crossbowman","Imifir Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4 |knows_power_strike_3|knows_athletics_6,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_veteran_spearman_multiplayer_ai","Imifir Spearman","Imifir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5 |knows_power_strike_4|knows_athletics_3,imifir_face_young_1, imifir_face_older_2],
  ["imifir_scout_multiplayer_ai","Imifir Scout","Imifir Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Hadvog Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2| knows_horse_archery_2|knows_power_throw_3,imifir_face_young_1, imifir_face_older_2],
  ["afirid_infantry_multiplayer_ai","Afirid Infantry","Afirid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_afirid_cav_armor_b,itm_afirid_horseman_helmet,itm_afirid_boots_b,itm_afirid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2 ,pravar_face_middle_1, pravar_face_old_2],
  ["afirid_archer_multiplayer_ai","Afirid Archer","Afirid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_afirid_boots_b,itm_afirid_helmet1,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,pravar_face_young_1, pravar_face_old_2],
  ["afirid_horseman_multiplayer_ai","Afirid Horseman","Afirid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_afirid_cav_armor_b,itm_afirid_boots_b,itm_afirid_boots_c,itm_afirid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2| knows_power_strike_3,pravar_face_young_1, pravar_face_old_2],



#Multiplayer troops (they must have the base items only, nothing else)
  ["pravar_crossbowman_multiplayer","Pravar Crossbowman","Pravar Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4 |knows_power_strike_2|knows_riding_1,pravar_face_young_1, pravar_face_old_2],
  ["pravar_infantry_multiplayer","Pravar Infantry","Pravar Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_ironflesh_5 |knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,pravar_face_middle_1, pravar_face_old_2],
  ["pravar_man_at_arms_multiplayer","Pravar Man at Arms","Pravar Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3| knows_power_throw_2|knows_power_strike_3|knows_athletics_3,pravar_face_young_1, pravar_face_old_2],
#  ["pravar_mounted_crossbowman_multiplayer","Pravar Mounted Crossbowman","Pravar Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4 |knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2 ,pravar_face_young_1, pravar_face_old_2],
  ["borovod_archer_multiplayer","Borovod Archer","Borovod Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3| knows_riding_1,borovod_face_young_1, borovod_face_older_2],
  ["borovod_spearman_multiplayer","Borovod Spearman","Borovod spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4| knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,borovod_face_young_1, borovod_face_older_2],
  ["borovod_horseman_multiplayer","Borovod Horseman","Borovod Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3 |knows_power_throw_4|knows_horse_archery_1,borovod_face_young_1, borovod_face_older_2],
  ["guhulay_veteran_horse_archer_multiplayer","Guhulay Horse Archer","Guhulay Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_guhulay_1,itm_nomad_bow,itm_arrows,
    itm_guhulay_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3 ,guhulay_face_middle_1, guhulay_face_older_2],
  ["guhulay_infantry_multiplayer","Guhulay Infantry","Guhulay Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_guhulay_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3 |knows_power_strike_3|knows_athletics_6|knows_riding_1,guhulay_face_middle_1, guhulay_face_older_2],
  ["guhulay_lancer_multiplayer","Guhulay Lancer","Guhulay Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_guhulay_1,itm_lance,itm_tab_shield_small_round_a,
    itm_guhulay_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3 |knows_power_strike_3|knows_athletics_4,guhulay_face_middle_1, guhulay_face_older_2],
  ["hadvog_archer_multiplayer","Hadvog Archer","Hadvog Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2 |knows_power_draw_5|knows_athletics_3|knows_riding_1,hadvog_face_young_1, hadvog_face_old_2],
  ["hadvog_veteran_multiplayer","Hadvog Huscarl","Hadvog Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6 |knows_riding_1,hadvog_face_young_1, hadvog_face_older_2],
  ["hadvog_scout_multiplayer","Hadvog Scout","Hadvog Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2| knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,borovod_face_young_1, borovod_face_older_2],
  ["imifir_pavise_crossbowman_multiplayer","Imifir Crossbowman","Imifir Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_ironflesh_2| knows_power_strike_2|knows_athletics_4|knows_riding_1,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_sergeant_multiplayer","Imifir Sergeant","Imifir Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_ironflesh_4 |knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,imifir_face_middle_1, imifir_face_older_2],
  ["imifir_horseman_multiplayer","Imifir Horseman","Imifir Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance,
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3 |knows_power_strike_3|knows_power_throw_1|knows_athletics_3,imifir_face_middle_1, imifir_face_older_2],
  ["afirid_archer_multiplayer","Afirid Archer","Afirid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_afirid_cloth_robe, itm_afirid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3| knows_riding_1|knows_weapon_master_1,borovod_face_young_1, borovod_face_older_2],
  ["afirid_footman_multiplayer","Afirid Footman","Afirid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_afirid_cloth_robe, itm_afirid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4| knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,borovod_face_young_1, borovod_face_older_2],
  ["afirid_mamluke_multiplayer","Afirid Mamluke","Afirid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_afirid_cloth_robe, itm_afirid_boots_b,itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2 |knows_power_throw_2|knows_weapon_master_1,borovod_face_young_1, borovod_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_long_hafted_knobbed_mace, itm_wooden_shield, itm_iron_staff, itm_throwing_daggers,
    itm_felt_hat, itm_fur_coat, itm_leather_boots, itm_leather_gloves],
   str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5 |knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_scimitar, itm_tab_shield_small_round_c, itm_sumpter_horse,
    itm_leather_armor, itm_splinted_greaves],
   str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4| knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_two_handed_b, itm_sword_medieval_c, itm_tab_shield_heater_c, itm_warhorse,
    itm_guard_helmet, itm_coat_of_plates, itm_mail_mittens, itm_mail_boots],
   str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_athletics_5| knows_weapon_master_5|knows_power_strike_2|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, pravar_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_mace_4, itm_tab_shield_kite_d,
    itm_bascinet_3, itm_scale_armor, itm_mail_mittens, itm_mail_boots],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_athletics_5 |knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, pravar_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,
   [itm_long_axe, itm_sword_viking_1, itm_light_throwing_axes, itm_tab_shield_round_d,
    itm_hadvog_fighter_helmet, itm_byrnie, itm_leather_gloves, itm_leather_boots],
   str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_athletics_5 |knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_strong_bow, itm_barbed_arrows, itm_barbed_arrows, itm_shortened_spear,
    itm_leather_warrior_cap, itm_leather_jerkin, itm_leather_gloves, itm_ankle_boots],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, pravar_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_bolts, itm_sword_medieval_b_small, itm_tab_shield_pavise_c,
    itm_nasal_helmet, itm_padded_leather, itm_leather_gloves, itm_leather_boots],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5 |knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_scimitar, itm_leather_covered_round_shield,
    itm_desert_turban, itm_skirmisher_armor, itm_leather_gloves, itm_afirid_boots_b],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5| knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_barbed_arrows, itm_scimitar_b,
    itm_splinted_greaves, itm_lamellar_vest],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7| knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, pravar_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_afirid_cavalry_sword, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_arabian_horse_b,
    itm_afirid_felt_head_cloth_b, itm_afirid_common_dress, itm_afirid_boots_b],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, pravar_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar, itm_tab_shield_round_d, itm_war_spear, itm_courser,
    itm_leather_gloves, itm_fur_hat, itm_leather_boots, itm_leather_jacket],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2 |knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, pravar_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2 ,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, borovod_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2 ,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, borovod_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2 ,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, borovod_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2 ,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, borovod_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_borovod_spiked_helmet,itm_borovod_fur_helmet,itm_borovod_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,borovod_face_young_1, borovod_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, borovod_face_older_2],
  ["tutorial_rider_1","Rider","{!}Borovod Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4| knows_ironflesh_3|knows_power_strike_2,borovod_face_middle_1, borovod_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Guhulay Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,guhulay_face_young_1, guhulay_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, borovod_face_older_2],

  ["pravar_merchant", "Merchant of Pravar", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["borovod_merchant", "Merchant of Nidgornia", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["guhulay_merchant", "Merchant of Khosot", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["hadvog_merchant", "Merchant of Burfell", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["imifir_merchant", "Merchant of Bilomadal", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["afirid_merchant", "Merchant of Jabba", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_afirid_cloth_robe, itm_afirid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_one_handed_battle_axe_c,itm_battle_axe,itm_spear,itm_hadvog_shield,itm_hadvog_shield,itm_hadvog_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_hadvog_helmet,itm_hadvog_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,hadvog_face_young_1, hadvog_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2 , 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],

  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

 ]

#Troop upgrade declarations
upgrade(troops,"townsman","watchman")
upgrade(troops,"watchman","caravan_guard")
#upgrade(troops,"caravan_guard","caravan_heavy_guard")

upgrade(troops,"pravar_recruit","pravar_militia")
upgrade(troops,"pravar_militia","pravar_footman")
upgrade2(troops,"pravar_footman","pravar_infantry","pravar_crossbowman")
upgrade2(troops,"pravar_infantry","pravar_man_at_arms","pravar_mounted_sergeant")
upgrade(troops,"pravar_squire","pravar_knight")

upgrade(troops,"borovod_recruit","borovod_footman")
upgrade2(troops,"borovod_footman","borovod_axeman","borovod_archer")
upgrade(troops,"borovod_archer","borovod_trained_archer")
upgrade(troops,"borovod_trained_archer","borovod_marksman")
upgrade(troops,"borovod_axeman","borovod_veteran")
upgrade(troops,"borovod_veteran","borovod_bardiche_master")
upgrade(troops,"borovod_horseman","borovod_knight")

upgrade2(troops,"guhulay_tribesman","guhulay_skirmisher","guhulay_native_militia")
upgrade(troops,"guhulay_skirmisher","guhulay_horseman")
upgrade(troops,"guhulay_horseman","guhulay_horse_archer")
upgrade(troops,"guhulay_horse_archer","guhulay_veteran_horse_archer")
upgrade(troops,"guhulay_native_militia","guhulay_native_footman")
upgrade(troops,"guhulay_native_footman","guhulay_native_infantry")
upgrade(troops,"guhulay_native_infantry","guhulay_foot_soldier")


upgrade(troops,"guhulay_lancer","guhulay_mirza")



upgrade(troops,"hadvog_recruit","hadvog_footman")
upgrade(troops,"hadvog_footman","hadvog_trained_footman")
upgrade(troops,"hadvog_trained_footman","hadvog_warrior")
upgrade(troops,"hadvog_warrior","hadvog_veteran")
upgrade(troops,"hadvog_huskarl","hadvog_chieftain")

upgrade(troops,"imifir_recruit","imifir_spearman")
upgrade2(troops,"imifir_spearman","imifir_trained_spearman","imifir_crossbowman")
upgrade(troops,"imifir_trained_spearman","imifir_pikeman")
upgrade(troops,"imifir_pikeman","imifir_halberdier")
upgrade(troops,"imifir_crossbowman","imifir_pavise_crossbowman")

upgrade(troops,"afirid_recruit","afirid_footman")
upgrade2(troops,"afirid_footman","afirid_light_infantry","afirid_skirmisher")
#upgrade(troops,"afirid_skirmisher","afirid_javeliner")
upgrade2(troops,"afirid_light_infantry","afirid_horseman","afirid_infantry")
upgrade(troops,"afirid_horseman","afirid_heavy_horseman")
upgrade(troops,"afirid_infantry","afirid_heavy_infantry")
upgrade(troops,"afirid_charif","afirid_caid")

#----------------dirim----------------
upgrade(troops,"dirim_recruit","dirim_militia")
upgrade(troops,"dirim_militia","dirim_footman")
upgrade(troops,"dirim_footman","dirim_regular")
upgrade(troops,"dirim_regular","dirim_veteran")
upgrade(troops,"dirim_forest_hunter","dirim_long_bowman")
upgrade(troops,"dirim_cavalryman","dirim_pronoiar")
#--------------------------------------------
#---------------company------------------
upgrade(troops,"company_colonial_militia","company_ranger")
upgrade(troops,"company_ranger","company_dragon")
#--------------------------------------------
#----------------player----------------
upgrade(troops,"farmer","militia")
upgrade(troops,"paysan","militia")
upgrade2(troops,"militia","footman","bowman")
upgrade(troops,"footman","light_infantry")
upgrade(troops,"light_infantry","sergeant")
upgrade(troops,"sergeant","elite_foot_soldier")

upgrade(troops,"cavalryman","trained_cavalryman")
upgrade(troops,"trained_cavalryman","veteran_cavalryman")

# upgrade(troops,"heavy_infantry","armoured_sergeant")
# upgrade(troops,"armoured_sergeant","elite_foot_soldier")

upgrade(troops,"knight","bachelor")
upgrade(troops,"bowman","archer")

upgrade(troops,"novice_pikeman","trained_pikeman")
upgrade(troops,"trained_pikeman","veteran_pikeman")

upgrade(troops,"novice_crossbowman","trained_crossbowman")
upgrade(troops,"trained_crossbowman","veteran_crossbowman")

# upgrade(troops,"novice_cavalryman","trained_cavalryman")
# upgrade(troops,"trained_cavalryman","light_cavalry")
# upgrade(troops,"heavy_cavalry","elite_cavalry")
#--------------------------------------------

# upgrade(troops,"looter","militia")

#new tree connections
#upgrade(troops,"mountain_bandit","imifir_recruit")
#upgrade(troops,"forest_bandit","pravar_recruit")
#upgrade(troops,"steppe_bandit","guhulay_tribesman")
#upgrade(troops,"taiga_bandit","borovod_recruit")
#upgrade(troops,"sea_raider","hadvog_recruit")
#upgrade(troops,"desert_bandit","afirid_recruit")
#new tree connections ended

#upgrade2(troops,"bandit","brigand","mercenary_swordsman")
# upgrade(troops,"manhunter","slave_driver")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")

# upgrade(troops,"slave_driver","slave_hunter")
# upgrade(troops,"slave_hunter","slave_crusher")
# upgrade(troops,"slave_crusher","slaver_chief")

# upgrade(troops,"follower_woman","hunter_woman")
# upgrade(troops,"hunter_woman","fighter_woman")

# upgrade(troops,"fighter_woman","sword_sister")
# upgrade(troops,"refugee","follower_woman")
# upgrade(troops,"peasant_woman","follower_woman")
