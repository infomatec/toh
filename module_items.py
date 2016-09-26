from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive)
items = [
#-------------------------------Rus_armour_pack--------------------------------------------
	["nikolskoe_helm", "Nikolskoe helm", [("nikolskoe_helm",0), ("inv_nikolskoe_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature  ,0, 820 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["novogrod_helm", "Novogrod helm", [("novogrod_helm",0), ("inv_novogrod_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 740 , weight(2)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["gnezdovo_helm_a", "Gnezdovo helm", [("gnezdovo_helm_a",0), ("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 640 , weight(2)|abundance(50)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["gnezdovo_helm_b", "Gnezdovo helm", [("gnezdovo_helm_b",0), ("inv_gnezdovo_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 700 , weight(2.2)|abundance(50)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["tagancha_helm_a", "Tagancha helm", [("tagancha_helm_a",0), ("inv_tagancha_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 580 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["tagancha_helm_b", "Tagancha helm", [("tagancha_helm_b",0), ("inv_tagancha_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 820 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
	["rus_helm", "Rus helm", [("rus_helm",0), ("inv_rus_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 230 , weight(2)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

	["rus_shoes", "Rus Ankle Boots", [("rus_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
	 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
	["rus_cav_boots", "Rus Cavalry Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
	 15 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],

	["rus_lamellar_a", "Rus lamellar", [("rus_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
	 1095 , weight(18)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
	["kuyak_a", "Kuyak", [("kuyak_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
	 980 , weight(16)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
	["kuyak_b", "Kuyak", [("kuyak_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
	 980 , weight(16)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
	["rus_scale", "Rus Scale", [("rus_scale",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
	 1295 , weight(19)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

	["litchina_helm", "litchina helm", [("litchina_helm",0), ("inv_litchina_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature|itp_covers_beard,0, 820 , weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

	["rus_splint_greaves", "Splinted Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
	 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 #-------------------------------Rus_armour_pack end--------------------------------------------
#-------------------------------kazakh_armor osp--------------------------------------------
	["guhulay_traditional_hat", "Guhulay Traditional Hat", [("kazakh_hat",0)],  itp_type_head_armor  |itp_civilian ,0,
	 70 , weight(1)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
	["guhulay_cav_boots", "Guhulay Cavalry Boots", [("kazakh_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
	 60 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 #-------------------------------Rus_armour_pack end--------------------------------------------
  #-------------------------------yelushaleng--------------------------------------------
 	["imperial_mask", "Imperial Mask", [("yelushaleng",0)], itp_merchandise| itp_type_head_armor,0, 1000 , weight(1)|abundance(2)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 #---------------------------------------------------------------------------
 #-------------------------------bogmir_heraldic--------------------------------------------
 ["mail_long_surcoat_new_heraldic", "Heraldic Mail with Tabard", [("mail_long_surcoat_new_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1412 , weight(21)|abundance(20)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_mail_long_surcoat_new", ":agent_no", ":troop_no")])]],
#
["brigandine_b_heraldic", "Heraldic Brigandine", [("brigandine_b_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2230 , weight(24)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(12) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_brigandine_b_heraldic_new", ":agent_no", ":troop_no")])]],
#
["brigandine_c_heraldic", "Heraldic Brigandine", [("brigandine_c_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2030 , weight(22)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(10) ,imodbits_armor
 #, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_brigandine_b_heraldic_new", ":agent_no", ":troop_no")])]
 ],

["heraldic_tunic_new", "Heraldic Tunic", [("heraldic_tunic_new",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2230 , weight(20)|abundance(10)|head_armor(0)|body_armor(47)|leg_armor(16)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_short_tunic_new", ":agent_no", ":troop_no")])]],
 #---------------------------------------------------------------------------------------
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(49) | shoot_speed(49) | thrust_damage(16 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(45) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 #["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 #["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],

 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
 ["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(2)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 ["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(3)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(100)|body_armor(4)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(100)|body_armor(5)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(6)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Afirid Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(110)|body_armor(7)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(120)|body_armor(8)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["warhorse","War Horse", [("warhorse_chain",0)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(120)|body_armor(30)|difficulty(4)|horse_speed(38)|horse_maneuver(41)|horse_charge(26)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
 ["charger","Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(122)|body_armor(36)|difficulty(4)|horse_speed(37)|horse_maneuver(44)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
#---------camel----------------
["camel","Camel", [("camel",0)], itp_merchandise|itp_type_horse, 0, 900,abundance(30)|hit_points(140)|body_armor(10)|difficulty(4)|horse_speed(34)|horse_maneuver(40)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
#------------------------------
["sumpter1","Sumpter Horse", [("sumpter1",0)], itp_merchandise|itp_type_horse, 0, 180,abundance(80)|hit_points(102)|body_armor(2)|difficulty(1)|horse_speed(38)|horse_maneuver(40)|horse_charge(10)|horse_scale(100),imodbits_horse_basic],
["sumpter2","Sumpter Horse", [("sumpter2",0)], itp_merchandise|itp_type_horse, 0, 180,abundance(80)|hit_points(102)|body_armor(2)|difficulty(1)|horse_speed(38)|horse_maneuver(40)|horse_charge(10)|horse_scale(100),imodbits_horse_basic],

#---------Bloc Northerner Horse----------------
#["northerner_horse","Northerner Horse", [("northerner_horse_black",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(30)|hit_points(130)|body_armor(12)|difficulty(3)|horse_speed(41)|horse_maneuver(46)|horse_charge(20)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2,fac_kingdom_4]],
#--------------stuff osp------------------
["rus_horse","Northerner Horse", [("rus_horse",0)], itp_merchandise|itp_type_horse, 0,
 700,abundance(30)|hit_points(130)|body_armor(12)|difficulty(3)|horse_speed(41)|horse_maneuver(46)|horse_charge(20)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2,fac_kingdom_4]],
# ["guhulay_watchman_armor", "Guhulay Watchman Armor", [("armor_lam",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 310 , weight(18)|abundance(60)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(6) ,imodbits_cloth ],
# ["guhulay_skin_cap", "Guhulay Skin Cap", [("skin_helmet",0)], itp_merchandise|itp_type_head_armor   ,0,
 # 60 , weight(1)|abundance(90)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

#-----------------------------------------

#------------------------------
#---------morehorse osp----------------
["rouncy","Rouncy", [("rouncy",0)], itp_merchandise|itp_type_horse, 0, 680,abundance(100)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(48)|horse_charge(20)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1,fac_kingdom_4,fac_kingdom_7]],
["destrier","destrier", [("destrier",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 910,abundance(100)|hit_points(122)|body_armor(10)|difficulty(3)|horse_speed(44)|horse_maneuver(44)|horse_charge(26)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
["courser_black","Courser Black", [("courserback",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(100)|body_armor(6)|hit_points(100)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
["steppe_horse_1","Steppe Horse", [("steppecestnutappy",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(100)|hit_points(100)|body_armor(4)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_3]],
 ["donkey","donkey", [("donkey",0)], itp_merchandise|itp_type_horse, 0, 100,abundance(10)|hit_points(90)|body_armor(4)|difficulty(1)|horse_speed(32)|horse_maneuver(32)|horse_charge(6)|horse_scale(90),imodbits_horse_basic],
 ["mule","mule", [("mule",0)], itp_merchandise|itp_type_horse, 0, 110,abundance(10)|hit_points(95)|body_armor(6)|difficulty(1)|horse_speed(35)|horse_maneuver(38)|horse_charge(9)|horse_scale(95),imodbits_horse_basic],
#------------------------------




#whalebone crossbow, yew bow, war bow, arming sword
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,cut)|max_ammo(30),imodbits_missile],
 ["guhulay_arrows","Guhulay Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,cut)|max_ammo(30),imodbits_missile],
 #---------poisoned arrow-----------
 ["guhulay_poisoned_arrows","Guhulay Poisoned Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(5)|weapon_length(95)|thrust_damage(5,cut)|max_ammo(40),imodbits_missile],
 #----------------------------------
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,cut)|max_ammo(30),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(28),imodbits_missile],
 ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(29),imodbits_missile],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(29),imodbits_missile],
 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(20,pierce)|max_ammo(30),imodbits_missile],
#--musket cartridges
["musket_cartridges","musket_cartridges", [("cartridge_a",0)], itp_type_bolts|itp_can_penetrate_shield|itp_default_ammo, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(3)|thrust_damage(30,pierce)|max_ammo(22),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],
["gauntlets_a","Gauntlets", [("gauntlets_a_L",0),("gauntlets_a_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],
#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 310 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 853 , weight(2.75)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
 2361 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor ],
["guhulay_leather_boots", "Guhulay Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["afirid_boots_a", "Afirid Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["afirid_boots_b", "Afirid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["afirid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["afirid_boots_d", "Afirid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 920 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_armor ],

["afirid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["afirid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["afirid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["afirid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["guhulay_lady_dress", "Guhulay Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["guhulay_lady_dress_b", "Guhulay Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["afirid_lady_dress", "Afirid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["afirid_lady_dress_b", "Afirid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["afirid_common_dress", "Afirid Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["afirid_common_dress_b", "Afirid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["guhulay_armor", "Guhulay Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],



#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],



["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hadvog_outfit", "Hadvog Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hadvog_armor", "Hadvog Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was aketon_a
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
 ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],

["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor ],
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "haubergeon_a"
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth , [],[fac_kingdom_3]],

["lamellar_vest_guhulay", "Guhulay Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

 #NEW: was mail_shirt
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1544 , weight(22)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
#["lamellar_cuirass", "Lamellar Cuirass", [("lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs,0, 1020 , weight(25)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(9) ,imodbits_armor ],
# ["maille_orn_212", "Surcoat Green", [("maille_orn_212",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],

#NEW: was "brigandine_a"
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
# ["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 2410 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(0) ,imodbits_armor ],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2020 , weight(25)|abundance(20)|head_armor(0)|body_armor(48)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
 #NEW: was "reinf_jerkin"
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
#---------------Narf's_Plate_Armour_Pack_WB-----------------
["flamberge",         "Flamberge Zweihander", [("flamberge",0)], itp_type_polearm|itp_merchandise|itp_always_loot|itp_two_handed|itp_primary, itc_poleaxe|itcf_carry_sword_back,
 1123 , weight(3.75)|difficulty(11)|spd_rtng(77) | weapon_length(125)|swing_damage(50, cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["chapel_de_fer", "Chapel-de-Fer", [("chapel-de-fer",0)], itp_merchandise| itp_type_head_armor,0, 293 , weight(1.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["plate_mittens","Plate Mittens", [("plate_mittens_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1940, weight(1.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor],
#["bnw_gauntlets","Black and White Gauntlets", [("bnw_gauntlet_R",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 2240, weight(1.75)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
["bear_paw_shoes", "Bear Paw Shoes", [("bear_paw_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 150 , weight(1)|abundance(1000)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#["visored_sallet", "Visored Sallet", [("visored_sallet",0)], itp_merchandise| itp_type_head_armor   ,0, 638 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["visored_sallet", "Visored Sallet", [("pravar_lord_sallet",0)],  itp_type_head_armor|itp_fit_to_head,0,
 638 , weight(2)|abundance(0)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
##### from Lucass_OSP_v4.7####
["visored_sallet_coif", "Visored Sallet with Coif", [("salet_new_l",0)], itp_merchandise| itp_type_head_armor   ,0,
 738 , weight(2.25)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
##############################
["open_sallet", "Open Sallet", [("open_salet",0)], itp_merchandise| itp_type_head_armor   ,0,
 538 , weight(1.75)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["open_sallet_coif", "Open Sallet with Coif", [("open_sallet_coif",0)], itp_type_head_armor   ,0, 638 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["open_sallet_coif", "Open Sallet with Coif", [("open_salet_coif",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 638 , weight(1.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["combed_morion", "Combed Morion", [("combed_morion",0)], itp_merchandise| itp_type_head_armor   ,0, 538 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["combed_morion_blued", "Blued Combed Morion", [("combed_morion_blued",0)], itp_merchandise| itp_type_head_armor   ,0, 538 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["milanese_armour", "Milanese Armour", [("milanese_armour",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 9496 , weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22)|difficulty(11) ,imodbits_plate ],
["gothic_armour", "Gothic Armour", [("gothic_armour",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 9996 , weight(24)|abundance(100)|head_armor(8)|body_armor(58)|leg_armor(20)|difficulty(11) ,imodbits_plate ],
["bnw_armour1", "Black and White Armour", [("bnw_armour_stripes",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3696 , weight(19)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8) ,imodbits_plate ],
  #--------------------------------------------------------------
 #---------------narfs_transitional_armour_pack-----------------
 ["corrazina_red", "Corrazina", [("corrazina_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["corrazina_green", "Corrazina", [("corrazina_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["corrazina_grey", "Corrazina", [("corrazina_grey",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["churburg_13", "Full Plate", [("churburg_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],

["churburg_13_brass", "Ornate Full Plate", [("churburg_13_brass",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],

["churburg_13_mail", "Ornate Full Plate", [("churburg_13_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],



["early_transitional_heraldic", "Heavy Mail and Plate", [("early_transitional_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_early_transitional_heraldic", ":agent_no", ":troop_no")])]],

# ["early_transitional_blue", "Heavy Mail and Plate", [("early_transitional_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

# ["early_transitional_orange", "Heavy Mail and Plate", [("early_transitional_orange",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["early_transitional_white", "Heavy Mail and Plate", [("early_transitional_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["unicorne_armor", "Unicorne Knight Armor", [("unicorne_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(10) ,imodbits_plate ],

["splinted_greaves_spurs", "Splinted Greaves with Spurs", [("splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],

["shynbaulds", "Shynbaulds", [("shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],

["toh_shynbaulds", "Blue Steel Greaves", [("toh_shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1429 , weight(3.0)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(8) ,imodbits_plate ],

["steel_greaves", "Cased Greaves", [("steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],

["oniontop_bascinet", "Onion-top Bascinet", [("onion-top_bascinet",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["pigface_klappvisor", "Pigface Bascinet", [("pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["pigface_klappvisor_open", "Pigface Bascinet", [("pigface_klappvisor_open",0)], itp_merchandise|itp_type_head_armor   ,0, 1180 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],






["hounskull", "Hounskull Bascinet", [("hounskull",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["hounskull_red", "Hounskull Bascinet", [("hounskull_red",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],


["wisby_gauntlets_black","Splinted Leather Gauntlets", [("wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

["wisby_gauntlets_red","Splinted Leather Gauntlets", [("wisby_gauntlets_red_L",0)], itp_merchandise|itp_type_hand_armor,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

#["mail_gauntlets","Mail Gauntlets", [("mail_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 490, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],

["hourglass_gauntlets_ornate","Ornate Gauntlets", [("hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 1190, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

#["hourglass_gauntlets","Hourglass Gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

#---------------------------------------------------
#--------------------pa osp--------------------
["company_armor", "Company Full Armor", [("pa",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 11000 , weight(30)|abundance(2)|head_armor(6)|body_armor(68)|leg_armor(20)|difficulty(12) ,imodbits_plate ],
 ["company_helm", "Company Full Helm", [("ph",0)], itp_merchandise| itp_type_head_armor,0,
1100 , weight(3)|abundance(2)|head_armor(62)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#-------------------------------------------------------------------------
#--------------------ans_weapons osp--------------------
# ["berserker_shield", "Berserker Armor", [("berserkershield",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1200 , weight(12)|abundance(2)|head_armor(4)|body_armor(12)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
 ["mongol_cap_b_new", "Nomade Helm", [("mongol_cap_b_new",0)], itp_merchandise| itp_type_head_armor,0,
360 , weight(1.5)|abundance(40)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_cloth ],
["horn_bow",         "Golden Horde Bow", [("horn_bow",0),("horn_bow_carry", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
700 , weight(1.5)|abundance(2)|difficulty(4)|spd_rtng(60) | shoot_speed(76) | thrust_damage(30 ,pierce),imodbits_bow ],


#-------------------------------------------------------------------------
#--------------------men-at-arms armour pack-3673-1-0--------------------

["zitta_bascinet_novisor", "Bascinet", [("zitta_bascinet_novisor",0), ("inv_zitta_bascinet_novisor",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 479 , weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["zitta_bascinet", "Klappvisier Bascinet", [("zitta_bascinet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

#["brigandine_red", "Brigandine", [("brigandine_red",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 #1830 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_armor ],




 #--marina brigandine
 ["brigandine_leg", "Brigandine", [("brigandine_leg",0)], itp_type_body_armor|itp_covers_legs,0,
 2030 , weight(18)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 #--
["brigandine_blue", "Brigandine", [("brigandine_blue",0)], itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(17)|abundance(1)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(7) ,imodbits_armor ],


# ["brigandine_red_mail", "Brigandine", [("brigandine_red_mail",0)], itp_type_body_armor|itp_covers_legs,0,
 # 2130 , weight(20)|abundance(1)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_armor ],



["brigandine_blue_mail", "Brigandine", [("brigandine_blue_mail",0)], itp_type_body_armor|itp_covers_legs,0,
 2130 , weight(20)|abundance(80)|head_armor(0)|body_armor(50)|leg_armor(12)|difficulty(8) ,imodbits_armor ],

 ["brigandine_grey_mail", "Brigandine", [("brigandine_grey_mail",0)], itp_type_body_armor|itp_covers_legs,0,
 2130 , weight(20)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_armor ],

 ["brigandine_grey", "Brigandine", [("brigandine_grey",0)], itp_type_body_armor|itp_covers_legs,0,
 1130 , weight(20)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_armor ],
# ["hose_kneecops_red", "Woolen Hose with Kneecops", [("hose_kneecops_red",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 # 760 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(6) ,imodbits_cloth ],



["chapel_de_fer_mail1", "Chapel-de-Fer", [("chapel-de-fer_mail1",0), ("inv_chapel-de-fer_mail1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 425 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["chapel_de_fer_mail2", "Chapel-de-Fer", [("chapel-de-fer_mail2",0), ("inv_chapel-de-fer_mail2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 425 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["chapel_de_fer_mail3", "Chapel-de-Fer", [("chapel-de-fer_mail3",0), ("inv_chapel-de-fer_mail3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 425 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["chapel_de_fer_cloth1", "Chapel-de-Fer", [("chapel-de-fer_cloth1",0), ("inv_chapel-de-fer_cloth1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 325 , weight(2.2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["chapel_de_fer_cloth2", "Chapel-de-Fer", [("chapel-de-fer_cloth2",0), ("inv_chapel-de-fer_cloth2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 325 , weight(2.2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["chapel_de_fer_cloth3", "Chapel-de-Fer", [("chapel-de-fer_cloth3",0), ("inv_chapel-de-fer_cloth3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 325 , weight(2.2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#---------------------------------------------------
#----------------------- Baraban's_Items_mini-------
["plate_harness_02", "Plate Harness", [("plate_harness_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 10200 , weight(34)|abundance(10)|head_armor(0)|body_armor(64)|leg_armor(26)|difficulty(12) ,imodbits_plate ],



["heraldic_platemail_01", "Heraldic Platemail", [("platemail_heraldic_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8000 , weight(27)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(18)|difficulty(9) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_platemail_harness_heraldic_02", ":agent_no", ":troop_no")])]],

["heraldic_platemail_02", "Heraldic Platemail with Cloak", [("platemail_heraldic_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8000 , weight(27)|abundance(20)|head_armor(0)|body_armor(58)|leg_armor(18)|difficulty(9) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_platemail_harness_heraldic_02", ":agent_no", ":troop_no")])]],

["heraldic_plate_01", "Heraldic Plate Armour", [("platemail_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 9000 , weight(27)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(9) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_platemail_harness_heraldic", ":agent_no", ":troop_no")])]],

["heraldic_plate_02", "Heraldic Plate Armour", [("plate_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 10000 , weight(28)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_plate_harness_heraldic", ":agent_no", ":troop_no")])]],

 ["platemail_harness_05", "Platemail Harness", [("platemail_harness_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 10500 , weight(34)|abundance(2)|head_armor(0)|body_armor(64)|leg_armor(26)|difficulty(12) ,imodbits_plate ],

#---------------------------------------------------


#-----------------------historic lords volume-------


#---------------------------------------------------
#-----------norman items------------------------------
["norman_short_hauberk_blue", "Short Hauberk", [("norman_short_hauberk_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 700 , weight(17)|abundance(80)|head_armor(0)|body_armor(38)|leg_armor(6)|difficulty(7) ,imodbits_armor ],
 # ["segmented_helmet_redwhite", "Pravar Segmented Helmet", [("segmented_helmet_redwhite",0)], itp_merchandise| itp_type_head_armor   ,0,
 # 250 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_hauberk_a", "Northern Hauberk", [("norman_hauberk_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1420 , weight(20)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["galnar_hauberk", "Galnar Hauberk", [("galnar_hauberk",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1520 , weight(22)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(9) ,imodbits_armor ],
#-----------------------------------------------------

#-----------------------armo ?-------


#---------------------------------------------------
#--tohlobaria
 ["long_barded_horse_black","Long Barded Horse Black", [("long_barded_horse_black",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(10)|hit_points(122)|body_armor(42)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["knight_armor", "Knight Armor", [("toh_brigandine_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2630 , weight(26)|abundance(10)|head_armor(0)|body_armor(56)|leg_armor(18)|difficulty(12) ,imodbits_armor
 #,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_toh_brigandine_heraldic_new", ":agent_no", ":troop_no")])]
 ],
#

 ["bachelor_platemail", "Bachelor Platemail", [("bachelor",0)],itp_type_body_armor  |itp_covers_legs ,0,
 8000 , weight(28)|abundance(10)|head_armor(0)|body_armor(58)|leg_armor(24)|difficulty(12) ,imodbits_plate ],
 ["baron_plate1", "Baron Plate", [("baron_plate1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 10200 , weight(30)|abundance(10)|head_armor(0)|body_armor(60)|leg_armor(25)|difficulty(12) ,imodbits_plate ],

    ["armet1", "Armet", [("armet_01",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 2040 , weight(3)|abundance(20)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
     ["armet2", "Armet", [("armet_02",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 2045 , weight(3)|abundance(20)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
      ["armet1_open", "Armet", [("armet_03",0)], itp_merchandise|itp_type_head_armor,0,
 2040 , weight(3)|abundance(20)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
      ["armet2_open", "Armet", [("armet_04",0)], itp_merchandise|itp_type_head_armor,0,
 2045 , weight(3)|abundance(20)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],


 #["toh_shield", "Toh Shield",   [("toh_shield" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
#114 , weight(2)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(40)|shield_height(40),imodbits_shield,],


["toh_padded", "Padded Cloth", [("toh_padded",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["light_mail_over_padded", "Mail Over Gambeson", [("toh_mail",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 520 , weight(18)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(12)|difficulty(5) ,imodbits_armor],
 ["toh_mail_plates", "Mail Over Gambeson", [("toh_mail_plates",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 780 , weight(22)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(8) ,imodbits_armor],
  ["toh_breastplate", "Breastplate Over Mail", [("toh_breastplate",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1080 , weight(26)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(8) ,imodbits_plate],

  ["toh_cav_breastplate_a", "Breastplate Over Mail", [("toh_cav_breastplate_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1080 , weight(26)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(7) ,imodbits_plate],
  ["toh_cav_breastplate_b", "Breastplate Over Mail", [("toh_cav_breastplate_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1280 , weight(28)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8) ,imodbits_plate],
  ["toh_cav_breastplate_c", "Breastplate Over Mail", [("toh_cav_breastplate_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1580 , weight(30)|abundance(60)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(10) ,imodbits_plate],

 # ["padded_leather_and_mail", "Padded Leather And Mail", [("toh_leather_mail",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 # 580 , weight(18)|abundance(40)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
  # ["padded_leather_and_mail_s", "Padded Leather And Mail", [("toh_sergeant",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 # 680 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],


 ["toh_open_sallet", "Open Sallet", [("toh_open_sallet",0)], itp_merchandise| itp_type_head_armor   ,0,
 338 , weight(1.75)|abundance(80)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["toh_sallet_cloth", "Sallet With Padded Coif", [("toh_sallet_cloth",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
 438 , weight(2)|abundance(60)|head_armor(42)|body_armor(2)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["toh_sallet_mail", "Sallet With Mail Coif", [("toh_sallet_mail",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
 538 , weight(2.5)|abundance(50)|head_armor(46)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["toh_sallet_mail_mask", "Sallet With Mask", [("toh_sallet_mail_mask",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
 738 , weight(3)|abundance(50)|head_armor(50)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["pikeman_gambeson", "Pikeman Gambeson", [("pikeman_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 280 , weight(5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["pikeman_mail", "Pikeman Mail", [("pikeman_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 880 , weight(12)|abundance(10)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
 ["pikeman_brigandine", "Pikeman Brigandine", [("pikeman_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1080 , weight(14)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(8) ,imodbits_plate ],
 ["halberdier_brigandine", "Halberdier Brigandine", [("halberdier_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2080 , weight(18)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(10) ,imodbits_plate ],


  ["crossbowman_gambeson", "Crossbowman Gambeson", [("crossbowman_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 280 , weight(5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["crossbowman_mail", "Crossbowman Mail", [("crossbowman_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 880 , weight(12)|abundance(10)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
 ["crossbowman_brigandine", "Crossbowman Brigandine", [("crossbowman_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1080 , weight(14)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(8) ,imodbits_plate ],
 ["sapper_plate", "Sapper Plate", [("sapper_plate",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 3080 , weight(24)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(12) ,imodbits_plate ],


["pikeman_helmet", "Helmet With Coif", [("pikeman_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
 340 , weight(3)|abundance(80)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

 ["halberdier_helmet", "Helmet Full Coif", [("halberdier_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
 540 , weight(3.5)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],

["crossbowman_kettle_hat_a", "Kettlehat", [("crossbowman_kettle_hat_a",0)], itp_merchandise|itp_type_head_armor,0,
 320 , weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
 ["crossbowman_kettle_hat_b", "Kettlehat With Coif", [("crossbowman_kettle_hat_b",0)], itp_merchandise|itp_type_head_armor,0,
 420 , weight(2.60)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
 ["crossbowman_kettle_hat_c", "Kettlehat Full Coif", [("crossbowman_kettle_hat_c",0)], itp_merchandise|itp_type_head_armor,0,
 450 , weight(2.80)|abundance(60)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],


["sallet_rondel", "Salet With Rondels", [("salet_rondels",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 638 , weight(2.75)|abundance(60)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],



  ["horseman_gambeson", "Horseman Gambeson", [("horseman_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 280 , weight(5)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["horseman_mail", "Horseman Mail", [("horseman_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 880 , weight(12)|abundance(10)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
 ["horseman_brigandine", "Horseman Brigandine", [("horseman_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1080 , weight(14)|abundance(10)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(8) ,imodbits_plate ],
 ["cavalry_brigandine", "Cavalry Brigandine", [("cavalry_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2080 , weight(18)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(10) ,imodbits_plate ],

 ["lobarian_simple_helmet", "Simple Helmet", [("lobarian_simple_helmet",0)], itp_merchandise|itp_type_head_armor,0,
 220 , weight(2)|abundance(80)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
 ["lobarian_helmet_coif", "Helmet Padded Coif", [("lobarian_helmet_coif",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature,0,
 320 , weight(2.40)|abundance(60)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
 ["lobarian_helmet_mail_coif", "Helmet Mail Coif", [("lobarian_helmet_mail_coif",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature,0,
 550 , weight(3)|abundance(60)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
  ["lobarian_faceplate", "Faceplate Helmet", [("lobarian_faceplate",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature,0,
 750 , weight(3.5)|abundance(40)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate ],


 ["lobarian_bowman_aketon", "Bowman Aketon", [("lobarian_bowman_aketon",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(80)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["lobarian_archer_aketon", "Archer Aketon", [("lobarian_archer_aketon",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 800 , weight(12)|abundance(60)|head_armor(0)|body_armor(34)|leg_armor(5)|difficulty(7) ,imodbits_armor ],
 ["lobarian_archer_brigandine", "Archer Brigandine", [("lobarian_archer_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1680 , weight(16)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(10) ,imodbits_plate ],

 ["simple_chapel", "Simple Chapel", [("simple_chapel",0)], itp_merchandise|itp_type_head_armor,0,
 250 , weight(2.5)|abundance(80)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

 ["fur_vest", "Fur Vest", [("fur_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 380 , weight(7)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],


#--
#--toh heraldic
["heraldic_churburg", "Heraldic Churburg", [("heraldic_churburg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8028 , weight(27)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(10) ,imodbits_plate,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_churburg", ":agent_no", ":troop_no")])]],
["heraldic_corrazina", "Heraldic Corrazina", [("heraldic_corrazina",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 8028 , weight(27)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(10) ,imodbits_plate,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_corrazina", ":agent_no", ":troop_no")])]],


["heraldic_gothic_armor", "Heraldic Gothic Armor", [("heraldic_gothic_armor",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs ,0,
 5496 , weight(28)|abundance(5)|head_armor(10)|body_armor(56)|leg_armor(18)|difficulty(10) ,imodbits_plate ,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_gothic_armor", ":agent_no", ":troop_no")])]],

#--
 # ["demon_robe", "Demon Robe", [("demonrobe",0)], itp_type_body_armor  |itp_covers_legs ,0,
 # 5000 , weight(1)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(24) ,imodbits_cloth ],
 # ["nizh_outfit", "Nizh Outfit", [("nizh_outfit",0)],itp_type_body_armor  |itp_covers_legs ,0,
 # 11000 , weight(5)|abundance(2)|head_armor(0)|body_armor(70)|leg_armor(30)|difficulty(20) ,imodbits_plate ],
 # ["nizh_mask", "Nizh Mask", [("nizh_gasmaskguard",0)], itp_type_head_armor  ,0, 5000 ,
 # weight(0.5)|abundance(2)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(20) ,imodbits_plate ],
 # ["nizh_greaves", "Nizh Greaves", [("nizh_man_calf_l",0)],itp_type_foot_armor|itp_attach_armature,0,
 # 2240 , weight(1)|abundance(2)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(0) ,imodbits_armor ],

#--
#--civilian
["afirid_pants", "Afirid Tunic", [("afirid_pants",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
50 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(4)|difficulty(1) ,imodbits_armor ],

["borov_noble_outfit", "Noble Outfit", [("borov_noble_outfit",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 448 , weight(4)|abundance(10)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["borov_noble_outfit_cloak", "Noble Outfit", [("borov_noble_outfit_cloak",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 500 , weight(4.5)|abundance(2)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

 ["empress_dress", "Empress Dress", [("empress_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 550 , weight(3)|abundance(1)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

["afirid_rich_caftan_a", "Afirid Caftan", [("afirid_rich_caftan_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 348 , weight(3)|abundance(10)|head_armor(0)|body_armor(12)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["afirid_rich_caftan_b", "Afirid Caftan", [("afirid_rich_caftan_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 370 , weight(3)|abundance(10)|head_armor(0)|body_armor(12)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["afirid_noble_caftan", "Afirid Noble Caftan", [("afirid_noble_caftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 470 , weight(4)|abundance(5)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["afirid_noble_caftan_cloak", "Afirid Sultan Caftan", [("afirid_noble_caftan_cloak",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0,
 570 , weight(4)|abundance(1)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
#--
##PRAVAR ITEMS
 #--unique items
 ["pravar_crown", "Pravar King Helm", [("pravar_crown",0)], itp_type_head_armor|itp_attach_armature|itp_covers_head,0,
 6980 , weight(2.5)|abundance(5)|head_armor(60)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["hounskull_plume", "Hounskull Plumes", [("hounskull_plume",0)], itp_type_head_armor|itp_attach_armature|itp_covers_head,0,
 1280 , weight(2.5)|abundance(5)|head_armor(54)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 ["red_armour", "Red Armour", [("red_armour",0)],itp_type_body_armor  |itp_covers_legs ,0,
 10996 , weight(22)|abundance(10)|head_armor(8)|body_armor(60)|leg_armor(20)|difficulty(12) ,imodbits_plate ],
["red_lion_armor", "Pravar King Armor", [("pravar_king_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 12800 , weight(34)|abundance(2)|head_armor(6)|body_armor(59)|leg_armor(19)|difficulty(12) ,imodbits_plate ],
 #==pravar quartermaster BEGIN
 #--armors
 ["pravar_cuirasse", "Pravar Cuirasse", [("pravar_cuirasse",0)], itp_type_body_armor|itp_covers_legs,0,
 2030 , weight(23)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
 ["pravar_noble_armor", "Pravar Noble Armor", [("pravar_noble_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(20)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
 ["pravar_knight_armor", "Pravar Knight Armor", [("pravar_knight_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 4028 , weight(24)|abundance(10)|head_armor(0)|body_armor(54)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
  ["pravar_gambeson", "Pravar Gambeson", [("pravar_gambeson",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["pravar_haubergeon", "Pravar Haubergeon", [("pravar_haubergeon",0)], itp_type_body_armor  |itp_covers_legs ,0,
 883 , weight(18)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(7) ,imodbits_armor ],
["pravar_light_brigandine", "Pravar Brigandine", [("pravar_light_brigandine",0)], itp_type_body_armor|itp_covers_legs,0,
 1730 , weight(22)|abundance(20)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
["brigandine_red_mail", "Brigandine", [("brigandine_red_mail",0)], itp_type_body_armor|itp_covers_legs,0,
 2130 , weight(20)|abundance(1)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(10) ,imodbits_armor ],
  ["medium_brigandine_red", "Brigandine", [("medium_brigandine_red",0)], itp_type_body_armor|itp_covers_legs,0,
 1430 , weight(18)|abundance(1)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["red_cuirass", "Pravar Cuirass", [("red_cuirass",0)], itp_type_body_armor|itp_covers_legs,0,
 2430 , weight(24)|abundance(1)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(12) ,imodbits_armor ],
 ["light_brigandine_red", "Light Brigandine", [("light_brigandine_red",0)], itp_type_body_armor|itp_covers_legs,0,
 730 , weight(14)|abundance(1)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#--horses
["pravar_warhorse","Pravar Warhorse", [("pravar_warhorse",0)],itp_type_horse, 0,
 1300,abundance(5)|hit_points(122)|body_armor(36)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["pravar_knight_warhorse","Pravar Warhorse", [("pravar_knight_warhorse",0)],itp_type_horse, 0,
 1500,abundance(5)|hit_points(124)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(42)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["pravar_barded_horse","Pravar Barded Horse", [("pravar_barded_horse",0)],itp_type_horse, 0,
 1600,abundance(5)|hit_points(122)|body_armor(40)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
 ["pravar_plated_warhorse","Pravar Warhorse", [("pravar_plated_warhorse",0)],itp_type_horse, 0,
 1600,abundance(5)|hit_points(122)|body_armor(42)|difficulty(4)|horse_speed(38)|horse_maneuver(38)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["pravar_plated_knight_warhorse","Pravar Warhorse", [("pravar_plated_knight_warhorse",0)],itp_type_horse, 0,
 1800,abundance(5)|hit_points(124)|body_armor(46)|difficulty(4)|horse_speed(40)|horse_maneuver(40)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["pravar_plated_barded_horse","Pravar Barded Horse", [("pravar_plated_barded_horse",0)],itp_type_horse, 0,
 1900,abundance(5)|hit_points(122)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(38)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
#--helms
["pravar_kettlehat", "Pravar Kettlehat", [("col1_kettlehat1",0)], itp_type_head_armor,0,
 420 , weight(2.60)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["oniontop_bascinet_red", "Onion-top Bascinet", [("onion-top_bascinet_red",0)], itp_type_head_armor   ,0,
 479 , weight(2.25)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["pigface_klappvisor_red", "Pigface Bascinet", [("pigface_klappvisor_red",0)],  itp_type_head_armor|itp_covers_head,0,
 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["pigface_klappvisor_open_red", "Pigface Bascinet", [("pigface_klappvisor_open_red",0)], itp_type_head_armor   ,0,
 1180 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["pravar_simple_helmet", "Simple Helmet", [("pravar_simple_helmet",0)], itp_type_head_armor,0,
 220 , weight(2)|abundance(80)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
 ["pravar_helmet_coif", "Helmet Padded Coif", [("pravar_helmet_coif",0)], itp_type_head_armor| itp_attach_armature,0,
 320 , weight(2.40)|abundance(60)|head_armor(36)|body_armor(4)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
 ["pravar_helmet_mail_coif", "Helmet Mail Coif", [("pravar_helmet_mail_coif",0)], itp_type_head_armor| itp_attach_armature,0,
 550 , weight(3)|abundance(60)|head_armor(42)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
  ["pravar_faceplate", "Faceplate Helmet", [("pravar_faceplate",0)], itp_type_head_armor| itp_attach_armature,0,
 800 , weight(3.5)|abundance(40)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
  ["pravar_faceplate_b", "Faceplate Helmet", [("pravar_faceplate_b",0)], itp_type_head_armor| itp_attach_armature,0,
 750 , weight(3.5)|abundance(40)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 #--weapons
["pravar_poleaxe",         "Pravar Poleaxe", [("pravar_poleaxe",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe,
 484 , weight(4.5)|difficulty(10)|spd_rtng(75) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
#==pravar quartermaster END	(constant end !)
["pravar_items_end", "Pravar Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
##PRAVAR ITEMS END
##DIRIM ITEMS
#--unique
["emperator_helm", "Emperator Helm", [("emperator_helm",0)],  itp_type_head_armor |itp_covers_beard ,0,
 1850 , weight(3.5)|abundance(2)|head_armor(52)|body_armor(4)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["lioness_helm", "Lioness Helm", [("lioness_helm",0)], itp_type_head_armor|itp_attach_armature ,0,
 1050 , weight(3)|abundance(2)|head_armor(48)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#==Dirim quartermaster BEGIN
#--armors
["vardian_guard_armor", "Vardian Guard Armor", [("vardian_guard_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 4120 , weight(25)|abundance(40)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(12) ,imodbits_armor ],

["dirim_lamellar", "Old Empire Lamellar", [("dirim_lamellar",0)], itp_type_body_armor  |itp_covers_legs ,0,
 2120 , weight(25)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(9) ,imodbits_plate ],
["dirim_jerkin", "Gambeson", [("dirim_armor_0",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 800 , weight(18)|abundance(40)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_plate ],
["dirim_footman_armor", "Dirim Footman Armor", [("dirim_armor_1",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1000 , weight(18)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
["dirim_regular_armor", "Dirim Regular Armor", [("dirim_armor_2",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
["dirim_veteran_armor", "Dirim Veteran Armor", [("dirim_armor_3",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1800 , weight(24)|abundance(30)|head_armor(0)|body_armor(50)|leg_armor(12)|difficulty(9) ,imodbits_plate ],
["pretorian_armor", "Pretorian Armor", [("pretorian_armor",0)], itp_type_body_armor |itp_covers_legs  ,0,
2000 , weight(26)|abundance(10)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(11) ,imodbits_plate ],
["bowman_armor", "Bowman Armor", [("bowman_armor",0)],  itp_type_body_armor|itp_covers_legs,0,
 1430 , weight(16)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
["archer_armor", "Archer Padded( Armor", [("archer_armor",0)],  itp_type_body_armor|itp_covers_legs,0,
 730 , weight(14)|abundance(60)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(7) ,imodbits_cloth ],
["dirim_breastplate", "Dirim Cuirass", [("dirim_breastplate",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(26)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
["dirim_plate_armor", "Dirim  Heavy Cuirass", [("dirim_plate_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4800 , weight(30)|abundance(8)|head_armor(0)|body_armor(52)|leg_armor(22)|difficulty(12) ,imodbits_plate ],
["dirim_general_armor", "Dirim General Armor", [("dirim_general_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4850 , weight(30)|abundance(2)|head_armor(0)|body_armor(52)|leg_armor(22)|difficulty(12) ,imodbits_plate ],
#--helms
["cataphract_helm", "Cataphract Helm", [("cataphract",0)],itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
 700 , weight(2)|abundance(60)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["pronoiar_helm", "Pronoiar Helm", [("pronoiar_helm",0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature  ,0,
  1024 , weight(3.5)|abundance(10)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["legion_helmet", "Legion Helmet", [("rathos_hellenistic_helm",0)], itp_type_head_armor   ,0,
 400 , weight(2)|abundance(20)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["dirim_helmet", "Dirim Helmet", [("dirim_helmet",0)], itp_type_head_armor  ,0,
 200 , weight(1.5)|abundance(20)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["dirim_footman_helmet", "Dirim Footman Helmet", [("dirim_footman_helmet",0)],  itp_type_head_armor|itp_attach_armature  ,0,
 400 , weight(1.7)|abundance(20)|head_armor(36)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["dirim_regular_helm", "Dirim Regular Helm", [("dirim_regular_helm",0)],  itp_type_head_armor|itp_attach_armature  ,0,
 500 , weight(2.5)|abundance(20)|head_armor(46)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dirim_veteran_helm", "Dirim Veteran Helm", [("dirim_veteran_helm",0)],  itp_type_head_armor|itp_attach_armature  ,0,
 600 , weight(3)|abundance(20)|head_armor(50)|body_armor(4)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["pretorian_helm", "Pretorian Helm", [("pretorian_helm",0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature ,0,
990 , weight(3)|abundance(10)|head_armor(52)|body_armor(4)|leg_armor(0)|difficulty(10)  ,imodbits_plate ],
["dirim_archer_helmet", "Dirim Archer Helmet", [("dirim_archer_helmet",0)],  itp_type_head_armor|itp_attach_armature  ,0,
 400 , weight(1.7)|abundance(20)|head_armor(36)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["dirim_bowman_helmet", "Dirim Bowman Helmet", [("dirim_bowman_helmet",0)],  itp_type_head_armor|itp_attach_armature  ,0,
 500 , weight(2.7)|abundance(10)|head_armor(44)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dirim_general_helm", "Dirim General Helm", [("dirim_general_helm",0)], itp_type_head_armor|itp_attach_armature ,0,
2190 , weight(3)|abundance(2)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10)  ,imodbits_plate ],
#--weapons
 ["luc_partisan",  "Dirim Poleaxe", [("luc_partisan",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(170)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["italian_scorpion_guisarme",  "Dirim Guisarme", [("italian_scorpion_guisarme",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 550 , weight(5.5)|difficulty(9)|spd_rtng(68) | weapon_length(180)|swing_damage(40 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm ],
 ["halberd_no1",  "Dirim Halberd", [("halberd_no1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 560 , weight(5)|difficulty(9)|spd_rtng(70) | weapon_length(160)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 ["poleaxe_no3",  "Dirim Poleaxe", [("poleaxe_no3",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(4)|difficulty(9)|spd_rtng(75) | weapon_length(145)|swing_damage(45 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["luc_german_winged_mace",         "Winged Mace", [("luc_german_winged_mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
380 , weight(2.5)|difficulty(7)|spd_rtng(88) | weapon_length(70)|swing_damage(26, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
#--horse
["romanhalfcata","Cataphract Warhorse", [("romanhalfcata",0)], itp_type_horse, 0,
 1500,abundance(10)|hit_points(122)|body_armor(30)|difficulty(4)|horse_speed(42)|horse_maneuver(40)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
#==Dirim quartermaster END
["dirim_items_end", "Dirim Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
["fluted_helmet_mail", "Fluted Helmet", [("fluted_helmet_mail",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature  ,0,
 555 , weight(2.5)|abundance(50)|head_armor(45)|body_armor(4)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["fluted_helmet", "Fluted Helmet", [("fluted_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
 355 , weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["dirim_sword", "Dirim cavalry Sword", [("dirim_sword",0),("roman_cav_sword_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
310 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(92)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],
["lobarian_sword_a", "Lobarian Short Sword", [("lobarian_sword_a",0),("lobarian_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 443 , weight(1)|difficulty(0)|spd_rtng(98) | weapon_length(72)|swing_damage(28, cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["dirim_half_greaves", "Dirim Half Greaves", [("dirim_half_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 110 , weight(1.5)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor ],
["dirim_greaves", "Dirim Greaves", [("dirim_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 250 , weight(2)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["dirim_mail_greaves", "Dirim Mail Greaves", [("dirim_mail_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 450 , weight(2.5)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(6) ,imodbits_armor ],
 ["leather_boots_black", "Leather Boots Black", [("leather_boots_black",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
 ["archers_hatchet",         "Hatchet", [("archers_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
70 , weight(2)|difficulty(0)|spd_rtng(98) | weapon_length(45)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["bowman_hatchet",         "Hatchet", [("bowman_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar,
140 , weight(2)|difficulty(0)|spd_rtng(96) | weapon_length(50)|swing_damage(24 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
##DIRIM ITEMS END
##IMIFIR ITEMS
 ["imifir_padded_coif", "Imifir Padded Coif", [("imifir_padded_coif",0)], itp_merchandise| itp_type_head_armor   ,0, 6 ,
 weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #--half_sword
 ["claymore", "Claymore", [("claymore",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_next_item_as_melee, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(12)|spd_rtng(85)| weapon_length(110)|swing_damage(38 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
 ["claymore", "Claymore", [("claymore",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur, itc_staff|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|abundance(20)|difficulty(12)|spd_rtng(98)| weapon_length(110)|swing_damage(35 , pierce) | thrust_damage(35 ,  pierce),imodbits_sword_high ],
 ["corseque",  "Corseque", [("corseque",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
 480 , weight(5)|abundance(20)|difficulty(12)|spd_rtng(70) | weapon_length(180)|swing_damage(34 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
 ["bilomadal_armor", "Bilomadal Armor", [("bilomadal_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2228 , weight(20)|abundance(5)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(10) ,imodbits_armor ],
 ["bilomadal_warhammer",         "Bilomadal Warhammer", [("bilomadal_warhammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_axe_left_hip ,
490 , weight(3)|difficulty(12)|spd_rtng(89) | weapon_length(92)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["imifir_fauchard_fork",         "Imifir Fauchard Fork", [("fauchard_fork_no1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe,
 284 , weight(4)|difficulty(8)|spd_rtng(77) | weapon_length(185)|swing_damage(32 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["imifir_axe",         "imifir_axe", [("arquebuser_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
540 , weight(2)|abundance(10)|difficulty(0)|spd_rtng(90) | weapon_length(60)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["duc_sallet", "Duc's Sallet", [("duc_sallet",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 825 ,
 weight(2.8)|abundance(5)|head_armor(46)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["imifir_breastplate", "Cuirass", [("imifir_breastplate",0)], itp_type_body_armor|itp_covers_legs,0,
 1030 , weight(20)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_armor ],
["green_gambeson_a", "Green Gambeson", [("green_gambeson_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["brigandine_green", "Brigandine", [("brigandine_green",0)], itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(17)|abundance(1)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["brigandine_green_mail", "Brigandine", [("brigandine_green_mail",0)], itp_type_body_armor|itp_covers_legs,0,
 2130 , weight(20)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(8) ,imodbits_armor ],
 ["brigandine_plackart", "Brigandine Plackart Gorget", [("brigandine_plackart",0)], itp_type_body_armor|itp_covers_legs,0,
 2430 , weight(18)|abundance(1)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["heavy_brigandine_plackart", "Heavy Brigandine Plackart", [("heavy_brigandine_plackart",0)], itp_type_body_armor|itp_covers_legs,0,
 2630 , weight(20)|abundance(1)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(10) ,imodbits_armor ],
 ["brigandine_plackart_gorget", "Brigandine Plackart Gorget", [("brigandine_plackart_gorget",0)], itp_type_body_armor|itp_covers_legs,0,
 3030 , weight(22)|abundance(1)|head_armor(4)|body_armor(52)|leg_armor(20)|difficulty(12) ,imodbits_armor ],
["milanese_armor_outfit", "Rich Plate Armor", [("milanese_armor_outfit",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9596 , weight(26)|abundance(2)|head_armor(0)|body_armor(60)|leg_armor(22)|difficulty(12) ,imodbits_plate ],
["rich_plate_armor", "Rich Plate Armor", [("rich_plate_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9396 , weight(25)|abundance(2)|head_armor(0)|body_armor(58)|leg_armor(22)|difficulty(12) ,imodbits_plate ],
 ["imifir_ducal_armor", "Imifir Ducal Armor", [("imifir_ducal_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 10600 , weight(30)|abundance(2)|head_armor(0)|body_armor(59)|leg_armor(19)|difficulty(18) ,imodbits_plate ],
["sallet_mask", "Sallet With Mask", [("sallet_mask",0)], itp_merchandise| itp_type_head_armor   ,0,
 638 , weight(2)|abundance(2)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["imifir_rich_jacket", "Rich Jacket", [("imifir_rich_jacket",0)], itp_merchandise| itp_type_body_armor| itp_covers_legs  |itp_civilian ,0,
 250 , weight(3)|abundance(10)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["imifir_rich_jacket_1", "Rich Jacket", [("imifir_rich_jacket_1",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0,
 280 , weight(3.5)|abundance(5)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["imifir_rich_jacket_2", "Rich Jacket", [("imifir_rich_jacket_2",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0,
 260 , weight(3.2)|abundance(5)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
##IMIFIR ITEMS END
##GUHULAY ITEMS
  ["guhulay_padded", "Light Padded Armor", [("gi_padded",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 300 , weight(12)|abundance(60)|head_armor(0)|body_armor(28)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],
   ["guhulay_padded_mail", "Guhulay Mail", [("gi_padded_mail",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 700 , weight(16)|abundance(50)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
    ["guhulay_padded_mail_lamellar", "Guhulay Lamellar", [("gi_lamellar",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 900 , weight(20)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
    ["guhulay_lamellar_armor", "Guhulay Heavy Lamellar", [("gi_padded_mail_lamellar",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1900 , weight(20)|abundance(50)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
  ["g_padded", "Light Padded Armor", [("g_padded",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 300 , weight(12)|abundance(60)|head_armor(0)|body_armor(28)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],
   ["g_padded_mail", "Guhulay Mail", [("g_padded_mail",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 700 , weight(16)|abundance(50)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
    ["g_coat_of_plates_a", "Guhulay Lamellar", [("g_coat_of_plates_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1800 , weight(20)|abundance(50)|head_armor(0)|body_armor(46)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
    ["g_coat_of_plates_b", "Guhulay Heavy Lamellar", [("g_coat_of_plates_b",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2200 , weight(24)|abundance(50)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
 ["guhulay_lamellar_armor_b", "Guhulay Lamellar Armor", [("guhulay_lamellar_armor",0)],itp_type_body_armor |itp_covers_legs  ,0,
3000 , weight(25)|abundance(2)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(11) ,imodbits_plate ],
 ["guhulay_coat_of_plates_a", "Guhulay Coat Of Plates", [("guhulay_coat_of_plates_a",0)],itp_type_body_armor |itp_covers_legs  ,0,
2800 , weight(24)|abundance(2)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
 ["guhulay_noble_armor", "Guhulay Coat Of Plates", [("guhulay_noble_armor",0)],itp_type_body_armor |itp_covers_legs  ,0,
3200 , weight(24)|abundance(2)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
 ["guhulay_mirza_armor", "Guhulay Coat Of Plates", [("guhulay_mirza_armor",0)],itp_type_body_armor |itp_covers_legs  ,0,
3400 , weight(24)|abundance(2)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
["guhulay_noyan_armor", "Guhulay Heavy Armor", [("guhulay_noyan_armor",0)],itp_type_body_armor |itp_covers_legs  ,0,
5400 , weight(24)|abundance(2)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
["khan_armor", "Khan Armor", [("khan_armor",0)],itp_type_body_armor |itp_covers_legs  ,0,
6400 , weight(26)|abundance(2)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(12) ,imodbits_plate ],
["gi_watchman_padded_mail", "Guhulay Mail", [("gi_watchman_padded_mail",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 700 , weight(16)|abundance(50)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
 ["guhulay_helmet_a", "Guhulay Helm", [("guhulay_helmet_a",0)], itp_type_head_armor    ,0,
 233 , weight(2)|abundance(80)|head_armor(28)|body_armor(0)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_b", "Guhulay Helm Padded Coif", [("guhulay_helmet_b",0)], itp_type_head_armor  |itp_attach_armature  ,0,
 333 , weight(2)|abundance(70)|head_armor(36)|body_armor(2)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_c", "Guhulay Helm Mail Coif", [("guhulay_helmet_c",0)], itp_type_head_armor  |itp_attach_armature   ,0,
 633 , weight(4)|abundance(60)|head_armor(42)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_d", "Guhulay Helm Full Coif", [("guhulay_helmet_d",0)], itp_type_head_armor  |itp_covers_beard   ,0,
 833 , weight(4)|abundance(60)|head_armor(48)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
 ["guhulay_helmet_e", "Guhulay Helm", [("guhulay_helmet_e",0)], itp_type_head_armor    ,0,
 233 , weight(2)|abundance(80)|head_armor(28)|body_armor(0)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_f", "Guhulay Helm Padded Coif", [("guhulay_helmet_f",0)], itp_type_head_armor  |itp_attach_armature  ,0,
 333 , weight(2)|abundance(70)|head_armor(36)|body_armor(2)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_g", "Guhulay Helm Mail Coif", [("guhulay_helmet_g",0)], itp_type_head_armor  |itp_attach_armature   ,0,
 633 , weight(4)|abundance(60)|head_armor(42)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_h", "Guhulay Helm full Coif", [("guhulay_helmet_h",0)], itp_type_head_armor  |itp_covers_beard|itp_attach_armature   ,0,
 833 , weight(4)|abundance(60)|head_armor(46)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_i", "Guhulay Helm full Coif", [("guhulay_helmet_i",0)], itp_type_head_armor  |itp_covers_beard|itp_attach_armature   ,0,
 2033 , weight(4)|abundance(5)|head_armor(44)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
  ["guhulay_helmet_j", "Guhulay Helm full Coif", [("guhulay_helmet_j",0)], itp_type_head_armor  |itp_covers_beard|itp_attach_armature   ,0,
 2233 , weight(4)|abundance(5)|head_armor(46)|body_armor(4)|leg_armor(0) ,imodbits_plate ],
 ["guhulay_battle_axe",  "Guhulay Battle Axe", [("guhulay_battle_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
 420 , weight(6)|difficulty(10)|spd_rtng(70) | weapon_length(135)|swing_damage(38 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 ["wyu_axe", "Wyu Axe", [("wyu_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
200 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(83)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["guhulay_horseman_scale", "Guhulay Scale", [("guhulay_horseman_scale",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
2600 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
 ["guhulay_horseman_armor", "Guhulay Armor", [("guhulay_horseman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
3600 , weight(24)|abundance(30)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
  ["guhulay_elite_helm", "Guhulay Elite Helm", [("guhulay_elite_helm",0)], itp_type_head_armor |itp_merchandise|itp_covers_beard |itp_attach_armature  ,0,
 533 , weight(3)|abundance(40)|head_armor(48)|body_armor(2)|leg_armor(0) ,imodbits_plate ],
 ["guhulay_noble_helmet", "Guhulay Noble Helmet", [("guhulay_noble_helmet",0)], itp_type_head_armor |itp_merchandise   ,0,
 533 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
 ["guhulay_noble_helm_2", "Guhulay Noble Helm", [("guhulay_noble_helm_2",0)], itp_type_head_armor |itp_merchandise   ,0,
 533 , weight(2)|abundance(10)|head_armor(44)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
 ["guhulay_khan_mask", "Khan Mask", [("guhulay_khan_mask",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
 1050 , weight(3)|abundance(2)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
  ["hafted_blade_1",         "Hafted Blade", [("luc_hafted_blade_1",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["hafted_blade_2",         "Hafted Blade", [("luc_hafted_blade_2",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["hafted_blade_3",         "Hafted Blade", [("luc_hafted_blade_3",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["hafted_blade_4",         "Hafted Blade", [("luc_hafted_blade_4",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["hafted_blade_5",         "Hafted Blade", [("luc_hafted_blade_5",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["hafted_blade_6",         "Hafted Blade", [("luc_hafted_blade_6",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 450 , weight(3.25)|difficulty(8)|spd_rtng(83) | weapon_length(152)|swing_damage(34 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
   ["guhulay_hafted_blad",         "Guhulay Hafted Blad", [("guhulay_hafted_blad",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 500 , weight(3.5)|difficulty(10)|spd_rtng(81) | weapon_length(166)|swing_damage(26 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 #--wyu
["wyu_sword", "Wyu Sword", [("bb_wyu_sword",0),("bb_wyu_sword_scabard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 500 , weight(1.7)|difficulty(0)|spd_rtng(98) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["tunic_lamellar", "Tunic Lamellar", [("tunic_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
860 , weight(16)|abundance(10)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
["wyu_ring_sword", "Wyu Ring Sword", [("wyu_ring_sword",0),("wyu_ring_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 110 , weight(1.20)|difficulty(0)|spd_rtng(98) | weapon_length(86)|swing_damage(29 , cut),imodbits_sword_high ],
 ["wyu_light_crossbow", "Wyu Light Crossbow", [("wyu_light_crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
180 , weight(2.5)|difficulty(0)|spd_rtng(50) | shoot_speed(32) | thrust_damage(30 ,  pierce)|max_ammo(1),imodbits_crossbow ],
##GUHULAY ITEMS END
##HADVOG ITEMS
["hadvog_warhorse","Hadvog Warhorse", [("hadvog_warhorse",0)], itp_type_horse, 0,
 1524,abundance(10)|hit_points(125)|body_armor(38)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(26)|horse_scale(112),imodbits_horse_basic|imodbit_champion],
["nord_warhorse","Hadvog Warhorse", [("nord_warhorse",0)],itp_type_horse, 0,
 1300,abundance(5)|hit_points(122)|body_armor(36)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],
["nord_plated_warhorse","Hadvog Plated Warhorse", [("nord_plated_warhorse",0)],itp_type_horse, 0,
 1600,abundance(5)|hit_points(122)|body_armor(42)|difficulty(4)|horse_speed(38)|horse_maneuver(38)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],
 ["large_lshield", "large leathercovered shield", [("leathershield_large",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
250 , weight(4.7)|hit_points(120)|body_armor(20)|spd_rtng(54)|shield_width(52),imodbits_shield ],
["mid_lshield", "medium leathercovered shield", [("leathershield_medium",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
240 , weight(4.0)|hit_points(110)|body_armor(20)|spd_rtng(61)|shield_width(47),imodbits_shield ],
["sml_lshield", "small leathercovered shield", [("leathershield_small",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
200 , weight(3.0)|hit_points(100)|body_armor(20)|spd_rtng(80)|shield_width(40),imodbits_shield ],
["large_rwshield", "large reinforced wooden shield", [("woodenshield_large",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
380 , weight(4.7)|hit_points(130)|body_armor(22)|spd_rtng(54)|shield_width(52),imodbits_shield ],
["mid_rwshield", "medium reinforced wooden shield", [("woodenshield_medium",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
360 , weight(4.1)|hit_points(120)|body_armor(22)|spd_rtng(60)|shield_width(47),imodbits_shield ],
["sml_rshield", "small reinforced wooden shield", [("woodenshield_small",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
340 , weight(3.1)|hit_points(110)|body_armor(22)|spd_rtng(78)|shield_width(40),imodbits_shield ],
["large_hadvog_shield", "Hadvog Shield", [("hadvog_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
390 , weight(4.8)|hit_points(140)|body_armor(23)|spd_rtng(52)|shield_width(53),imodbits_shield ],
["colored_hadvog_shield", "Colored Hadvog Shield", [("hadvog_shield_colored",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
390 , weight(4.8)|hit_points(140)|body_armor(23)|spd_rtng(52)|shield_width(53),imodbits_shield ],
 ["hadvog_gambeson", "Hadvoh Gambeson", [("hadvog_gambeson",0)], itp_type_body_armor  |itp_covers_legs ,0,
 320 , weight(8)|abundance(10)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["hadvog_gambeson_mail", "Hadvoh Gambeson Mail", [("hadvog_gambeson_mail",0)], itp_type_body_armor  |itp_covers_legs ,0,
 620 , weight(14)|abundance(5)|head_armor(0)|body_armor(36)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
  ["hadvog_coat_of_plates_a", "Coat Of Plates", [("hadvog_coat_of_plates_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 820 , weight(22)|abundance(80)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
  ["hadvog_coat_of_plates_b", "Coat Of Plates", [("hadvog_coat_of_plates_b",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1120 , weight(26)|abundance(80)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(12) ,imodbits_plate ],
["nasal_helmet_cloth_blue", "Nasal Helmet", [("nasal_helmet_cloth_blue",0)], itp_type_head_armor| itp_attach_armature,0,
 260 , weight(2.5)|abundance(80)|head_armor(40)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nasal_helmet_mail_blue", "Nasal Helmet", [("nasal_helmet_mail_blue",0)],  itp_type_head_armor| itp_attach_armature,0,
 360 , weight(3)|abundance(60)|head_armor(44)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["big_nasal_helmet", "Big Nasal Helmet", [("big_nasal_helmet",0)],  itp_type_head_armor| itp_attach_armature,0,
 460 , weight(3.2)|abundance(60)|head_armor(46)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["hadvog_faceplate_a", "Faceplate", [("hadvog_faceplate_a",0)],  itp_type_head_armor|itp_covers_beard| itp_attach_armature,0,
 560 , weight(4)|abundance(60)|head_armor(48)|body_armor(4)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 ["norman_helm_1", "Hadvog Helm", [("normanhelmcoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 350 , weight(1.60)|abundance(60)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helm_coif", "Hadvog Helm With Coif", [("normanhelmbalaclavacoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 360 , weight(1.80)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["norman_helm_full_coif", "Hadvog Helm Full Coif", [("normanhelmfullcoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 370 , weight(2)|abundance(60)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
  ["norman_faceplate_a", "Hadvog Faceplate", [("norman_faceplate_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,
 670 , weight(3)|abundance(50)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 ["nord_battle_axe",         "Nord Battle Axe", [("nord_battle_axe",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
340 , weight(4)|difficulty(9)|spd_rtng(90) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["royal_huskarl_armor", "Berserk Armor", [("royal_huskarl_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(26)|abundance(5)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(12) ,imodbits_plate ],
   ["hadvog_champion_helm", "Hadvog Champion Helm", [("royal_huskarl",0)], itp_type_head_armor|itp_attach_armature,0,
 570 , weight(2.5)|abundance(10)|head_armor(50)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["huskarl_axe", "Huskarl's Axe", [("huskarl_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 750 , weight(2.2)|difficulty(10)|spd_rtng(94) | weapon_length(76)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["huskarl_axe_a", "Huskarl's Axe", [("huskarl_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 650 , weight(2.2)|difficulty(10)|spd_rtng(94) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["hadvog_coat_of_plates", "Hadvog Coat Of Plates", [("hadvog_coat_of_plates",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3300 , weight(24)|abundance(20)|head_armor(0)|body_armor(50)|leg_armor(14)|difficulty(12) ,imodbits_plate ],
  ["coat_of_plates_blue", "Coat Of Plates Blue", [("coat_of_plates_blue",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3000 , weight(26)|abundance(20)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(12) ,imodbits_plate ],
["heraldic_jarl_armor", "Heraldic Jarl Armor", [("heraldic_jarl_armor",0)],  itp_type_body_armor|itp_covers_legs,0,
 3230 , weight(24)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(12) ,imodbits_plate,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_jarl_armor", ":agent_no", ":troop_no")])]],
["hadvog_cuir_bouilli", "Cuir Bouilli", [("wei_xiadi_nord_cuir_bouilli",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(17)|difficulty(8) ,imodbits_armor ],

 ["hadvog_king_helm", "Hadvog Chieftain Helmet", [("hadvog_king_helm",0)],  itp_type_head_armor|itp_attach_armature ,0, 3880 ,
 weight(2.25)|abundance(1)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["chieftain_armour", "Chieftain Armour", [("huscarl_armour",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(26)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(10) ,imodbits_armor ],
["nord_ornate_visored_helmet", "Nord Ornate Visored Helmet", [("nord_ornate_visored_helmet",0)],  itp_type_head_armor|itp_attach_armature ,0,
 680 , weight(2.5)|abundance(60)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nord_coat_of_plates", "Nord Coat Of Plates", [("nord_coat_of_plates",0)], itp_type_body_armor  |itp_covers_legs ,0,
 3300 , weight(24)|abundance(10)|head_armor(0)|body_armor(53)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
 ["nord_coat_of_plates_pelt", "Nord Coat Of Plates With Pelt", [("nord_coat_of_plates_pelt",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3300 , weight(25)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
 ["nord_splinted_greaves", "Nordic Splinted Greaves", [("nord_splinted_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 800 , weight(2.75)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_armor ],
##HADVOG ITEMS END
##BOROVOD ITEMS
 ["hussar_armor", "Hussar Armor", [("prince_hussard",0)], itp_type_body_armor  |itp_covers_legs ,0,
 4300 , weight(22)|abundance(5)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(12) ,imodbits_plate ],
["knyaz_kuyak", "Knight's kuyak", [("knyaz_kuyak",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1595 , weight(24)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(24)|difficulty(10) ,imodbits_armor ],
["knyaz_kuyak_1", "Knight's kuyak", [("knyaz_kuyak_1",0)],itp_type_body_armor  |itp_covers_legs ,0,
1395 , weight(24)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(9) ,imodbits_armor ],
["knyaz_kuyak_2", "Knight's kuyak", [("knyaz_kuyak_2",0)], itp_type_body_armor  |itp_covers_legs ,0,
1495 , weight(24)|abundance(10)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(9) ,imodbits_armor ],
["knyaz_armor", "Borovod Knight Armor", [("knyaz_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2300 , weight(24)|abundance(5)|head_armor(0)|body_armor(52)|leg_armor(24)|difficulty(11) ,imodbits_plate ],
["boyar_armor", "Boyar Armor", [("boyar_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2400 , weight(24)|abundance(1)|head_armor(0)|body_armor(54)|leg_armor(24)|difficulty(12) ,imodbits_plate ],
["borovod_lamellar_armor", "Borovod Noble Lamellar", [("borovod_lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1600 , weight(24)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(24)|difficulty(10) ,imodbits_armor ],
["bardiche_master_armor", "Borovod Elite Armor", [("borovod_elite_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2680 , weight(28)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(22)|difficulty(12) ,imodbits_plate ],
["kapalin", "Kapalin", [("kapalin2",0)], itp_type_head_armor,0,
 470 , weight(2.5)|abundance(10)|head_armor(48)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["hussar_sword", "Hussar_sword", [("hussar_sword",0),("hussar_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.5)|abundance(5)|difficulty(7)|spd_rtng(98) | weapon_length(98)|swing_damage(30 , cut) | thrust_damage(28 ,  pierce),imodbits_sword  ,[], [fac_kingdom_2]],
["borovod_guard_armor", "Borovod Guard Armor", [("borovod_armor_1",0)], itp_type_body_armor  |itp_covers_legs ,0,
 880 , weight(20)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["borovod_guard_helmet", "Borovod Guard Helmet", [("byzantion",0)], itp_merchandise|itp_type_head_armor,0,
 320 , weight(1.60)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["archer_heavy_armor", "Archer Heavy Armor", [("archer_heavy_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1063 , weight(22)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
["borovod_kuyak", "Borovod Kuyak", [("borovod_kuyak",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1080 , weight(20)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
["rich_padded", "rich_padded", [("rich_padded",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(12)|abundance(80)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["facecover_kettlehat", "Facecover Kettlehat", [("facecovermail_kettlehat_s",0)], itp_merchandise|itp_type_head_armor,0,
 350 , weight(1.75)|abundance(60)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["borovod_glaive",         "Borovod Glaive", [("borovod_glaive",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 552 , weight(5)|difficulty(0)|spd_rtng(75) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["borovod_light_charger","Borovod Light Charger", [("borovod_light_charger",0)], itp_type_horse, 0,
 1211,abundance(50)|hit_points(120)|body_armor(32)|difficulty(4)|horse_speed(40)|horse_maneuver(46)|horse_charge(30)|horse_scale(111),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2]],
["hussar_horse","Hussar Horse", [("hussar_horse",0)],itp_type_horse, 0,
 1300,abundance(30)|hit_points(120)|body_armor(36)|difficulty(4)|horse_speed(42)|horse_maneuver(46)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2]],
["lamellar_armor_horse","Lamellar Armor Horse", [("lamellar_armor_horse",0)], itp_type_horse, 0,
 1500,abundance(10)|hit_points(122)|body_armor(40)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2]],
["mail_armor_horse","Mail Armor Horse", [("mail_armor_horse",0)], itp_type_horse, 0,
 1400,abundance(10)|hit_points(122)|body_armor(38)|difficulty(4)|horse_speed(40)|horse_maneuver(42)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2]],
 ["rus_padded_cloth", "Rus Padded Cloth", [("mailruss",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(80)|head_armor(0)|body_armor(22)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["padded_cloth_mails", "Padded Cloth And Mails ", [("mailrusss",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(20)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["rus_mails", "Rus Mails", [("rusmails",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 880 , weight(20)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heavy_leather_kuyak", "Heavy Leather Kuyak", [("heavy_leather_kuyak",0)], itp_type_body_armor  |itp_covers_legs ,0,
920 , weight(24)|abundance(20)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
##BOROVOD ITEMS END
#--galnar
["galnar_chief_axe", "Galnar Chief Axe", [("luc_waronehandedaxec",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 290 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(70)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#--
##AFIRID ITEMS
["afirid_inf_armor", "Afirid Padded Armor", [("afirid_inf_armor",0)],  itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
300 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(5) ,imodbits_cloth ],
["afirid_inf_armor_a", "Afirid Mail", [("afirid_inf_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
800 , weight(16)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["afirid_inf_armor_b", "Afirid Lamellar", [("afirid_inf_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
1300 , weight(20)|abundance(50)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["afirid_inf_armor_c", "Afirid Heavy Lamellar", [("afirid_inf_armor_c",0)],  itp_type_body_armor |itp_covers_legs  ,0,
1800 , weight(26)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(9) ,imodbits_plate ],
["afirid_cav_armor_a", "Afirid Lamellar", [("afirid_cav_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
1300 , weight(20)|abundance(50)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["afirid_cav_armor_b", "Afirid Lamellar", [("afirid_cav_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
1500 , weight(22)|abundance(40)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(8) ,imodbits_plate ],
["afirid_ran_armor_a", "Afirid Light Lamellar", [("afirid_ran_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
700 , weight(14)|abundance(80)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(6) ,imodbits_armor ],
["afirid_ran_armor_b", "Afirid Light Lamellar", [("afirid_ran_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
1500, weight(14)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(6) ,imodbits_armor ],
["afirid_nob_armor_a", "Afirid Mail And Plates", [("afirid_nob_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
2600 , weight(18)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8) ,imodbits_plate ],
["afirid_nob_armor_b", "Afirid Mail And Plates", [("afirid_nob_armor_b",0)], itp_type_body_armor |itp_covers_legs ,0,
3200 , weight(24)|abundance(30)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_plate ],
["afirid_emir_armor", "Afirid Emir Armor", [("afirid_emir_armor",0)], itp_type_body_armor |itp_covers_legs  ,0,
7400 , weight(24)|abundance(2)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(10) ,imodbits_plate ],
["afirid_emir_armor_b", "Afirid Double Mail", [("afirid_emir_armor_b",0)], itp_type_body_armor |itp_covers_legs  ,0,
2200 , weight(26)|abundance(2)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(12) ,imodbits_plate ],
["afirid_cavalry_mail", "Afirid Cavalry Mail", [("afirid_cavalry_mail",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0,
1400 , weight(20)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["afirid_cavalry_lamellar", "Afirid Cavalry Lamellar", [("afirid_cavalry_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
1800 , weight(24)|abundance(30)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(9) ,imodbits_armor ],
["southern_lamellar", "Southern Lamellar", [("southern_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
1600 , weight(26)|abundance(30)|head_armor(0)|body_armor(48)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
["afirid_crossbow", "Afirid Crossbow", [("afirid_crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow,
180 , weight(2.3)|difficulty(0)|spd_rtng(46) | shoot_speed(30) | thrust_damage(28 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["sultan_helm", "Sultan Helm", [("sultan_helm",0)], itp_type_head_armor   ,0, 1055 ,
 weight(2.5)|abundance(1)|head_armor(48)|body_armor(2)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["sultan_armor", "Sultan's Armor", [("sultan_armor",0)], itp_type_body_armor|itp_covers_legs  ,0,
7048 , weight(24)|abundance(1)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(10) ,imodbits_armor ],
["turban_helmet", "Turban Helmet", [("moorish_helmet_a",0)], itp_type_head_armor,0, 550 ,
 weight(2.50)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["turban_helmet_1", "Turban Helmet", [("moorish_helmet_c",0)], itp_type_head_armor,0, 550 ,
 weight(2.50)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 # ["afirid_mail_shirt", "Afirid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 # 1400 , weight(19)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
 # ["afirid_mail_shirt_green", "Afirid Mail Shirt", [("afirid_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 # 1400 , weight(19)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
 ["sultan_guard_armor", "Sultan's Guard Armor", [("sultan_guard",0)], itp_type_body_armor|itp_covers_legs ,0,
4848 , weight(22)|abundance(10)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(12) ,imodbits_plate ],
["sultan_guard_helm", "Sultan Guard Helm", [("sultan_guard_helm",0)], itp_merchandise| itp_type_head_armor   ,0,
 855 , weight(2.8)|abundance(5)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 ["sultan_charger","Sultan Charger", [("sultan_charger",0)], itp_merchandise|itp_type_horse, 0,
 1911,abundance(10)|hit_points(125)|body_armor(40)|difficulty(5)|horse_speed(42)|horse_maneuver(45)|horse_charge(36)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["southern_axe", "Southern Axe", [("nordic_axe_no1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
80 , weight(2)|difficulty(1)|spd_rtng(99) | weapon_length(56)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["afirid_long_lamellar", "Afirid Long Lamellar", [("afirid_long_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
2800 , weight(24)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(14)|difficulty(10) ,imodbits_armor ],
["afirid_emir_lamellar", "Afirid Emir Lamellar", [("afirid_emir_lamellar",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
3200 , weight(24)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(10) ,imodbits_armor ],
["afirid_light_lamellar", "Afirid Light Lamellar", [("afirid_light_lamellar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(18)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(6)|difficulty(5) ,imodbits_armor],
["afirid_light_lamellar_1", "Afirid Light Lamellar", [("afirid_light_lamellar_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1400 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(6) ,imodbits_armor],
 ["charif_armor", "Afirid Noble Armor", [("charif_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
3200 , weight(25)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(10) ,imodbits_plate ],
["afirid_helmet_inf_1", "Afirid Infantry Helmet", [("afirid_helmet_inf_1",0)], itp_merchandise| itp_type_head_armor, 0,
 480 , weight(2.5)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["afirid_helmet_inf_2", "Afirid Infantry Helmet", [("afirid_helmet_inf_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 540 , weight(3)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_helmet_inf_3", "Afirid Face Helmet", [("afirid_helmet_inf_3",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard    ,0,
 680 , weight(3.2)|abundance(30)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_helmet_cav_1", "Afirid Cavalry Helmet", [("afirid_helmet_cav_1",0)], itp_merchandise| itp_type_head_armor, 0,
 480 , weight(2.5)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["afirid_helmet_cav_2", "Afirid Cavalry Helmet", [("afirid_helmet_cav_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 540 , weight(3)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_conical_helmet_1", "Afirid Conical Helmet", [("afirid_conical_helmet_1",0)], itp_merchandise| itp_type_head_armor, 0,
 480 , weight(2.5)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["afirid_conical_helmet_2", "Afirid Conical Helmet", [("afirid_conical_helmet_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 540 , weight(3)|abundance(40)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_face_helm_n_1", "Afirid Face Helm", [("afirid_face_helm_n_1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard, 0,
 700 , weight(3.2)|abundance(5)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_face_helm_n_2", "Afirid Face Helm", [("afirid_face_helm_n_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 700 , weight(3.2)|abundance(5)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_caid_helmet_1", "Afirid Noble Helmet", [("afirid_caid_helmet_1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard, 0,
 650 , weight(3.2)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["afirid_caid_helmet_2", "Afirid Noble Helmet", [("afirid_caid_helmet_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 650 , weight(3.2)|abundance(10)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["afirid_charif_helmet_1", "Afirid Noble Helmet", [("afirid_charif_helmet_1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard, 0,
 600 , weight(3.2)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_charif_helmet_2", "Afirid Noble Helmet", [("afirid_charif_helmet_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 600 , weight(3.2)|abundance(10)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_emir_helmet_1", "Afirid Noble Helmet", [("afirid_emir_helmet_1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard, 0,
 600 , weight(3.2)|abundance(5)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_emir_helmet_2", "Afirid Noble Helmet", [("afirid_emir_helmet_2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard ,0,
 600 , weight(3.2)|abundance(5)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["afirid_sallet", "Afirid Sallet", [("afirid_sallet",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard   ,0,
 638 , weight(3.5)|abundance(20)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["turban_mail_a", "Turban Mail", [("turban_mail_a",0)], itp_merchandise| itp_type_head_armor   ,0,
 180 , weight(1.5)|abundance(80)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["afirid_warhorse","Afirid War Horse", [("afirid_warhorse",0)], itp_merchandise|itp_type_horse, 0,
 1224,abundance(10)|hit_points(120)|body_armor(30)|difficulty(4)|horse_speed(40)|horse_maneuver(42)|horse_charge(26)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_warhorse_lamellar","Afirid War Horse", [("afirid_warhorse_lamellar",0)], itp_merchandise|itp_type_horse, 0,
 1424,abundance(5)|hit_points(120)|body_armor(35)|difficulty(4)|horse_speed(39)|horse_maneuver(41)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_noble_warhorse","Afirid War Horse", [("afirid_noble_warhorse",0)], itp_merchandise|itp_type_horse, 0,
 1624,abundance(3)|hit_points(120)|body_armor(40)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_emir_warhorse","Afirid Emir Warhorse", [("afirid_emir_warhorse",0)], itp_merchandise|itp_type_horse, 0,
 2424,abundance(1)|hit_points(124)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_warhorse_deco","Afirid War Horse", [("afirid_warhorse_deco",0)], itp_merchandise|itp_type_horse, 0,
 1250,abundance(10)|hit_points(120)|body_armor(30)|difficulty(4)|horse_speed(40)|horse_maneuver(42)|horse_charge(26)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_warhorse_lamellar_deco","Afirid War Horse", [("afirid_warhorse_lamellar_deco",0)], itp_merchandise|itp_type_horse, 0,
 1450,abundance(5)|hit_points(120)|body_armor(35)|difficulty(4)|horse_speed(39)|horse_maneuver(41)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_noble_warhorse_deco","Afirid War Horse", [("afirid_noble_warhorse_deco",0)], itp_merchandise|itp_type_horse, 0,
 1650,abundance(3)|hit_points(120)|body_armor(40)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_emir_warhorse_deco","Afirid Emir Warhorse", [("afirid_emir_warhorse_deco",0)], itp_merchandise|itp_type_horse, 0,
 2450,abundance(1)|hit_points(124)|body_armor(46)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["afirid_spears_a",         "Afirid Trident Spear", [("afirid_spears_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur|itp_two_handed, itc_pike,
 120 , weight(2.2)|difficulty(0)|spd_rtng(115) | weapon_length(180)|swing_damage(34 , pierce) | thrust_damage(34 ,  pierce),imodbits_polearm ],
["afirid_spears_b",         "Afirid  Spear", [("afirid_spears_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur|itp_two_handed, itc_pike,
 100 , weight(2)|difficulty(0)|spd_rtng(115) | weapon_length(180)|swing_damage(34 , pierce) | thrust_damage(34 ,  pierce),imodbits_polearm ],
["afirid_long_spear",         "Long Spear", [("afirid_long_spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur|itp_two_handed, itc_pike,
 198 , weight(2.5)|difficulty(0)|spd_rtng(115) | weapon_length(180)|swing_damage(34 , pierce) | thrust_damage(34 ,  pierce),imodbits_polearm ],
["afirid_medium_spear",         "Infantry Spear", [("afirid_medium_spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_staff,
 84 , weight(1.8)|difficulty(0)|spd_rtng(120) | weapon_length(130)|swing_damage(36 , pierce) | thrust_damage(36 ,  pierce),imodbits_polearm ],
##AFIRID ITEMS END
##ATIA ITEMS
["atian_short_sword", "Atian Short Sword", [("atian_short_sword",0),("atian_short_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 343 , weight(1)|difficulty(0)|spd_rtng(100) | weapon_length(72)|swing_damage(28, cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["atian_padded_vest", "atian_padded_vest", [("atian_padded_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 360 , weight(6)|abundance(20)|head_armor(0)|body_armor(28)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["baretunic_blue", "Baretunic Blue", [("baretunic_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian  ,0,
 50 , weight(2)|abundance(10)|head_armor(0)|body_armor(6)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["atian_colonial_tunic", "Baretunic Blue", [("atian_colonial_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian  ,0,
 150 , weight(6)|abundance(5)|head_armor(0)|body_armor(20)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
  ["colonial_ranger_tunic", "Colonial Ranger Tunic", [("colonial_ranger_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs  ,0,
 150 , weight(6)|abundance(5)|head_armor(0)|body_armor(20)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
 ["colonial_torso", "Colonial Torso", [("colonial_torso",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 600 , weight(12)|abundance(5)|head_armor(0)|body_armor(44)|leg_armor(4)|difficulty(6) ,imodbits_plate ],
  ["colonial_pikeman_armor", "Colonial Pikeman Armor", [("colonial_pikeman_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 700 , weight(16)|abundance(5)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(8) ,imodbits_plate ],
 ["black_boots", "Black Boots", [("black_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
	 50 , weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["atian_guisarme",         "Atian Guisarme", [("atian_guisarme",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 400 , weight(7)|difficulty(9)|spd_rtng(72) | weapon_length(180)|swing_damage(42 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
  ["musketeer_tunic_1", "Colonial Ranger Tunic", [("musketeer_tunic_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs  ,0,
 150 , weight(6)|abundance(5)|head_armor(0)|body_armor(15)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
  ["musketeer_tunic_2", "Colonial Ranger Tunic", [("musketeer_tunic_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs  ,0,
 150 , weight(6)|abundance(5)|head_armor(0)|body_armor(15)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

 ["plated_charger_6","Plated Charger", [("WPlatedCharger6",0)], itp_merchandise|itp_type_horse, 0, 12600,
 abundance(10)|hit_points(125)|body_armor(60)|difficulty(5)|horse_speed(37)|horse_maneuver(44)|horse_charge(40)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
 ["plated_Charger_1","Plated Charger", [("WPlatedCharger1",0)], itp_merchandise|itp_type_horse, 0, 12600,
 abundance(10)|hit_points(125)|body_armor(60)|difficulty(5)|horse_speed(37)|horse_maneuver(44)|horse_charge(40)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],


##ATIA ITEMS END
##DESERT ITEMS
["desert_turban_blue", "Desert Turban", [("desert_turban",0)], itp_merchandise|itp_type_head_armor | itp_covers_beard  ,0,
 90 , weight(1)|abundance(50)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ,[], [fac_kingdom_3, fac_kingdom_6]],
["desert_armor_a", "Desert Padded Armor", [("desert_armor_a",0)],  itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
300 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(5) ,imodbits_cloth ,[], [fac_kingdom_3, fac_kingdom_6]],
["desert_armor_b", "Desert Light Lamellar", [("desert_armor_b",0)],  itp_merchandise|itp_type_body_armor |itp_covers_legs  ,0,
700 , weight(14)|abundance(80)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(6) ,imodbits_armor ,[], [fac_kingdom_3, fac_kingdom_6]],
##DESERT ITEMS END
##DOOMCALL ITEMS
 ["doomcall_cap", "Doomcall Cap", [("doomcall_cap",0)], itp_type_head_armor |itp_merchandise   ,0,
 233 , weight(1)|abundance(5)|head_armor(24)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#DOOMCALL ITEMS END
##NEW ORDER ITEMS
["new_order_plate", "new_order_plate", [("white_order_plate",0)],itp_type_body_armor  |itp_covers_legs ,0,
 5000 , weight(28)|abundance(10)|head_armor(0)|body_armor(56)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
 ["new_order_brigandine", "White Order Brigandine", [("white_order_brigandine",0)], itp_type_body_armor|itp_covers_legs,0,
 2130 , weight(20)|abundance(1)|head_armor(0)|body_armor(50)|leg_armor(10)|difficulty(8) ,imodbits_armor ],
#NEW ORDER END
##MERCENARIES ITEMS
    ["aketon", "Aketon", [("aketon",0)],  itp_type_body_armor|itp_covers_legs,0,
	 425 , weight(12)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
	["long_gambeson", "Gambeson", [("long_gambeson",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian,0,
	 360 , weight(10)|abundance(80)|head_armor(0)|body_armor(26)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
	["padded_jack", "Padded Jack", [("gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
	 315 , weight(6)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
	 ["common_breastplate_orange", "Breastplate Over Gambeson", [("common_breastplate_orange",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 725 , weight(16)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(6)|difficulty(0) ,imodbits_armor ],
	["common_breastplate_green", "Breastplate Over Gambeson", [("common_breastplate_green",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 825 , weight(18)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
	["common_breastplate_blue", "Breastplate Over Gambeson", [("common_breastplate_blue",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 825 , weight(18)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
	["common_breastplate_red", "Breastplate Over Gambeson", [("common_breastplate_red",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 740 , weight(16)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(0) ,imodbits_armor ],
    ["common_breastplate_brown", "Breastplate Over Gambeson", [("common_breastplate_brown",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 825 , weight(18)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
	["common_breastplate", "Plates Over Gambeson", [("common_breastplate",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1025 , weight(24)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(20)|difficulty(0) ,imodbits_plate ],

	["common_cuirass_orange", "Cuirass Over Gambeson", [("common_cuirass_orange",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1525 , weight(26)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
	["common_cuirass_green", "Cuirass Over Gambeson", [("common_cuirass_green",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1425 , weight(25)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(0) ,imodbits_plate ],
	["common_cuirass_blue", "Cuirass Over Gambeson", [("common_cuirass_blue",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1225 , weight(24)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
	["common_cuirass_red", "Cuirass Over Gambeson", [("common_cuirass_red",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1325 , weight(24)|abundance(80)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(0) ,imodbits_armor ],
	["common_cuirass_brown", "Cuirass Over Gambeson", [("common_cuirass_brown",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1325 , weight(24)|abundance(80)|head_armor(0)|body_armor(44)|leg_armor(8)|difficulty(0) ,imodbits_armor ],
	["common_cuirass", "Plates Over Gambeson", [("common_cuirass",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1425 , weight(25)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(16)|difficulty(0) ,imodbits_plate ],

	 ["long_gambeson_mail", "Mail Over Gambeson", [("long_gambeson_mail",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1225 , weight(24)|abundance(80)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0) ,imodbits_armor ],
     ["nord_breastplate_over_gambeson", "Breastplate Over Gambeson", [("nord_breastplate_over_gambeson",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 925 , weight(18)|abundance(80)|head_armor(0)|body_armor(36)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
	["nord_cuirass_over_gambeson", "Breastplate Over Gambeson", [("nord_cuirass_over_gambeson",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1325 , weight(26)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(20)|difficulty(0) ,imodbits_armor ],
	["nord_breastplate_over_mail", "Breastplate Over Mail", [("nord_breastplate_over_mail",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1725 , weight(28)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
	["nord_cuirass_over_mail", "Cuirass Over Mail", [("nord_cuirass_over_mail",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 1925 , weight(32)|abundance(50)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
	["nord_heavy_cuirass_over_mail", "Heavy Cuirass Over Mail", [("nord_heavy_cuirass_over_mail",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 2425 , weight(34)|abundance(40)|head_armor(0)|body_armor(50)|leg_armor(22)|difficulty(0) ,imodbits_plate ],

	["common_breastplate_orange", "Breastplate Over Gambeson", [("common_breastplate_orange",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs,0,
	 925 , weight(16)|abundance(80)|head_armor(0)|body_armor(38)|leg_armor(16)|difficulty(0) ,imodbits_armor ],

    ["padded_coif_mail", "Padded Coif Mail", [("padded_coif_mail",0)], itp_merchandise| itp_type_head_armor   ,0,
    40, weight(1.5)|abundance(80)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
    ["short_coat_of_plates_a", "Leather Coat Of Plates", [("short_coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
    1690 , weight(30)|abundance(50)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(12) ,imodbits_armor ],
    ["short_coat_of_plates_b", "Coat Of Plates", [("short_coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
    1590 , weight(28)|abundance(70)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(11) ,imodbits_armor ],
    ["short_coat_of_plates_c", "Coat Of Plates", [("short_coat_of_plates_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
    1090 , weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(9) ,imodbits_armor ],

    #south
    ["south_long_armor_a", "South Mail Armor", [("south_long_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    800 , weight(16)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
    ["south_long_armor_b", "South Lamellar", [("south_long_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1300 , weight(20)|abundance(50)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
    ["south_long_armor_c", "South Lamellar", [("south_long_armor_c",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1300 , weight(20)|abundance(50)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
    ["south_long_armor_d", "South Heavy Lamellar", [("south_long_armor_d",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1800 , weight(26)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(9) ,imodbits_plate ],

    ["south_armor_a", "South Armor", [("south_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    900 , weight(16)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
    ["south_armor_b", "South Armor", [("south_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1300 , weight(20)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
    ["south_armor_c", "South Armor", [("south_armor_c",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    900 , weight(16)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
    ["south_armor_d", "South Armor", [("south_armor_d",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1100 , weight(18)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(8) ,imodbits_armor ],

    ["steppe_armor_a", "South Armor", [("steppe_armor_a",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    900 , weight(16)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
    ["steppe_armor_b", "South Armor", [("steppe_armor_b",0)],  itp_type_body_armor |itp_covers_legs  ,0,
    1300 , weight(20)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["arabian_mail_shirt_b", "Southern Mail Shirt", [("arabian_mail_shirt_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
2600 , weight(22)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
  ["southern_light_armor", "Southern Light Armor", [("southern_light_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 990 , weight(15)|abundance(60)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],


 ["merc_padded_armor", "Heavy Padded Armor", [("merc_padded_armor",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 930 , weight(16)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
 ["darenbay_armor", "Darenbay Armor", [("darenbay_armor",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1930 , weight(20)|abundance(20)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(10) ,imodbits_plate ],
 ["darenbay_armor_1", "Darenbay Armor", [("darenbay_armor_1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1930 , weight(20)|abundance(20)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(10) ,imodbits_plate ],

["tares_helmet_0", "Tares Helmet", [("tares_helmet_0",0)], itp_merchandise| itp_type_head_armor,0, 490 ,
 weight(3)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["tares_helmet_1", "Tares Helmet Open", [("tares_helmet_1",0)], itp_merchandise| itp_type_head_armor,0, 690 ,
 weight(3.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["tares_helmet_2", "Tares Helmet Open", [("tares_helmet_2",0)], itp_merchandise| itp_type_head_armor,0, 690 ,
 weight(3.5)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

 ["lobarian_helmet_4", "Bascinet Helmet", [("lobarian_helmet_4",0)], itp_merchandise| itp_type_head_armor,0,
340 , weight(2)|abundance(70)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["breastplate_over_gambeson", "Breastplate Over Gambeson", [("breastplate_over_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1030 , weight(26)|abundance(80)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_plate ],

 ["common_sword_a", "Sword", [("common_sword_a",0),("common_sword_a_scabbard_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 263 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
  ["common_sword_b", "Sword", [("common_sword_b",0),("common_sword_b_scabbard_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 273 , weight(1.6)|difficulty(0)|spd_rtng(94) | weapon_length(75)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
  ["common_sword_c", "Sword", [("common_sword_c",0),("common_sword_c_scabbard_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 283 , weight(1.8)|difficulty(0)|spd_rtng(92) | weapon_length(80)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
  ["common_sword_d", "Sword", [("common_sword_d",0),("common_sword_e_scabbard_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 293 , weight(2)|difficulty(0)|spd_rtng(90) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
  ["common_sword_e", "Sword", [("common_sword_e",0),("common_sword_e_scabbard_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 283 , weight(1.8)|difficulty(0)|spd_rtng(92) | weapon_length(82)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
##MERCENARIES ITEMS END
#--civilian
["fur_coat_green", "Fur Coat", [("fur_coat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],

 ["noble_doublet", "Arming Doublet", [("noble_doublet",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 375 , weight(6)|abundance(4)|head_armor(0)|body_armor(24)|leg_armor(5)|difficulty(0) ,imodbits_armor ],
 ["pravar_doublet", "Arming Doublet", [("pravar_doublet",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 375 , weight(6)|abundance(4)|head_armor(0)|body_armor(24)|leg_armor(5)|difficulty(0) ,imodbits_armor ],

 ["noble_doublet_cloack", "Arming Doublet", [("noble_doublet_cloack",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 475 , weight(7)|abundance(2)|head_armor(0)|body_armor(26)|leg_armor(5)|difficulty(0) ,imodbits_armor ],
  ["pravar_doublet_cloack", "Arming Doublet", [("pravar_doublet_cloack",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 475 , weight(7)|abundance(2)|head_armor(0)|body_armor(26)|leg_armor(5)|difficulty(0) ,imodbits_armor ],
#--
#--knight's maces
 ["knights_winged_mace_1h",         "Knight's Winged Mace", [("knights_winged_mace_1h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
1080 , weight(3.5)|difficulty(12)|spd_rtng(90) | weapon_length(68)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
 ["war_hammer_no4",         "War Hammer", [("war_hammer_no4",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
1080 , weight(3)|difficulty(12)|spd_rtng(92) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
 ["sapper_warhammer",         "War Hammer", [("knights_warhammer_no1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
980 , weight(3)|difficulty(10)|spd_rtng(93) | weapon_length(60)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["bastard_mace",         "Bastard Mace", [("bastard_mace_no1",0)], itp_crush_through|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_morningstar|itcf_carry_mace_left_hip,
805 , weight(3.5)|difficulty(10)|spd_rtng(90) | weapon_length(84)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],



["horsemans_axe_no3", "Horsemans Axe", [("horsemans_axe_no3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 650 , weight(2.0)|difficulty(10)|spd_rtng(94) | weapon_length(78)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["ball_mace_no2",         "Ball Mace", [("ball_mace_no2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
680 , weight(3)|difficulty(11)|spd_rtng(90) | weapon_length(72)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["morningstar_no1",         "Morningstar", [("morningstar_no1",0)], itp_crush_through|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
905 , weight(4)|difficulty(12)|spd_rtng(88) | weapon_length(62)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["arming_winged_mace",         "Arming Winged Mace", [("arming_winged_mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
1080 , weight(4)|difficulty(12)|spd_rtng(88) | weapon_length(75)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["byzantine_mace_3",         "Kalisos Winged Mace", [("byzantine_mace_3",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_morningstar|itcf_carry_mace_left_hip,
1080 , weight(4)|difficulty(12)|spd_rtng(90) | weapon_length(71)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],


["morningstar_2",         "Morningstar", [("morningstar_2",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
1020 , weight(4)|difficulty(12)|spd_rtng(90) | weapon_length(70)|swing_damage(36 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["morningstar_3",         "Morningstar", [("morningstar_3",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
620 , weight(3)|difficulty(10)|spd_rtng(94) | weapon_length(66)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["light_knightly_axe", "Light Knightly Axe", [("light_knightly_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 850 , weight(2.0)|difficulty(11)|spd_rtng(92) | weapon_length(80)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["warhammer_ita",         "warhammer", [("warhammer_ita",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_mace_left_hip,
600 , weight(2.5)|difficulty(8)|spd_rtng(92) | weapon_length(80)|swing_damage(26 , pierce) | thrust_damage(26 ,  pierce),imodbits_mace ],

["gothic_hammer",         "Knight Hammer", [("gothic_hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
980 , weight(4)|difficulty(12)|spd_rtng(88) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["gothic_puncture_mace",         "Puncture Mace", [("gothic_puncture_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
1080 , weight(3)|difficulty(12)|spd_rtng(88) | weapon_length(80)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


 ["long_war_club",         "Long War Club", [("luc_long_war_club_blunt",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 150 , weight(2)|difficulty(8)|spd_rtng(90) | weapon_length(140)|swing_damage(30 , blunt) | thrust_damage(10 ,  blunt),imodbits_polearm ],


 ["spiked_war_club_no1",         "Spiked War Club", [("spiked_war_club_no1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(3)|difficulty(7)|spd_rtng(88) | weapon_length(72)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

 ["italian_warhammer",         "Infantry Warhammer", [("italian_warhammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
580 , weight(3.5)|difficulty(8)|spd_rtng(90) | weapon_length(60)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

 ["one_handed_war_axe_spiked",         "War Axe With Spikes", [("one_handed_war_axe_spiked",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
480 , weight(3.5)|difficulty(8)|spd_rtng(90) | weapon_length(68)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_mace ],

 ["knights_war_axe_1h",         "Lobarian War Axe", [("knights_war_axe_1h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
580 , weight(3.5)|difficulty(9)|spd_rtng(92) | weapon_length(60)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_mace ],

 ["dirim_infantry_mace",         "Dirim Infantry Mace", [("dirim_infantry_mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
480 , weight(3)|difficulty(7)|spd_rtng(93) | weapon_length(60)|swing_damage(26, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],


#--
#--weapons
##one-handed axes
["borov_axe", "Borov Axe", [("luc_waronehandedaxec",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(8)|spd_rtng(88) | weapon_length(70)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#--



##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
##armors_e
# ["guhulay_elite_armor", "Guhulay Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["borovod_elite_armor", "Borovod Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["afirid_elite_armor", "Afirid Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


 ["afirid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["afirid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["afirid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["afirid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 74 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 260 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["afirid_leather_armor", "Afirid Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
 # ["desert_robe", "Desert Robe", [("desert_robe_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 66 , weight(1)|abundance(70)|head_armor(0)|body_armor(14)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],


 ["afirid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 990 , weight(15)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(0) ,imodbits_armor ],
["arabian_armor_b", "Afirid Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_armor],
 # ["afirid_mail_shirt", "Afirid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 # 1400 , weight(19)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
2900 , weight(24)|abundance(40)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
#-----------------fredsbunchofarmours OSP--------------------------------
["sar_haubergeon", "Southern Haubergeon", [("sar_haubergeon",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
1000 , weight(18)|abundance(60)|head_armor(0)|body_armor(32)|leg_armor(4)|difficulty(6) ,imodbits_armor ],
["sar_pants", "Southern Tunic", [("sar_pants",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
50 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(4)|difficulty(1) ,imodbits_armor ],
###KHERGIT
# ["guhulay_leather_armor", "Guhulay Leather Armor", [("guhulay_leather_armor",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0,
 # 150 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["guhulay_mail_c", "Guhulay Mail", [("khergit_mail_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
2600 , weight(22)|abundance(10)|head_armor(0)|body_armor(48)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["guhulay_vest_a", "Guhulay Vest", [("khergit_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 56 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["guhulay_vest_c", "Guhulay Vest Blue", [("khergit_vest_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 56 , weight(1)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ##dirim archers##
   ["forest_padded_leather", "Forest Padded Leather", [("padded_leather_c.lod1",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
#-----------------------------------------------------------
#-----------------al mansur OSP--------------------------------
#["andalusian_helmet_a", "Southern Noble Helmet", [("andalusian_helmet_a",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["andalusian_helmet_b", "Southern Noble Helmet", [("andalusian_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["andalusian_helmet_f", "Light Southern Noble Helmet", [("andalusian_helmet_f",0)], itp_merchandise| itp_type_head_armor   ,0, 420 , weight(2.5)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["andalusian_helmet_d", "Full Southern Helmet", [("andalusian_helmet_d",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["mamluk_helmet", "Southern Helmet With Mails", [("mamluk_helmet",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(40)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["moorish_helmet_b", "Full Southern Helmet", [("moorish_helmet_b",0)], itp_type_head_armor,0, 600 , weight(2.60)|abundance(40)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["saracen_helmet_f", "Light Southern Helmet", [("saracen_helmet_f",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 260 , weight(2.5)|abundance(80)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#["gilded_nasal_helmet", "Gilded Nasal Helmet", [("gilded_nasal_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(40)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["simple_iberian_helmet", "Simple Helmet", [("simple_iberian_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 200 , weight(2.5)|abundance(80)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["iberian_helmet", "Helmet", [("iberian_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 200 , weight(2.5)|abundance(80)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],

#["simple_nasal_helmet", "Simple Nasal Helmet", [("simple_nasal_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 210 , weight(2.7)|abundance(80)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
#["nasal_helmet_1", "Nasal Helmet", [("nasal_helm",0)], itp_merchandise| itp_type_head_armor   ,0, 310 , weight(3)|abundance(70)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],

#["simple_phrygian_helmet", "Simple Phrygian Helmet", [("simple_phrygian_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 210 , weight(2.7)|abundance(80)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
#["phrygian_helmet", "Phrygian Helmet", [("phrygian_helmet",0)], itp_merchandise| itp_type_head_armor   ,0, 310 , weight(3)|abundance(70)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],

["castillan_helm", "Order knight Helm", [("castillan_helm",0)], itp_type_head_armor,0, 500 , weight(4)|abundance(2)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#-----------------------------------------------------------

#-----------le_medieval_swords-----
["order_sword_1", "Order Arming Sword", [("le_german_sword_b",0),("le_german_sword_b_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|abundance(10)|difficulty(0)|spd_rtng(101) | weapon_length(90)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
#-----------------------------------

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],


["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_b", "Hood", [("hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_c", "Hood", [("hood_c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_d", "Hood", [("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0,
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0,
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0,
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_helmet", "Hadvog Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["guhulay_lady_hat", "Guhulay Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["guhulay_lady_hat_b", "Guhulay Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["afirid_felt_hat", "Afirid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 28 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 38 , weight(1.50)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["afirid_warrior_cap", "Afirid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["desert_helmet", "Desert Helmet", [("desert_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 180 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_helmet1", "Afirid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 290 , weight(2.50)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_mail_coif", "Afirid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 430 , weight(3)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["afirid_veiled_helmet", "Afirid Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 810 , weight(3.50)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_archer_helmet", "Hadvog Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0, 40 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_veteran_archer_helmet", "Hadvog Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0, 70 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_footman_helmet", "Hadvog Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0, 150 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_fighter_helmet", "Hadvog Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 240 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_huscarl_helmet", "Hadvog Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor   ,0, 390 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["hadvog_warlord_helmet", "Hadvog Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0, 880 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["borovod_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 50 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_fur_helmet", "Borovod Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 110 , weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 230 , weight(2.50)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0, 360 , weight(2.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_noble_helmet", "Borovod Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0, 710, weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_war_helmet", "Borovod War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0, 820 , weight(3)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["borovod_mask", "Borovod War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 950 , weight(3.50)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(20)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#-------------------Dejawolf Helmets pack---------------------
["kettlehat_full_coif", "kettlehat full coif", [("kettlehatfullcoif",0)], itp_merchandise|itp_type_head_armor,0,
 250 , weight(1.75)|abundance(60)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["kettlehat1", "kettlehat with coif", [("kettlehat1",0)], itp_merchandise|itp_type_head_armor,0,
 220 , weight(1.60)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
  ["weimar_helm", "Weimar Helm", [("weimarhelm",0)], itp_merchandise|itp_type_head_armor,0,
 2040 , weight(3)|abundance(20)|head_armor(64)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
  ["milanese_sallet", "Milanese Sallet", [("milanese_sallet",0)], itp_merchandise|itp_type_head_armor,0,
 1900 , weight(3)|abundance(20)|head_armor(62)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
 ["great_helm_1", "Great Helmet", [("greathelm1",0)], itp_merchandise| itp_type_head_armor,0, 980 ,
 weight(2.75)|abundance(60)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 ["great_bascinet_1", "Great Bascinet", [("greatbascinet1",0)], itp_merchandise| itp_type_head_armor,0, 1020 ,
 weight(2.80)|abundance(60)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
   ["flemish_armet", "Flemish Armet", [("flemish_armet",0)], itp_merchandise|itp_type_head_armor,0,
 2040 , weight(3)|abundance(20)|head_armor(64)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],



["munitions_helm_1", "Munitions Helm", [("munitionshelm1",0)], itp_merchandise| itp_type_head_armor,0, 1000 ,
 weight(2.80)|abundance(40)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 # ["pepperpot_helm_1", "Pepperpot Helm", [("pepperpothelm1",0)], itp_merchandise| itp_type_head_armor,0, 990 ,
 # weight(2.70)|abundance(50)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
  ["norman_pepperpot", "Norman Pepperpot", [("normanpepperpot",0)], itp_merchandise| itp_type_head_armor,0, 990 ,
 weight(2.70)|abundance(50)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
 ["barbuta1", "Soldat Barbuta", [("barbuta1",0)], itp_merchandise|itp_type_head_armor,0,
 220 , weight(1.80)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
  ["barbuta2", "Soldat Barbuta", [("barbuta2",0)], itp_merchandise|itp_type_head_armor,0,
 220 , weight(1.80)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
 ["new_order_helm", "new_order_helm", [("frenchpepperpot",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0, 1000 ,
 weight(2.80)|abundance(40)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
  ["conic_helm", "Conic Helm", [("conichelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0, 360 ,
 weight(3)|abundance(60)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],


 #--------------------------------------------------------------
 #-------------------yoman's helmets---------------------
# ["face_cover_lamellar", "Face Cover lamellar", [("facecovermail_plume",0)], itp_merchandise|itp_type_head_armor,0,
 # 600 , weight(2)|abundance(40)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 #-------------------------------------------------------------
 #------------OSP_RGCoTL_Rome----------------------------------

  # ["dirim_mail", "Dirim Mail", [("a_roman_chain",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1320 , weight(19)|abundance(20)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
# ["dirim_light_breast_plate", "Dirim Light Breast Plate", [("a_tribune",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1000 , weight(18)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(7) ,imodbits_plate ],
 # ["dirim_breast_plate", "Dirim  Breast Plate", [("a_tribune_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1100 , weight(20)|abundance(40)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(7) ,imodbits_plate ],
  # ["dirim_heavy_breast_plate", "Dirim Heavy Breast Plate", [("a_tribune_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1200 , weight(22)|abundance(30)|head_armor(0)|body_armor(44)|leg_armor(12)|difficulty(7) ,imodbits_plate ],
  #--------------------------------------------------------------
  #------------TLD dirim_armors----------------------------------
  # ["dirim_jerkin", "Dirim Jerkin", [("pelargir_jerkin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 900 , weight(18)|abundance(40)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_plate ],
 # ["dirim_footman_armor", "Dirim Fotman Armor", [("pelargir_footman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1000 , weight(18)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(7) ,imodbits_plate ],
 # ["dirim_regular_armor", "Dirim  Regular Armor", [("pelargir_regular",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 1100 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(12)|difficulty(7) ,imodbits_plate ],


  #--------------------------------------------------------------
  #------------roman_armor (mount and gladius----------------------------------
["dirim_cav_sword", "Dirim Cavalry Sword", [("roman_cav_sword_1",0),("roman_cav_sword_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
310 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(92)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],
["dirim_pilum", "Dirim Pilum", [("roman_jav",0),("roman_jav_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
525 , weight(3)|difficulty(2)|spd_rtng(80) | shoot_speed(22) | thrust_damage(50 ,  pierce)|max_ammo(3)|weapon_length(69),imodbits_thrown ],
# ["dirim_gladius", "Dirim Gladius", [("roman_gladius_1",0),("roman_gladius_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 # 170 , weight(1.3)|difficulty(0)|spd_rtng(106) | weapon_length(67)|swing_damage(30, cut) | thrust_damage(20, pierce),imodbits_sword_high ],

  #--------------------------------------------------------------
 #------------amade_bronzewarrior----------------------------------

 ["empress_plate", "Empress Plate Armor", [("empress_plate",0)], itp_type_body_armor|itp_covers_legs ,0,
 7500 , weight(24)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(10) ,imodbits_plate ],
# ["bronze_gauntlet","Bronze Gauntlet", [("bronze_gauntlet_R",0),("bronze_gauntlet_R",imodbit_reinforced)], itp_type_hand_armor,0,
 # 1040, weight(1.0)|abundance(0)|body_armor(7)|difficulty(0),imodbits_armor],
# ["bronze_greaves", "Bronze Greaves", [("bronze_greaves",0)],  itp_type_foot_armor | itp_attach_armature,0,
 # 800 , weight(2)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],

 #--------------------------------------------------------------
  #------------wei_xiadi osp----------------------------------


 # ["guhulay_armor_0", "Guhulay Armor", [("wei_xiadi_cataphract_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3000 , weight(23)|abundance(10)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["guhulay_armor_1", "Guhulay Armor", [("wei_xiadi_lamellar_armor01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3200 , weight(25)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["guhulay_armor_2", "Guhulay Armor", [("wei_xiadi_lamellar_armor02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 # 3200 , weight(25)|abundance(10)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
     # ["guhulay_elite_armor_1", "Guhulay Elite Armor", [("wei_xiadi_samurai_armor01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3300 , weight(25)|abundance(5)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
 # ["guhulay_elite_armor_2", "Guhulay Elite Armor", [("wei_xiadi_samurai_armor02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3300 , weight(25)|abundance(5)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
 #------------------------------------------------------------------



 #-----------indo_helmets_mini---------------
# ["guhulay_black_mask", "Guhulay Black Mask", [("helm_sultanmask",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 850 , weight(3)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["guhulay_lancer_helm", "Guhulay Lancer Helmet", [("helm_rajplumevi",0)], itp_type_head_armor |itp_merchandise   ,0, 500 , weight(2)|abundance(60)|head_armor(42)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#-------------------------------------

#-----------saracen helm osp---------------
#["guhulay_lancer_helm", "Guhulay Lancer Helmet", [("guhulay_lancer_helm",0)], itp_type_head_armor |itp_merchandise   ,0, 500 , weight(2)|abundance(60)|head_armor(44)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#------------------------------------------

#--helmets
["lobarian_bascinet_visor", "Vosored Bascinet", [("lobarian_bascinet_visor",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0,
 738 , weight(3)|abundance(40)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["lobarian_bascinet_visor_open", "Vosored Bascinet", [("lobarian_bascinet_visor_open",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0,
 738 , weight(3)|abundance(40)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
 ["bilomadal_helmet_1", "Helmet Mail Coif", [("bilomadal_helmet_1",0)], itp_merchandise|itp_type_head_armor,0,
 550 , weight(3)|abundance(20)|head_armor(44)|body_armor(6)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 #--
#--polearm
["lobarian_polehammer_1",         "Polehammer", [("luc_english_polehammer",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe,
 484 , weight(4.5)|difficulty(13)|spd_rtng(80) | weapon_length(120)|swing_damage(30 , blunt) | thrust_damage(24 ,  pierce),imodbits_polearm ],

#--
#--swords
["lobarian_falchion",         "Falchion", [("luc_english_falchion",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
150, weight(2.5)|difficulty(7)|spd_rtng(92) | weapon_length(85)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],

#--

#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
122 , weight(3.5)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
180 , weight(3.5)|difficulty(0)|spd_rtng(90) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(85) | weapon_length(70)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
97 , weight(6)|difficulty(11)|spd_rtng(69) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
101 , weight(7)|difficulty(12)|spd_rtng(66) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
290 , weight(9)|difficulty(14)|spd_rtng(69) | weapon_length(75)|swing_damage(41 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
27 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
83 , weight(3)|difficulty(0)|spd_rtng(90) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
108 , weight(1.0)|difficulty(0)|spd_rtng(92) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(70)|swing_damage(29 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
305 , weight(4.5)|difficulty(13)|spd_rtng(85) | weapon_length(85)|swing_damage(36 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["hadvog_sword", "Hadvog Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
105 , weight(2.5)|difficulty(8)|spd_rtng(98) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
290 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(103)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Afirid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
108 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Afirid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
218 , weight(1.7)|difficulty(0)|spd_rtng(96) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["afirid_cavalry_sword",         "Afirid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
310 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Afirid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
420 , weight(1.7)|difficulty(0)|spd_rtng(96) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
#--half sword
["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_next_item_as_melee, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(81) | weapon_length(125)|swing_damage(37 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur, itc_staff|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(94) | weapon_length(125)|swing_damage(32 , pierce) | thrust_damage(32 ,  pierce),imodbits_sword_high ],


 ["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(11)|spd_rtng(80) | weapon_length(130)|swing_damage(38 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
13 , weight(2)|difficulty(0)|spd_rtng(96) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
24 , weight(2)|difficulty(7)|spd_rtng(92) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
# ["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
# 77 , weight(2.5)|difficulty(9)|spd_rtng(90) | weapon_length(90)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
65 , weight(4)|difficulty(8)|spd_rtng(81) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
129 , weight(4.5)|difficulty(7)|spd_rtng(77) | weapon_length(119)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
240 , weight(5)|difficulty(9)|spd_rtng(78) | weapon_length(108)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
264 , weight(5)|difficulty(10)|spd_rtng(76) | weapon_length(110)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],





#--half sword
["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_next_item_as_melee, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(8)|spd_rtng(87) | weapon_length(110)|swing_damage(38 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_b_alt",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_no_blur, itc_staff|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(8)|spd_rtng(100) | weapon_length(110)|swing_damage(34 , pierce) | thrust_damage(34 ,  pierce),imodbits_sword_high ],

#--half sword
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_next_item_as_melee, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(9)|spd_rtng(86) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["sword_two_handed_a_alt",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_no_blur , itc_staff|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(9)|spd_rtng(98) | weapon_length(120)|swing_damage(35 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ],

["guhulay_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|difficulty(10)|spd_rtng(86) | weapon_length(120)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["guhulay_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|difficulty(10)|spd_rtng(86) | weapon_length(120)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

#--a remplacer
["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|difficulty(10)|spd_rtng(83) | weapon_length(120)|swing_damage(38 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|difficulty(9)|spd_rtng(92) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

#--half sword
["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_next_item_as_melee, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|difficulty(9)|spd_rtng(96) | weapon_length(101)|swing_damage(31 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_no_blur, itc_staff|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|difficulty(9)|spd_rtng(110) | weapon_length(101)|swing_damage(34 , pierce) | thrust_damage(34 ,  pierce),imodbits_sword_high ],
 #--half sword
 ["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_next_item_as_melee, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|difficulty(9)|spd_rtng(95) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
 ["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn| itp_primary |itp_no_blur, itc_staff|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|difficulty(9)|spd_rtng(108) | weapon_length(105)|swing_damage(35 , pierce) | thrust_damage(25 ,  pierce),imodbits_sword_high ],


["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|difficulty(9)|spd_rtng(94) | weapon_length(71)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|difficulty(9)|spd_rtng(94) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|difficulty(9)|spd_rtng(94) | weapon_length(76)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|difficulty(9)|spd_rtng(94) | weapon_length(72)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|difficulty(9)|spd_rtng(94) | weapon_length(76)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#--boarding axes osp
["axe_a", "One Handed Axe", [("axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar,
 110 , weight(1.8)|difficulty(1)|spd_rtng(96) | weapon_length(42)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["axe_b", "One Handed Axe", [("axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar,
 130 , weight(1.5)|difficulty(1)|spd_rtng(98) | weapon_length(35)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["axe_c", "One Handed Axe", [("axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar,
 220 , weight(1.5)|difficulty(1)|spd_rtng(96) | weapon_length(48)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["axe_d", "One Handed Axe", [("axe_d",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar,
 130 , weight(1.5)|difficulty(1)|spd_rtng(98) | weapon_length(40)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["bastard_axe", "Hand Long Axe", [("bastard_axe",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip,
 550 , weight(1.5)|difficulty(1)|spd_rtng(90) | weapon_length(78)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#--
["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|difficulty(10)|spd_rtng(76) | weapon_length(90)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|difficulty(10)|spd_rtng(76) | weapon_length(92)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|difficulty(10)|spd_rtng(72) | weapon_length(100)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(74) | weapon_length(96)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_poleaxe|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(73) | weapon_length(120)|swing_damage(36 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(68) | weapon_length(120)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_poleaxe|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(72) | weapon_length(125)|swing_damage(40 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(67) | weapon_length(125)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_poleaxe|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(12)|spd_rtng(71) | weapon_length(127)|swing_damage(44 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(12)|spd_rtng(65) | weapon_length(127)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|difficulty(10)|spd_rtng(70) | weapon_length(102)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|difficulty(12)|spd_rtng(68) | weapon_length(116)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_poleaxe,
 120 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_poleaxe,
390 , weight(4.75)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(42 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_guandao,
 660 , weight(5.0)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(44 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],

 ["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 185 , weight(2.75)|difficulty(0)|spd_rtng(85) | weapon_length(135)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
 ["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 350 , weight(3.25)|difficulty(0)|spd_rtng(83) | weapon_length(153)|swing_damage(34 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|difficulty(10)|spd_rtng(80) | weapon_length(112)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|difficulty(0)|spd_rtng(97) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|difficulty(0)|spd_rtng(98) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|difficulty(0)|spd_rtng(96) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(30 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],

#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

["sword_viking_1", "Hadvog Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Hadvog Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Hadvog Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|difficulty(0)|spd_rtng(98) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Hadvog War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Hadvog Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|difficulty(0)|spd_rtng(98) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_guhulay_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|difficulty(0)|spd_rtng(98) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_guhulay_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_guhulay_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_guhulay_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|difficulty(0)|spd_rtng(96) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],



["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|difficulty(0)|spd_rtng(89) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|difficulty(9)|spd_rtng(85) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 264 , weight(3)|difficulty(0)|spd_rtng(86) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 324 , weight(3)|difficulty(0)|spd_rtng(85) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 310 , weight(3)|difficulty(0)|spd_rtng(84) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["afirid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
470 , weight(4.5)|difficulty(10)|spd_rtng(80) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],


["afirid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|difficulty(0)|spd_rtng(89) | weapon_length(73)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["afirid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(9)|spd_rtng(87) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["afirid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|difficulty(9)|spd_rtng(87) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["afirid_two_handed_axe_a",         "Afirid Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|difficulty(10)|spd_rtng(79) | weapon_length(95)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["afirid_two_handed_axe_b",         "Afirid War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|difficulty(10)|spd_rtng(80) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_poleaxe|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_cutting_spear, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_cutting_spear, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(115) | weapon_length(128)|swing_damage(29 ,  pierce) | thrust_damage(29 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(70) | weapon_length(157)|swing_damage(35 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe,
 384 , weight(4.5)|difficulty(13)|spd_rtng(60) | weapon_length(180)|swing_damage(40 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
# ["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 # 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(40 , blunt) | thrust_damage(30 ,  blunt),imodbits_polearm ],
# ["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 # 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
# ["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 # 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_nodachi |itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],
#-----------fladin osp-----------------
# ["guhulay_elite_armor", "Guhulay Elite Armor", [("guhulay_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["black_tabard", "Black Tabard", [("black_tabard",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 407 , weight(12)|abundance(20)|head_armor(0)|body_armor(35)|leg_armor(6)|difficulty(6) ,imodbits_armor ],
 ["order_surcoat_over_mail", "Order Surcoat over Mail", [("order_surcoat_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1730 , weight(22)|abundance(10)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(7) ,imodbits_armor ],

  # ["leather_warhorse","Leather War Horse", [("leather_warhorse",0)], itp_merchandise|itp_type_horse, 0,
  # 1250,abundance(40)|hit_points(125)|body_armor(26)|difficulty(4)|horse_speed(38)|horse_maneuver(30)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
 # ["leather_charger","Leather Charger", [("leather_charger",0)], itp_merchandise|itp_type_horse, 0,
 # 1511,abundance(30)|hit_points(125)|body_armor(34)|difficulty(4)|horse_speed(37)|horse_maneuver(36)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion],
["bw_knight_horse","Warhorse", [("bw_knight_horse",0)],itp_type_horse, 0,
 1300,abundance(20)|hit_points(122)|body_armor(36)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
["plated_bw_knight_horse","Plated Warhorse", [("plated_bw_knight_horse",0)],itp_type_horse, 0,
 1600,abundance(5)|hit_points(122)|body_armor(42)|difficulty(4)|horse_speed(37)|horse_maneuver(38)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion],

 # ["heavy_leather_charger","Heavy Leather Charger", [("heavy_leather_charger",0)], itp_merchandise|itp_type_horse, 0,
 # 1611,abundance(20)|hit_points(125)|body_armor(36)|difficulty(4)|horse_speed(37)|horse_maneuver(40)|horse_charge(34)|horse_scale(112),imodbits_horse_basic|imodbit_champion],



#-------------------------------------
 #--------------Lucas's_OSP_Pack_I----------------------
 ["luc_english_bill",         "Bill", [("luc_english_bill",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 460 , weight(6)|difficulty(8)|spd_rtng(68) | weapon_length(189)|swing_damage(43 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
 ["luc_bill_guisarme_long",         "Long Guisarme", [("luc_bill_guisarme_long",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 420 , weight(8)|difficulty(8)|spd_rtng(68) | weapon_length(211)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
 ["halberd",  "Halberd", [("luc_flemish_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
 420 , weight(6)|difficulty(8)|spd_rtng(70) | weapon_length(130)|swing_damage(39 , cut) | thrust_damage(32 ,  pierce),imodbits_polearm ],
 ["heavy_halberd",  "Heavy Halberd", [("luc_swiss_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
 480 , weight(7)|difficulty(9)|spd_rtng(68) | weapon_length(185)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],

 ["atian_longsword", "Atian Sword", [("luc_italian_longsword",0),("luc_italian_longsword_scabbard", ixmesh_carry)],  itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 350 , weight(1.5)|difficulty(7)|spd_rtng(98) | weapon_length(100)|swing_damage(28 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
 ["luc_hache_d_armes_b", "Hache d'Armes", [("luc_hache_d'armes_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 200 , weight(1.8)|difficulty(10)|spd_rtng(84) | weapon_length(76)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["luc_celtic_sword_3",         "Dirim Guard Sword", [("luc_celtic_sword_3",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
420 , weight(1.8)|difficulty(7)|spd_rtng(102) | weapon_length(92)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],

 ["luc_scramasax",         "Scramasax", [("luc_scramasax",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
120 , weight(2.5)|difficulty(7)|spd_rtng(102) | weapon_length(65)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["luc_celtic_sword",         "Dirim Sword", [("luc_celtic_sword",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
420 , weight(1.8)|difficulty(7)|spd_rtng(100) | weapon_length(92)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["luc_ball_mace_one_handed",         "Ball Mace", [("luc_ball_mace_one_handed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
150 , weight(4)|difficulty(8)|spd_rtng(80) | weapon_length(72)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["luc_burgundian_axe", "Dirim Axe", [("luc_burgundian_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 300 , weight(1.6)|difficulty(8)|spd_rtng(86) | weapon_length(73)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["desert_scimitar",         "Desert Scimitar", [("luc_sarranid_falchion_m",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
230 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["winged_mace_1",         "W Mace", [("luc_winged_mace_za",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
150 , weight(3.5)|difficulty(0)|spd_rtng(88) | weapon_length(70)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["winged_mace_2",         "Mace", [("luc_english_mace_15th",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_longsword|itcf_carry_mace_left_hip,
200 , weight(3.5)|difficulty(0)|spd_rtng(86) | weapon_length(82)|swing_damage(26 , blunt) | thrust_damage(26 ,  pierce),imodbits_mace ],
["bronze_mace",         "Bronze Mace", [("luc_bronze_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
180 , weight(3.5)|difficulty(0)|spd_rtng(87) | weapon_length(75)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["bronze_spiked_mace_5p",         "Bronze Spiked Mace", [("luc_spiked_mace_5p_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
300 , weight(4.5)|difficulty(12)|spd_rtng(85) | weapon_length(83)|swing_damage(35 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["guhulay_mace", "Guhulay Mace", [("luc_burgundian_mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
180 , weight(3.5)|difficulty(0)|spd_rtng(86) | weapon_length(72)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["war_hammer_no2", "War Hammer", [("war_hammer_no2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(3.5)|difficulty(0)|spd_rtng(88) | weapon_length(68)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["war_hammer_no3", "War Hammer", [("war_hammer_no3",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
300 , weight(3.4)|difficulty(0)|spd_rtng(88) | weapon_length(68)|swing_damage(27 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],


["luc_flanged_mace_iron", "Iron Flanged Mace", [("luc_flanged_mace_iron",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
300 , weight(4)|abundance(20)|difficulty(12)|spd_rtng(85) | weapon_length(82)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["luc_flanged_mace_z", "flanged Mace", [("luc_flanged_mace_z",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
200 , weight(3.5)|abundance(60)|difficulty(6)|spd_rtng(86) | weapon_length(71)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["luc_zulfiqar",         "Zulfaqar", [("luc_zulfiqar",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
1000 , weight(2.5)|difficulty(7)|spd_rtng(102) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(32 ,  pierce),imodbits_sword ],

["luc_throwing_hammer", "Throwing Hammer", [("luc_throwing_hammer",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
100, weight(3)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(26,blunt)|max_ammo(3)|weapon_length(31),imodbits_thrown_minus_heavy ],
["luc_throwing_hammer", "Hammer", [("luc_throwing_hammer",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
100, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(31)| swing_damage(26,blunt),imodbits_thrown_minus_heavy ],


["luc_hammer_spike", "Spiked Hammer", [("luc_hammer_spike",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced|itp_bonus_against_shield, itc_morningstar|itcf_carry_mace_left_hip,
300 , weight(4.5)|difficulty(12)|spd_rtng(80) | weapon_length(77)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["luc_knightly_axe_v2", "Knightly Bastard Axe", [("luc_knightly_axe_v2",0)], itp_type_two_handed_wpn| itp_merchandise| itp_primary | itp_bonus_against_shield|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_left_hip,
 200 , weight(2.0)|difficulty(10)|spd_rtng(90) | weapon_length(105)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["luc_horseman_pick", "Horseman Pick", [("luc_horseman_pick",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(1.5)|difficulty(6)|spd_rtng(87) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["luc_horsemans_axe", "Horsemans Axe", [("luc_horsemans_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip,
 450 , weight(2.0)|difficulty(9)|spd_rtng(88) | weapon_length(79)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["luc_knights_warhammer",         "Knights Warhammer", [("luc_knights_warhammer",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary, itc_nodachi|itcf_carry_mace_left_hip,
470 , weight(4.5)|difficulty(10)|spd_rtng(80) | weapon_length(80)|swing_damage(35 , blunt) | thrust_damage(0 ,  blunt),imodbits_mace ],
["luc_kriegshammer", "Pick Hammer", [("luc_kriegshammer",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(1.5)|difficulty(6)|spd_rtng(87) | weapon_length(70)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
 ["luc_horsemans_hammer",         "luc_horsemans_hammer", [("luc_horsemans_hammer",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_mace_left_hip,
400 , weight(5)|difficulty(10)|spd_rtng(82) | weapon_length(73)|swing_damage(30 , blunt) | thrust_damage(0 ,  blunt),imodbits_mace ],




#-----------------------------------------------------
 #--halberds
 ["decorated_halberd",  "Decorated Halberd", [("decorated_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe|itcf_carry_spear,
 720 , weight(6)|difficulty(9)|spd_rtng(69) | weapon_length(180)|swing_damage(40 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm ],

  ["imifir_halberd_1",  "Heavy Halberd", [("imifir_halberd_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
   ["imifir_halberd_2",  "Heavy Halberd", [("imifir_halberd_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
    ["imifir_halberd_3",  "Heavy Halberd", [("imifir_halberd_3",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
    ["imifir_halberd_4",  "Heavy Halberd", [("imifir_halberd_4",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
   ["imifir_halberd_5",  "Heavy Halberd", [("imifir_halberd_5",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
    ["imifir_halberd_6",  "Heavy Halberd", [("imifir_halberd_6",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_poleaxe,
 520 , weight(6)|difficulty(9)|spd_rtng(68) | weapon_length(190)|swing_damage(40 , cut) | thrust_damage(34 ,  pierce),imodbits_polearm ],
#--



#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_staff|itcf_carry_spear,
 53 , weight(2.0)|difficulty(0)|spd_rtng(125) | weapon_length(120)|swing_damage(37 ,  pierce) | thrust_damage(37 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_staff,
 85 , weight(2.25)|difficulty(0)|spd_rtng(122) | weapon_length(135)|swing_damage(36 ,  pierce) | thrust_damage(36 ,  pierce),imodbits_polearm ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_staff,
 80 , weight(2.0)|difficulty(0)|spd_rtng(113) | weapon_length(200)|swing_damage(26 ,  pierce) | thrust_damage(26 ,  pierce),imodbits_polearm ],




["war_spear",  "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_staff|itcf_carry_spear,
 140 , weight(2.5)|difficulty(0)|spd_rtng(117) | weapon_length(150)|swing_damage(34 ,  pierce)| thrust_damage(34 ,  pierce),imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_poleaxe|itcf_carry_spear,
 155 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 410 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
 #---------osp colored lance---------------
 ["colored_lance_a", "Knight Lance", [("colored_lance_a",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
  ["colored_lance_b", "Knight Lance", [("colored_lance_b",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
  ["colored_lance_c", "Knight Lance", [("colored_lance_c",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
  ["colored_lance_d", "Knight Lance", [("colored_lance_d",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
  ["colored_lance_e", "Knight Lance", [("colored_lance_e",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 ["colored_lance_f", "Knight Lance", [("colored_lance_f",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
  ["colored_lance_g", "Knight Lance", [("colored_lance_g",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 500 , weight(4.5)|difficulty(12)|spd_rtng(60) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 #----------------------------------------
 #--cwe lances
["afirid_lance",         "Afirid Lance", [("afirid_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 370 , weight(2.8)|difficulty(9)|spd_rtng(80) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

 #--

 ["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed,itc_pike,
 125 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(245)|swing_damage(30 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_cant_use_on_horseback| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur|itp_two_handed , itc_staff|itcf_carry_spear,
 345 , weight(2.25)|difficulty(0)|spd_rtng(100) | weapon_length(165)|swing_damage(40 ,  pierce) | thrust_damage(40 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_cant_use_on_horseback|  itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur|itp_two_handed , itc_pike,
 385 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(185)|swing_damage(38 ,  pierce) | thrust_damage(38 ,  pierce),imodbits_polearm ],
["pike_long",         "Long Pike", [("imifir_long_pike",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur  ,itc_pike,
 420 , weight(5.0)|difficulty(0)|spd_rtng(85) | weapon_length(450)|swing_damage(32 ,  pierce) | thrust_damage(32 ,  pierce),imodbits_polearm ],


  #---------OSP miniupdate---------------

 #----------------------------------------


["doomcall_coat_of_plates", "doomcall_coat_of_plates", [("doomcall_coat_of_plates",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1828 , weight(30)|abundance(1)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(10) ,imodbits_armor ],




  #---------------teutonic helm------------------------
  ["order_winged_helmet", "Order Winged Helmet", [("teutonichelm_e",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,
  1640 , weight(3)|abundance(2)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
    ["high_priest_helmet", "High Priest Helmet", [("teutonichelm_d",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,
  1740 , weight(3.5)|abundance(2)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
 #-------------------------------------------
 #---------------NJUNJA OSP------------------------
    ### NJUNJA BEGIN
#horses
# ["charger_steel","Barded Charger", [("charger_new_steel",0)], itp_merchandise|itp_type_horse, 0, 2011,abundance(20)|hit_points(120)|body_armor(30)|difficulty(4)|horse_speed(38)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_7]],
# ["plate_charger_brown","Plated Charger", [("charger_plate_brown",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(20)|hit_points(120)|body_armor(40)|difficulty(4)|horse_speed(36)|horse_maneuver(42)|horse_charge(36)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["steppe_char_iron","Barded Steppe Charger", [("steppe_charger_iron",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(20)|hit_points(120)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3]],
#/horses

#armors
# ["afirid_royal_armor", "Afirid Royal Armor", [("saladin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(10)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
# ["heavy_lamellar_armor", "Heavy Lamellar Armor", [("heavy_lamellar_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3628 , weight(25)|abundance(20)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
# ["leather_armor_padded", "Padded Leather Coat", [("leather_armor_padded1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1190 , weight(18)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
#/armors



#/shields
### NJUNJA END
#------------------------------------
#["shield_royal", "Pravar Steel Shield", [("shield_royal",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  1390 , weight(4.5)|hit_points(800)|body_armor(17)|spd_rtng(59)|shield_width(40)|shield_height(60),imodbits_shield ],
#["kalisos_shield", "Kalisos Steel Shield", [("kalisos_shield",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  1390 , weight(4.5)|hit_points(800)|body_armor(17)|spd_rtng(59)|shield_width(40)|shield_height(50),imodbits_shield ],


 #["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

["bec_de_corbin_a",  "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_poleaxe|itcf_carry_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(71) | weapon_length(120)|swing_damage(34, pierce) | thrust_damage(38 ,  pierce),imodbits_polearm ],



# SHIELDS
["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,
#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["hadvog_shield", "Hadvog Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",         "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(81),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],
["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],
["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
105 , weight(3.5)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],
["steel_buckler1", "Steel Buckler", [("steel_buckler1",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(35)|shield_height(35),imodbits_shield ],
["steel_buckler2", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(28)|shield_height(45),imodbits_shield ],
["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
#["dec_steel_shield", "Decorated Steel Shield", [("dec_steel_shield",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(600)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["brass_shield1", "Decorated Brass Shield", [("brass_shield1",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(600)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["painted_brass_shield", "Painted Brass Shield", [("brass_shield2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(600)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["painted_brass_shield1", "Painted Brass Shield", [("brass_shield3",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(600)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
# ["painted_brass_shield5", "Painted Brass Shield", [("brass_shield7",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(600)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["steel_shield_heater", "Steel Heater Shield", [("steel_heater1",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  1290 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40)|shield_height(50),imodbits_shield ],
["bw_knight_shield", "B&W Knight Shield", [("bw_knight_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
200, weight(2)|abundance(10)|body_armor(20)|hit_points(165)|spd_rtng(96)|shield_height(46)|shield_width(36),imodbits_shield ],
["bw_horseman_shield", "B&W Horseman Shield", [("bw_horseman_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
180, weight(2.3)|abundance(20)|body_armor(18)|hit_points(160)|spd_rtng(94)|shield_height(46)|shield_width(36),imodbits_shield ],
["bw_kite_shield", "B&W Kite Shield", [("bw_kite_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
160, weight(2.3)|abundance(20)|body_armor(16)|hit_points(150)|spd_rtng(94)|shield_height(70)|shield_width(36),imodbits_shield ],
 #["jalik_kit_shield", "Jalik Kit Shield",   [("crusadsss" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
#320 , weight(3.5)|hit_points(300)|body_armor(16)|spd_rtng(88)|shield_width(30)|shield_height(55),imodbits_shield],
#["desert_shield_red",  "Desert Shield", [("saracenshielss",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(400)|body_armor(8)|spd_rtng(80)|shield_width(80),imodbits_shield ],
#["desert_shield_black",  "Desert Shield", [("saracensh",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(400)|body_armor(8)|spd_rtng(80)|shield_width(80),imodbits_shield ],
#["desert_shield_blue",  "Desert Shield", [("saracenshsss",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(400)|body_armor(8)|spd_rtng(80)|shield_width(80),imodbits_shield ],
#["desert_shield_brown",  "Desert Shield", [("saracenshsss",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(400)|body_armor(8)|spd_rtng(80)|shield_width(80),imodbits_shield ],

["pavise", "Pavise Shield",   [("pavise_wep" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
488 , weight(6.6)|hit_points(660)|body_armor(16)|spd_rtng(60)|shield_width(57)|shield_height(132),imodbits_shield ],
# ["desert_shield_1", "Desert Round Shield", [("desert_shield1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
# ["desert_shield_2", "Desert Round Shield", [("desert_shield2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["afirid_shield_l", "Decorated Afirid Shield", [("afirid_shield_l",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 597 , weight(3.5)|hit_points(200)|body_armor(40)|spd_rtng(65)|shield_width(38),imodbits_shield ],
["afirid_shield_p", "Decorated Afirid Shield", [("afirid_shield_p",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 597 , weight(3.5)|hit_points(200)|body_armor(40)|spd_rtng(65)|shield_width(38),imodbits_shield ],
["afirid_shield_q", "Decorated Afirid Shield", [("afirid_shield_q",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 597 , weight(3.5)|hit_points(200)|body_armor(40)|spd_rtng(65)|shield_width(38),imodbits_shield ],
["wooden_shield_1", "Wooden Shield", [("spak_shield_wood",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
240 , weight(3.5)|hit_points(100)|body_armor(20)|spd_rtng(70)|shield_width(40),imodbits_shield ],
["wooden_shield_2", "Wooden Shield", [("spak_shield_wood2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
240 , weight(3.5)|hit_points(100)|body_armor(20)|spd_rtng(70)|shield_width(40),imodbits_shield ],
["lobarian_pavise", "Lobarian Pavise",   [("lobarian_pavise" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
488 , weight(6.6)|hit_points(660)|body_armor(16)|spd_rtng(60)|shield_width(57)|shield_height(132),imodbits_shield ],
# ["steel_shield_kite", "Steel Kite Shield", [("steel_kite1",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  890 ,
 # weight(5.5)|hit_points(700)|body_armor(30)|spd_rtng(55)|shield_width(40)|shield_height(70),imodbits_shield ],
#-- toh 0.5 fantasy's torch
["left_torch", "torch", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,
  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,43,32,-5),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 20, 40),])]],
#--
#--bogmir heraldic shield
 ["tab_shield_sarranid_a", "Lobarian Shield",   [("tableau_shield_sarranid_a" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 156 , weight(3)|hit_points(280)|body_armor(4)|spd_rtng(90)|shield_width(40)|shield_height(55),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_a", ":agent_no", ":troop_no")])]],
 ["tab_shield_sarranid_b", "Lobarian Shield",   [("tableau_shield_sarranid_b" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
 274 , weight(3)|hit_points(360)|body_armor(8)|spd_rtng(90)|shield_width(45)|shield_height(60),imodbits_shield,
  [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_b", ":agent_no", ":troop_no")])]],
 ["tab_shield_sarranid_c", "Loabrian Guard Shield",   [("tableau_shield_sarranid_c" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
 360 , weight(3)|hit_points(430)|body_armor(10)|spd_rtng(88)|shield_width(40)|shield_height(50),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_c", ":agent_no", ":troop_no")])]],
#--
#--cwe heraldic shield
 ["tab_lobarian_knight_shield", "Lobarian Knight Shield",   [("tableau_lobarian_knight_shield" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 56 , weight(3)|hit_points(280)|body_armor(4)|spd_rtng(90)|shield_width(40)|shield_height(55),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_lobarian_knight", ":agent_no", ":troop_no")])]],
#--
# SHIELDS END



 #RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
155 , weight(4)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(5)|weapon_length(75),imodbits_thrown ],
# ["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
# 300, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
525 , weight(3)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
# ["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
# 525 , weight(1)|difficulty(1)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
560 , weight(2.75)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
# ["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
# 560 , weight(1)|difficulty(2)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
17 , weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(54) | thrust_damage(26 ,  cut),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
58 , weight(1)|difficulty(1)|spd_rtng(71) | shoot_speed(57) | thrust_damage(32 ,  cut  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 , weight(1.25)|difficulty(2)|spd_rtng(73) | shoot_speed(58) | thrust_damage(34 ,  cut),imodbits_bow ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,
145 , weight(1.75)|difficulty(4)|spd_rtng(56) | shoot_speed(92) | thrust_damage(28 ,  pierce),imodbits_bow ],
["guhulay_bow",         "Guhulay Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , weight(1.25)|difficulty(3)|spd_rtng(72) | shoot_speed(59) | thrust_damage(36 ,cut),imodbits_bow ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
437 , weight(1.25)|difficulty(3)|spd_rtng(68) | shoot_speed(60) | thrust_damage(37 ,cut),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,
728 , weight(1.5)|difficulty(4)|spd_rtng(58) | shoot_speed(81) | thrust_damage(30 ,pierce),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
150 , weight(2.25)|difficulty(0)|spd_rtng(44) | shoot_speed(32) | thrust_damage(27 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
200 , weight(2.5)|difficulty(8)|spd_rtng(42) | shoot_speed(40) | thrust_damage(32 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
232 , weight(3)|difficulty(8)|spd_rtng(41) | shoot_speed(44) | thrust_damage(47,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
399 , weight(3.5)|difficulty(9)|spd_rtng(40) | shoot_speed(46) | thrust_damage(52 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
633 , weight(3.75)|difficulty(10)|spd_rtng(36) | shoot_speed(48) | thrust_damage(57 ,pierce)|max_ammo(1),imodbits_crossbow ],
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_cant_reload_while_moving|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
#-------------------flintlock osp------------------------
 ["flintlock_pistol_1", "Flintlock Pistol", [("flintlock_pistol_1",0)], itp_type_pistol |itp_merchandise|itp_cant_reload_while_moving|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol,
 1200 , weight(1)|difficulty(0)|spd_rtng(55) | shoot_speed(120) | thrust_damage(70 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"), (position_move_x, pos1, 27), (position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15),(particle_system_burst, "psys_pistol_muzzle", pos1, 15)])]
 ],
 ["flintlock_rifle", "Flintlock Rifle",[("flintlock_rifle_1",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 4500 , weight(1.5)|abundance(1)|difficulty(0)|spd_rtng(40) | shoot_speed(160) | thrust_damage(110 ,pierce)|max_ammo(1)|accuracy(99),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
 ],
["arquebus", "Arquebus",[("arquebus",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 2600 , weight(2)|abundance(1)|difficulty(0)|spd_rtng(38) | shoot_speed(140) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(96),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,100),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],

["blunderbus", "Blunderbus",[("blunderbus",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 2000 , weight(2.5)|abundance(1)|difficulty(0)|spd_rtng(40) | shoot_speed(100) | thrust_damage(110 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,72),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["matchlock_2", "Matchlock Rifle",[("matchlock_2",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 2700 , weight(2)|abundance(1)|difficulty(0)|spd_rtng(48) | shoot_speed(150) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(90),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_matchlock_musket_fire"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
],

 # ["flintlock_rifle", "Flintlock Rifle",[("flintlock_rifle_1",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 # 4500 , weight(1.5)|abundance(1)|difficulty(0)|spd_rtng(40) | shoot_speed(160) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(99),imodbits_none,
# [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
 # ],


["matchlock_1", "Matchlock Rifle",[("matchlock_1",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 2700 , weight(2)|abundance(1)|difficulty(0)|spd_rtng(38) | shoot_speed(150) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(86),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_matchlock_musket_fire"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
],
 #-------------------flintlock osp END ------------------------
#-------------------osp firearms_mini ------------------------
["hand_canon", "Hand Canon",[("rrr_handgonne",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 800 , weight(3)|abundance(20)|difficulty(0)|spd_rtng(32) | shoot_speed(120) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_hand_canon_shot"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
],
["early_arquebuse", "Early Arquebuse",[("rrr_arquebuse",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_primary|itp_bonus_against_shield|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 800 , weight(2.5)|abundance(20)|difficulty(0)|spd_rtng(30) | shoot_speed(100) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(85),imodbits_none,
[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"), (position_move_x,pos1,17), (position_move_y,pos1,106),(particle_system_burst, "psys_musket_smoke", pos1, 15),(particle_system_burst, "psys_rifle_muzzle", pos1, 15)])]
 ],
#--------------------------------------------------------------

 ["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],



##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor ],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
# ["guhulay_guard_armor", "Guhulay Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0,
# 3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["guhulay_war_helmet", "Guhulay War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["guhulay_helmet", "Guhulay Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["guhulay_sword", "Guhulay Sword", [("guhulay_sword",0),("guhulay_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],
#["guhulay_guard_boots",  "Guhulay Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
#["guhulay_guard_helmet", "Guhulay Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise   ,0, 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["guhulay_cavalry_helmet", "Guhulay Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

# ["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
#["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
#["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(24)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(12)|difficulty(8) ,imodbits_armor ],
#["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 590 , weight(20)|abundance(40)|head_armor(0)|body_armor(44)|leg_armor(14)|difficulty(8) ,imodbits_armor ],

["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("rabati",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0,
 weight(1.5)|spd_rtng(45) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,
weight(1.5)|weapon_length(47)|max_ammo(80),imodbits_missile],


["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["warhorse_afirid","Sultan War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(120)|body_armor(22)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(120)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],
["warhorse_steppe_golden","Wyu Golden Charger", [("warhorse_steppe_golden",0)], itp_merchandise|itp_type_horse, 0, 1800,abundance(10)|hit_points(122)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(30)|horse_scale(113),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3]],


#--spears
  ["lobarian_spear_a","Spear", [("lobarian_spear_a", 0),("invalid_item", ixmesh_carry),("lobarian_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur, itcf_carry_revolver_right|itc_staff,
  140, weight(2)|abundance(90)|spd_rtng(110)|weapon_length(154)|thrust_damage(30, pierce)|swing_damage(30, pierce), imodbits_none, []],
  ["lobarian_spear_b","Lobarian Spear", [("lobarian_spear_b", 0),("invalid_item", ixmesh_carry),("lobarian_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur, itcf_carry_revolver_right|itc_staff,
  140, weight(2)|abundance(90)|spd_rtng(112)|weapon_length(160)|thrust_damage(31, pierce)|swing_damage(31, pierce), imodbits_none, []],
  ["lobarian_spear_c","Lobarian Spear", [("lobarian_spear_c", 0),("invalid_item", ixmesh_carry),("lobarian_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur, itc_staff|itcf_carry_spear,
  140, weight(2)|abundance(90)|spd_rtng(115)|weapon_length(147)|thrust_damage(32, pierce)|swing_damage(32, pierce), imodbits_none, []],
  # ["lobarian_spear_inf_a","lobarian_spear_inf_a", [("lobarian_spear_inf_a", 0),("invalid_item", ixmesh_carry),("lobarian_spear_inf_a", ixmesh_carry|imodbit_cheap)], 0, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,
  # 140, weight(2.5)|abundance(100)|hit_points(20480)|spd_rtng(100)|weapon_length(155)|thrust_damage(27, pierce)|swing_damage(20, pierce), imodbits_none, []],
  # ["lobarian_spear_inf_b","lobarian_spear_inf_b", [("lobarian_spear_inf_b", 0),("invalid_item", ixmesh_carry),("lobarian_spear_inf_b", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,
  # 140, weight(2.5)|abundance(100)|hit_points(20480)|spd_rtng(100)|weapon_length(160)|thrust_damage(27, pierce)|swing_damage(20, pierce), imodbits_none, []],
  # ["lobarian_spear_inf_c","lobarian_spear_inf_c", [("lobarian_spear_inf_c", 0),("invalid_item", ixmesh_carry),("lobarian_spear_inf_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,
  # 140, weight(2.5)|abundance(100)|hit_points(20480)|spd_rtng(100)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(20, pierce), imodbits_none, []],
 #--spears_end
 #--helmets
["hadvog_helmet_1", "Simple Hadvog Helmet", [("simple_hadvog_helmet",0)], itp_merchandise|itp_type_head_armor,0,
 275 , weight(2)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["hadvog_helmet_2", "Hadvog Helmet", [("hadvog_helmet",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
 325 , weight(2.5)|abundance(90)|head_armor(36)|body_armor(2)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["hadvog_helmet_3", "Hadvog Helmet", [("hadvog_helmet_mail",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0,
 525 , weight(3)|abundance(80)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 #--helmets ends






#-----------grenade-----------
#item entry of the fragments, one could give an invisible inflight model to them
#changing damage doesn't do anything here
["fragmentation_grenade_fragment","Fragment(do not use)", [(0,0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(0)|weapon_length(3)|thrust_damage(0,pierce)|max_ammo(1),imodbits_missile,
 [
 (ti_on_missile_hit,
[
#play sound and dust effect at fragment location
#it is advisable use a custom particle effect and sound here instead
(play_sound_at_position, "snd_blunt_hit", pos1),
#(particle_system_burst, "psys_fragmentation_grenade_fragment_dust", pos1, 1),
(particle_system_burst, "psys_game_hoof_dust", pos1, 1),
]
)
]],

#the launcher determines the damage of the fragments, changing fracment damage in the other entry someohow doesnt effect damage
#if you change the fragment shot speed in the add_missile op, then change it here too or the damage might change (not sure)
["fragmentation_grenade_fragment_launcher", "Fragment Launcher(do not use)", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|abundance(0)|difficulty(0)|spd_rtng(100) | shoot_speed(9) | thrust_damage(30 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,
],

["fragmentation_grenade",         "Fragmentation Grenade", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(15) | thrust_damage(4 ,  blunt)|max_ammo(1)|weapon_length(8),imodbit_large_bag,
[
(ti_on_missile_hit,
[
(store_trigger_param_1, ":frag_thrower_agent"),
(set_fixed_point_multiplier, 100),
#play sound and dust effect at fragment location
#one should use a custom explosion particle effect and explosion sound here instead
#(play_sound_at_position,"snd_frag_explode", pos1),
#(particle_system_burst, "psys_frag_explosion", pos1, 10),
(play_sound_at_position,"snd_pistol_shot", pos1),
(particle_system_burst, "psys_village_fire_big", pos1, 6),
(particle_system_burst, "psys_dummy_smoke_big", pos1, 24),
#blast effect part
    (try_for_agents, ":cur_agent"), #check every agent if he is close enough to the nade to directly suffer from the detonation, ignoring armour
(agent_is_alive, ":cur_agent"),
(agent_get_position, pos4, ":cur_agent"),
(get_sq_distance_between_positions,":blast_distance",pos1, pos4),
#(assign, reg10, ":blast_distance"),
#(display_message, "@Distance2={reg10}cm2.", 0xCCCCCC),
(lt, ":blast_distance", 3600), #within 6m radius(using squared distance)
(store_random_in_range, ":blast_damage", 3200,4000),#randomised damage part
(val_sub, ":blast_damage", ":blast_distance"),
(val_div, ":blast_damage", 100),
(gt, ":blast_damage", 0),#max dam at distance 0= 40; max dam at 6m = 4;	min dam at distance 0 = 34; min dam at 6m = 0;
(agent_deliver_damage_to_agent, ":frag_thrower_agent", ":cur_agent", ":blast_damage"),
(gt, ":blast_damage", 5),#if blast damage is big enough, knock agent down
        (agent_is_human, ":cur_agent"),	#prevent horses from knockdown
(agent_get_horse, ":cur_agent_mount_id",":cur_agent"),#prevent mounted agents form knockdown
(lt, ":cur_agent_mount_id", 0),
(try_begin),
(position_is_behind_position,pos1,pos4),#blast from behind ->fall forward
(agent_set_animation, ":cur_agent", "anim_rider_fall_roll"),
(else_try),
(agent_set_animation, ":cur_agent", "anim_strike_fall_back_rise"), #blast infront ->fall backwards
(agent_set_animation, ":cur_agent", "anim_strike_fall_back_rise_upper"),
(try_end),
(try_end),
#fragmentation part
(assign, ":fragment_number", 20), #number of fragments, dont go above 2000, never go full retard
(position_copy_origin, pos2, pos1),#take xyz of the nade landing point
(init_position, pos3),
(position_copy_rotation,pos2,pos3),#give standard orientation of the axis, with z axis looking up
(position_rotate_x_floating, pos2, 9000),#turn y axis up, the fire direction of the add_missile operation
#fire x(=fragment_number) fragments , 1 each loop run
    (try_for_range, ":unused", 1,  ":fragment_number"),
#randomise speed of fragments, should help with the problem that an agent can only hit once per frame
(store_random_in_range,":fragment_speed",-450,450),
(val_add,":fragment_speed",900),#average speed of a fragment, determines max fragment range
#vary the starting position of the fragments a bit, should help with the problem that an agent can only hit once per frame
(store_random_in_range,":fragment_random_pos_x",0,10),
(store_random_in_range,":fragment_random_pos_y",0,10),
(store_random_in_range,":fragment_random_pos_z",0,40),
#fragment fanning, no fragments should be released with downward component(would be wasted)
(copy_position, pos3, pos2), #pos3 is used for emiting the missile later on,
(position_move_x,pos3,":fragment_random_pos_x",1),# move x for better fragment	spread
(position_move_y,pos3,":fragment_random_pos_y",1),# move y for better fragment	spread
(position_move_z,pos3,":fragment_random_pos_z",1),# move z for better fragment	spread
(store_random_in_range,":fragmentation_rot_x", -9000,-3000), #don't release fragments too vertically	up, for complete hemisphere change -3000 to 0
(position_rotate_x_floating, pos3, ":fragmentation_rot_x"),
(store_random_in_range,":fragmentation_rot_z", 0, 359),	#not in fixed point, so it's 0-359 degree
(position_rotate_z, pos3, ":fragmentation_rot_z", 1),#use global z axis, not the already randomised one of the nade
(add_missile, ":frag_thrower_agent", pos3, ":fragment_speed", "itm_fragmentation_grenade_fragment_launcher", 0, "itm_fragmentation_grenade_fragment", 0),
(try_end),
]
)
]],
#-----------------------------

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
]
