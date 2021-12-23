import pandas as pd


class DataTable:
    def __init__(self, *args):
        super(DataTable, self).__init__(*args)

    def save_file(self, filename):
        self.df.to_csv(filename, index=False)


class IndustryallDataTable(DataTable):
    def __init__(self, *args):
        super(DataTable, self).__init__(*args)

    def modify_dataframe(self, table_head, industryalls, corporates, homepages):
        self.df = pd.DataFrame(industryalls, columns=table_head)
        for i, company in enumerate(self.df["企業一覧"]):
            if company is None:
                continue
            else:
                self.df.at[i, self.df.columns[4]] = corporates.pop(0)
        for i, homepage in enumerate(self.df["ホームページ"]):
            if homepage is None:
                continue
            else:
                self.df.at[i, self.df.columns[5]] = homepages.pop(0)
