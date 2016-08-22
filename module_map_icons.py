from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
  ("player",0,"player", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("town",mcn_no_shadow,"map_town_a", 0.35,0),
  ("town_steppe",mcn_no_shadow,"map_town_steppe_a", 0.35,0),
  ("town_capital",mcn_no_shadow,"dutch_town", 0.35,0),#--dirim
  ("town_pravar",mcn_no_shadow,"map_town_pravar", 0.35,0),#--pravar
  ("town_kalisos",mcn_no_shadow,"map_town_kalisos", 2,0),#--kalisos
  ("town_lankladel",mcn_no_shadow,"map_town_lankladel", 0.35,0),#--lankladel
  ("map_imifir_party",0,"dedal_map_rhodok_band_e", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),#imifir #--dedal map icons osp
  ("map_hadvog_party",0,"map_hadvogs", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),#hadvog#--dedal map icons osp
  ("map_pravar_knight",0,"icon_pravar_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),#pravar#--cwe
  ("map_afirid_knight",0,"icon_afirid_knight", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),#afirid#--cwe
  ("map_camel_rider",0,"icon_camel_rider", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),#desert#--cwe  
  
  ("town_desert",mcn_no_shadow,"map_town_desert_a", 0.35,0),
  ("town_with_port",mcn_no_shadow,"map_tradeport", 0.20, 0),#--free port
  ("village_a",mcn_no_shadow,"map_village_a", 0.45, 0),
  ("village_b",mcn_no_shadow,"map_village_b", 0.45, 0),
  ("village_c",mcn_no_shadow,"map_village_c", 0.45, 0),
  ("village_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
  ("village_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),
  ("village_burnt_b",mcn_no_shadow,"map_village_burnt_b", 0.45, 0),
  ("village_deserted_b",mcn_no_shadow,"map_village_deserted_b", 0.45, 0),
  ("village_burnt_c",mcn_no_shadow,"map_village_burnt_c", 0.45, 0),
  ("village_deserted_c",mcn_no_shadow,"map_village_deserted_c", 0.45, 0),
  ("village_snow_a",mcn_no_shadow,"map_village_snow_a", 0.45, 0),
  ("village_snow_burnt_a",mcn_no_shadow,"map_village_snow_burnt_a", 0.45, 0),
  ("village_snow_deserted_a",mcn_no_shadow,"map_village_snow_deserted_a", 0.45, 0),
  ("camp",mcn_no_shadow,"camp_tent", 0.13, 0),
  ("ship",mcn_no_shadow,"boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"boat_sail_off", 0.23, 0),
  ("castle_a",mcn_no_shadow,"map_castle_a", 0.35,0),
  ("castle_b",mcn_no_shadow,"map_castle_b", 0.35,0),
  ("castle_c",mcn_no_shadow,"map_castle_c", 0.35,0),
  ("castle_d",mcn_no_shadow,"map_castle_d", 0.35,0),
  ("castle_borovod_1",mcn_no_shadow,"map_brorovod_castle", 0.35,0),#--ismirala castle
  ("town_snow",mcn_no_shadow,"map_town_snow_a", 0.35,0),
  ("castle_snow_a",mcn_no_shadow,"map_castle_snow_a", 0.35,0),
  ("castle_snow_b",mcn_no_shadow,"map_castle_snow_b", 0.35,0),
  ("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
  ("training_ground",mcn_no_shadow,"training", 0.35,0),
  ("bridge_a",mcn_no_shadow,"map_river_bridge_a", 1.27,0),
  ("bridge_b",mcn_no_shadow,"map_river_bridge_b", 0.7,0),
  ("bridge_snow_a",mcn_no_shadow,"map_river_bridge_snow_a", 1.27,0),
  ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   [
     (ti_on_init_map_icon,
      [
        (store_trigger_param_1, ":party_no"),
        (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        (try_end),
        ]),
     ]),
  # Banners
  ("banner_pravar_01",0,"map_flag_pravar01", banner_scale,0),#--pravar
  ("banner_pravar_02",0,"map_flag_pravar02", banner_scale,0),
  ("banner_pravar_03",0,"map_flag_pravar03", banner_scale,0),
  ("banner_pravar_04",0,"map_flag_pravar04", banner_scale,0),
  ("banner_pravar_05",0,"map_flag_pravar05", banner_scale,0),
  ("banner_pravar_06",0,"map_flag_pravar06", banner_scale,0),
  ("banner_pravar_07",0,"map_flag_pravar07", banner_scale,0),
  ("banner_pravar_08",0,"map_flag_pravar08", banner_scale,0),
  ("banner_pravar_09",0,"map_flag_pravar09", banner_scale,0),
  ("banner_pravar_10",0,"map_flag_pravar10", banner_scale,0),
  ("banner_pravar_11",0,"map_flag_pravar11", banner_scale,0),
  ("banner_pravar_12",0,"map_flag_pravar12", banner_scale,0),
  ("banner_imifir_01",0,"map_flag_imifir01", banner_scale,0),#--imifir
  ("banner_imifir_02",0,"map_flag_imifir02", banner_scale,0),
  ("banner_imifir_03",0,"map_flag_imifir03", banner_scale,0),
  ("banner_imifir_04",0,"map_flag_imifir04", banner_scale,0),
  ("banner_imifir_05",0,"map_flag_imifir05", banner_scale,0),
  ("banner_imifir_06",0,"map_flag_imifir06", banner_scale,0),
  ("banner_imifir_07",0,"map_flag_imifir07", banner_scale,0),
  ("banner_imifir_08",0,"map_flag_imifir08", banner_scale,0),
  ("banner_imifir_09",0,"map_flag_imifir09", banner_scale,0),
  ("banner_imifir_10",0,"map_flag_imifir10", banner_scale,0),
  ("banner_imifir_11",0,"map_flag_imifir11", banner_scale,0),
  ("banner_imifir_12",0,"map_flag_imifir12", banner_scale,0),
  ("banner_guhulay_01",0,"map_flag_guhulay01", banner_scale,0),#--guhulay
  ("banner_guhulay_02",0,"map_flag_guhulay02", banner_scale,0),
  ("banner_guhulay_03",0,"map_flag_guhulay03", banner_scale,0),
  ("banner_guhulay_04",0,"map_flag_guhulay04", banner_scale,0),
  ("banner_guhulay_05",0,"map_flag_guhulay05", banner_scale,0),
  ("banner_guhulay_06",0,"map_flag_guhulay06", banner_scale,0),
  ("banner_guhulay_07",0,"map_flag_guhulay07", banner_scale,0),
  ("banner_guhulay_08",0,"map_flag_guhulay08", banner_scale,0),
  ("banner_guhulay_09",0,"map_flag_guhulay09", banner_scale,0),
  ("banner_guhulay_10",0,"map_flag_guhulay10", banner_scale,0),
  ("banner_guhulay_11",0,"map_flag_guhulay11", banner_scale,0),
  ("banner_guhulay_12",0,"map_flag_guhulay12", banner_scale,0),
  ("banner_afirid_01",0,"map_flag_afirid01", banner_scale,0),#--afirid
  ("banner_afirid_02",0,"map_flag_afirid02", banner_scale,0),
  ("banner_afirid_03",0,"map_flag_afirid03", banner_scale,0),
  ("banner_afirid_04",0,"map_flag_afirid04", banner_scale,0),
  ("banner_afirid_05",0,"map_flag_afirid05", banner_scale,0),
  ("banner_afirid_06",0,"map_flag_afirid06", banner_scale,0),
  ("banner_afirid_07",0,"map_flag_afirid07", banner_scale,0),
  ("banner_afirid_08",0,"map_flag_afirid08", banner_scale,0),
  ("banner_afirid_09",0,"map_flag_afirid09", banner_scale,0),
  ("banner_afirid_10",0,"map_flag_afirid10", banner_scale,0),
  ("banner_afirid_11",0,"map_flag_afirid11", banner_scale,0),
  ("banner_afirid_12",0,"map_flag_afirid12", banner_scale,0),
  ("banner_borovod_01",0,"map_flag_borovod01", banner_scale,0),#--borovod
  ("banner_borovod_02",0,"map_flag_borovod02", banner_scale,0),
  ("banner_borovod_03",0,"map_flag_borovod03", banner_scale,0),
  ("banner_borovod_04",0,"map_flag_borovod04", banner_scale,0),
  ("banner_borovod_05",0,"map_flag_borovod05", banner_scale,0),
  ("banner_borovod_06",0,"map_flag_borovod06", banner_scale,0),
  ("banner_borovod_07",0,"map_flag_borovod07", banner_scale,0),
  ("banner_borovod_08",0,"map_flag_borovod08", banner_scale,0),
  ("banner_borovod_09",0,"map_flag_borovod09", banner_scale,0),
  ("banner_borovod_10",0,"map_flag_borovod10", banner_scale,0),
  ("banner_borovod_11",0,"map_flag_borovod11", banner_scale,0),
  ("banner_borovod_12",0,"map_flag_borovod12", banner_scale,0),
  ("banner_hadvog_01",0,"map_flag_hadvog01", banner_scale,0),#--hadvog
  ("banner_hadvog_02",0,"map_flag_hadvog02", banner_scale,0),
  ("banner_hadvog_03",0,"map_flag_hadvog03", banner_scale,0),
  ("banner_hadvog_04",0,"map_flag_hadvog04", banner_scale,0),
  ("banner_hadvog_05",0,"map_flag_hadvog05", banner_scale,0),
  ("banner_hadvog_06",0,"map_flag_hadvog06", banner_scale,0),
  ("banner_hadvog_07",0,"map_flag_hadvog07", banner_scale,0),
  ("banner_hadvog_08",0,"map_flag_hadvog08", banner_scale,0),
  ("banner_hadvog_09",0,"map_flag_hadvog09", banner_scale,0),
  ("banner_hadvog_10",0,"map_flag_hadvog10", banner_scale,0),
  ("banner_hadvog_11",0,"map_flag_hadvog11", banner_scale,0),
  ("banner_hadvog_12",0,"map_flag_hadvog12", banner_scale,0),
  ("banner_baron_01",0,"map_flag_baron01", banner_scale,0),#--barons
  ("banner_baron_02",0,"map_flag_baron02", banner_scale,0),
  ("banner_baron_03",0,"map_flag_baron03", banner_scale,0),
  ("banner_baron_04",0,"map_flag_baron04", banner_scale,0),
  ("banner_baron_05",0,"map_flag_baron05", banner_scale,0),
  ("banner_baron_06",0,"map_flag_baron06", banner_scale,0),
  ("banner_baron_07",0,"map_flag_baron07", banner_scale,0),
  ("banner_baron_08",0,"map_flag_baron08", banner_scale,0),
  ("banner_baron_09",0,"map_flag_baron09", banner_scale,0),
  ("banner_baron_10",0,"map_flag_baron10", banner_scale,0),
  ("banner_baron_11",0,"map_flag_baron11", banner_scale,0),
  ("banner_baron_12",0,"map_flag_baron12", banner_scale,0),
  ("banner_baron_13",0,"map_flag_baron13", banner_scale,0),
  ("banner_baron_14",0,"map_flag_baron14", banner_scale,0),
  ("banner_baron_15",0,"map_flag_baron15", banner_scale,0),
  ("banner_baron_16",0,"map_flag_baron16", banner_scale,0),
  ("banner_baron_17",0,"map_flag_baron17", banner_scale,0),
  ("banner_baron_18",0,"map_flag_baron18", banner_scale,0),
  ("banner_baron_19",0,"map_flag_baron19", banner_scale,0),
  ("banner_baron_20",0,"map_flag_baron20", banner_scale,0),
  #("banner_baron_21",0,"map_flag_baron21", banner_scale,0),
  ("banner_01",0,"map_flag_01", banner_scale,0),#--others banners
  ("banner_02",0,"map_flag_02", banner_scale,0),
  ("banner_03",0,"map_flag_03", banner_scale,0),
  ("banner_04",0,"map_flag_04", banner_scale,0),
  ("banner_05",0,"map_flag_05", banner_scale,0),
  ("banner_06",0,"map_flag_06", banner_scale,0),
  ("banner_07",0,"map_flag_07", banner_scale,0),
  ("banner_08",0,"map_flag_08", banner_scale,0),
  ("banner_09",0,"map_flag_09", banner_scale,0),
  ("banner_10",0,"map_flag_10", banner_scale,0),
  ("banner_11",0,"map_flag_11", banner_scale,0),
  ("banner_12",0,"map_flag_12", banner_scale,0),
  ("banner_13",0,"map_flag_13", banner_scale,0),
  ("banner_14",0,"map_flag_14", banner_scale,0),
  ("banner_15",0,"map_flag_15", banner_scale,0),
  ("banner_16",0,"map_flag_16", banner_scale,0), 
  ("banner_17",0,"map_flag_17", banner_scale,0),
  ("banner_18",0,"map_flag_18", banner_scale,0),
  ("banner_19",0,"map_flag_19", banner_scale,0),
  ("banner_20",0,"map_flag_20", banner_scale,0),
  ("banner_21",0,"map_flag_21", banner_scale,0),
  ("banner_22",0,"map_flag_22", banner_scale,0),
  ("banner_23",0,"map_flag_23", banner_scale,0),
  ("banner_24",0,"map_flag_24", banner_scale,0),
  ("banner_25",0,"map_flag_25", banner_scale,0),
  ("banner_26",0,"map_flag_26", banner_scale,0),
  ("banner_27",0,"map_flag_27", banner_scale,0),
  ("banner_28",0,"map_flag_28", banner_scale,0),
  ("banner_29",0,"map_flag_29", banner_scale,0),
  ("banner_30",0,"map_flag_30", banner_scale,0),
  ("banner_31",0,"map_flag_31", banner_scale,0),
  ("banner_32",0,"map_flag_32", banner_scale,0),
  ("banner_33",0,"map_flag_33", banner_scale,0),
  ("banner_34",0,"map_flag_34", banner_scale,0),
  ("banner_35",0,"map_flag_35", banner_scale,0),
  ("banner_36",0,"map_flag_36", banner_scale,0),
  ("banner_37",0,"map_flag_37", banner_scale,0),
  ("banner_38",0,"map_flag_38", banner_scale,0),
  ("banner_39",0,"map_flag_39", banner_scale,0), 
  ("banner_40",0,"map_flag_40", banner_scale,0),
  ("banner_41",0,"map_flag_41", banner_scale,0),
  ("banner_42",0,"map_flag_42", banner_scale,0),
  ("banner_43",0,"map_flag_43", banner_scale,0),
  ("banner_44",0,"map_flag_44", banner_scale,0),
  ("banner_45",0,"map_flag_45", banner_scale,0),
  ("banner_46",0,"map_flag_46", banner_scale,0),
  ("banner_47",0,"map_flag_47", banner_scale,0),
  ("banner_48",0,"map_flag_48", banner_scale,0),
  ("banner_49",0,"map_flag_49", banner_scale,0), 
  ("banner_50",0,"map_flag_50", banner_scale,0),
  ("banner_51",0,"map_flag_51", banner_scale,0),
  ("banner_52",0,"map_flag_52", banner_scale,0),
  ("banner_53",0,"map_flag_53", banner_scale,0),
  ("banner_54",0,"map_flag_54", banner_scale,0),
  #("banner_45",0,"map_flag_47", banner_scale,0),

  ("map_flag_kingdom_a",0,"map_flag_kingdom_a", banner_scale,0),
  ("map_flag_kingdom_b",0,"map_flag_kingdom_b", banner_scale,0),
  ("map_flag_kingdom_c",0,"map_flag_kingdom_c", banner_scale,0),
  ("map_flag_kingdom_d",0,"map_flag_kingdom_d", banner_scale,0),
  ("map_flag_kingdom_e",0,"map_flag_kingdom_e", banner_scale,0),
  ("map_flag_kingdom_f",0,"map_flag_kingdom_f", banner_scale,0),
  #-------dirim-------
  ("map_flag_kingdom_t_a",0,"map_flag_kingdom_t_a", banner_scale,0),
  #----------------
   #-------dirim-------
  ("map_flag_kingdom_t_b",0,"map_flag_kingdom_t_b", banner_scale,0),
  #----------------
  #("banner_136",0,"map_flag_15", banner_scale,0),
  #("banner_56",0,"map_flag_56", banner_scale,0),
  ("banner_baron_21",0,"map_flag_baron21", banner_scale,0),
  
  ("bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),
  
]
