# LIS3DH Sensor - Reading and plotting data from serial monitor
# Atman Patel - Green Team
# November 1, 2020
# Version 1.0

import numpy as np # Used to make math operations easier for data
from matplotlib import pyplot as plt  # For data plotting library

# DATA READING FROM TXT FILE
#
# Opening file using built in Python commands
fileName = "../Data/ccwCircles.txt"
fh = open(fileName, 'r')

# Empty arrays to hold data from file
# Raw values signify the raw sensor reading
# Adj (adjusted) values signify the output in m/s^2 from the sensor
timeStamp = [] # Values will be converted to ms
rawX = []
rawY = []
rawZ = []
adjX = []
adjY = []
adjZ = []

# Iterating through each line in the file to store data into arrays
for line in fh:
    #print(line, end = '') # See what the file looks like

    # Making sure the line has data
    if (line[16] == 'X'):
        segments = line.split(' ') # Divides line into strings seperated by spaces

        #print(segments) # To view what the line looks like after splitting

        # Timestamp first
        timeSegments = segments[0].split(':') # Subdividing first portion
        hour = int(timeSegments[0])
        minute = int(timeSegments[1])
        seconds = float(timeSegments[2])
        # Converting each hour/min/seconds into ms
        hour = hour * 60 * 60 * 1000
        minute = minute * 60 * 1000
        seconds = seconds * 1000
        # Adding all together for a timestamp
        curTimestamp = hour + minute + seconds


        # Raw values follow timestamps, will be indexing segments for respective value
        # Raw values at indexes: 4, 8, 12
        curRawX = int(segments[4])
        curRawY = int(segments[8])

        curRawZ = segments[12] # Contains "#####\t\tX:" so need to fix
        curRawZ = curRawZ.split("\t") # Split but with tab character
        curRawZ = int(curRawZ[0])

        # Raw values follow timestamps, will be indexing segments for respective value
        # Raw values at indexes: 4, 8, 12
        curAdjX = float(segments[13])
        curAdjY = float(segments[15])
        curAdjZ = float(segments[17])


        # Appending each value to an array
        timeStamp.append(curTimestamp)
        rawX.append(curRawX)
        rawY.append(curRawY)
        rawZ.append(curRawZ)
        adjX.append(curAdjX)
        adjY.append(curAdjY)
        adjZ.append(curAdjZ)

# Closing file at end
fh.close()



# PLOTTING DATA FROM THE TEXT THAT WAS READ

# Adjust timestamp so it starts at 0
timeStamp = np.asarray(timeStamp) # Making it a numpy array for math
timeStamp = timeStamp - timeStamp[0]

# Plot 1 - Simple timestamp vs raw data value plots
# Initial setup for plot and axis titles
plt.figure()
plt.title("1 - Raw Sensor Output")
plt.xlabel("Timestamp [ms]")
plt.ylabel("Raw Sensor Output [unitless]")
# Plotting the raw values from the data that was read
plt.scatter(timeStamp, rawX, c='r', marker='.')
plt.scatter(timeStamp, rawY, c='g', marker='.')
plt.scatter(timeStamp, rawZ, c='b', marker='.')
# To view the figure
plt.show()
# A viewer won't exactly know which data points are which, should add a legend




# Plot 2 - Simple timestamp vs raw data value plots with labels
# Initial setup for plot and axis titles
plt.figure()
plt.title("2 - Raw Sensor Output")
plt.xlabel("Timestamp [ms]")
plt.ylabel("Raw Sensor Output [unitless]")
# Plotting the raw values from the data that was read
a = plt.scatter(timeStamp, rawX, c='r', marker='.')
b = plt.scatter(timeStamp, rawY, c='g', marker='.')
c = plt.scatter(timeStamp, rawZ, c='b', marker='.')
# Adding a legend
plt.legend([a, b, c], ["Raw X", "Raw Y", "Raw Z"])
# To view the figure
plt.show()
# Plots are labeled, but the points are so numerous and close together that it
# is hard to get any information from it


# Plot 3 - Creating subplots to zoom in on data
# Setting up subplot
fig, ax = plt.subplots(3)
fig.suptitle("3 - Raw Sensor Output (subplots)")
# Plotting the raw values from the data that was read
# Need to set titles individual for subplots
ax[0].scatter(timeStamp, rawX, c='r', marker='.')
ax[0].set_title("Raw X Data")
ax[1].scatter(timeStamp, rawY, c='g', marker='.')
ax[1].set_title("Raw Y Data")
ax[2].scatter(timeStamp, rawZ, c='b', marker='.')
ax[2].set_title("Raw Z Data")
# Setting the x and y axis labels
for curAx in ax:
    curAx.set(xlabel="Timestamp [ms]", ylabel="Raw Output")
