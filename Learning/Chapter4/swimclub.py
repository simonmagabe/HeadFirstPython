import statistics

FOLDER = "..\swimdata/"

def read_swim_data(filename):
    '''Return swim data from a file
    
    Given the name of a swimmer's file (in filename), extract all the required
    data, then return it into the caller as a tuple.
    '''
    swimmer, age, distance, stroke = getFileNameData(filename)
    times = getDataFromFile(FOLDER, filename)
    converted_time_ms = convertTimesToMilliseconds(times)
    average = getAverageTimeString(converted_time_ms)
    return swimmer, age, distance, stroke, times, average # Returned as a tuple.

def getFileNameData(FileName):
    return FileName.removesuffix(".txt").split("-")

def getDataFromFile(FOLDER_PATH, FILE_NAME):
    with open(FOLDER_PATH + FILE_NAME) as file:
        return file.readlines()[0].strip().split(",")

def convertTimesToMilliseconds(times):
    converted_times = []
    for time in times:
        minutes = 0
        # The minutes value might be missing, so guard against this causing a crash
        if ":" in time:
            minutes, seconds, hundreths = time.replace(":", ".").split(".")
        else:
            seconds, hundreths = time.split(".")
        converted_times.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundreths))
    return converted_times

def getAverageTimeString(conveted_time_ms):
    average = statistics.mean(conveted_time_ms)
    min_secs, hundreths = str(round(average/100, 2)).split(".")
    min_secs = int(min_secs)
    minutes = min_secs // 60
    seconds = min_secs - minutes*60
    return f"{minutes}:{seconds}.{hundreths}"
