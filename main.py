import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



data_new = pd.read_csv("C:/Users/yurar/PycharmProjects/diplom/csv/data_new.csv", encoding='UTF-8', delimiter=',')

teams = ['Real Madrid', 'Barcelona', 'Ath Madrid', 'Sevilla', 'Villarreal', 'Sociedad',
         'Getafe', 'Valencia', 'Ath Bilbao', 'Levante', 'Valladolid', 'Eibar', 'Betis',
         'Alaves', 'Celta', 'Leganes', 'Espanol', 'Huesca', 'Girona', 'Vallecano']

deleteTeam = [x for x in pd.unique(data_new['Хозяева(Х)']) if x not in teams]

for name in deleteTeam:
    data = data[data['Хозяева(Х)'] != name]
    data = data[data['Гости(Г)'] != name]
data = data.reset_index(drop=True)


data.loc[(data['ГолыХ'] > data['ГолыГ']), 'Победитель'] = data['Хозяева(Х)']
data.loc[(data['ГолыХ'] == data['ГолыГ']), 'Победитель'] = 'Ничья'
data.loc[(data['ГолыХ'] < data['ГолыГ']), 'Победитель'] = data['Гости(Г)']
data.loc[(data['ГолыХ'] > data['ГолыГ']), 'Проигравший'] = data['Гости(Г)']
data.loc[(data['ГолыХ'] == data['ГолыГ']), 'Проигравший'] = 'Ничья'
data.loc[(data['ГолыХ'] < data['ГолыГ']), 'Проигравший'] = data['Хозяева(Х)']


def GetSeasonTeamStat(team, seasons):
    goalScored = 0  # Голов забито
    goalAllowed = 0  # Голов пропущено

    gameWin = 0  # Выиграно
    gameDraw = 0  # Ничья
    gameLost = 0  # Проиграно

    totalScore = 0  # Количество набранных очков

    matches = 0  # Количество сыгранных матчей

    shot = 0  # Удары
    shotOnTarget = 0  # Удары в створ

    cross = 0  # Угловые
    foul = 0  # Фолы

    YC = 0  # Желтые карточки
    RC = 0  # Красные карточки

    for i in range(len(data)):
        if data['Хозяева(Х)'][i] == team and seasons == data['Дата'][i]:
            matches += 1

            goalScored += data['ГолыХ'][i]
            goalAllowed += data['ГолыГ'][i]

            if (data['ГолыХ'][i] > data['ГолыГ'][i]):
                totalScore += 3
                gameWin += 1
            elif (data['ГолыХ'][i] < data['ГолыГ'][i]):
                gameLost += 1
            else:
                totalScore += 1
                gameDraw += 1

            shot += data['УдарыХ'][i]
            shotOnTarget += data['Удары по воротам Х'][i]

            foul += data['ФолыХ'][i]

            YC += data['ЖКХ'][i]
            RC += data['ККХ'][i]
            cross += data['УгловыеХ'][i]

    for j in range(len(data)):
        if data['Гости(Г)'][j] == team and seasons == data['Дата'][j]:
            matches += 1

            goalScored += data['ГолыГ'][j]
            goalAllowed += data['ГолыХ'][j]

            if (data['ГолыГ'][j] > data['ГолыХ'][j]):
                totalScore += 3
                gameWin += 1
            elif (data['ГолыГ'][j] < data['ГолыХ'][j]):
                gameLost += 1
            else:
                totalScore += 1
                gameDraw += 1

            shot += data['УдарыГ'][j]
            shotOnTarget += data['Удары по воротам Г'][j]

            foul += data['ФолыГ'][j]

            YC += data['ЖКГ'][j]
            RC += data['ККГ'][j]
            cross += data['УгловыеГ'][j]

    return [gameWin, gameDraw, gameLost,
            goalScored, goalAllowed, totalScore,
            shot, shotOnTarget, foul, YC, RC,
            cross]


returnNames = ["Выиграно", "Ничья", "Проиграно",
               "\nГолов забито", "Голов пропущено", "\nНабрано очков",
               "\nУдары", "Удары в створ",
               "\nФолы", "Желтые карточки",
               "\nКрасные карточки", "Угловые"]