# To view the figure
plt.tight_layout() # Prevents overlapping of titles and axes
plt.show()
# Now it is easier to see the spread in each of the data but there are so many
# values that reducing the range could be helpful


# Plot 4 - Reducing range of subplots to zoom in on data
# Setting up subplot
fig, ax = plt.subplots(3)
fig.suptitle("4 - Raw Sensor Output (subplots)")
# Plotting the raw values from the data that was read
# Need to set titles individual for subplots
ax[0].scatter(timeStamp, rawX, c='r', marker='.')
ax[0].set_title("Raw X Data")
ax[1].scatter(timeStamp, rawY, c='g', marker='.')
ax[1].set_title("Raw Y Data")
ax[2].scatter(timeStamp, rawZ, c='b', marker='.')
ax[2].set_title("Raw Z Data")
# Setting the x and y axis labels
for curAx in ax:
    curAx.set(xlabel="Timestamp [ms]", ylabel="Raw Output")
    curAx.set_xlim([0, 10000]) # First 10 seconds of data
# To view the figure
plt.tight_layout() # Prevents overlapping of titles and axes
plt.show()
# From this it is much easier to see the variation between data values


# The same thing can be done for the adjusted X/Y/Z Data
# Plot 5 - Plotting the adjusted values
# Setting up subplot
fig, ax = plt.subplots(3)
fig.suptitle("5 - Adjusted Sensor Output (subplots)")
# Plotting the raw values from the data that was read
# Need to set titles individual for subplots
ax[0].scatter(timeStamp, adjX, c='r', marker='.')
ax[0].set_title("Adjusted X Data")
ax[1].scatter(timeStamp, adjY, c='g', marker='.')
ax[1].set_title("Adjusted Y Data")
ax[2].scatter(timeStamp, adjZ, c='b', marker='.')
ax[2].set_title("Adjusted Z Data")
# Setting the x and y axis labels
for curAx in ax:
    # Using text between $ lets it be interpreted as LaTex which allows for nicer formatting
    curAx.set(xlabel="Timestamp [ms]", ylabel="Acceleration [$m/s^2$]")
# To view the figure
plt.tight_layout() # Prevents overlapping of titles and axes
plt.show()
# It would be beneficial to compare these two together in the same plot



# Plot 6 - Plotting the raw and adjusted values
# Setting up subplot
fig, ax = plt.subplots(3, 2) # Changed this to be 3x2
fig.suptitle("6 - Raw and Adjusted OutPut Comparison (subplots)")
# Plotting the raw values from the data that was read
# Need to set titles individual for subplots
ax[0,0].plot(timeStamp, rawX, c='r', marker='.')
ax[0,0].set_title("Raw X Data")
ax[1,0].scatter(timeStamp, rawY, c='g', marker='.')
ax[1,0].set_title("Raw Y Data")
ax[2,0].scatter(timeStamp, rawZ, c='b', marker='.')
ax[2,0].set_title("Raw Z Data")
ax[0,1].scatter(timeStamp, adjX, c='r', marker='.')
ax[0,1].set_title("Adjusted X Data")
ax[1,1].scatter(timeStamp, adjY, c='g', marker='.')
ax[1,1].set_title("Adjusted Y Data")
ax[2,1].scatter(timeStamp, adjZ, c='b', marker='.')
ax[2,1].set_title("Adjusted Z Data")
# Setting the x and y axis labels
# Two loops to label each column differently
for curAx in ax[:,0]:
    # Using text between $ lets it be interpreted as LaTex which allows for nicer formatting
    curAx.set(xlabel="Timestamp [ms]", ylabel="Raw Output")
for curAx in ax[:,1]:
    # Using text between $ lets it be interpreted as LaTex which allows for nicer formatting
    curAx.set(xlabel="Timestamp [ms]", ylabel="Acceleration [$m/s^2$]")
# To view the figure
plt.tight_layout() # Prevents overlapping of titles and axes
plt.show()
# What can be done next?

# Thinking points:
# - For a non moving sensor, what would be the expected acceleration values?
# - The z-direction has large values even for a non moving sensor, what could that be measuring?
# - The expected values are off from the measured values, can this be adjusted?
#       - (Sensor calibration)
# - Are there better ways to plot data with smoothing or averaging?
# - What can you gain after analyzing acceleration data?
#       - (Integration to find velocity and integrate again for position)
# - With the polling rate and sensor data, how useful is this sensor? How could it be better?
#
#
# Areas of improvement:
# - Reading in data from a .txt file each time is not ideal, would be better to
#       read the data in once and output it as a .csv file
#       - .csv files allow for the usage of pandas (Python library) dataframes
# - Numpy can be used to perform averages/standard deviation of the data before plotting
# - Actually calibrating the sensors using the still motion data would help get more accurate results
