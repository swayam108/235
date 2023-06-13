import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go 
import plotly.express as px


dataset=pd.read_csv('pro_234.csv')
football_club=dataset['Club'].value_counts().head(20)
print("top 20 clubs with maximum panelty accuracy premier league \n",football_club)
club_fix=go.Figure(data=[go.Pie(labels=football_club.index,values=football_club.values,hole=.5)])
club_fix.show()