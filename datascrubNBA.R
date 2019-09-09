players <- subset(player_data, player_data$year_end > 1984)
season.stats <- subset(Seasons_Stats, Seasons_Stats$Year > 1984)
write.csv(players, "players.csv")
write.csv(season.stats, "season_stats.csv")

