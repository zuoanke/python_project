import copy
import os
mem = []

class PCB(object):
    def __init__(self):
        pass

class queue(object):
    def __init__(self):
        self.qlist = []

    def push(self, item):
        self.qlist.append(item)

    def pop(self):
        self.qlist.pop()

    def bpop(self):
        del self.qlist[0]

    def dele(self, value):
        del self.qlist[self.qlist.index(value)]

    def dele_by_pid(self, pid):
        for i in self.qlist:
            for j in i[0:1]:
                if j == pid:
                    self.dele(i)
                else:
                    pass

    def gettail(self):
        return self.qlist[len(self.qlist) - 1]

    def gethead(self):
        return self.qlist[0]

    def getitems(self):
        output = list(reversed(self.qlist))
        return output

    def getitems_int(self):
        temp1 = list(reversed(self.qlist))
        temp2 = []
        output = []
        for i in temp1:
            for j in i:
                temp2.append(int(j))
            output.append(list(temp2))
            del temp2[:]
        return output

    def getpid(self):
        temp = list(reversed(self.qlist))
        pid = []
        for i in temp:
            for j in i[0:1]:
                pid.append(int(j))
        return pid

    def sort_by_time(self):
        temp = []
        temp2 = []
        output = []
        for i in self.qlist:
            for j in i[1:2]:
                if j not in temp:
                    temp.append(j)
                else:
                    i[1] += 0.1
                    temp.append(j + 0.1)
        while temp:
            for i in self.qlist:
                for j in i[1:2]:
                    if j == min_num(temp):
                        temp2.append(i)
                    else:
                        pass
            del temp[temp.index(min_num(temp))]
            output = list(reversed(temp2))
        self.qlist = temp2
        pid = []
        for i in output:
            for j in i[0:1]:
                pid.append(int(j))
        return pid

    def sort_by_pror(self):
        temp = []
        temp2 = []
        output = []
        for i in self.qlist:
            for j in i[3:4]:
                if j not in temp:
                    temp.append(j)
                else:
                    i[3] += 0.1
                    temp.append(j + 0.1)
        while temp:
            for i in self.qlist:
                for j in i[3:4]:
                    if j == min_num(temp):
                        temp2.append(i)
                    else:
                        pass
            del temp[temp.index(min_num(temp))]
            output = list(reversed(temp2))
        self.qlist = temp2
        pid = []
        for i in output:
            for j in i[0:1]:
                pid.append(int(j))
        return pid

    def sort_by_burst(self):
        temp1 = []
        temp2 = []
        output = []
        pid = []
        for i in self.qlist:
            for j in i[2:3]:
                if j not in temp1:
                    temp1.append(j)
                else:
                    pass
        while temp1:
            for i in self.qlist:
                for j in i[2:3]:
                    if j == min_num(temp1):
                        temp2.append(i)
                    else:
                        pass
            del temp1[temp1.index(min_num(temp1))]
            output = list(reversed(temp2))
        self.qlist = temp2
        for i in output:
            for j in i[0:1]:
                pid.append(int(j))
        return pid

    def get_certain_item(self,pid):
        for i in self.qlist:
            if i[0] == pid:
                return i

    def insert(self, position_in, PCB):
        position_out = len(self.qlist) - position_in
        pcb = []
        pcb.append(PCB.pid)
        pcb.append(PCB.atime)
        pcb.append(PCB.rtime)
        pcb.append(PCB.pror)
        self.qlist.insert(position_out, pcb)

waiting_queue = queue()

def register(list):
    pcb = PCB()
    pcb.pid = list[0]
    pcb.atime = list[1]
    pcb.rtime = list[2]
    pcb.pror = list[3]
    return pcb

def memory(PCB):
    cache = []
    cache.append(PCB.pid)
    cache.append(PCB.atime)
    cache.append(PCB.rtime)
    cache.append(PCB.pror)
    output = list(cache)
    mem.append(output)

def inputer(PCB):
    PCB.pid = input('please input a pid:\n')
    PCB.atime = input('please input a arrive time:\n')
    PCB.rtime = input('please input a burst time:\n')
    PCB.pror = input('please input a priority:\n')

def inputer_f(PCB):
    PCB.pid = float(input('please input a pid:\n'))
    PCB.atime = float(input('please input a arrive time:\n'))
    PCB.rtime = float(input('please input a burst time:\n'))
    PCB.pror = float(input('please input a priority:\n'))

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

