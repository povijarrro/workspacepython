#!python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    G1 = nx.complete_graph(5)
    G2 = nx.complete_graph(5)
    G2 = nx.relabel_nodes(G2,{0:"A",1:"B",2:"C",3:"D",4:"E"})
    G_con = nx.from_edgelist([(0,"A"),(1,"B")])
    G = nx.compose_all((G1,G2,G_con))

    fig,ax = plt.subplots(2,3)
    fig.suptitle("Networkx with subplots")
    man = plt.get_current_fig_manager()
    man.set_window_title("Graphs with networkx")
    man.window.wm_iconbitmap("test.ico")

    ax[0,0].set_title("G1")
    ax[0,1].set_title("G2")
    ax[1,0].set_title("G_con")
    ax[1,1].set_title("nx.compose_all((G1,G2,G_con))")
    ax[0,2].set_title("Petersen graph")

    nx.draw_networkx(G1,with_labels=True,ax = ax[0,0])
    nx.draw_networkx(G2,with_labels=True,ax = ax[0,1])
    nx.draw_networkx(G_con,with_labels=True,ax = ax[1,0])
    nx.draw_networkx(G,with_labels=True,ax = ax[1,1])
    
    petersen = nx.petersen_graph()

    pos = {}

# Pentagon (outer cycle)
    for i in range(5):
        angle = np.pi/2 + 2 * np.pi * (i-3) / 5
        pos[i] = (np.cos(angle), np.sin(angle))

# 5-star (inner cycle)
    for i in range(5, 10):
        angle = np.pi/2 + 2 * np.pi * (i - 8) / 5  # offset by 0.5 to place between pentagon nodes
        pos[i] = (0.5 * np.cos(angle), 0.5 * np.sin(angle))

    nx.draw(petersen,pos,with_labels=True,ax=ax[0,2])
    print(nx.astar_path(G,"C",3))

    plt.show()

if __name__ == "__main__":
    main()