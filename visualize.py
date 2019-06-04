import matplotlib.pyplot as plt


def plot(generation, allBestFitness, bestGenome, cityLoc):
    plt.subplot(2, 1, 1)
    plt.text((generation / 2) - 0.5, allBestFitness[0] + 1.2, "Generation: {0} Best Fitness: {1}".format(
        generation, bestGenome.fitness), ha='center', va='bottom')
    plt.plot(range(0, generation), allBestFitness, c="green")
    plt.subplot(2, 1, 2)

    xx = []
    yy = []
    startPoint = None
    for x, y in cityLoc:
        if startPoint is None:
            startPoint = cityLoc[0]
            plt.scatter(startPoint[0], startPoint[1], c="green", marker=">")
        else:
            plt.scatter(x, y, c="black")

    for i in bestGenome.chromosomes:
        xx.append(cityLoc[i][0])
        yy.append(cityLoc[i][1])
    plt.plot(xx, yy, color="red", linewidth=1.75, linestyle="-")
    plt.show()
