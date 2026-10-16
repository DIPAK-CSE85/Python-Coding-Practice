import statistics
def mean_mode_medium(list):
    mean=statistics.mean(list)
    mode=statistics.mode(list)
    medium=statistics.median(list)
    return[mean,mode,medium]
data=mean_mode_medium([3,4,5,2,7,3,6])
print(data)