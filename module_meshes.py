from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("pic_bandits", 0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_mb_warrior_1", 0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_messenger", 0, "pic_messenger", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_siege_sighted", 0, "pic_siege_sighted", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_siege_sighted_fem", 0, "pic_siege_sighted_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_victory", 0, "pic_victory", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_steppe_bandits", 0, "pic_steppe_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_mountain_bandits", 0, "pic_mountain_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sea_raiders", 0, "pic_sea_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_deserters", 0, "pic_deserters", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_forest_bandits", 0, "pic_forest_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_village_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_village_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_village_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_swadian", 0, "pic_arms_swadian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_vaegir", 0, "pic_arms_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_khergit", 0, "pic_arms_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_nord", 0, "pic_arms_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_rhodok", 0, "pic_arms_rhodok", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sarranid_arms", 0, "pic_sarranid_arms", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #-----new factions-------
  ("pic_arms_dirim", 0, "pic_arms_dirim", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_company", 0, "pic_arms_company", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_tohlobaria", 0, "pic_arms_tohlobaria", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #------------------------
  ("pic_swad", 0, "pic_swad", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_vaegir", 0, "pic_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_khergit", 0, "pic_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_nord", 0, "pic_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_rhodock", 0, "pic_rhodock", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sarranid_encounter", 0, "pic_sarranid_encounter", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_castle1", 0, "pic_castle1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_castledes", 0, "pic_castledes", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_castlesnow", 0, "pic_castlesnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_charge", 0, "pic_charge", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sally_out", 0, "pic_sally_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_siege_attack", 0, "pic_siege_attack", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_town1", 0, "pic_town1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_towndes", 0, "pic_towndes", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_townriot", 0, "pic_townriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_townsnow", 0, "pic_townsnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_villageriot", 0, "pic_villageriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #--
  ("pic_mb_weapons", 0, "pic_mb_weapons", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_town_recruit", 0, "pic_town_recruit", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("pic_castle_recruit", 0, "pic_castle_recruit", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("pic_siege_of_dirim", 0, "pic_siege_of_dirim", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("pic_menu_death", 0, "pic_menu_death", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  #--

  ("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("color_picker", 0, "color_picker",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("custom_map_banner_01", 0, "custom_map_banner_01",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_02", 0, "custom_map_banner_02",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_03", 0, "custom_map_banner_03",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_banner_01", 0, "custom_banner_01",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_02", 0, "custom_banner_02",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_bg", 0, "custom_banner_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg01", 0, "custom_banner_fg01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg02", 0, "custom_banner_fg02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg03", 0, "custom_banner_fg03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg04", 0, "custom_banner_fg04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg05", 0, "custom_banner_fg05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg06", 0, "custom_banner_fg06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg07", 0, "custom_banner_fg07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg08", 0, "custom_banner_fg08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg09", 0, "custom_banner_fg09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg10", 0, "custom_banner_fg10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg11", 0, "custom_banner_fg11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg12", 0, "custom_banner_fg12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg13", 0, "custom_banner_fg13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg14", 0, "custom_banner_fg14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg15", 0, "custom_banner_fg15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg16", 0, "custom_banner_fg16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg17", 0, "custom_banner_fg17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg18", 0, "custom_banner_fg18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg19", 0, "custom_banner_fg19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg20", 0, "custom_banner_fg20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg21", 0, "custom_banner_fg21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg22", 0, "custom_banner_fg22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg23", 0, "custom_banner_fg23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_01", 0, "custom_banner_charge_01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_02", 0, "custom_banner_charge_02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_03", 0, "custom_banner_charge_03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_04", 0, "custom_banner_charge_04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_05", 0, "custom_banner_charge_05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_06", 0, "custom_banner_charge_06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_07", 0, "custom_banner_charge_07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_08", 0, "custom_banner_charge_08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_09", 0, "custom_banner_charge_09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_10", 0, "custom_banner_charge_10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_11", 0, "custom_banner_charge_11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_12", 0, "custom_banner_charge_12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_13", 0, "custom_banner_charge_13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_14", 0, "custom_banner_charge_14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_15", 0, "custom_banner_charge_15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_16", 0, "custom_banner_charge_16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_17", 0, "custom_banner_charge_17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_18", 0, "custom_banner_charge_18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_19", 0, "custom_banner_charge_19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_20", 0, "custom_banner_charge_20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_21", 0, "custom_banner_charge_21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_22", 0, "custom_banner_charge_22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_23", 0, "custom_banner_charge_23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_24", 0, "custom_banner_charge_24",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_25", 0, "custom_banner_charge_25",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_26", 0, "custom_banner_charge_26",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_27", 0, "custom_banner_charge_27",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_28", 0, "custom_banner_charge_28",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_29", 0, "custom_banner_charge_29",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_30", 0, "custom_banner_charge_30",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_31", 0, "custom_banner_charge_31",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_32", 0, "custom_banner_charge_32",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_33", 0, "custom_banner_charge_33",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_34", 0, "custom_banner_charge_34",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_35", 0, "custom_banner_charge_35",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_36", 0, "custom_banner_charge_36",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_37", 0, "custom_banner_charge_37",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_38", 0, "custom_banner_charge_38",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_39", 0, "custom_banner_charge_39",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_40", 0, "custom_banner_charge_40",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_41", 0, "custom_banner_charge_41",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_42", 0, "custom_banner_charge_42",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_43", 0, "custom_banner_charge_43",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_44", 0, "custom_banner_charge_44",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_45", 0, "custom_banner_charge_45",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_46", 0, "custom_banner_charge_46",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_shield_round_1",  0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_2",  0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_3",  0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_4",  0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_5",  0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_1",  0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_2",  0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_3",  0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_1",   0, "tableau_mesh_shield_kite_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_2",   0, "tableau_mesh_shield_kite_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_3",   0, "tableau_mesh_shield_kite_3",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_4",   0, "tableau_mesh_shield_kite_4",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("heraldic_armor_bg", 0, "heraldic_armor_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("heraldic_armor_bg_new", 0, "heraldic_armor_bg_new",  0, 0, 0, 0, 0, 0, 10, 10, 10),#--toh 0.51

  ("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("outer_terrain_plain_1", 0, "ter_border_a", -90, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #--banners
  ("banner_pravar_01", 0, "banner_pravar_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--pravar
  ("banner_pravar_02", 0, "banner_pravar_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_03", 0, "banner_pravar_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_04", 0, "banner_pravar_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_05", 0, "banner_pravar_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_06", 0, "banner_pravar_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_07", 0, "banner_pravar_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_08", 0, "banner_pravar_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_09", 0, "banner_pravar_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_10", 0, "banner_pravar_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_11", 0, "banner_pravar_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_pravar_12", 0, "banner_pravar_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_01", 0, "banner_imifir_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--imifir
  ("banner_imifir_02", 0, "banner_imifir_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_03", 0, "banner_imifir_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_04", 0, "banner_imifir_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_05", 0, "banner_imifir_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_06", 0, "banner_imifir_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_07", 0, "banner_imifir_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_08", 0, "banner_imifir_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_09", 0, "banner_imifir_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_10", 0, "banner_imifir_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_11", 0, "banner_imifir_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imifir_12", 0, "banner_imifir_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_01", 0, "banner_guhulay_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--guhulay
  ("banner_guhulay_02", 0, "banner_guhulay_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_03", 0, "banner_guhulay_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_04", 0, "banner_guhulay_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_05", 0, "banner_guhulay_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_06", 0, "banner_guhulay_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_07", 0, "banner_guhulay_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_08", 0, "banner_guhulay_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_09", 0, "banner_guhulay_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_10", 0, "banner_guhulay_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_11", 0, "banner_guhulay_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guhulay_12", 0, "banner_guhulay_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_01", 0, "banner_afirid_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--afirid
  ("banner_afirid_02", 0, "banner_afirid_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_03", 0, "banner_afirid_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_04", 0, "banner_afirid_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_05", 0, "banner_afirid_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_06", 0, "banner_afirid_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_07", 0, "banner_afirid_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_08", 0, "banner_afirid_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_09", 0, "banner_afirid_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_10", 0, "banner_afirid_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_11", 0, "banner_afirid_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_afirid_12", 0, "banner_afirid_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_01", 0, "banner_borovod_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--borovod
  ("banner_borovod_02", 0, "banner_borovod_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_03", 0, "banner_borovod_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_04", 0, "banner_borovod_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_05", 0, "banner_borovod_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_06", 0, "banner_borovod_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_07", 0, "banner_borovod_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_08", 0, "banner_borovod_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_09", 0, "banner_borovod_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_10", 0, "banner_borovod_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_11", 0, "banner_borovod_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_borovod_12", 0, "banner_borovod_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_01", 0, "banner_hadvog_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--hadvog
  ("banner_hadvog_02", 0, "banner_hadvog_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_03", 0, "banner_hadvog_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_04", 0, "banner_hadvog_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_05", 0, "banner_hadvog_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_06", 0, "banner_hadvog_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_07", 0, "banner_hadvog_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_08", 0, "banner_hadvog_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_09", 0, "banner_hadvog_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_10", 0, "banner_hadvog_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_11", 0, "banner_hadvog_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_hadvog_12", 0, "banner_hadvog_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_01", 0, "banner_baron_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--baron
  ("banner_baron_02", 0, "banner_baron_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_03", 0, "banner_baron_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_04", 0, "banner_baron_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_05", 0, "banner_baron_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_06", 0, "banner_baron_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_07", 0, "banner_baron_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_08", 0, "banner_baron_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_09", 0, "banner_baron_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_10", 0, "banner_baron_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_11", 0, "banner_baron_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_12", 0, "banner_baron_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_13", 0, "banner_baron_13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_14", 0, "banner_baron_14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_15", 0, "banner_baron_15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_16", 0, "banner_baron_16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_17", 0, "banner_baron_17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_18", 0, "banner_baron_18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_19", 0, "banner_baron_19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_20", 0, "banner_baron_20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_01", 0, "banner_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),#--others banners
  ("banner_02", 0, "banner_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_03", 0, "banner_03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_04", 0, "banner_04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_05", 0, "banner_05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_06", 0, "banner_06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_07", 0, "banner_07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_08", 0, "banner_08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_09", 0, "banner_09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_10", 0, "banner_10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_11", 0, "banner_11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_12", 0, "banner_12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_13", 0, "banner_13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_14", 0, "banner_14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_15", 0, "banner_15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_16", 0, "banner_16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_17", 0, "banner_17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_18", 0, "banner_18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_19", 0, "banner_19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_20", 0, "banner_20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_21", 0, "banner_21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_22", 0, "banner_22", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_23", 0, "banner_23", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_24", 0, "banner_24", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_25", 0, "banner_25", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_26", 0, "banner_26", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_27", 0, "banner_27", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_28", 0, "banner_28", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_29", 0, "banner_29", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_30", 0, "banner_30", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_31", 0, "banner_31", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_32", 0, "banner_32", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_33", 0, "banner_33", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_34", 0, "banner_34", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_35", 0, "banner_35", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_36", 0, "banner_36", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_37", 0, "banner_37", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_38", 0, "banner_38", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_39", 0, "banner_39", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_40", 0, "banner_40", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_41", 0, "banner_41", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_42", 0, "banner_42", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_43", 0, "banner_43", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_44", 0, "banner_44", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_45", 0, "banner_45", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_46", 0, "banner_46", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_47", 0, "banner_47", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_48", 0, "banner_48", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_49", 0, "banner_49", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_50", 0, "banner_50", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_51", 0, "banner_51", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_52", 0, "banner_52", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_53", 0, "banner_53", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_54", 0, "banner_54", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  #----------------
  ("banner_kingdom_t_a", 0, "banner_kingdom_t_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  #----------------
    #----------------
  ("banner_kingdom_t_b", 0, "banner_kingdom_t_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  #----------------
  #("banner_f21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_baron_21", 0, "banner_baron_21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

# ("arms_a01", 0, "arms_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  # ("arms_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  # ("arms_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  # ("arms_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  # ("arms_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  # ("arms_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),  
  # ("arms_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),
	##------------------
  # ("arms_kingdom_t_a", 0, "banner_kingdom_t_a", 0, 0, 0, -90, 0, 0, 1, 1, 1), 
	##----------------------
  # ("arms_f21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),


  ("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  
  ("troop_label_banner",  0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("ui_kingdom_shield_1", 0, "ui_kingdom_shield_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_2", 0, "ui_kingdom_shield_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_3", 0, "ui_kingdom_shield_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_4", 0, "ui_kingdom_shield_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_5", 0, "ui_kingdom_shield_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_6", 0, "ui_kingdom_shield_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #("flag_pravar", 0, "banner_a01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_borovod", 0, "banner_a02", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_guhulay", 0, "banner_d01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_hadvog", 0, "banner_a03", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_imifir", 0, "banner_a04", 0, 0, 0, 0, 0, 0, 1, 1, 1),  

  ("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("status_ammo_ready", 0, "status_ammo_ready", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("ui_quick_battle_a", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_infantry", 0, "cb_ui_icon_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_archer", 0, "cb_ui_icon_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_horseman", 0, "cb_ui_icon_horseman", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_host_maps_14", 0, "mp_ui_host_maps_c4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_15", 0, "mp_ui_host_maps_c5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("quit_adv", 0, "quit_adv", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("quit_adv_b", 0, "quit_adv_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("flag_project_rb", 0, "flag_project_rb", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rb_miss", 0, "flag_project_rb_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_16", 0, "mp_ui_host_maps_d1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_17", 0, "mp_ui_host_maps_d2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_18", 0, "mp_ui_host_maps_d3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_19", 0, "mp_ui_host_maps_e2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_20", 0, "mp_ui_host_maps_e1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
	#------------bogmir_items------
  ("tableau_mesh_mail_long_surcoat_new_heraldic", 0, "tableau_mesh_mail_long_surcoat_new_heraldic",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_brigandine_b_heraldic", 0, "tableau_mesh_brigandine_b_heraldic",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_toh_brigandine_heraldic", 0, "tableau_mesh_toh_brigandine_heraldic",  0, 0, 0, 0, 0, 0, 1, 1, 1),#--
  ("tableau_mesh_heraldic_tunic_new", 0, "tableau_mesh_heraldic_tunic_new",  0, 0, 0, 0, 0, 0, 1, 1, 1),
   #--------------------------------
   #--------------narf's_transitional_armour_pack-----------
    ("tableau_mesh_early_transitional_heraldic_banner", 0, "tableau_mesh_early_transitional_heraldic_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_early_transitional_heraldic", 0, "tableau_mesh_early_transitional_heraldic",  0, 0, 0, 0, 0, 0, 1, 1, 1),
   #--------------------------------------------------------
	#----------------upgrade troop in town (akademy osp by somebody)---------- 
	("face_gen_window", 0, "upgrade_troop", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	("icon_gold", 0, "mp_ico_gold", 0, 0, 0, 0, 0, 0, 1, 1, 1),
	("icon_arrow_left", 0, "arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
   #---------------------------------------------------------------------------
   
   #--------------baraban's items-----------
  ("tableau_mesh_platemail_banner", 0, "tableau_mesh_platemail_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_platemail", 0, "tableau_mesh_platemail",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_platemail_02_banner", 0, "tableau_mesh_platemail_02_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_platemail_02", 0, "tableau_mesh_platemail_02",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_platemail_08_banner", 0, "tableau_mesh_platemail_08_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_platemail_08", 0, "tableau_mesh_platemail_08",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_costumes9_banner", 0, "tableau_mesh_costumes9_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_costumes9", 0, "tableau_mesh_costumes9",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_brig_plate", 0, "tableau_mesh_brig_plate",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_brig_plate_banner", 0, "tableau_mesh_brig_plate_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),   
   #-----------------------------------
   #--toh heraldic
   ("tableau_mesh_heraldic_churburg_banner", 0, "tableau_mesh_heraldic_churburg_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("tableau_mesh_heraldic_churburg", 0, "tableau_mesh_heraldic_churburg",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("tableau_mesh_heraldic_corrazina_banner", 0, "tableau_mesh_heraldic_corrazina_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("tableau_mesh_heraldic_corrazina", 0, "tableau_mesh_heraldic_corrazina",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("tableau_mesh_gothic_armor_banner", 0, "tableau_mesh_gothic_armor_banner",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_gothic_armor", 0, "tableau_mesh_gothic_armor",  0, 0, 0, 0, 0, 0, 1, 1, 1),
   #--
   #--bogmir heraldic shield
  ("tableau_mesh_shield_sarranids_a", 0, "tableau_mesh_shield_sarranids_a",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_sarranids_b", 0, "tableau_mesh_shield_sarranids_b",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_sarranids_c", 0, "tableau_mesh_shield_sarranids_c",  0, 0, 0, 0, 0, 0, 10, 10, 10),
   #--
   #--cwe heraldic shield
   ("tableau_mesh_lobarian_knight_shield", 0, "tableau_mesh_lobarian_knight_shield",  0, 0, 0, 0, 0, 0, 10, 10, 10),
   #--
   #--heraldic huscarl armor
   ("tableau_mesh_heraldic_jarl_armor", 0, "tableau_mesh_heraldic_jarl_armor",  0, 0, 0, 0, 0, 0, 1, 1, 1),
   #--
   ]