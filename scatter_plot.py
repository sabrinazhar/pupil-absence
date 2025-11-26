import matplotlib.pyplot as plt
import numpy as np

# Data
schools = [
    'Allerton\nGrange\nSchool', 'Allerton High\nSchool', 'Benton Park\nSchool', 
    'Boston Spa\nAcademy', 'Brigshaw High School\nand Language College', 'Bruntcliffe\nSchool', 
    'Cardinal Heenan Catholic\nHigh School', 'Carr Manor\nCommunity\nSchool', 'Cockburn\nSchool', 
    'Corpus Christi\nCatholic College', 'Guiseley\nSchool', 'Lawnswood\nSchool', 
    'Mount St Mary\'s\nCatholic High School', 'Priesthorpe\nSchool', 'Pudsey\nGrammar School', 
    'Ralph Thoresby\nSchool', 'Roundhay\nSchool', 'Royds\nSchool', 
    'Temple Moor\nHigh School\nScience\nCollege', 'Wetherby High\nSchool'
]

authorised_absence_sessions = [
    14472, 11993, 14721, 10750, 13098, 7321, 11604, 
    11010, 11582, 14822, 14357, 9325, 11522, 16367, 
    16091, 11121, 16418, 15291, 15093, 8271
]

unauthorised_absence_sessions = [
    11554, 2783, 5817, 7752, 9800, 7238, 4632, 
    8794, 9817, 6501, 3690, 8464, 7435, 6596, 
    3908, 4675, 4804, 9749, 9041, 3016
]

# Create scatter plot with flipped axes
plt.figure(figsize=(18, 12))
scatter = plt.scatter(
    unauthorised_absence_sessions, authorised_absence_sessions, 
    color="#0072B2", alpha=0.8, label="Schools", edgecolor="black", s=100
)

# Labels for each school
for i, school in enumerate(schools):
    plt.text(
        unauthorised_absence_sessions[i] + 100, authorised_absence_sessions[i] + 100, 
        school, fontsize=11, fontweight='bold'
    )

# Title and axis labels
plt.title("Unauthorised vs Authorised Absence Sessions across 20 Leeds City Council-Funded Secondary Schools in 2014/2015 academic year", fontsize=17, fontweight='bold')
plt.xlabel("Number of Unauthorised Absence", fontsize=20, fontweight='bold')
plt.ylabel("Number of Authorised Absence", fontsize=20, fontweight='bold')

# Set x and y axis scales and ticks at intervals of 500
plt.xticks(np.arange(2500, 12500, 500), fontsize=11, fontweight='bold')  # 500 intervals for unauthorised absences
plt.yticks(np.arange(7000, 17500, 500), fontsize=11, fontweight='bold')  # 500 intervals for authorised absences

# Set x and y axis limits
plt.xlim(2500, 12000)  # Set x-axis min to 2500
plt.ylim(7000, 17000)  # Set y-axis min to 7000

# Add a legend
plt.legend(fontsize=15)

# Grid for better readability
plt.grid(True, linestyle="--", alpha=1, color='#575757')

# Add tight layout
plt.tight_layout()

# Show the plot
plt.show()
