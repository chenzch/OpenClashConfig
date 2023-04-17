#!/usr/bin/python3
import json
import re
import subprocess

def get_ping_time(ip_address):
    try:
        result = subprocess.run(['ping', '-c', '1', '-w', '5', ip_address], capture_output=True)
        output = result.stdout.decode('utf-8')
        time_str = output.split('time=')[1].split('ms')[0]
        time = float(time_str)
        return time
    except:
        return -1

history = {}

def count_history(s) -> str:
    if s in history:
        count = history[s]
        history[s] += 1
    else:
        count = 1
        history[s] = 2
    return str(count)

def getName(inName) -> str:
    Index = inName.find('->')
    if (Index != -1) :
        inName = inName[Index + 2:]
    inName = re.sub(r"_\d+$", "", inName)
    if (inName.count("_") > 1) :
        Index = inName.find("_")
        if (Index != -1) :
            inName = inName[Index + 1:]
    return inName

def rename(inputfilename, outputfilename) -> None:
    with open(outputfilename, 'w') as o:
        with open(inputfilename, 'r') as f:
            for line in f:
                if len(line) <= 3:
                    break
                data = json.loads(line[3:])
                time = get_ping_time(data['server'])
                print(data['name'] + " " + data['server'] + " : " + str(time))
                if (time > 0) :
                    name = getName(data['name'])
                    if (not name == "CN_中国") :
                        data['name'] = name + "_" + count_history(name)
                        o.write("  - " + json.dumps(data, ensure_ascii=False).replace(": ", ":").replace(", ", ",") + "\n")

if __name__ == '__main__':
    rename('input.list', 'output.list')
