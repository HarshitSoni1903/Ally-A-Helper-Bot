# Ally: A Helper Bot
The internet can be used as a means of communication between a mental health practitioner and a patient. Some online systems combine self-help and interaction with a live therapist, a user may work through some content independently, and a therapist periodically reviews their progress and answers any questions they may have. But it is often seen that people feel shy or uncomfortable sharing their mental health issues compared to their physical health. Thus, systems were embedded in special purpose computers, such as robots or they may use sophisticated Artifical Intelligence (AI) technology to bridge the gap between computerized and live therapy. Thus, in this project we use Neural Networks and Speech Recognition to create a basic therapist to interact with people dealing with mental health issues. The objective of our project is to promoto awareness about these common issues that people hardly speak about and make is easier for people to get through with it.

## Ally in brief - a flow-chart:

#### Modules:
1. Chatbot: 
   - 3 Neural networks. one for classifications, two RNNs for conversation.
   - A system for administering CBT that can be a pre-feeded dialog system.
2. Controller interface for devices to be operated, like television, music player, computer etc.
3. Voice to text interface.
4. Text to speeech interface.
5. Log generation for patient's data.
6. Fail-safe module(extreme cases like suicidal/self-harm thoughts and other such conversation). 
7. Voice analysis.
8. Facial analysis(if applicable).

#### Architecture for Chatbot: 

![Architecture](/images/chatbot_flow.PNG)

> **Neual network-1:** _A network that analyses the text input and classifies it under 3 categories, finally decides upon what system to use:_
> - Neutral conversations: _Where the system functions like a normal chatbot(**Neual network-2**)._
> - Weak-Emotion conversation: _Where the system generates emotional responses(**Neual network-3**)._
> - Strong-Emotion conversation: _where administering subtle CBT is required._

## Checklist:

 - [ ] Complete the literature survey from available research papers, and refer to new papers if required.
 - [ ] Find a suilable algorithm to construct our RNN. 
 - [x] Following algorithms are finalized as of now:
 -  Sequence-to-Sequence using LSTM for sentence generation, but not much information is collected yet.
 - Classifie neural network using NLU for understanding the emotions of a statement.
 -  [Facial emotion recognition](https://www.apprendimentoautomatico.it/apprendimentoautomatico-wpblog/en/emotions-detection-via-facial-expressions-with-python-opencv/), is finalized with code and dataset as well. Although the feasibility is not decided yet. Hence, we have the module at least. There are other codes for facial-emotion as well, which can be found in [bookmarks](https://github.com/HarshitSoni1903/Ally-A-Helper-Bot/blob/master/bookmarks) (for better use, open the html file in browser, not in github website).

 - [ ] Check the feasibility of  facial-emotion module in the project. 
 - [ ] A few algorithms and inbuilt python modules were found that allowed detection of emotions from the voice. which might find a good use in the project, and gives more credibility to it, which is yet to researched upon.
 #### The Dataset
 - [ ] The dataset is yet to be found for emotional conversation.
      > _If the dataset is not found, generating subtitles from videos present on youtube is our last resort._
       
 - [x] The dataset for normal conversation already exists and can be used as soon as neural network is decided.   
 - [ ] The data on how to administer CBT is yet to be found, we came accross a few books and some articles but no conclusion is made so far.  

