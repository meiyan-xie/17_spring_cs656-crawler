# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 51
menMeans = (31475000,75000500,39000000,48900000,59300000,81750000,56500000,25100000,28466666.6666667,28816666.6666667,4500000,28200000,59000000,39500000,44567940,39200000,58500000,15000000,7300000,97000000,45000000,43900000,25075000,104000000,23100000,39000000,12000000,67500000,32162500,47753684.2105263,47400000,10000000,31975000,106000000,11500000,33450000,111500000,8000000,58500000,30000000,70869852.9411765,15000000,7974999.50000000,58850000,65500000,112800000,50000000,40700000,15000000,51500000,44600000)
ind = np.arange(N)    # the x locations for the groups
width = 0.4       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, color='blue')


plt.ylabel('Dollars')
plt.title('Average Total Fund for each location')
plt.xticks(ind, ('Arlington','Atlanta','Austin','Bedford','Billerica','Boston','Brighton','Burlington','Cambridge','Chicago','Columbus','Dedham','Dublin','Earth','Emeryville','Florian?_polis','Ghent','India','Japan','Jerusalem','Krak?_w','Lexington','London','Los Altos','Madrid','Menlo Park','Milan','Montreal','Mountain View','Nashville','New York City','Oakland','Ottawa','Palo Alto','Paris','Plano','Redwood City','Richmond','SaaS','San Carlos','San Diego','San Francisco','San Mateo','Santa Monica','Seattle','Shawnee','Singapore','Sydney','Tokyo','Toronto','Wakefield','Washington'),rotation='vertical')
plt.yticks(np.arange(0, 120000000, 30000000))
plt.margins(0.1)
plt.subplots_adjust(bottom=0.30)

plt.show()
