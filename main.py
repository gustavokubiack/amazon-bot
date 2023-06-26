from src.title_analysis import TitleAnalysis


def main():
    run = TitleAnalysis()
    run.generate_pie_chart()
    run.generate_spreadsheet()


if __name__ == "__main__":
    main()
