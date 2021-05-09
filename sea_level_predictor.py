import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  # Create scatter plot
  plt.scatter(df.Year, df["CSIRO Adjusted Sea Level"])

  # Create first line of best fit
  LOBF1 = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
  x1 = np.arange(df.Year.iloc[0], 2050)
  plt.plot(x1, LOBF1.intercept + LOBF1.slope*x1, 'r', label='fitted line 1')

  # Create second line of best fit
  LOBF1 = linregress(df[df.Year >= 2000].Year, df[df.Year >= 2000]["CSIRO Adjusted Sea Level"])
  x2 = np.arange(2000, 2050)
  plt.plot(x2, LOBF1.intercept + LOBF1.slope*x2, 'r', label='fitted line 2')

  # Add labels and title
  plt.title("Rise in Sea Level")
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  # Save plot and return data for testing (DO NOT MODIFY)
  # plt.show()
  plt.savefig('sea_level_plot.png')
  return plt.gca()