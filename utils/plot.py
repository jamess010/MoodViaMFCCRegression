import matplotlib.pyplot as plt


def show_for_id_va(song_id, valence, arousal, ids, valence_dict, arousal_dict):
    idx = ids.index(song_id)
    plt.clf()
    plt.plot(valence_dict[song_id], arousal_dict[song_id], 'o', color='green', markersize=1)
    plt.plot(valence[idx], arousal[idx], 'o', color='blue')
    plt.plot(sum(valence_dict[song_id])/float(len(valence_dict[song_id])), sum(arousal_dict[song_id])/float(len(arousal_dict[song_id])), 'o', color='red')
    plt.axis([-1, 1, -1, 1])
    plt.savefig('results/' + str(song_id) + '.png')


def plot_all_va(all_val, all_aro, all_ids, valence, arousal):
    for id_s in all_ids:
        show_for_id_va(id_s, all_val, all_aro, all_ids, valence, arousal)