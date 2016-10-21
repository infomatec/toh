from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
("bogus", "cant_find_this.ogg", 0, 0),
("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),

# ("ambushed_by_neutral", "toh_Rohan_Ambush.mp3", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
# ("ambushed_by_khergit", "toh_Orc_Ambush.mp3", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),

("arena_1", "arena_1.ogg", mtf_sit_arena, 0),
#MV: next two commented out only because they are Native
#("armorer", "armorer.ogg", mtf_sit_travel, 0), 
#("bandit_fight", "bandit_fight.ogg", mtf_sit_fight|mtf_sit_ambushed, 0),
  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

#("calm_night_1", "toh_NightMusic.mp3", mtf_module_track|mtf_sit_night, mtf_sit_tavern|mtf_sit_travel),
("captured", "capture.ogg", mtf_persist_until_finished, 0),

("defeated_by_neutral","toh_killed.mp3",                mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),
# ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg",                            mtf_persist_until_finished|mtf_sit_killed, 0),
# ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg",                            mtf_persist_until_finished|mtf_sit_killed, 0),
# ("killed_by_swadian", "killed_by_swadian.ogg" ,                  mtf_culture_1|mtf_persist_until_finished|mtf_sit_killed, 0),
# ("killed_by_khergit", "toh_killed.mp3", mtf_culture_3|mtf_persist_until_finished|mtf_sit_killed, 0),
  
#("armorer", "armorer.ogg", mtf_sit_travel, 0),

#TLD battle music
("toh_battle_pravar",   	"toh_battle_pravar.ogg",   mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_empire",   	"toh_battle_empire.ogg",   mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_borovod",  	"toh_battle_borovod.ogg",    mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_hadvog",   	"toh_battle_hadvog.ogg",   mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_guhulay",   	"toh_battle_guhulay.ogg",  mtf_module_track|mtf_sit_fight,  mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_imifir",   	"toh_battle_imifir.mp3",    mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_afirid_1",     	"toh_battle_afirid_1.ogg",     mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_afirid_2",     	"toh_battle_afirid_2.ogg",     mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_afirid_3",     	"toh_battle_afirid_3.ogg",     mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_dirim",		"toh_battle_dirim.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
#("toh_battle_atia",  	"toh_battle_atia.mp3",mtf_module_track,mtf_sit_fight|mtf_sit_ambushed),
#("toh_battle_tohlobaria", 	"toh_battle_tohlobaria.mp3", mtf_module_track,mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_doom_knights",     	"toh_battle_doom_knights.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
#("toh_battle_new_order",    	"toh_battle_new_order.mp3", mtf_module_track, mtf_sit_fight|mtf_sit_ambushed),
#("toh_battle_golden_horde",  	"toh_battle_golden_horde.mp3", mtf_module_track,mtf_sit_fight|mtf_sit_ambushed),
#("toh_battle_desert_tribes",  	"toh_battle_desert_tribes.mp3", mtf_module_track, mtf_sit_fight|mtf_sit_ambushed),
("toh_battle_galnar_clan",  	"toh_battle_galnar_clan.ogg", mtf_module_track, mtf_sit_fight|mtf_sit_ambushed),

("toh_battle_deploy",  	"toh_battle_deploy_ogg", mtf_module_track|mtf_sit_fight, mtf_sit_fight|mtf_sit_ambushed),
("fight_1", "fight_1.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("fight_2", "fight_2.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight),
("fight_3", "fight_3.ogg", mtf_module_track|mtf_sit_ambushed,mtf_sit_fight|mtf_sit_ambushed),
("fight_4", "fight_4.ogg", mtf_module_track,mtf_sit_fight),
("fight_5", "fight_5.ogg", mtf_module_track|mtf_sit_ambushed,mtf_sit_fight|mtf_sit_ambushed),
#("percussion_battery", "percussion_battery.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("fight_while_mounted_1", "fight_while_mounted_1.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("fight_while_mounted_2", "fight_while_mounted_2.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("warband_action", "warband_action.ogg", mtf_module_track|mtf_sit_fight,mtf_sit_fight|mtf_sit_ambushed),
("toh_fight_neutral", "toh_fight_neutral.ogg", mtf_module_track,mtf_sit_fight|mtf_sit_ambushed),

#Faction territory tracks - faction tracks need to be kept together
#If any of these tracks change, you need to update script_music_set_situation_with_culture
# ("toh_map_pravar", "toh_map_pravar.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),#

("toh_map_pravar_1", "toh_map_pravar_1.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_pravar_2", "toh_map_pravar_2.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_borovod_1", "toh_map_borovod_1.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_borovod_2", "toh_map_borovod_2.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_borovod_3", "toh_map_borovod_3.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_guhulay_1", "toh_map_guhulay_1.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_guhulay_2", "toh_map_guhulay_2.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_hadvog_1", "toh_map_hadvog_1.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_hadvog_2", "toh_map_hadvog_2.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_imifir_1", "toh_map_imifir_1.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_imifir_2", "toh_map_imifir_2.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_afirid_1", "toh_map_afirid_1.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_afirid_2", "toh_map_afirid_2.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),

("toh_map_dirim_1", "toh_map_dirim_1.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_dirim_2", "toh_map_dirim_2.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#

("toh_map_atia", "toh_map_atia.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#

#--ambient tracks
("toh_ambient_map", "toh_ambient_map.ogg",mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night),
("toh_ambient_battle", "toh_ambient_battle.ogg", mtf_module_track|mtf_sit_travel,mtf_sit_fight|mtf_sit_ambushed),
("toh_ambient_town",   "toh_ambient_town.ogg",    mtf_module_track|mtf_sit_travel,mtf_sit_town|mtf_sit_travel|mtf_sit_night),
#--

#TLD town tracks
("toh_central_town",   "toh_central_town.ogg",    mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_pravar_town",   "toh_pravar_town.ogg",    mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_borovod_town",   "toh_borovod_town.ogg",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_hadvog_town",   "toh_hadvog_town.ogg",    mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_guhulay_town",   "toh_guhulay_town.ogg",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_imifir_town",   "toh_imifir_town.ogg",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_afirid_town",   "toh_afirid_town.ogg",  mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_dirim_town",   "toh_dirim_town.mp3",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_atia_town",   "toh_atia_town.mp3",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),
("toh_tohlobaria_town",   "toh_tohlobaria_town.mp3",   mtf_module_track,mtf_sit_tavern|mtf_sit_town|mtf_sit_travel|mtf_sit_night),


#old travel tracks
# ("travel_khergit", "travel_khergit.ogg",                 mtf_culture_3|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_neutral", "travel_neutral.ogg",                               mtf_sit_travel, mtf_sit_tavern|mtf_sit_night                ),
# ("travel_nord",    "travel_nord.ogg"   ,                 mtf_culture_4|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_rhodok",  "travel_rhodok.ogg" ,                 mtf_culture_5|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_swadian", "toh_Gondor_Map.mp3",mtf_module_track|mtf_culture_1|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_vaegir",  "travel_vaegir.ogg" ,                 mtf_culture_2|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_khand",  "travel_neutral.ogg" ,                 mtf_culture_5|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("travel_umbar", "toh_Corsair_Map.mp3" ,mtf_module_track|mtf_culture_5|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("uncertain_homestead", "uncertain_homestead.ogg", mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),

#TLD travel tracks
#Common travel and night tracks
#If the number of the Day tracks change, update script_music_set_situation_with_culture
("toh_map_day_1", "toh_map_day_1.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_day_2", "toh_map_day_2.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_day_3", "toh_map_day_3.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_day_4", "toh_map_day_4.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_day_5", "toh_map_day_5.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),#
("toh_map_day_6", "toh_map_day_6.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_day_7", "toh_map_day_7.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_day_8", "toh_map_day_8.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_day_9", "toh_map_day_8.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
("toh_map_day_10", "toh_map_day_8.ogg",  mtf_module_track|mtf_sit_travel,mtf_sit_travel|mtf_sit_night|mtf_sit_tavern),
#Night tracks are played by the MB jukebox, plus night travel scripting
("toh_map_night_1", "toh_map_night_1.ogg", mtf_module_track|mtf_sit_night, mtf_sit_travel|mtf_sit_tavern),#
("toh_map_night_2", "toh_map_night_2.ogg", mtf_module_track|mtf_sit_night, mtf_sit_travel|mtf_sit_tavern),#
#("toh_map_night_3", "toh_map_night_3.ogg", mtf_module_track|mtf_sit_night, mtf_sit_travel),#
("toh_map_night_4", "toh_map_night_4.ogg", mtf_module_track|mtf_sit_night, mtf_sit_travel|mtf_sit_tavern),#

  ("tavern_1", "tavern_1.ogg", mtf_module_track|mtf_sit_feast|mtf_sit_tavern, 0),
  ("tavern_2", "tavern_2.ogg", mtf_module_track|mtf_sit_feast|mtf_sit_tavern, 0),
  ("tavern_3", "tavern_3.ogg", mtf_module_track|mtf_sit_feast|mtf_sit_tavern, 0),
  ("tavern_4", "tavern_4.ogg", mtf_module_track|mtf_sit_feast|mtf_sit_tavern, 0),
  ("tavern_5", "tavern_5.ogg", mtf_module_track|mtf_sit_feast|mtf_sit_tavern, 0),
  ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
  ("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  
    ("seige_neutral", "seige_neutral.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),

  ("siege_attempt", "siege_attempt.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  


#siege tracks
("toh_bad_siege",  "toh_bad_siege.ogg",  mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),
("toh_siege_2", "toh_siege_2.ogg", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),


#old battle music - all Native tracks
# ("fight_1"              , "fight_1.ogg"              ,               mtf_sit_fight|mtf_sit_ambushed, 0),
# ("fight_2"              , "fight_2.ogg"              ,               mtf_sit_fight|mtf_sit_ambushed, 0),
# ("fight_3"              , "fight_3.ogg"              ,               mtf_sit_fight|mtf_sit_ambushed, 0),
# ("fight_as_vaegir"      , "fight_as_vaegir.ogg"      , mtf_culture_2|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
# ("fight_as_khergit"     , "fight_as_khergit.ogg"     , mtf_culture_3|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
# ("fight_as_nord"        , "fight_as_nord.ogg"        , mtf_culture_4|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
# ("fight_as_rhodok"      , "fight_as_rhodok.ogg"      , mtf_culture_5|mtf_sit_fight|mtf_sit_ambushed, mtf_culture_all),
# ("fight_while_mounted_1", "fight_while_mounted_1.ogg",               mtf_sit_fight|mtf_sit_ambushed, 0),
# ("fight_while_mounted_2", "fight_while_mounted_2.ogg",               mtf_sit_fight|mtf_sit_ambushed, 0),
 
# ("infiltration_evil", "toh_Infiltration_Evil.mp3", mtf_module_track|mtf_culture_evil|mtf_sit_town_infiltrate, mtf_culture_all),
# ("infiltration_good", "toh_Infiltrate_Good.mp3"  , mtf_module_track|mtf_culture_good|mtf_sit_town_infiltrate, mtf_culture_all),

("toh_lords_hall_afirid", "toh_lords_hall_afirid.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_pravar", "toh_lords_hall_pravar.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_imifir", "toh_lords_hall_imifir.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_dirim", "toh_lords_hall_dirim.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_atia", "toh_lords_hall_atia.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_hadvog", "toh_lords_hall_hadvog.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_borovod", "toh_lords_hall_borovod.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_guhulay", "toh_lords_hall_guhulay.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
("toh_lords_hall_tohlobaria", "toh_lords_hall_tohlobaria.ogg"    ,                mtf_module_track| mtf_sit_lords_hall, mtf_sit_feast| mtf_sit_lords_hall),
# ("lords_hall_goodmen", "toh_Rohan_LordHall.mp3"    ,mtf_module_track|mtf_culture_2|mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),
# ("lords_hall_orcs"   , "lords_hall_khergit.ogg"    ,                 mtf_culture_3|mtf_sit_travel, mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
# ("lords_hall_nord"   , "lords_hall_nord.ogg"       ,                               mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),
# ("lords_hall_rhodok" , "lords_hall_rhodok.ogg"     ,                               mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),
# ("lords_hall_khand","toh_Easterlings_LordsHall.mp3",mtf_module_track|mtf_culture_5|mtf_sit_travel, mtf_sit_night|mtf_sit_tavern|mtf_culture_all),

# ("mounted_snow_terrain_calm", "mounted_snow_terrain_calm.ogg", mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),
#("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),
# ("outdoor_beautiful_land", "outdoor_beautiful_land.ogg", mtf_sit_travel, mtf_sit_night|mtf_sit_tavern),
#("retreat", "retreat.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

#("seige_neutral", "toh_Siege.mp3", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),

#no taverns in TLD
# ("tavern_1", "tavern_1.ogg", mtf_sit_tavern, 0),
# ("tavern_2", "tavern_2.ogg", mtf_sit_tavern, 0),

#old town music
# ("town_neutral", "toh_Town_Neutral.mp3" ,mtf_module_track|              mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
# ("town_khergit", "toh_Isengard_Town.mp3",mtf_module_track|mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("town_nord"   , "town_nord.ogg"        ,                 mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("town_rhodok" , "toh_Harad_Town.mp3"   ,mtf_module_track|mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("town_swadian", "toh_Town_Gondor.mp3"  ,mtf_module_track|mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
# ("town_vaegir" , "toh_Rohan_Town.mp3"   ,mtf_module_track|mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),








   ("tragic_village", "tragic_village.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

# victory tracks, never called directly
  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("victorious_swadian", "victorious_swadian.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_vaegir.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("black_order", "black_order.ogg", mtf_sit_fight|mtf_sit_ambushed,0), 
  ("ruins", "ruins.ogg",mtf_persist_until_finished, 0),
  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),
  ("death", "death.ogg", mtf_module_track|mtf_start_immediately, 0),

]
