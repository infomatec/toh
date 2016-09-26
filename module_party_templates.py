from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("borovod_nobleman","Borovod Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_borovod_knight,2,6),(trp_borovod_horseman,4,12)]),
##  ("pravar_nobleman","Pravar Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_pravar_knight,2,6),(trp_pravar_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_guhulay_raiders","Black Guhulay Raiders",icon_guhulay_horseman_b|carries_goods(2),0,fac_black_guhulays,bandit_personality,[(trp_black_guhulay_guard,1,10),(trp_black_guhulay_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60)]),
  #("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50)]),
	("sea_raiders","Galnar Raiders Party",icon_axeman|carries_goods(2),0,fac_galnar_clan,bandit_personality,[(trp_galnar_warrior,1,10),(trp_galnar_ship_captain,0,1),(trp_sea_raider,10,50)]),
	("north_free_company","Free Company",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_nord_mercenary,10,50),(trp_mercenary_archer,5,20)]),
	("south_free_company","Free Company",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_south_cavalry,4,20),(trp_south_spearman,9,52),(trp_mounted_archer,2,8)]),
	("west_free_company","Free Company",icon_gray_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_mercenary_crossbowman,10,30),(trp_mercenary_halberdier,10,30)]),	
  
  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),
	#-------------
	("dirim_centuri","Empire Centuri ",icon_gray_knight|pf_dont_attack_civilians,0,fac_kingdom_7,soldier_personality,[(trp_dirim_pronoiar,1,1),(trp_dirim_regular,60,60),(trp_dirim_footman,30,30),(trp_dirim_veteran,10,10)]),
	("jalik_patrol","Jalik Mercenaries",icon_gray_knight|pf_dont_attack_civilians|pf_quest_party,0,fac_jalik_mercenaries,soldier_personality,[(trp_jalik_mercenary,5,20),(trp_npc2,1,1,pmf_is_prisoner),(trp_caravan_guard,2,2,pmf_is_prisoner)]),
	("jalik_army","Jalik Army",icon_gray_knight|pf_dont_attack_civilians,0,fac_jalik_mercenaries,soldier_personality,[(trp_jalik,1,1),(trp_jalik_mercenary,200,500)]),
	
	("order_guards","Order Guards",icon_gray_knight|pf_quest_party,0,fac_knights_of_doomcall,soldier_personality,[(trp_order_knight,1,3),(trp_order_follower,2,6),(trp_npc20,1,1,pmf_is_prisoner),(trp_paysan,20,20,pmf_is_prisoner)]),
	#("black_patrol","Black Patrol",icon_gray_knight,0,fac_knights_of_doomcall,soldier_personality,[(trp_order_knight,1,10),(trp_order_follower,10,100),(trp_paysan,2,20,pmf_is_prisoner),(trp_common_prisoner,1,10,pmf_is_prisoner)]),
	("doomcall_patrol","Doomcall Patrol",icon_gray_knight,0,fac_knights_of_doomcall,soldier_personality,[(trp_order_priest,0,4),(trp_order_knight,1,20),(trp_order_follower,10,100),(trp_paysan,2,20,pmf_is_prisoner),(trp_common_prisoner,1,10,pmf_is_prisoner)]),

	("sun_cult_patrol","Sun Cult Patrol",icon_gray_knight,0,fac_sun_cult,soldier_personality,[(trp_sacrifice_hunter,4),(trp_sun_followers,1,20),(trp_order_follower,10,100),(trp_paysan,2,20,pmf_is_prisoner),(trp_common_prisoner,1,10,pmf_is_prisoner)]),

	#("white_patrol","New Order Patrol",icon_gray_knight,0,fac_the_new_order,soldier_personality,[(trp_order_billman,1,10),(trp_order_gunner,10,100),(trp_common_prisoner,1,10,pmf_is_prisoner)]),
	("new_order_patrol","New Order Patrol",icon_gray_knight,0,fac_the_new_order,soldier_personality,[(trp_order_billman,1,10),(trp_order_gunner,10,100),(trp_common_prisoner,1,10,pmf_is_prisoner)]),

	("black_army","The Black Army",icon_gray_knight,0,fac_knights_of_doomcall,soldier_personality,[(trp_sorobodol,1,1),(trp_order_priest,5,10),(trp_order_knight,50,70),(trp_order_follower,100,200)]),
	("golden_horde","Golden Horde",icon_gray_knight,0,fac_golden_horde,soldier_personality,[(trp_wyu_golden_warrior,200,300)]),
	("desert_army","Desert Army",icon_gray_knight,0,fac_desert_tribes,soldier_personality,[(trp_desert_camel_rider,100,200),(trp_desert_warrior,50,100)]),	
	("6th_legion","The 6th legion",icon_gray_knight|pf_dont_attack_civilians,0,fac_kingdom_7,soldier_personality,[(trp_npc17,1,1),(trp_dirim_pronoiar,4,8),(trp_dirim_regular,400,800)]),
	#----------------
#--pretenders armies
	("galnar_clan_army","Galnar Clan Army",icon_gray_knight|pf_always_visible,0,fac_galnar_clan,soldier_personality,[(trp_kingdom_4_pretender,1,1),(trp_galnar_warrior,200,300),(trp_galnar_ship_captain,10,20),(trp_sea_raider,10,100)]),
