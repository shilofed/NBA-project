package com.example.a2_screens.data

import com.example.a2_screens.R
import com.example.a2_screens.model.Team

val TEAMS_NAMES = listOf<String>("Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards")
class Datasource{
    fun loadTeams(): Map<Int, Team>{
        return mapOf(
            1610612737 to Team(R.integer.atlanta_hawks_id, R.string.atlanta_hawks, R.string.atlanta_hawks_abr, R.drawable.atlanta_hawks),
            1610612738 to Team(R.integer.boston_celtics_id, R.string.boston_celtics, R.string.boston_celtics_abr, R.drawable.boston_celtics),
            1610612751 to Team(R.integer.brooklyn_nets_id, R.string.brooklyn_nets, R.string.brooklyn_nets_abr, R.drawable.brooklyn_nets),
            1610612766 to Team(R.integer.charlotte_hornets_id, R.string.charlotte_hornets, R.string.charlotte_hornets_abr, R.drawable.charlotte_hornets),
            1610612741 to Team(R.integer.chicago_bulls_id, R.string.chicago_bulls, R.string.chicago_bulls_abr, R.drawable.chicago_bulls),
            1610612739 to Team(R.integer.cleveland_cavaliers_id, R.string.cleveland_cavaliers, R.string.cleveland_cavaliers_abr, R.drawable.cleveland_cavaliers),
            1610612742 to Team(R.integer.dallas_mavericks_id, R.string.dallas_mavericks, R.string.dallas_mavericks_abr, R.drawable.dallas_mavericks),
            1610612743 to Team(R.integer.denver_nuggets_id, R.string.denver_nuggets, R.string.denver_nuggets_abr, R.drawable.denver_nuggets),
            1610612765 to Team(R.integer.detroit_pistons_id, R.string.detroit_pistons, R.string.detroit_pistons_abr, R.drawable.detroit_pistons),
            1610612744 to Team(R.integer.golden_state_warriors_id, R.string.golden_state_warriors, R.string.golden_state_warriors_abr, R.drawable.golden_state_warriors),
            1610612745 to Team(R.integer.houston_rockets_id, R.string.houston_rockets, R.string.houston_rockets_abr, R.drawable.houston_rockets),
            1610612754 to Team(R.integer.indiana_pacers_id, R.string.indiana_pacers, R.string.indiana_pacers_abr, R.drawable.indiana_pacers),
            1610612746 to Team(R.integer.los_angeles_clippers_id, R.string.los_angeles_clippers, R.string.los_angeles_clippers_abr, R.drawable.los_angeles_clippers),
            1610612747 to Team(R.integer.los_angeles_lakers_id, R.string.los_angeles_lakers, R.string.los_angeles_lakers_abr, R.drawable.los_angeles_lakers),
            1610612763 to Team(R.integer.memphis_grizzlies_id, R.string.memphis_grizzlies, R.string.memphis_grizzlies_abr, R.drawable.memphis_grizzlies),
            1610612748 to Team(R.integer.miami_heat_id, R.string.miami_heat, R.string.miami_heat_abr, R.drawable.miami_heat),
            1610612749 to Team(R.integer.milwaukee_bucks_id, R.string.milwaukee_bucks, R.string.milwaukee_bucks_abr, R.drawable.milwaukee_bucks),
            1610612750 to Team(R.integer.minnesota_timberwolves_id, R.string.minnesota_timberwolves, R.string.minnesota_timberwolves_abr, R.drawable.minnesota_timberwolves),
            1610612740 to Team(R.integer.new_orleans_pelicans_id, R.string.new_orleans_pelicans, R.string.new_orleans_pelicans_abr, R.drawable.new_orleans_pelicans),
            1610612752 to Team(R.integer.new_york_knicks_id, R.string.new_york_knicks, R.string.new_york_knicks_abr, R.drawable.new_york_knicks),
            1610612760 to Team(R.integer.oklahoma_city_thunder_id, R.string.oklahoma_city_thunder, R.string.oklahoma_city_thunder_abr, R.drawable.oklahoma_city_thunder),
            1610612753 to Team(R.integer.orlando_magic_id, R.string.orlando_magic, R.string.orlando_magic_abr, R.drawable.orlando_magic),
            1610612755 to Team(R.integer.philadelphia_76ers_id, R.string.philadelphia_76ers, R.string.philadelphia_76ers_abr, R.drawable.philadelphia_76ers),
            1610612756 to Team(R.integer.phoenix_suns_id, R.string.phoenix_suns, R.string.phoenix_suns_abr, R.drawable.phoenix_suns),
            1610612757 to Team(R.integer.portland_trail_blazers_id, R.string.portland_trail_blazers, R.string.portland_trail_blazers_abr, R.drawable.portland_trail_blazers),
            1610612758 to Team(R.integer.sacramento_kings_id, R.string.sacramento_kings, R.string.sacramento_kings_abr, R.drawable.sacramento_kings),
            1610612759 to Team(R.integer.san_antonio_spurs_id, R.string.san_antonio_spurs, R.string.san_antonio_spurs_abr, R.drawable.san_antonio_spurs),
            1610612761 to Team(R.integer.toronto_raptors_id, R.string.toronto_raptors, R.string.toronto_raptors_abr, R.drawable.toronto_raptors),
            1610612762 to Team(R.integer.utah_jazz_id, R.string.utah_jazz, R.string.utah_jazz_abr, R.drawable.utah_jazz),
            1610612764 to Team(R.integer.washington_wizards_id, R.string.washington_wizards, R.string.washington_wizards_abr, R.drawable.washington_wizards)
        )
    }
}