def loader(filename):
    temp1 = open(filename)
    for line in temp1:
        mem.append(list(map(int,line.split(','))))


def loader_f(filename):
    temp1 = open(filename)
    for line in temp1:
        mem.append(list(map(float,line.split(','))))



def SJF(mem):
    time_list = []
    ready_queue = queue()
    core_queue = queue()
    result = []
    timer = 0
    counter = []
    time = copy.deepcopy(mem)
    for i in mem:
        ready_queue.push(i)
    cache = copy.deepcopy(ready_queue.getitems())
    while ready_queue.getitems():
        for i in cache:
            if int(i[1]) <= timer and i not in core_queue.getitems():
                pcb = register(i)
                ready_queue.dele_by_pid(i[0])
                core_queue.insert(0, pcb)
                cache = filter(lambda x: x != i, cache)
                core_queue.sort_by_burst()
                print 'ready queue:', core_queue.getitems_int()
            else:
                pass
        while core_queue.getitems():
            run = core_queue.gethead()
            print 'RUN', map(int, run)
            time_list.append(run[0])
            time_list.append(timer)
            while run[2] != 0:
                print 'now is processing pid:', int(run[0])
                run[2] -= 1
                timer += 1
            result.append(run)
            core_queue.bpop()
            for i in time:
                if i[0] == run[0]:
                    counter.append(timer - run[1] - i[2])
                    time_list.append(timer - run[1] - i[2])
            time_list.append(timer)
    del mem[:]
    mem = result
    tot_time = 0
    for i in counter:
        tot_time += i
    print 'SJF finish!'
    for i in mem:
        t = -1
        for j in time_list:
            t += 1
            if j == i[0]:
                print 'pid:', int(j), 'start time:', time_list[t + 1], 'finish time:', time_list[t + 3], 'waiting time:', int(round(time_list[t + 2]))
                break
    print 'average waiting time:', tot_time / 5


def FCFS(mem):
    cache = []
    timer_list = []
    timer = 0
    ready_queue = queue()
    waiting_queue = queue()
    count1 = []
    count2 = 0
    print 'system memory status:'
    time = copy.deepcopy(mem)
    for i in mem:
        print map(int, i)
        for j in i[1:2]:
            if j not in cache:
                cache.append(j)
            else:
                i[1] += 0.1
                cache.append(j + 0.1)
            ready_queue.push(i)
    print 'waiting  queue:',waiting_queue.getitems()
    print 'initialize ready queue:',ready_queue.sort_by_time()
    print '*'*100
    while cache:
        for k in mem:
            for m in k[1:2]:
                if m == min_num(cache):
                    print 'now processing process: PID', int(k[0])
                    timer_list.append(int(round(k[0])))
                    timer_list.append(timer)
                    while k[2] != 0:
                        k[2] -= 1
                        timer += 1
                        print 'processing status:', map(int, k)
                    print timer
                    for i in time:
                        if i[0] == k[0]:
                            count1.append(timer - int(round(k[1])) - i[2])
                            timer_list.append(timer - int(round(k[1])) - i[2])
                    timer_list.append(timer)
                else:
                    pass
        for i in cache:
            if i == min_num(cache):
                for j in ready_queue.getitems():
                    for k in j[1:2]:
                        if k == i:
                            ready_queue.dele(j)
        del cache[cache.index(min_num(cache))]
        print 'waiting  queue:', map(int, waiting_queue.getitems())
        print 'currently ready queue:',map(int, ready_queue.sort_by_time())
        print '*' * 50

    for i in count1:
        count2 += i

    print 'system memory status:'
    for k in mem:
        print map(int, k)
    print 'FCFS finish!'
    for i in mem:
        t = -1
        for j in timer_list:
            t += 1
            if j == i[0]:
                print 'pid:', int(j), 'start time:', timer_list[t + 1], 'finish time:', timer_list[t + 3], 'waiting time:', int(round(timer_list[t + 2]))
                break
    print 'Average waiting time:', float(count2)/5


