#Importar librerias
import matplotlib.pyplot as plt
import seaborn as sns

# Función para graficar variables en un Data Frame
def visualize_rows (df):
    for n, i in enumerate(df):
        plt.subplot((len(list(df.columns))/3)+1,3,n+1)
        if df[i].dtypes ==float:
            sns.distplot(df[i])
            plt.title(i)
            plt.xlabel("")
        elif df[i].dtypes =="object":
            sns.countplot(df[i])
            plt.title(i)
            plt.xlabel("")
        else:
            sns.distplot(df[i],kde=False)
            plt.title(i)
            plt.xlabel("")
    plt.tight_layout()

