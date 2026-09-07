iep_list=[]
with open('/home/mad149/Metagenome_grassmere/Halicovarius_salinus_genome/genome/EMBOSS_iep_Sept8.txt', 'r') as iep:
    for line in iep:
        if 'Isoelectric Point' in line:
            iep_list.append(float(line.split('= ')[-1].split('\n')[0]))
import statistics
average = statistics.mean(iep_list)
print(average)
