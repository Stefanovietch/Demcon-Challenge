shows = []
planning = [["stage_1"]]
planning_time = [0]

with open("shows.txt","r") as f:
    for line in f:
        s = line.rstrip().split(" ")
        shows.append([s[0],int(s[1]),int(s[2])])

for show in sorted(shows,key=lambda x:(x[1], x[2])):
    planned = False
    for i in range(len(planning_time)):
        if show[1] > planning_time[i] and not planned:
            planning[i].append(show)
            planning_time[i] = show[2]
            planned = True
    if not planned:
        planning_time.append(show[2])
        planning.append(["stage_"+str(len(planning_time)),show])

with open("planning.txt","w") as f:
    for stage in planning:
        for line in stage:
            f.write(f"{line} ")
        f.write("\n")
    f.close()

        
