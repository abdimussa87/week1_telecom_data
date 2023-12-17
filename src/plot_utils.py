import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(12, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=3, aspect=5)
    plt.title(f'Distribution of {column}', size=10, fontweight='bold')
    plt.show()