def NPP(mem):
    cache = []
    timer_list = []
    timer = 0
    time = copy.deepcopy(mem)
    waiting_queue = queue()
    ready_queue = queue()
    time_count = []
    print 'system memory status:'
    for i in mem:
        print map(int, i)
    for i in mem:
        for j in i[3:4]:
            if j not in cache:
                cache.append(j)
            else:
                if i[1] >= mem[cache.index(j)][1]:
                    i[3] += 0.1
                    cache.append(j + 0.1)
                else:
                    i[3] -= 0.1
                    cache.append(j - 0.1)
            waiting_queue.push(i)
    print 'initial waiting queue:', map(int, waiting_queue.sort_by_pror())
    print 'initial ready queue:', map(int, ready_queue.getitems())
    print '*' * 50
    ready_queue.push(waiting_queue.sort_by_pror()[-1])
    while cache:
        for k in mem:
            for m in k[3:4]:
                if m == min_num(cache):
                    waiting_queue.dele(k)
                    print 'currently waiting queue:', waiting_queue.sort_by_pror()
                    print 'currently ready queue:', ready_queue.getitems()
                    ready_queue.pop()
                    timer_list.append(int(round(k[0])))
                    timer_list.append(timer)
                    while k[2] != 0:
                        print 'now processing PID:', int(k[0])
                        k[2] -= 1
                        timer += 1
                    timer_list.append(timer)
                    for i in time:
                        if i[0] == k[0]:
                            time_count.append(timer - k[1] - i[2])
                            timer_list.append(timer - k[1] - i[2])
                    print 'PID:', int(k[0]),'finish!'
                    print '*' * 50
                else:
                    pass
        if waiting_queue.getitems():
            ready_queue.push(waiting_queue.sort_by_pror()[-1])
        del cache[cache.index(min_num(cache))]
    print 'currently waiting queue:', waiting_queue.sort_by_pror()
    print 'currently ready queue:', ready_queue.getitems()
    print 'system memory status:'
    for i in mem:
        print map(int, i)
    print 'NPP finish!'
    print timer_list
    for i in mem:
        t = -1
        for j in timer_list:
            t += 1
            if j == i[0]:
                print 'pid:', int(j), 'start time:', timer_list[t + 1], 'finish time:', timer_list[t + 2], 'waiting time:', int(round(timer_list[t + 3]))
                break
    k = 0
    for i in time_count:
        k += i
    print 'Average waiting time:', float(k)/5


def RR(mem):
    time = copy.deepcopy(mem)
    time_count = []
    cache = []
    system_memory = []
    ready_queue = []
    timer_list = []
    timer = 0
    q = input('input the length of window:\n')
    timer_list_f = []
    print 'system memory status:'
    for i in mem:
        print map(int, i)
    for i in mem:
        for j in i[1:2]:
            if j not in cache:
                cache.append(j)
            else:
                i[1] -= 0.1
                cache.append(j - 0.1)
    while cache:
        for k in mem:
            for m in k[1:2]:
                if m == min_num(cache):
                    system_memory.append(k[0])
                else:
                    pass
        del cache[cache.index(min_num(cache))]
    system_memory = list(reversed(system_memory))
    print 'initialize system memory:', map(int, system_memory)
    print '*' * 50
    while system_memory:
        for n in mem:
            for o in n[0:1]:
                if o in system_memory and n[1] <= timer and o not in ready_queue:
                    ready_queue.insert(len(ready_queue), o)
        for i in mem:
            for j in i[0:1]:
                if j == ready_queue[len(ready_queue) - 1]:
                    timer_list.append(j)
                    timer_list.append(timer)
                    print 'system time:', timer
                    print 'ready queue:', map(int, ready_queue)
                    print 'system memory', map(int, system_memory)
                    print 'pid', int(j), 'is now in processing!'
                    for p in range(q):
                        if i[2] != 0:
                            print 'processing PID:', int(j)
                            i[2] -= 1
                            timer += 1
                        else:
                            break
                    ready_queue.pop()
                    del system_memory[system_memory.index(j)]
                    if i[2] != 0:
                        ready_queue.insert(0, j)
                        system_memory.insert(0, j)
                    else:
                        print 'PID', int(j), 'is finish!'
                        timer_list_f.append(int(j))
                        timer_list_f.append(timer)
                        for k in time:
                            if k[0] == i[0]:
                                time_count.append(timer - int(round(i[1])) - k[2])
                                timer_list_f.append(timer - int(round(i[1])) - k[2])
                        pass
                    print '*' * 100
                else:
                    pass
    print 'RR finish!'
    print '*' * 100
    for i in mem:
        t = -1
        for j in timer_list:
            t += 1
            if j == i[0]:
                c = -1
                for k in timer_list_f:
                    c += 1
                    if k == j:
                        print 'pid:', int(j), 'start time:', timer_list[t + 1], 'finish time:', timer_list_f[c + 1], 'waiting time:', int(round(timer_list_f[c + 2]))
                        break
                break

    atime = 0
    for i in time_count:
        atime += i
    print 'Average waiting time:', float(atime/5)


