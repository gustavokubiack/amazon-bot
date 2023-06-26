import matplotlib.pyplot as plt
import pandas as pd

from src.data_mining import SeleniumDataMining


class TitleAnalysis(SeleniumDataMining):
    def __init__(self):
        super().__init__()
        self.data = self.get_data_mining()

    def generate_spreadsheet(self):
        df = pd.DataFrame(self.data, columns=["Títulos"])

        writer = pd.ExcelWriter("titulos.xlsx", engine="xlsxwriter")

        df.to_excel(writer, index=False, sheet_name="Sheet1")

        worksheet = writer.sheets["Sheet1"]

        max_title_length = max([len(title) for title in df["Títulos"]])
        column_width = max_title_length + 2
        worksheet.set_column(0, 0, column_width)

        writer.close()

    def generate_pie_chart(self):
        df = pd.DataFrame(self.data, columns=["Títulos"])

        df_python = df[df["Títulos"].str.contains("python", case=False)]
        counts = df_python.shape[0]
        total = df.shape[0] - counts

        values = pd.Series([counts, total], index=["Python", "Outros"])
        values.plot(kind="pie", autopct="%1.1f%%")
        plt.axis("equal")
        plt.savefig("graph.png")