#	("galnar_raiders_party","Galnar Raiders Party",icon_gray_knight,0,fac_galnar_clan,soldier_personality,[(trp_galnar_warrior,1,10),(trp_galnar_ship_captain,0,1),(trp_galnar_raiders,10,50)]),
#--

	("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_pravar_militia,7,14),(trp_pravar_guard,1,2)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_pravar_infantry,3,6),(trp_pravar_footman,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_pravar_man_at_arms,1,3),(trp_pravar_mounted_sergeant,2,3),(trp_pravar_squire,1,2),(trp_pravar_knight,0,1)]), #Pravars are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_sellsword,4,8),(trp_mercenary_archer,3,6)]), 
  

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_borovod_footman,5,10),(trp_borovod_guard,1,2),(trp_borovod_archer,1,1)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_borovod_axeman,4,6),(trp_borovod_trained_archer,1,3)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_borovod_veteran,2,3),(trp_borovod_marksman,1,2),(trp_borovod_horseman,1,2),(trp_borovod_knight,0,1)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_nord_mercenary,4,8),(trp_mercenary_archer,3,6)]), 
  
  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_guhulay_skirmisher,1,4),(trp_guhulay_native_militia,6,10),(trp_guhulay_guard,1,2)]), #Guhulays are a bit less-powered thats why they have a bit more 2nd upgraded(trp_guhulay_skirmisher) than non-upgraded one(trp_guhulay_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_guhulay_horseman,1,5),(trp_guhulay_native_footman,3,4)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_guhulay_horse_archer,2,4),(trp_guhulay_lancer,1,2),(trp_guhulay_mirza,0,1),(trp_desert_camel_rider,1,1),(trp_wyu_golden_warrior,0,1)]), #Guhulays are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_mounted_archer,4,8)]), 
  
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_hadvog_footman,7,14),(trp_hadvog_guard,1,2)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hadvog_trained_footman,4,10)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hadvog_warrior,3,5),(trp_hadvog_huskarl,1,2),(trp_hadvog_chieftain,0,1)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_nord_mercenary,5,9),(trp_mercenary_archer,2,5)]), 
  
  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_imifir_spearman,7,14),(trp_imifir_guard,1,2)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_imifir_trained_spearman,2,4),(trp_imifir_crossbowman,2,4),(trp_imifir_pikeman,1,2)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_imifir_halberdier,2,3),(trp_imifir_pavise_crossbowman,1,2),(trp_imifir_bodyguard,1,2),(trp_imifir_richman,0,1)]), 
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_mercenary_halberdier,4,8),(trp_mercenary_crossbowman,3,6)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_afirid_footman,7,14),(trp_afirid_guard,1,2)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_afirid_light_infantry,1,2),(trp_afirid_skirmisher,1,2),(trp_afirid_horseman,1,2),(trp_afirid_infantry,2,4)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_afirid_heavy_infantry,1,2),(trp_afirid_heavy_horseman,2,3),(trp_afirid_charif,1,2),(trp_afirid_caid,0,1)]),
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_south_cavalry,1,2),(trp_south_spearman,3,6)]),
  #------------------
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dirim_militia,3,9),(trp_dirim_pretorian_guard,6,8),(trp_dirim_forest_hunter,1,2)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dirim_regular,4,8),(trp_dirim_long_bowman,1,2)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dirim_veteran,3,6),(trp_dirim_cavalryman,2,3),(trp_dirim_pronoiar,1,3),(trp_dirim_pretorian_guard,5,6)]), 
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_sellsword,4,8),(trp_mercenary_archer,3,6)]), 
  #---------------------
  ("player_supporters_faction_reinforcements_a", "{!}player_supporters_faction_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_militia,4,11),(trp_footman,6,8)]),
  ("player_supporters_faction_reinforcements_b", "{!}player_supporters_faction_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_footman,3,6),(trp_archer,2,4)]),
  ("player_supporters_faction_reinforcements_c", "{!}player_supporters_faction_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_footman,8,14),(trp_cavalryman,1,3),(trp_elite_foot_soldier,1,2),(trp_heavy_archer,1,2)]),
  #---------------------
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_pravar_footman,3,7),(trp_pravar_skirmisher,5,10),(trp_pravar_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_pravar_man_at_arms,5,10),(trp_pravar_infantry,5,10),(trp_pravar_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_pravar_knight,2,6),(trp_pravar_sergeant,2,5),(trp_pravar_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_borovod_axeman,3,7),(trp_borovod_skirmisher,5,10),(trp_borovod_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_borovod_horseman,4,9),(trp_borovod_veteran,5,10),(trp_borovod_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_borovod_knight,3,7),(trp_borovod_guard,2,5),(trp_borovod_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_guhulay_horseman,3,7),(trp_guhulay_skirmisher,5,10),(trp_guhulay_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_guhulay_veteran_horse_archer,4,9),(trp_guhulay_horse_archer,5,10),(trp_guhulay_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_guhulay_lancer,3,7),(trp_guhulay_veteran_horse_archer,2,5),(trp_guhulay_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_hadvog_trained_footman,3,7),(trp_hadvog_footman,5,10),(trp_hadvog_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hadvog_veteran,4,9),(trp_hadvog_warrior,5,10),(trp_hadvog_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hadvog_champion,1,3),(trp_hadvog_veteran,2,5),(trp_hadvog_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_imifir_spearman,3,7),(trp_imifir_crossbowman,5,10),(trp_imifir_recruit,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_imifir_trained_spearman,4,9),(trp_imifir_spearman,5,10),(trp_imifir_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_imifir_sergeant,3,7),(trp_imifir_veteran_spearman,2,5),(trp_imifir_pavise_crossbowman,2,5)]),


  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Galnar Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
]
