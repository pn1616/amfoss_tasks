import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import csv
import datetime

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

csv_file_path = "live_scores.csv"

bot = commands.Bot(command_prefix="/")

def write_to_csv(team1_name, team2_name, overs_score_text, match_summary):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([current_time, team1_name, team2_name, overs_score_text, match_summary])

@bot.command(name="livescore")
async def get_livescore(ctx):
    team1_name = "Team 1"
    team2_name = "Team 2"
    overs_score_text = "42/0"
    match_summary = "Team 2 chose to bat"
    
    write_to_csv(team1_name, team2_name, overs_score_text, match_summary)
    
    await ctx.send(f"Team 1 Name: {team1_name}\nTeam 2 Name: {team2_name}\nOvers and Score: {overs_score_text}\nMatch Summary: {match_summary}")

@bot.command(name="generate")
async def generate_csv(ctx):
    if not os.path.exists(csv_file_path):
        await ctx.send("No live scores available in the CSV file.")
        return
    
    with open(csv_file_path, "rb") as file:
        file_data = discord.File(file, filename="live_scores.csv")
        await ctx.send("Here is the live scores CSV file:", file=file_data)

@bot.command(name="help")
async def bot_help(ctx):
    help_message = (
        "Available commands:\n"
        "/livescore - Get the live score of the match and save to CSV.\n"
        "/generate - Retrieve the live scores CSV file.\n"
        "/help - Display this help message."
    )
    await ctx.send(help_message)

bot.run(TOKEN)
