# WordCloud - version 0.0 English Templates

from wordcloud import WordCloud
import matplotlib.pyplot as plt 

# Open text
text = open('../constitution.txt').read()

# Generate object
wc = WordCloud().generate(text)

# Display the wordcloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# Save file
wc.to_file('wc_v0_0.png')