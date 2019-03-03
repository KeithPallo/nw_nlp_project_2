




def human_readable():

    f = open('%s_human_readable_results.txt' % year, 'w')
    f.write('Hosts: ' + ', '.join(hosts) + '\n\n')
    f.write('Awards: ' + ', '.join(awards) + '\n\n')

    for award in award_list:
        f.write('Award: ' + award + '\n')
        f.write('Presenters: ' + ', '.join(final_pres[award]) + '\n')
        f.write('Nominees: ' + ', '.join(final_nom[award]) + '\n')
        f.write('Winner: ' + final_winner[award] + '\n\n')

    f.write('Best Dressed: ' + ', '.join(best_dressed) + '\n')
    f.write('Worst Dressed: ' + ', '.join(worst_dressed) + '\n\n')

    f.write('Best Jokes: ' + '\n'.join(best_jokes) + '\n\n')
    f.write('Worst Jokes: ' + '\n'.join(worst_jokes) + '\n')

    f.close()

    return
