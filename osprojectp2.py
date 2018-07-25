space = []
cache = []
mem = []
blocked = []
log = []

counter_mem_use = 0
counter_mem_total = 0
counter_total = 0
counter_blocked = 0
counter_space_number = 0
counter_fragmentation = 0

def loader_f(filename):
    global counter_mem_total
    global counter_space_number
    global counter_total
    line_num = 0
    temp1 = open(filename)
    for line in temp1:
        line_num += 1
        if line_num == 1:
            counter_mem_total = line
        elif line_num == 2:
            counter_space_number = line
        elif line_num > 2 and line_num < 3 + int(counter_space_number):
            space.append(list(map(float, line.split(','))))
        elif line_num == 3 + int(counter_space_number):
            counter_total = line
        elif line_num > 3 + int(counter_space_number):
            cache.append(list(map(float, line.split(','))))



def min_num(input_list):
    if input_list:
        num = input_list[0]
        for i in input_list:
            if i < num:
                num = i
            else:
                pass
        return num
    else:
        pass


def max_num(input_list):
    if input_list:
        num = input_list[0]
        for i in input_list:
            if i > num:
                num = i
            else:
                pass
        return num
    else:
        pass


def allocater_ff(cache, space):
    global counter_mem_total
    global counter_mem_use
    global counter_blocked
    global counter_fragmentation
    print '*' * 60
    print 'First fit:'
    print '*' * 60
    print 'original available memory space:'
    for i in space:
        print 'base address: ', int(i[0]), 'available space: ', int(i[1])
    print '*' * 60
    print 'processes for assignment:'
    for i in cache:
        print ' pid:', int(i[0]), ' arrive time:', int(i[1]), ' duration:', int(i[2]), ' size of memory:', int(i[3])
    print '*' * 60
    print 'assigning:'
    for i in cache:
        for j in space:
            if i[3] <= j[1]:
                temp = []
                j[1] -= i[3]
                temp.append(j[0])
                j[0] += i[3]
                mem.append(i)
                temp.append(i[0])
                temp.append(i[3])
                log.append(temp)
                print '*' * 60
                print 'assigning pid', int(i[0]), 'at address', int(j[0] - i[3])
                print 'possible fragmentation:', int(j[1]), 'units'
                break
            else:
                pass
    for i in cache:
        if i not in mem:
            blocked.append(i)
    for i in blocked:
        counter_blocked += 1
    for i in mem:
        counter_mem_use += i[3]
    print '*' * 60
    print 'assigned:'
    for i in log:
        print 'pid', int(i[1]), 'base address', int(i[0]), 'allocated length', int(i[2])
    print '*' * 60
    print 'blocked:'
    for i in blocked:
        print 'pid', int(i[0])
    print '*' * 60
    print 'fragmentation:'
    for i in space:
        if i[1] !=0:
            print 'starting address:', int(i[0]), 'fragmentation length:', int(i[1]), 'units'
            counter_fragmentation += int(i[1])
    print '*' * 60
    print 'memory utilization:', round(((int(counter_mem_total) - counter_fragmentation) / float(counter_mem_total)) * 100, 2), '%'
    print 'blocking probability:', round((float(counter_blocked) / int(counter_total)) * 100, 2), '%'
    print '*' * 60


def allocater_bf(cache, space):
    global counter_mem_total
    global counter_mem_use
    global counter_total
    global counter_blocked
    global counter_fragmentation
    print '*' * 60
    print 'Best fit:'
    print '*' * 60
    print 'original available memory space:'
    for i in space:
        print 'base address: ', int(i[0]), 'available space: ', int(i[1])
    print '*' * 60
    print 'processes for assignment:'
    for i in cache:
        print ' pid:', int(i[0]), ' arrive time:', int(i[1]), ' duration:', int(i[2]), ' size of memory:', int(i[3])
    print '*' * 60
    print 'assigning:'
    dynamic_space = []
    for i in space:
        dynamic_space.append(i[1])
    for i in cache:
        temp = []
        for j in space:
            if i[3] <= j[1]:
                temp.append(j[1])
        for k in space:
            if k[1] == min_num(temp):
                temp2 = []
                k[1] -= i[3]
                temp2.append(k[0])
                k[0] += i[3]
                mem.append(i)
                temp2.append(i[0])
                temp2.append(i[3])
                log.append(temp2)
                print '*' * 60
                print 'assigning pid', int(i[0]), 'at address', int(k[0] - i[3])
                print 'possible fragmentation:', int(k[1]), 'units'
                break
            else:
                pass
    for i in cache:
        if i not in mem:
            blocked.append(i)
    for i in blocked:
        counter_blocked += 1
    for i in mem:
        counter_mem_use += i[3]
    print '*' * 60
    print 'assigned:'
    for i in log:
        print 'pid', int(i[1]), 'base address', int(i[0]), 'allocated length', int(i[2])
    print '*' * 60
    print 'blocked:'
    for i in blocked:
        print 'pid', int(i[0])
    print '*' * 60
    print 'fragmentation:'
    for i in space:
        if i[1] != 0:
            print 'starting address:', int(i[0]), 'fragmentation length:', int(i[1]), 'units'
            counter_fragmentation += int(i[1])
    print '*' * 60
    print 'memory utilization:', round(((int(counter_mem_total) - counter_fragmentation) / float(counter_mem_total)) * 100, 2), '%'
    print 'blocking probability:', round((float(counter_blocked) / float(counter_total)) * 100, 2), '%'
    print '*' * 60


