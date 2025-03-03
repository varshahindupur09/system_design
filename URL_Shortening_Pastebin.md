## What is this System?
For example, if we shorten the following URL through ShorteningURL:

https://www.designsystems.org/course/grokking-the-system-design-interview

We would get:

https://shorteningurl.com/qxet23pt

## FR (Functional Requirements)
1. Shorten the URL (unique short identifier)
2. Redirect to Orginal URL
3. URL expiration (expiration timestamp)
4. User Account Management (Manage URLs, View Analytics - No. of clicks, location of user, referring platform)
5. Creating Custom Short URLs with specified keywords


## Non FR
1. Highly available (Short URLs must be accessible)
2. Security (Spamming, Phishing)
3. Scalability (Service must handle large number of users)
4. Performance (Fast retrieval (minimum latency when redirected to original URL))

## Cap Theorem
The CAP theorem says that a distributed system can deliver only two of three desired characteristics: **consistency, availability and partition tolerance** (the 'C,' 'A' and 'P' in CAP).

## PACELC Theorem
During a **network partition**, a distributed system must choose between **availability and consistency** 
When the system is running **normally**, it must choose between **latency and consistency** 

<img width="891" alt="image" src="https://github.com/user-attachments/assets/02475615-9d4e-44a3-a3ac-28a6934f8131" />

Multiple copies of data -> different servers -> how we sync b/w data? choose it. Most of the systems are supposed to be highly available during peak traffic and normally low latency -> making most customers happy and a few unhappy.

## Back-of-the-Envolope Estimations (Scale)
**Traffic Estimates**
- **New URL shortenings/sec** = 200 URLs/sec (518 million/month)
- **URL redirections/sec:** 100:1 read:write ratio.  20,000 URLs/sec

**Storage Estimates**
- **How many new URLs are stored**: 30 billion (518 * 12 * 5)
- **Storage**: Each URL may need 500 bytes (15TB) P.S.. TB has 12 zeros and PB 15 zeros more
- A petabyte is 1,000 terabytes (TB). A terabyte is 1,000 gigabytes (GB). A gigabyte is 1,000,000,000 bytes.

## System APIs
1. Create Short URL APIs
   Endpoint: POST/shorten
   Parameters:
     * original_url (string)
     * custom_alias (string)
     * expiration_date (timestamp/datetime)
     * user_id (string)


