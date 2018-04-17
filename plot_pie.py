import matplotlib.pyplot as plt

def plot_tags(tags):
    weights = []
    tag_names = []
    for tag, weight in tags.items():
        weights.append(weight)
        tag_names.append(tag)
    plt.pie(weights, labels=tag_names)
