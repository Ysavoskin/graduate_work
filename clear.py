import pandas as pd



df = pd.read_csv("C:/Users/yurar/PycharmProjects/diplom/csv/allstats14-19.csv", encoding='cp1251', delimiter=',')
data = df.drop(['Div', 'HTHG', 'HTAG', 'HTR', 'B365H', 'B365D', 'B365A',
                       'BWH', 'BWD', 'BWA', 'IWH', 'IWD',
                       'IWA', 'LBH', 'LBD', 'LBA', 'WHH',
                       'WHD', 'WHA', 'SJH', 'SJD', 'SJA', 'VCH', 'VCD', 'VCA',
                       'PSH', 'PSD', 'PSA', 'PSCH', 'PSCD', 'PSCA',
                       'Bb1X2', 'BbMxH', 'BbAvH', 'BbMxD',
                       'BbAvD', 'BbMxA', 'BbAvA', 'BbOU', 'BbMx>2.5', 'BbAv>2.5',
                       'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 'BbMxAHH', 'BbAvAHH', 'BbMxAHA', 'BbAvAHA'], axis=1)

data_new = data.rename(columns={'Date': 'Дата', 'HomeTeam': 'Хозяева(Х)', 'AwayTeam': 'Гости(Г)','FTHG': 'ГолыХ',
                         'FTAG': 'ГолыГ', 'FTR': 'Результат', 'HS': 'УдарыХ', 'AS': 'УдарыГ',
                         'HST': 'Удары по воротам Х', 'AST': 'Удары по воротам Г', 'HF': 'ФолыХ', 'AF': 'ФолыГ',
                         'HC': 'УгловыеХ', 'AC': 'УгловыеГ', 'HY': 'ЖКХ', 'AY': 'ЖКГ', 'HR': 'ККХ', 'AR': 'ККГ'}, inplace=True)



