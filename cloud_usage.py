print('CLOUD RESOURCE USAGE CHECKER'.center(70))
Cpu_limit = 70
Memory_limit = 75
Storage_limit = 80

current_cpu_usage = int(input('Enter current CPU usage (%): '))
current_memory_usage = int(input('Enter current MEMORY usage (%): '))
current_storage_usage = int(input('Enter current STORAGE usage (%): '))

alert_found = False

if current_cpu_usage > Cpu_limit:
    print(f'⚠ WARNING! CPU Limit reached. Current: {current_cpu_usage}% (Limit: {Cpu_limit}%)')
    alert_found = True
    print('Suggested Action: Scale up Computing Resources.')
else:
    print('CPU SYSTEM IS HEALTHY.')
    
if current_memory_usage > Memory_limit:
    print(f'⚠ WARNING! Memory Limit reached. Current: {current_memory_usage}% (Limit: {Memory_limit}%)')
    alert_found = True
    print('Suggested Action: Optimize or restart Services ')
else:
    print('MEMORY SYSTEM IS HEALTHY.') 
    
if current_storage_usage > Storage_limit:
    print(f'⚠ WARNING! Storage Limit reached. Current: {current_storage_usage}% (Limit: {Storage_limit}%)')
    alert_found = True
    print('Suggested Action: Clean or expand storage ')
else:
    print('STORAGE SYSTEM IS HEALTHY.')
    
if alert_found:
    print('SYSTEM STATUS: UNHEALTHY')
else:
    print('SYSTEM STATUS: HEALTHY')
 
print() 
print('Cloud resource evaluation completed successfully.')