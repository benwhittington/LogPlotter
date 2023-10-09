import re
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as dates

_timePattern = "\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d\.\d\d\d"

_typeToTypeMapper = {
    float: lambda x: float(x),
    int: lambda x: int(x),
    bool: lambda x: True if x == 'true' else False
}

def readPatternAndTime(file: [str], pattern: str, dataType: type):
    t = []
    ft = []
    dataTypeMapper = _typeToTypeMapper[dataType]

    with open(file) as f:
        for i, ln in enumerate(f):

            timeRaw = re.findall(_timePattern, ln)
            try:
                timeParsed = datetime.strptime(timeRaw[0], '%Y-%m-%d %H:%M:%S.%f')
                e = re.findall(pattern, ln)[0]
                fAtX = dataTypeMapper(e)
            except IndexError:
                continue

            if (fAtX is not None and timeParsed is not None):
                ft.append(fAtX)
                t.append(timeParsed)
    
    return t, ft

def plotForPattern(file: str, pattern: str, ax: plt.Axes, dataType: type):
    t, fx = readPatternAndTime(file, pattern, dataType)
    

    ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d\n%H:%M:%S'))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d\n%H:%M:%S'))
    ax.plot(t, fx)