def allocater_wf(cache, space):
    global counter_mem_total
    global counter_mem_use
    global counter_total
    global counter_blocked
    global counter_fragmentation
    print '*' * 60
    print 'Worst fit:'
    print '*' * 60
    print 'original available memory space:'
    for i in space:
        print 'base address: ', int(i[0]), 'available space: ', int(i[1])
    print '*' * 60
    print 'processes for assignment:'
    for i in cache:
        print ' pid:', int(i[0]), ' arrive time:', int(i[1]), ' duration:', int(i[2]), ' size of memory:', int(i[3])
    print '*' * 60
    print 'assigning:'
    dynamic_space = []
    for i in space:
        dynamic_space.append(i[1])
    for i in cache:
        temp = []
        for j in space:
            if i[3] <= j[1]:
                temp.append(j[1])
        for k in space:
            if k[1] == max_num(temp):
                temp2 = []
                k[1] -= i[3]
                temp2.append(k[0])
                k[0] += i[3]
                mem.append(i)
                temp2.append(i[0])
                temp2.append(i[3])
                log.append(temp2)
                print '*' * 60
                print 'assigning pid', int(i[0]), 'at address', int(k[0] - i[3])
                print 'possible fragmentation:', int(k[1]), 'units'
                break
            else:
                pass
    for i in cache:
        if i not in mem:
            blocked.append(i)
    for i in blocked:
        counter_blocked += 1
    for i in mem:
        counter_mem_use += i[3]
    print '*' * 60
    print 'assigned:'
    for i in log:
        print 'pid', int(i[1]), 'base address', int(i[0]), 'allocated length', int(i[2])
    print '*' * 60
    print 'blocked:'
    for i in blocked:
        print 'pid', int(i[0])
    print '*' * 60
    print 'fragmentation:'
    for i in space:
        if i[1] != 0:
            print 'starting address:', int(i[0]), 'fragmentation length:', int(i[1]), 'units'
            counter_fragmentation += int(i[1])
    print '*' * 60
    print 'memory utilization:', round(((int(counter_mem_total) - counter_fragmentation) / float(counter_mem_total)) * 100, 2), '%'
    print 'blocking probability:', round((float(counter_blocked) / float(counter_total)) * 100, 2), '%'
    print '*' * 60


def main():
    while 1:
        del space[:]
        del cache[:]
        del blocked[:]
        del mem[:]
        del log[:]

        global counter_mem_use
        global counter_mem_total
        global counter_total
        global counter_blocked
        global counter_space_number
        global counter_fragmentation

        counter_mem_use = 0
        counter_mem_total = 0
        counter_total = 0
        counter_blocked = 0
        counter_space_number = 0
        counter_fragmentation = 0

        print 'select an algorithm:'
        print '1: first fit'
        print '2: best fit'
        print '3: worst fit'
        print '4: exit'
        switcher = input('>')
        if switcher == 1:
            loader_f('anke_testcase')
            allocater_ff(cache, space)

        elif switcher == 2:
            loader_f('anke_testcase')
            allocater_bf(cache, space)

        elif switcher == 3:
            loader_f('anke_testcase')
            allocater_wf(cache, space)

        elif switcher == 4:
            exit()
        else:
            print 'wrong input'


if __name__ == '__main__':
    main()