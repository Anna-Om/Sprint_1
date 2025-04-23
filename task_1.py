time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_value in time_values.split(','):

    time_value = time_value.replace(' ', '') 
    
    if 'h' in time_value:
        hours = time_value[0:time_value.index('h')]
        total_minutes += int(hours) * 60
        time_value = time_value[time_value.index('h')+1: len(time_value)]
        
        
    if 'm' in time_value:
        minutes = time_value[0:time_value.index('m')]
        total_minutes += int(minutes)
        time_value = time_value[time_value.index('m')+1: len(time_value)]
            
        
    if 's' in time_value:
        seconds = time_value[0:time_value.index('s')]
        total_minutes += int(seconds) // 60
        time_value = time_value[time_value.index('s')+1: len(time_value)]
            
        
print(total_minutes)
