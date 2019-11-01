# WordCloud - version 1 English Templates

from wordcloud import WordCloud
import matplotlib.pyplot as plt 

# Open text
text = open('../constitution.txt').read()

# Generate object
wc = WordCloud(font_path='../Hiragino.ttf', width=800, height=600, 
	mode='RGBA', background_color=None).generate(text)

# Display wordcloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# Save pic
wc.to_file('wc_v1.png')