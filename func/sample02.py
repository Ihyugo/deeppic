from matplotlib.colors import ListedColormap

def plot_decison_regions(X, y, classifier, resolution=0.02):
	#マーカーとカラーマップの準備
	markers = ('s', 'x', 'o', '^', 'v')
	colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
	cmap = ListedColormap(colors[:len(np.unique(y))])

