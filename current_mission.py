if __name__ == "__main__":
    curr_mission = -1
    mission_choice = int(input("Enter the current mission number: "))

    
    match mission_choice:
        case 1:
            from Missions.mission_01 import run_mission;
            curr_mission = run_mission()
        case 3:
            from Missions.mission_03 import run_mission;
            curr_mission = run_mission()
        case 4:
            from Missions.mission_04 import run_mission;
            curr_mission = run_mission()
        case 5:
            from Missions.mission_05 import run_mission;
            curr_mission = run_mission()
        case 6:
            from Missions.mission_06 import run_mission;
            curr_mission = run_mission()
        case 7:
            from Missions.mission_07 import run_mission
            curr_mission = run_mission()
        case 8:
            from Missions.mission_08 import run_mission
            curr_mission = run_mission()
        case 12:
            from Missions.mission_12 import run_mission
            curr_mission = run_mission()
        case 13:
            from Missions.mission_13 import run_mission
            curr_mission = run_mission()
        case 14:
            from Missions.mission_14 import run_mission
            curr_mission = run_mission()
        case _:
            print(f"ERROR: Mission {mission_choice} does not exist!\nEnding program")
    
    if (curr_mission != -1):
        curr_mission