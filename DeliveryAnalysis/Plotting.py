import numpy as np
import matplotlib.pyplot as plt

NPT_Text_means, NPR_Text_std = (5409.75,1382.75,873.75 ,174,373.25,373.25), (31.159535726109,113.58807155683,45.879370818121,6.9761498454855,32.49198619147,32.49198619147)
PR_TEXT_means, PT_Text_std = (5409.75,1227,790.75,178.25,305,303.25), (31.159535726109,19.612920911141,12.093386622448,7.2743842809317,14.944341180973,14.198004554631)

ind = np.arange(len(NPT_Text_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, NPT_Text_means, width, yerr=NPR_Text_std,
                color='SkyBlue', label='NON_Priority')
rects2 = ax.bar(ind + width/2, PR_TEXT_means, width, yerr=PT_Text_std,
                color='IndianRed', label='Priority')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of packets')
ax.set_title('Delivery of Image Message by Interface')
ax.set_xticks(ind)
ax.set_xticklabels(('DTN', 'ADB', 'CD', 'GC', 'GC_WIFI','MCS'))
ax.legend()


plt.show()