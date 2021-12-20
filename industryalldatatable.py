import pandas as pd


class IndustryallDataTable:
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

    def save_file(self):
        self.df.to_csv("pandas.csv", index=False)
