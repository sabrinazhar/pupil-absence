import matplotlib.pyplot as plt
import numpy as np

schools = [
    'Allerton Grange School', 'Allerton High School', 'Benton Park School', 
    'Boston Spa Academy', 'Brigshaw High School and Language College', 'Bruntcliffe School', 
    'Cardinal Heenan Catholic High School', 'Carr Manor Community School', 'Cockburn School', 
    'Corpus Christi Catholic College', 'Guiseley School', 'Lawnswood School', 
    'Mount St Mary\'s Catholic High School', 'Priesthorpe School', 'Pudsey Grammar School', 
    'Ralph Thoresby School', 'Roundhay School', 'Royds School', 
    'Temple Moor High School Science College', 'Wetherby High School'
]

overall_rates = [
    6.08882, 4.22912, 5.0686, 6.56535, 5.90992, 5.93216, 4.84961, 
    5.87203, 5.10675, 6.118, 4.58463, 5.89547, 5.70228, 6.98135, 
    5.51248, 5.78481, 4.16003, 7.18036, 5.9764, 5.18995
]

authorised_rates = [
    3.38575, 3.43258, 3.63301, 3.81459, 3.38057, 2.98299, 3.46605, 
    3.26454, 2.76398, 4.25273, 3.64723, 3.09041, 3.46583, 4.976, 
    4.43529, 4.07273, 3.21833, 4.38478, 3.73754, 3.80314
]

unauthorised_rates = [
    2.70308, 0.79654, 1.43558, 2.75076, 2.52936, 2.94917, 1.38355, 
    2.60748, 2.34277, 1.86527, 0.9374, 2.80506, 2.23645, 2.00536, 
    1.07719, 1.71208, 0.9417, 2.79558, 2.23886, 1.38681
]

# Create positions for bars
indices = np.arange(len(schools)) * 1.5 # Number of schools
bar_width = 0.5 # Width of each bar

# Create the figure and axis
plt.figure(figsize=(18, 12))

# Plot bars for each rate type
plt.barh(indices, authorised_rates, bar_width, label='Authorised', color='#C78800')
plt.barh(indices - bar_width, unauthorised_rates, bar_width, label='Unauthorised', color='#004875')

# Add school names on the y-axis
plt.xticks(fontsize=15, fontweight='bold')
plt.yticks(indices - bar_width / 2, schools, fontsize=15, fontweight='bold')
plt.xlabel('Absence Rate (%)', fontsize=25, fontweight='bold')
plt.ylabel('School', fontsize=25, fontweight='bold')
plt.title('Absence Rates in 20 Leeds City Council-Funded Secondary Schools (2014/2015)', fontsize=19, fontweight='bold')

# Adjust x-axis ticks to increments of 0.5
plt.xticks(np.arange(0, 5.5, 0.5))

# Add a legend
plt.legend(fontsize=15)

# Add a grid for better readability
plt.grid(axis='x', linestyle='--', alpha=1, color='#575757')
plt.grid(axis='y', linestyle='--', alpha=1, color='#575757')

# Adjust layout to fit everything
plt.tight_layout()

# Show the plot
plt.show()
