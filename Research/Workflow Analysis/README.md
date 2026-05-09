
Search prompts:
```
figma livestream no speaking
figma livestream asmr
figma livestream design asmr
figma real time work livestream design asmr
figma real time 
figma real time livestream
figma speed design live
figma speed design livestream
design with me live
Design With Me Live Long Session
```

Key creators:
```
DesignCode - 345k Subscribers - Large Quanity of Livestreams
CharliMarieTV - 237k Subscribers - Large Quanity of "Design with me Livestreams" Livestreams 
NAM Design - 33.4k Subscribers- does silent UI speed design challenges - super useful
Charli Cheung - 31.5k Subscribers
ASMR Design - 342 Subscribers - but very useful as has no talking 

```

https://www.youtube.com/watch?v=e3ZB0jGHoTA

This is FigJam not Figma:
https://www.youtube.com/watch?v=3xxTwfWzNj8

---
## Sample Workflow 1 - incomplete
Sampled from NAM Design - random sample from UI Speed Design Weekly Challenge (had 38 videos at the time):

```run-python
import random
print(random.randint(1,38))
```
Selected video 6: https://www.youtube.com/watch?v=JkC4o1U5zgM&list=PLfrBp-7QhDqtmJ8oAjYhP6PLQqwDI0z1S&index=6

Skipped to 0:21 for the start of the design interaction. 

Learnings:
Making mistakes is cheap with mouse and keyboard (often < 1 second for clicking the wrong object)
Making mistakes with voice is frustrating and significantly slows down the design process and interrupts the design flow
The longest tasks with mouse and keyboard are often associated with typing text - selecting, dragging and clicking things is usually super quick

This exercise aims to subtly highlight how quick all of these actions are when its easy to work with the mouse and keyboard but how time consuming they would be if that was not possible

Simultaneous clicking + keyboard shortcut is probably hard - need to check 

## Sample Workflow 2 - incomplete (need to review it)
Sampled from ASMR Design - random sample from UI Speed Design Weekly Challenge (had 8 videos at the time):

```run-python
import random
print(random.randint(1,8))
```
Selected video 7: https://www.youtube.com/watch?v=OLb7Rqo1KVQ

## Sample Workflow 3 - incomplete
Unit flows - two videos other 15 minutes long
https://www.youtube.com/@unitflows

```run-python
import random
print(random.randint(1,2))
```
Selected video: https://www.youtube.com/watch?v=GfVA26-Z-SE

```run-python
import random

def random_timestamp(end="67.02", start="0.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp(start="0.54", end="40.00"))
```

Start time = 10.38 - sample from here - moved to 10.36 for first clear action

Learnings:
- Being able to maintain an internal state history may be relevant e.g. if the user wants to say something like "zoom back to the original position"
- Desired positions will be hard to verbally dictate without some kind of visual support e.g. a grid interface or similar
- Repeated sequences are common which would be time-consuming to replicate with voice - but these can potentially be encoded as a 'macro' or 'function' defined by the user e.g. repeat sequence on object x; if the software can identify a sequence and remap it to new objects that could potentially be meaningful - e.g. that was a sequence you just did on an object would you like to do that again?

hovering is difficult to achieve via voice but is required for some information revealing purposes e.g. finding where a layer is; revealing tooltips etc. 

Sample two start time: 
```run-python
import random

def random_timestamp(end="67.02", start="0.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp(start="0.54", end="40.00"))
```
24.54

clicking on GUI values / updating these values is important - in theory all of these values could be rewritten as voice inputs but that could potentially be quite time consuming -> a more intuitive method would try to take what already exists and makes it easier to navigate 
-> rewriting everything as plaintext
lots of actions may not be required for a voice tool as they are mistakes/misclicks 

deep select is probably **HARD** for voice since it requires explicit hierarchy knowledge that a mouse user gets visually for free.

for users without disabilities many actions can be 'comfort' actions e.g. zooming in and out briefly or deselecting an object and reselecting an object when necessary. These actions are redundancies and not crucial to actual tangible design updates but can help the user with way-finding. In comparison these actions are extremely costly for users with disabilities - although that does not eliminate that they might actually be desirable. 

---
## Sample Workflow 4 - incomplete
Sample from here: https://www.youtube.com/playlist?list=PLuCVsS_EScKHdEgqHps_rFxCFX8IpUF8g


```run-python
import random
print(random.randint(1,16))
```
Selected video 3: https://www.youtube.com/watch?v=YFQI1mMyLPY&list=PLuCVsS_EScKHdEgqHps_rFxCFX8IpUF8g&index=3

Total video length: 1:07:02
Start time simple:

```run-python
import random

def random_timestamp(end="67.02", start="0.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp("67.02"))
```

Start time = 21.30 - sample from here


---
## Coding Decision-Making

Key word search via youtube - then use exclusion criteria to remove invalid videos
From creators that have multiple high quality streams - randomly sample if there is no clear distinction between them otherwise purposive sample for videos that are most likely to best reflect a full workflow e.g. not just investigating one Figma feature
Aim for 5 minutes per video 
First pass -> open/inductive coding with timestamps 
Second pass -> code to specific taxonomy 

Braun & Clarke 

Thematic saturation

Approach -> timestamped notes -> second-pass with structured taxonomy e.g. similar to inductive coding? not sure if that is the right wording here?

Cohen's Kappa can make coding more rigorous - this is inter-rater reliability

---
# Analysis

- Most common actions across samples 
- Hardest actions to achieve with voice
- Biggest gap between voice time and keyboard time

What meaningful data I can get out of this:
I can eliminate easy actions and see what is left -> these are the things we need to prioritise. I can eliminate actions where the time difference between voice and manual entry is not very high -> but this requires doing the benchmarking step. 