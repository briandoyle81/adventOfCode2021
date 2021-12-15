# adventOfCode2021

This readme has spoilers, as of course, does the code within.

As with before, I might someday use this for students, so I'm not cleaning up my
final answers.  See inside for a window into how my brain works.

## 01



...

## 06
This is the first one I wasn't able to do part 2 with my goal of < 5 minutes, <
5 new lines of code.  I did brute force for part 1

## 07

First one wasn't too hard.  Realized the median would be the middle of all
distances total.

Part 2 is the first one I didn't get right on the first submission.  I was
thinking that since the median discounts outliers, and average includes it, that
it would be a good approach to try for the second problem where costs increase.
Didn't work, but it felt like it might be an off by 1 error or a rounding error.

I tested a -1, +1, and a few beyond in each direction, and -1 provided the
lowest cost, so I submitted that and it worked.  Not satisfied with this
solution though.

## 08
Not very hard, but so very messy.  Still, I like problems with very ugly
solutions, although this one could use a lot of cleaning up.

I feel like there is a more elegant solution using a graph, similar to word
ladder, but I couldn't find it.

## 09
Finally a graph problem!  First part was straightforward.  Correct first sub,
much cleaner code than last time.

Second part more or less straightforward as well.  Wrong first submission
though...because I'm a dunce and didn't retest after I moved the last few lines
into a function, and I dropped sorting the array of basin sizes in doing so.

# 10
Balanced brackets!

Had a gauntlet thrown down.  Part 1 in 5 to 10 minutes or so!

Part 2 took a bit longer.  Was rushing to compete with a friend and of course
had lots of typos, etc.  Initially thought that my solution was wrong, then I
realized I didn't count the score from the right direction.

# 11
This one was ugly.  Started after driving home after a long weekend.  Spent
forever fighting through minor errors in my approach for part 1.

But I got part 2 in less than 5 minutes and less than 5 lines of code!

# 12
This one was a ton of fun for part 1.  Knew it would be a traversal.  Took a
little bit to hone it to produce the correct result.

Part 2 was straightforward but took 30 lines and 30 minutes, mostly because I
have a hard time with complicated logic statements.

# 13
Pretty simple for part 1, part two was fast and a ton of fun!  Very clever!

# 14
Part 1 is a simple string manipulation problem.  I need to circle back and
figure out an elegant way to find the least value while counting.

Stuck for the first time on part 2 of this one.  After a good bit of thinking, I
thought maybe it might be made better by memoizing already calculated
sub-patterns.  It appears to be, but it's still, very, very slow, and I don't
think it will get to the end in doable time.

Computer is chugging right now on step 30.

Not possible to calculate the polymer.  Asked for and received a hint from a
friend confirming.

So how to calculate the result each step without calculating the polymer...

With a second hint, reminding me of what I know at the start, what the pairs
are, the starting polymer, and the ruleset, I picked up on keeping track of the
number of each pairs and built a solution that way.

TODO: I'm annoyed that the solution cheats and doesn't actually find what you
need in the story.  I should try to find that polymer...

# 15
Today I remembered that you _can_ put a tuple in a set :facepalm:

Anyhow, got to do Djikstra for the first time in awhile.  I like that one, got
me a job once.  But I haven't done it in years, so I looked up the algo and
implemented it from the description.

Took longer than I would have liked to put the expanded data set in memory,
particularly since I don't think I can use it.

In the meantime, letting Djikstra run.  250000 nodes in linear time will only
take an hour or so.

Culling options above and left of each step make it much faster, but still slow.

I think I could improve this by tracking if I went down or right and only adding
a row or column.

Nope, another wrong answer.  It must be able to go back up.  Or not, misread a
test on the small data.

Second answer wrong as well.  Something wrong with the last step of the heap?

Ah, I misread the heap docs about what replace does.  I needed to implement a
priority queue as described in the docs for heapq.

Tough, and wrong entries, but I didn't need help, just research to relearn
Dijkstr and the docs for Pythons built-in heap.
