import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

arg=sys.argv

if len (arg) < 2 : 
    print("Missing arguments : <log_directory> <csv_file_name> <no_of_clustures> <output_file_name>")
    exit()

else :
    csv_file=arg[1]
    log_dir=arg[2]
    log_dir = arg[1]
    csv_file = arg[2]
    nclusters = int(arg[3])
    output_file_name = arg[4]


plt.figure()

df = pd.read_csv(log_dir + '/' + csv_file)
sns.scatterplot(x=df.x, y=df.y, 
                hue=df.cluster_id, 
                palette=sns.color_palette("hls", n_colors=5))
plt.xlabel("Annual income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Clustered: spending (y) vs income (x)")

plt.show()
plt.savefig(log_dir + '/' + output_file_name + '_serial.png')