def main():
    while 1:
        print 'main menu:'
        print 'please input a number to make a selection:'
        print '1 for System memory manager.'
        print '2 for Scheduler.'
        print '3 for Process manager.'
        print '4 for Exit.'
        switch_main = input('>')
        if switch_main == 1:
            while 1:
                print '*' * 50
                print 'System memory manager\n'
                print 'Please input a number to make a selection:\n'
                print '1: Manually loading processes into system memory.\n'
                print '2: Loading processes from a file.\n'
                print '3: Show system memory status.\n'
                print '4: Initializing system memory.\n'
                print '5: Back.\n'
                print '*' * 50
                switch_main_input = input('>')
                if switch_main_input == 1:
                    for i in range(5):
                        pcb_rr = PCB()
                        inputer_f(pcb_rr)
                        memory(pcb_rr)
                    print 'Input finish!'
                    print '*' * 50
                    print 'system memory status:'
                    print '*' * 50
                    print 'pid arrival burst priority'
                    for i in mem:
                        print map(int, i)
                    print '*' * 50
                if switch_main_input == 2:
                    while 1:
                        file_name = raw_input('input a file name(input "exit" for exit):')
                        if file_name == 'exit':
                            break
                        else:
                            if os.path.exists(file_name):
                                loader_f(file_name)
                                print '*' * 50
                                print 'Loading finish!'
                                print '*' * 50
                                print 'system memory status:'
                                print '*' * 50
                                print 'pid arrival burst priority'
                                for i in mem:
                                    print map(int, i)
                                print '*' * 50
                                break
                            else:
                                print "Can't find the file!"
                if switch_main_input == 3:
                    print '*' * 50
                    print 'system memory status:'
                    print '*' * 50
                    print 'pid arrival burst priority'
                    for i in mem:
                        print map(int, i)

                if switch_main_input == 4:
                    print '*' * 50
                    print 'Initializing memory.'
                    del mem[:]
                    print 'Finish!'
                    print '*' * 50

                if switch_main_input == 5:
                    print '*' * 50
                    print 'Back'
                    print '*' * 50
                    break

        elif switch_main == 2:
            while 1:
                print 'Please input a number to select an algorithm:'
                print '1: SJF.'
                print '2: FCFS.'
                print '3: NPP.'
                print '4: RR.'
                print '5: Show system memory status.'
                print '6: Initializing memory.'
                print '7: Back'
                switch_alg = input('>')
                if switch_alg == 1:
                    if mem:
                        print '*' * 50
                        print 'processes are already in the system.'
                        print '*' * 50
                        SJF(mem)
                        print '*' * 50
                    else:
                        print 'no process in system.'
                        print 'Please input a number to select a processes loading method:\n'
                        print '1 for manual input.\n'
                        print '2 for load from a file.\n'
                        switch_input = input('>')
                        if switch_input == 1:
                            for i in range(5):
                                pcb_sjf = PCB()
                                inputer(pcb_sjf)
                                memory(pcb_sjf)
                            print '*' * 50
                            SJF(mem)
                            print '*' * 50
                        elif switch_input == 2:
                            while 1:
                                file_name = raw_input('input a file name (input "exit" for exit):\n')
                                if file_name == 'exit':
                                    break
                                else:
                                    if os.path.exists(file_name):
                                        loader(file_name)
                                        print '*' * 50
                                        SJF(mem)
                                        print '*' * 50
                                        break
                                    else:
                                        print "Can't find the file!"
                        else:
                            print '*' * 50
                            print 'Wrong input!'
                            print '*' * 50


                elif switch_alg == 2:
                    if mem:
                        print '*' * 50
                        print 'processes are already in the system.'
                        print '*' * 50
                        FCFS(mem)
                        print '*' * 50
                    else:
                        print '*' * 50
                        print 'no process in system.'
                        print 'Please input a number to select a processes loading method:\n'
                        print '1 for manual input.\n'
                        print '2 for load from a file.\n'
                        switch_input = input('>')
                        if switch_input == 1:
                            for i in range(5):
                                pcb_fcfs = PCB()
                                inputer(pcb_fcfs)
                                memory(pcb_fcfs)
                            print '*' * 50
                            FCFS(mem)
                            print '*' * 50
                        elif switch_input == 2:
                            while 1:
                                file_name = raw_input('input a file name (input "exit" for exit):\n')
                                if file_name == 'exit':
                                    break
                                else:
                                    if os.path.exists(file_name):
                                        loader_f(file_name)
                                        print '*' * 50
                                        FCFS(mem)
                                        print '*' * 50
                                        break
                                    else:
                                        print "Can't find the file!"
                        else:
                            print '*' * 50
                            print 'Wrong input!'
                            print '*' * 50


                elif switch_alg == 3:
                    if mem:
                        print '*' * 50
                        print 'processes are already in the system.'
                        print '*' * 50
                        NPP(mem)
                        print '*' * 50
                    else:
                        print 'no process in system.'
                        print 'Please input a number to select a processes loading method:\n'
                        print '1 for manual input.\n'
                        print '2 for load from a file.\n'
                        switch_input = input('>')
                        if switch_input == 1:
                            for i in range(5):
                                pcb_npp = PCB()
                                inputer_f(pcb_npp)
                                memory(pcb_npp)
                            print '*' * 50
                            NPP(mem)
                            print '*' * 50
                        elif switch_input == 2:
                            while 1:
                                file_name = raw_input('input a file name (input "exit" for exit):\n')
                                if file_name == 'exit':
                                    break
                                else:
                                    if os.path.exists(file_name):
                                        loader_f(file_name)
                                        print '*' * 50
                                        NPP(mem)
                                        print '*' * 50
                                        break
                                    else:
                                        print "Can't find the file!"

                        else:
                            print '*' * 50
                            print 'Wrong input!'
                            print '*' * 50



                elif switch_alg == 4:
                    if mem:
                        print '*' * 50
                        print 'processes are already in the system.'
                        print '*' * 50
                        RR(mem)
                        print '*' * 50
                    else:
                        print 'no process in system.'
                        print 'Please input a number to select an input method:\n'
                        print '1 for manual input.\n'
                        print '2 for load from a file.\n'
                        switch_input = input('>')
                        if switch_input == 1:
                            for i in range(5):
                                pcb_rr = PCB()
                                inputer_f(pcb_rr)
                                memory(pcb_rr)
                            RR(mem)
                        elif switch_input == 2:
                            while 1:
                                file_name = raw_input('input a file name (input "exit" for exit):\n')
                                if file_name == 'exit':
                                    break
                                else:
                                    if os.path.exists(file_name):
                                        loader_f(file_name)
                                        print '*' * 50
                                        RR(mem)
                                        print '*' * 50
                                        break
                                    else:
                                        print "Can't find the file!"


                        else:
                            print '*' * 50
                            print 'Wrong input!'
                            print '*' * 50

                elif switch_alg == 5:
                    print '*' * 50
                    print 'system memory status:'
                    print '*' * 50
                    print 'pid arrival burst priority'
                    for i in mem:
                        print map(int, i)
                    print '*' * 50

                elif switch_alg == 6:
                    print '*' * 50
                    print 'Initializing memory.'
                    del mem[:]
                    print 'Finish!'
                    print '*' * 50

                elif switch_alg == 7:
                    print 'Back'
                    break
                else:
                    print '*' * 50
                    print 'Wrong input!'
                    print '*' * 50

        elif switch_main == 3:
            while 1:
                print '*' * 50
                print 'welcome to the process manager!'
                print '*' * 50
                print 'please input a number to choose a function:'
                print '1: load processes into system.'
                print '2: show the system memory status.'
                print '3: Initializing memory.'
                print '4: show the PCB status.'
                print '5: queue operations.'
                print '6: back to main menu.'
                switch_pm = input('>')
                if switch_pm == 1:
                    while 1:
                        print 'load processes into system.'
                        print 'please inout a number to choose a method for loading'
                        print '1: loading from a file.'
                        print '2: loading by manually input.'
                        print '3: back to upper menu.'
                        switch_load = input('>')
                        if switch_load == 1:
                            while 1:
                                file_name = raw_input('input a file name(input "exit" for exit):')
                                if file_name == 'exit':
                                    break
                                else:
                                    if os.path.exists(file_name):
                                        loader_f(file_name)
                                        print '*' * 50
                                        print 'Loading finish!'
                                        print '*' * 50
                                        break
                                    else:
                                        print "Can't find the file!"
                        elif switch_load == 2:
                            for i in range(5):
                                pcb = PCB()
                                inputer(pcb)
                                memory(pcb)
                        elif switch_load == 3:
                            break
                        else:
                            print '*' * 50
                            print 'Wrong input!'
                            print '*' * 50
                elif switch_pm == 2:
                    if mem:
                        print '*' * 50
                        print 'system memory status:'
                        print '*' * 50
                        print 'pid arrival burst priority'
                        for i in mem:
                            print i
                        print '*' * 50
                    else:
                        print '*' * 50
                        print 'There is 0 process in the system now! You must load some process into system!'
                        print '*' * 50

                elif switch_pm == 3:
                    print '*' * 50
                    print 'Initializing memory.'
                    del mem[:]
                    print 'Finish!'
                    print '*' * 50

                elif switch_pm == 4:
                    if mem:
                        while 1:
                            pcb_queue = queue()
                            for i in mem:
                                pcb_queue.push(i)
                            pid = input('Please input a pid (input 88 for exit):')
                            print 'pid arrival burst priority'
                            print pcb_queue.get_certain_item(pid)
                            if pid == 88:
                                break
                    else:
                        print '*' * 50
                        print 'There is 0 process in the system now! You must load some process into system!'
                        print '*' * 50
                elif switch_pm == 5:
                    if mem:
                        print 'Automatic loading processes in to waiting queue.'
                        for i in mem:
                            waiting_queue.push(i)
                        print '*' * 50
                        print 'Loading finish!\n'
                        print '*' * 50
                        print 'current queue status:', waiting_queue.getpid()
                        while 1:
                            print 'how do you want to sort the queue?'
                            print '1: By arrive time.'
                            print '2: By priority.'
                            print '3: By CPU burst time.'
                            print '4: Back.'
                            switch_sort = input('>')
                            if switch_sort == 1:
                                print 'current queue status:', waiting_queue.sort_by_time()
                            elif switch_sort == 2:
                                print 'current queue status:', waiting_queue.sort_by_pror()
                            elif switch_sort == 3:
                                print 'current queue status:', waiting_queue.sort_by_burst()
                            elif switch_sort == 4:
                                print 'Back'
                                break
                            else:
                                print '*' * 50
                                print 'Wrong input!'
                                print '*' * 50
                            while 1:
                                print 'Input a number to select a queue operation:'
                                print '1: Add a PCB to the tail (LEFT is the tail!) of the queue:'
                                print '2: Delete a PCB from the head (RIGHT is the head) of the queue:'
                                print '3: Add a PCB to a certain position of the queue:'
                                print '4: Delete a PCB by pid:'
                                print '5: Show the detail queue status'
                                print '6: Back (re-sort the queue)'
                                switch_queue_op = input('>')
                                if switch_queue_op == 1:
                                    pcb = PCB()
                                    temp = []
                                    inputer(pcb)
                                    temp.append(pcb.pid)
                                    temp.append(pcb.atime)
                                    temp.append(pcb.rtime)
                                    temp.append(pcb.pror)
                                    waiting_queue.push(temp)
                                    print 'current queue status:', waiting_queue.getpid()
                                    print '*' * 50
                                elif switch_queue_op == 2:
                                    waiting_queue.bpop()
                                    print 'current queue status:', waiting_queue.getpid()
                                    print '*' * 50
                                elif switch_queue_op == 3:
                                    pcb = PCB()
                                    temp = []
                                    inputer(pcb)
                                    temp.append(pcb.pid)
                                    temp.append(pcb.atime)
                                    temp.append(pcb.rtime)
                                    temp.append(pcb.pror)
                                    waiting_queue.insert(input('Please input the insert position (a number):'), pcb)
                                    print 'current queue status:', waiting_queue.getpid()
                                    print '*' * 50
                                elif switch_queue_op == 4:
                                    waiting_queue.dele_by_pid(input('Input a pid: '))
                                    print 'current queue status:', waiting_queue.getpid()
                                    print '*' * 50
                                elif switch_queue_op == 5:
                                    print waiting_queue.getitems_int()
                                    print '*' * 50
                                elif switch_queue_op == 6:
                                    break
                                else:
                                    print '*' * 50
                                    print 'Wrong input!'
                                    print '*' * 50
                    else:
                        print '*' * 50
                        print 'There is 0 process in the system now! You must load some process into system!'
                        print '*' * 50

                elif switch_pm == 6:
                    print 'Back'
                    break

                else:
                    print '*' * 50
                    print 'Wrong input!'
                    print '*' * 50

        elif switch_main == 4:
            print 'Bye!'
            exit()
        else:
            print '*' * 50
            print 'Wrong input!'
            print '*' * 50


if __name__ == '__main__':
    main()