for i, n in zip(returnNames, GetSeasonTeamStat('Barcelona', 'Сезон 18/19')):
    print(i, n)

total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

seasons = ['Сезон 09/10', 'Сезон 10/11', 'Сезон 11/12', 'Сезон 12/13', 'Сезон 13/14',
           'Сезон 14/15', 'Сезон 15/16', 'Сезон 16/17', 'Сезон 17/18', 'Сезон 18/19']

def GetAllTeamStat(team):
    for i in range(12):
        total[i] = GetSeasonTeamStat(team, 'Сезон 09/10')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 10/11')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 11/12')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 12/13')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 13/14')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 15/16')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 16/17')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 17/18')[i] \
                   + GetSeasonTeamStat(team, 'Сезон 18/19')[i]
        return total


def GetSeasonAllTeamStat(seasons):
    annual = {}
    for team in teams:
        team_vector = GetSeasonTeamStat(team, seasons)
        annual[team] = team_vector
    return annual


print(GetSeasonAllTeamStat('Сезон 18/19'))



def GetTrainingData(seasons):
    totalNumGames = 0
    for season in seasons:
        annual = data[data['Дата'] == season]
        totalNumGames += len(annual.index)
    numFeatures = len(GetSeasonTeamStat('Barcelona', 'Сезон 18/19'))  # случайная команда для определения размерности
    xTrain = np.zeros((totalNumGames, numFeatures))
    yTrain = np.zeros((totalNumGames))
    indexCounter = 0
    for season in seasons:
        team_vectors = GetSeasonAllTeamStat(season)
        annual = data[data['Дата'] == season]
        numGamesInYear = len(annual.index)
        xTrainAnnual = np.zeros((numGamesInYear, numFeatures))
        yTrainAnnual = np.zeros((numGamesInYear))
        counter = 0
        for index, row in annual.iterrows():
            team = row['Хозяева(Х)']
            t_vector = team_vectors[team]
            rivals = row['Гости(Г)']
            r_vector = team_vectors[rivals]

            diff = [a - b for a, b in zip(t_vector, r_vector)]

            if len(diff) != 0:
                xTrainAnnual[counter] = diff
            if team == row['Победитель']:
                yTrainAnnual[counter] = 1
            else:
                yTrainAnnual[counter] = 0
            counter += 1
        xTrain[indexCounter:numGamesInYear + indexCounter] = xTrainAnnual
        yTrain[indexCounter:numGamesInYear + indexCounter] = yTrainAnnual
        indexCounter += numGamesInYear
    return xTrain, yTrain


years = seasons
xTrain, yTrain = GetTrainingData(years)

model = LinearRegression()
model.fit(xTrain, yTrain)


def createGamePrediction(team1_vector, team2_vector):
    diff = [[a - b for a, b in zip(team1_vector, team2_vector)]]
    predictions = model.predict(diff)
    return predictions


def result(team1_name, team2_name):
    team1_vector = GetSeasonTeamStat(team1_name, 'Сезон 18/19')
    team2_vector = GetSeasonTeamStat(team2_name, 'Сезон 18/19')
    rez = ''

    if createGamePrediction(team1_vector, team2_vector) - createGamePrediction(team2_vector, team1_vector) >= 0.3:
        rez = 'Вероятный исход: Победа ' + team1_name
    elif createGamePrediction(team1_vector, team2_vector) - createGamePrediction(team2_vector, team1_vector) >= -0.3:
        rez = 'Вероятный исход: Ничья'
    else:
        rez = 'Вероятный исход: Поражение ' + team1_name

    res = 'Вероятность, что выиграет ' + team1_name + ': ' + str(
        createGamePrediction(team1_vector, team2_vector)) + '\n' + '\n' \
        + 'Вероятность, что выиграет ' + team2_name + ': ' + str(
        createGamePrediction(team2_vector, team1_vector)) + '\n' + '\n' + rez
    return res

print(result('Ath Madrid', 'Barcelona'))




