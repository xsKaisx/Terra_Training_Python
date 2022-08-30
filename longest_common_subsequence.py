"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

from unittest import result


text_1 = """ Crazy Men - Justatee
Now I'm wandering again
Love is still nowhere to be found
Sitting by the piano in the daylight, floating with the clouds
Looking at you makes me so dazed
My heart suddenly feels strange
Love comes right on time as the light (you) comes through
Your smile shines like the sun
Sunrise and white clouds,
All tell me that: "Oh here comes the love"
No one has to wonder
'Cause I've already had my answer
"Baby, please come and take my soul"

I wistfully smiled then suddenly felt confused, 'cause I didn't know whether it was a dream
Waiting days and nights, I feel happy just thinking about you

I'm in love 
Sunshine embraces the cloud
I'm in love 
I only see us in the city
I'm in love 
Lean on our new earnestly love
Only crazy man falls in love
I'm in love 
Happiness only ends when I stop dreaming
I'm in love 
Life just like a dreamy poem
I'm in love 
Lying beside the bare tree
Hug you while it is misty day
Although it's just a dream... Although it's just a dream...
"Crazy man falls in love.." 

Alone in a place where everyone see me getting high (like a crazy guy)
Uhh well, no one wants to be ordinary when they're in love (love crazy guy)
I am dreaming about the sky full of moon and stars, you are as a fairy, we singing and dancing like a silly couple on the grassy hill (la la la)
Here we are...You look like Beyoncé while singing
Here we are...I look like Jay-Z while rapping, rap about every sunny day, every windy day, every day I have you.
But I don't know who you are.. 

Wistfully smiled and suddenly I feel confused, cause I don't know if it was a dream or not
Waiting day or night, I feel happy by just thinking about you

I'm in love 
Sunshine embraces the cloud
I'm in love 
I only see us in the city
I'm in love 
Lean on our new earnestly love
Only crazy man falls in love
I'm in love 
Happiness only ends when I stop dreaming
I'm in love 
Life just like a dreamy poem
I'm in love 
Lying beside the bare tree
In the fog
Although it's just a dream... 

Wake up, I wake up 
Autumn is already here, can you see ?
You're gone, I'm still waiting
Wake up, and wake up 
Break the imagination
Wake me up in heaven where I was dream about
Heaven where I was dream about
Wherever you are, it's so peaceful, I always like an amorist
No matter how far I go, I just can't get to you...

I'm in love 
Sunshine embrace the cloud
I'm in love 
I could only see us in the city
I'm in love 
Lean on our new earnestly love
Only Crazy man falls in love
I'm in love 
Happiness only ends when I stop dreaming
I'm in love 
Life just like a dreamy poem
I'm in love, giving your hand and hug you
Lying beside the bare tree
Misty give my hand to hug you
Although it's just a dream...

Forget about the world
Wear a new shirt
Waiting for you
Rain falls... falls... falls...

Forget about the world
Wear a new shirts
Waiting for you
Rain falls... falls... falls...
..
Only crazy men fall in love.. """

text_2 = """ Love you too much - Justatee
Loving you too much then I can only watch the rain
Looking through the trees to see how much rain
As I was this much missing you
Loving you too much then I can only count the stars
Looking up at the sky to see how many stars
As my heart is in this much longer worries
Fear of losing you when, fall is coming, suddenly green leaves turn yellow 
When the rain still hasn't come, you have your new lover, oh no no
Fear of making you fader between immensity...
Baby, please wait for me
(That's all I got to tell you)

Since loving you too much, don't dare to promise 
Just close your eyes and feel my love
Though sunny or rainy through seasons
My love is always here for you
Don't have to look for anywhere else 
That remains our own sky
Let wind carry away to a deserted place 

Loving you too much and that's all I know
Though later tomorrow we won't be next to each other
Though my heart hurts knowing you have loved someone else
Loving you too much then I'll despite all
Though the rain, the thunderstorm, though deep river, the sea from far away
Though scorching sun, I don't worry at all
Only fear of losing you when fall is coming, suddenly green leaves turn yellow
When the rain still hasn't come, you have your new lover, oh no no
Fear of making you fader between immensity
Baby, please wait for me
(That's all I got to tell you)

Since loving you too much, don't dare to promise 
Just close your eyes and feel my love
Though sunny or rainy through seasons
My love is always here for you
Don't have to look for anywhere else 
That remains our own sky
Let wind carry away to a deserted place 

Nah nah loving you too much..nah
U know, oh loving you too much nah nah nah...
I love you so, bae I love you
We have to slow down because tomorrow is very long 
Loving you too much...nah nah nah
U know, oh loving you too much...nah nah nah
I love you so, bae I love you so
We have to slow down, slow down ...

Because who knows, waking up in the morning tomorrow
You are not here to hug me, to kiss me lightly
Let our love keep drifting
Wait for a thunderstorm and storm to suddenly sweep away
If someday, our dream fail
You're not on my shoulder, our love turn so fragile
Then one person stands waiting, the other keep dreaming...

Since loving you too much, don't dare to promise 
(Don't dare to promise anything else no no no no no)
Just close your eyes and feel my love
(Can You Feel My Love, love bae?)
(I'm still here through seasons)
Don't have to look for anywhere else
(I love you so
Love you so
Love you so
I love you so ..)
Loving you.. cause someone has been loving, loving...
"""

text_3 = "Crazy Men - Justatee"
text_4 = "Love you too much - Justatee"

text_5 = "abcde"
text_6 = "ace"


def longest_common_subsequence(text_1, text_2):
    # text_1 > text_2 in default
    if len(text_1) < len(text_2):
        text_1, text_2 = text_2, text_1
    
    result = {
        'len':  0,
        'common_string':  []
    }
    
    # for i in range(0, len(text_2)):
    #     for j in range(i, len(text_2)):
    #         if text_2[j:] in text_1 and len(text_2[j:]) > result['len']:
    #             result['len'] = len(text_2[j:])
    #             result['common_string'] = text_2[j:]

    for i in text_2:
        if i in text_1:
            result['common_string'].append(i) 
    result["len"] = len(result["common_string"])
    print(result)

longest_common_subsequence(text_3, text_4)
