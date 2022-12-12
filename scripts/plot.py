import seaborn as sns
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, df) -> None:
        self.df = df

    #More useful for Continuous variables (Histogram)
    def plot_hist(self, column:str, color:str)->None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(12, 7))
        sns.displot(data=self.df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()


    #Recommended for discrete variables (Countplot)
    def plot_count(self, column:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=self.df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
        
    #Enable Bivariate Analysis
    def plot_bar(self,  x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
        plt.figure(figsize=(12, 7))
        sns.barplot(data = self.df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()

    def plot_heatmap(self, title:str, cbar=False)->None:
        plt.figure(figsize=(12, 7))
        sns.heatmap(self.df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
        plt.title(title, size=18, fontweight='bold')
        plt.show()

    #Easy to determine outliers with
    def plot_box(self, x_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = self.df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()


    def plot_box_multi(self, x_col:str, y_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = self.df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.show()

    def plot_scatter(self,  x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data = self.df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks( fontsize=14)
        plt.show()

    def plot_pairs(self, hue:str, diag_kind:str):
        sns.pairplot(self.df, hue, diag_kind,
                plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
                height=4)

        """
        Depends on the number of columns provided
        """