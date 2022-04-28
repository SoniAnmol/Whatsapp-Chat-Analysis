# Whatsapp Chat Analysis

## What is this?

This is a little fun project to analyse the whatsapp chat data.

## Why?

This all started with a pity argument with my girlfriend about my lousy texting habits. Therefore, I decided to scavenge
through internet to find resources to analyse the chats and prove my point. This project is heavily inspired by the work
of [WhatsApp Chat Analysis with Python](https://thecleverprogrammer.com/2021/04/09/whatsapp-chat-analysis-with-python/)
by [Aman Kharwal](https://thecleverprogrammer.com/author/amankharwal/)
and [WhatsApp Group Chat Analysis using Python](https://www.analyticsvidhya.com/blog/2021/04/whatsapp-group-chat-analyzer-using-python/)
by [Ronil Patil](https://www.analyticsvidhya.com/blog/author/ronyl0080/). After geeking through the code, I decided to
make a few changes and added some features. However, all the credit for the code goes to the original authors. I hope
you enjoy!

## How to use?

* Step 1: Check the [Requirements](#requirements) section and install the required libraries.
* Step 2: Check the [Structure](#structure) section to understand the structure of the project.
* Step 2: Export the chat from [WhatsApp](https://web.whatsapp.com/). and save it in the data folder.
* Step 3: Open the [notebook](/notebook/WhatsApp%20Chat%20Analysis.ipynb) specify the chat file name and run all the
  cells.

## How to export the chat?
To extract whatsapp chat, follow these steps:
1. Open whatsapp application on your phone
2. Open the chat you want to extract
3. Click on the options and select "Export chat"
4. Select "Export Chat"
5. Save the file as "WhatsApp Chat.csv" in the 'data' folder

## Requirements

For using this project, you need to install following packages:

* [pandas](https://pandas.pydata.org/)
* [numpy](https://www.numpy.org/)
* [Regex](https://regex101.com/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [Emoji](https://pypi.org/project/emoji/)
* [Wordcloud](https://pypi.org/project/wordcloud/)
* [Plotly](https://pypi.org/project/plotly/)
* [Heatmap](https://pypi.org/project/heatmap/)
* [NLTK](https://www.nltk.org/)

## Structure

Structure of the project:

[chat_analysis](..)\
|-- [README.md](ReadMe.md)\
|-- [data](data/) - contains the exported chat data\
|-- [notebook](notebook/) - contains the  notebook to analyze the chat data\
|-- [scripts](scripts/) - contains the scripts with methods to extract the chat data

