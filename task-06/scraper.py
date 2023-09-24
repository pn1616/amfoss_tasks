import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/live-cricket-score"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    team1_element = soup.find("div", class_="ci-team-score")
    team2_element = soup.find_all("div", class_="ci-team-score")[1]  
    
    match_summary_element = soup.find("p", class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo")
    
    if team1_element and team2_element and match_summary_element:
    
        team1_name = team1_element.find("span", class_="ds-font-bold").text
        team1_overs_score_element = team1_element.find("div", class_="ds-text-compact-m")
        team1_overs_score_text = team1_overs_score_element.text if team1_overs_score_element else ""
        
        team2_name = team2_element.find("span", class_="ds-font-bold").text
        team2_overs_score_element = team2_element.find("div", class_="ds-text-compact-m")
        team2_overs_score_text = team2_overs_score_element.text if team2_overs_score_element else ""
        
        match_summary = match_summary_element.find("span").text
        
        print("Team 1 Name:", team1_name)
        print("Team 1 Overs and Score:", team1_overs_score_text)
        print("\nTeam 2 Name:", team2_name)
        print("Team 2 Overs and Score:", team2_overs_score_text)
        print("\nMatch Summary:", match_summary)
    else:
        print("Elements not found on the page.")
else:
    print("Failed to retrieve the webpage.")
