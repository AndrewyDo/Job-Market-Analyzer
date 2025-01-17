import pandas as pd
from collections import Counter

def analyze_skills(file_path):
    """
    Analyzes skills from job titles in the given CSV file and outputs a frequency count.
    """
    df = pd.read_csv(file_path)
    skills = ["Python", "SQL", "Machine Learning", "Data Analysis", "Java"]
    skill_counts = Counter()

    for title in df["Title"]:
        for skill in skills:
            if skill.lower() in title.lower():
                skill_counts[skill] += 1

    # Save analysis to JSON
    skill_counts_dict = dict(skill_counts)
    with open("../data/skill_analysis.json", "w") as f:
        import json
        json.dump(skill_counts_dict, f)

    print("Skill analysis saved to 'skill_analysis.json'.")
    return skill_counts_dict

if __name__ == "__main__":
    analyze_skills("../data/linkedin_jobs.csv")
