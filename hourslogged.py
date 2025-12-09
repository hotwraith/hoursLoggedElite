import os
import json
import glob

#TODO: make this cleaner, none of this should be that long for what it does

def ReadJournal(keypass, CMDR, z):
    global data
    local = os.environ['USERPROFILE']
    infolder = glob.glob(fr'{local}\Saved Games\Frontier Developments\Elite Dangerous\*.log')
    why = len(infolder)-1
    #for z in range(j):
    exit = True
    why = len(infolder)-1
    while exit:
        important = []
        keep_phrase = [f"{keypass[0]}", f"{keypass[1]}"]
        try:
            with open(infolder[why], 'r') as file:
                try:
                    data = file.readlines()
                except UnicodeDecodeError as e:
                    # print(f"Reader threw an {type(e)}, error in carrier DB")
                    pass
            for line in data:
                for phrase in keep_phrase:
                    if phrase in line:
                        important.append(line)
                        break
        except IndexError as e:
            #Sprint(f"No data was found for this carrier ({carrierDB['shortname'][z]}). Skipping to next one (returned {type(e)})")
            exit = False
        try:
            if(len(important) > 0):
                jsonFile = json.dumps(important[0])
                data = json.loads(jsonFile)
                data = json.loads(data)
                if(data['Name'].upper() == CMDR.upper()):
                    jsonFile = json.dumps(important[len(important)-1])
                    data = json.loads(jsonFile)
                    data = json.loads(data)
                    data1 = json.dumps(data['Exploration'])
                    data1 = json.loads(data1)
                    time = round(int(data1['Time_Played'])/3600, 2)
            #        print(f"{CMDR} : {time}h")
                    data = open("CMDRS.json", "r")
                    dataDict = json.load(data)
                    data.close()
                    data2 = open("CMDRS.json", "w")
                    dataDict['PLAYTIME'].append(time)
                    json.dump(dataDict, indent= 4, fp=data2)
                    
                    data2.close()
                    exit =False
        except json.decoder.JSONDecodeError:
            pass
        why -= 1

def sync():
    global data
    carrierDB = json.load(open('CMDRS.json', 'r'))
    local = os.environ['USERPROFILE']
    infolder = glob.glob(fr'{local}\Saved Games\Frontier Developments\Elite Dangerous\*.log')
    why = len(infolder)-1
    #for z in range(j):
    exit = True
    why = len(infolder)-1
    while exit:
        important = []
        keep_phrase = ["FID"]
        try:
            with open(infolder[why], 'r') as file:
                try:
                    data = file.readlines()
                except UnicodeDecodeError as e:
                    # print(f"Reader threw an {type(e)}, error in carrier DB")
                    pass
            for line in data:
                for phrase in keep_phrase:
                    if phrase in line:
                        important.append(line)
                        break
        except IndexError as e:
            #Sprint(f"No data was found for this carrier ({carrierDB['shortname'][z]}). Skipping to next one (returned {type(e)})")
            exit = False
        try:
            if(len(important) > 0):
                jsonFile = json.dumps(important[0])
                data = json.loads(jsonFile)
                data = json.loads(data)
                addCMDR(data['Name'])
                if(why == len(infolder)-101):
                    exit = False
        except json.decoder.JSONDecodeError:
            pass
        why -= 1

def createDict():
    out_file = open("CMDRS.json", "w")
    namedict = {
    "NAME": [],
    "PLAYTIME": []
    }
    json.dump(namedict, indent= 4, fp=out_file)
    out_file.close()

def addCMDR(CMDR):
    thefile = open("CMDRS.json", "r")
    appendCMDR(json.load(thefile), CMDR)
    thefile.close()

def appendCMDR(namedict, CMDR):
    passornot = False
    for i in range(len(namedict['NAME'])):
        if(namedict['NAME'][i].upper() == CMDR.upper()):
            passornot = True
    if(not passornot):
        out_file = open("CMDRS.json", "w")
        namedict['NAME'].append(CMDR)
        json.dump(namedict, indent= 4, fp=out_file)
        out_file.close()

def summation():
    data = open("CMDRS.json", "r")
    dataDict = json.load(data)
    sum = 0
    for i in range(len(dataDict['PLAYTIME'])):
        sum += dataDict['PLAYTIME'][i]
    data.close()
    return sum

def sort_by_hours() -> list:
    infoList = json.load(open('CMDRS.json', 'r'))
    hours = list(infoList['PLAYTIME'])
    sorted_hours =[]
    indexes = []
    for el in hours:
        sorted_hours.append(el)
    sorted_hours.sort(reverse=True)
    for hour in sorted_hours:
        indexes.append(hours.index(hour))
    return indexes


def main():
    createDict()
    sync()
    out_file = open('CMDRS.json', 'r')
    nameList = json.load(out_file)
    for i in range(len(nameList['NAME'])):
        ReadJournal(['FID', 'Statistics'], nameList['NAME'][i], i)
    out_file.close()
    out_file = open('CMDRS.json', 'r')
    infoList = json.load(out_file)
    indexes = sort_by_hours()
    total = summation()
    for i in indexes:
        print(f"{infoList['NAME'][i]} : {infoList['PLAYTIME'][i]} ({round(round(infoList['PLAYTIME'][i]/total, 3)*100, 2)}%)")
    print(f"Total time : {round(total, 2)}h")
    if(input("\nPress enter to continue...")):
        pass

if __name__ == '__main__':
    main()