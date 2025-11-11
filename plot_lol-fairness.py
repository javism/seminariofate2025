import pandas as pd
import matplotlib.pyplot as plt

svg = False

df = pd.read_csv('data/lol-fairness.csv')

with plt.xkcd():
    ax = df.plot.bar(x='Year', y='Articles', legend=False,
                color='red', title='Brief history of fairness in ML (nov\'22)')
    ax.set_ylabel('Papers')
    ax.annotate('LOL FAIRNESS!!', xy=(2,3000))
    ax.annotate('OH, CRAP.\n  (2017)', xy=(5,6000))
    ax.annotate('OH, CRAP.\n  (2021)', xy=(8,20000))
    plt.xticks(rotation = 25)
    if svg:
        plt.savefig('pics/lol-fairness.svg')
    else: 
        plot_margin = 1.25
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,
              x1 + plot_margin,
              y0 - plot_margin,
              y1 + plot_margin))
        plt.savefig('pics/lol-fairness.png',dpi=300)
