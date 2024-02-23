from flask import Flask, render_template
from pandas import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt,dates as mdates
import numpy as np

app = Flask(__name__,template_folder="template")

df = pd.read_csv("Ghibli characters.csv")
antigo = df['movie'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
antigo = antigo[2:]
ano1 =  df['release date'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
ano1 = ano1[2:]

novo = df['movie'][df['release date'] == df['release date'].max()].drop_duplicates().to_string()
novo = novo[2:]
ano2 =  df['release date'][df['release date'] == df['release date'].max()].drop_duplicates().to_string()
ano2 = ano2[2:]

time = df[['movie','release date']].drop_duplicates()
time["Level"] = [np.random.randint(-6,-2) if (i%2)==0 else np.random.randint(2,6) for i in range(len(time))]
time["release date"] = pd.to_datetime(df['release date'], format="%Y")

fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")

ax.vlines(time['release date'], 0, time['Level'], color="black")  # The vertical stems.
ax.plot(time['release date'], np.zeros_like(time['release date']), "-o",
        color="black", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(time['release date'], time['Level'], time['movie']):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="left",rotation=45,
                verticalalignment="bottom" if l > 0 else "top")

# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=24))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.setp(ax.get_xticklabels(), rotation=90, ha="center")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)
ax.spines["bottom"].set_position(("axes", 0.5 ))



ax.margins(y=0.1)
ax.patch.set_facecolor('#0178C1')
fig.patch.set_facecolor('#0178C1')

timeline = plt

@app.route("/")
def home():
    return render_template("home.html",antigo = antigo,ano1=ano1,novo = novo,ano2 = ano2, timeline = timeline)

    
if __name__ == "__main__":
    app.run(debug=True)