import csv
from matplotlib import pyplot
# data from https://github.com/tonmcg/County_Level_Election_Results_12-16


with open('2016_US_County_Level_Presidential_Results.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    print data.fieldnames
    totalVotes = 0
    totalVotesList = []
    totalDemVotes = 0
    totalDemVotesList = []
    totalGOPVotes = 0
    totalGOPVotesList = []
    countyList = []
    for row in data:
        totalVotes += float(row['total_votes'])
        totalVotesList.append(totalVotes)
        totalDemVotes += float(row['votes_dem'])
        totalDemVotesList.append(totalDemVotes)
        totalGOPVotes += float(row['votes_gop'])
        totalGOPVotesList.append(totalGOPVotes)
        # totalVotesList.append(row['total_votes'])
        countyList.append(row[''])
        # totalDemVotes.append(row['votes_dem'])
        # totalGOPVotes.append(row['votes_gop'])
    print(totalVotes)
    print(totalDemVotes)
    print(totalGOPVotes)
    # totalVotesList = [row['total_votes'] for row in data]
    # print totalVotesList
    # print len(totalVotesList)
    # print len(totalVotesList)
    # print len(countyList)
    # pyplot.xlabel('County number')
    # pyplot.ylabel('Total Votes')
    pyplot.plot(countyList, totalVotesList, label='TotalVotes')
    pyplot.plot(countyList, totalDemVotesList, label='TotalDem')
    pyplot.plot(countyList, totalGOPVotesList, label='TotalGOP')
    pyplot.legend()
    pyplot.show()


