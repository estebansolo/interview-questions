# Python Test Questions

## Requirements

It is necessary to install `requirements.txt` in order to run the tests.

```
pip install -r requirements.txt

python -m pytest question_a/tests/ question_b/tests question_c/tests
```


## Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

[Solution](/question_a)

## Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## Question C

We want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to our stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

1. Simplicity. Integration needs to be dead simple.
1. Resilient to network failures or crashes.
1. Near real time replication of data across Geolocation. Writes need to be in real time.
1. Data consistency across regions
1. Locality of reference, data should almost always be available from the closest region
1. Flexible Schema
1. Cache can expire

