#!/usr/bin/env python
# -*- coding: windows-1252 -*-

def gerarScore(df,grupo):
    import pandas as pd # Python Data Analysis Library
    import csv
    import sys
    import statistics
    import numpy as np  # Scientific computing package
    total = []

    with open('worldcup2018.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            pais = row[0]
            if row[1] != grupo:
                continue

            timeEmcasa = df[df['home_team'] == pais ]
            timeForaCasa = df[df['away_team'] == pais ]
            time = pd.concat([timeEmcasa,timeForaCasa])

            totalPartidas = len(time)
            vitorias = time[time['winner'] == 1 ]
            derrotas = time[time['loser']  == 1 ]
            empates = time[time['winner'] == 3 ]


            #print(len(vitorias.winner.values))
            #print(totalPartidas)

            porcentagemVitorias = float(len(vitorias.winner.values))/ totalPartidas
            aproveitamento = porcentagemVitorias * 100
            score = time[time['away_score'] != 0]
            scoreEmCasa = time[time['home_score'] != 0]


            sumScore = []
            sumScore = np.append(score.away_score.values,scoreEmCasa.home_score.values)
            print(sumScore)




            total.append([grupo,pais,len(vitorias.winner.values),len(derrotas.loser.values), len(empates.winner.values),totalPartidas,statistics.variance(sumScore),aproveitamento])




	    '''
            if pais == 'Russia':
                score = time[time['home_score'] != 0]
                total.append([grupo,pais,len(vitorias.winner.values),len(derrotas.loser.values), len(empates.winner.values),totalPartidas,statistics.variance(score.home_score.values),aproveitamento])

            else:
                score = time[time['away_score'] != 0]
	   '''

    return total
